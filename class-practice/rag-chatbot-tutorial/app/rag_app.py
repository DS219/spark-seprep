from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from manage_vectordb import VectorDB
import tempfile
import streamlit as st
import os
import time

# Configuration from environment variables
model_service = os.getenv("MODEL_ENDPOINT", "http://0.0.0.0:8888")
model_service = f"{model_service}/v1"
model_name = os.getenv("MODEL_NAME", "phi4-mini-instruct")
chunk_size = int(os.getenv("CHUNK_SIZE", "512"))
chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "50"))
embedding_model = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

# PostgreSQL/pgvector configuration
db_host = os.getenv("POSTGRES_HOST", "127.0.0.1")
db_port = os.getenv("POSTGRES_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "ragdb")
db_user = os.getenv("POSTGRES_USER", "postgres")
db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
collection_name = os.getenv("COLLECTION_NAME", "documents")

# Initialize VectorDB
vdb = VectorDB(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password,
    collection_name=collection_name,
    embedding_model=embedding_model
)

def split_docs(raw_documents):
    """Split documents into chunks for embedding"""
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = text_splitter.split_documents(raw_documents)
    return docs


def read_file(file):
    """Read uploaded PDF, text, or markdown file"""
    file_type = file.type
    file_name = file.name.lower()

    if file_type == "application/pdf":
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        with open(temp.name, "wb") as f:
            f.write(file.getvalue())
        loader = PyPDFLoader(temp.name)

    elif file_type == "text/plain" or file_name.endswith('.txt'):
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        with open(temp.name, "wb") as f:
            f.write(file.getvalue())
        loader = TextLoader(temp.name)

    elif file_type == "text/markdown" or file_name.endswith('.md'):
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
        with open(temp.name, "wb") as f:
            f.write(file.getvalue())
        loader = TextLoader(temp.name)

    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    raw_documents = loader.load()
    return raw_documents


# Streamlit UI Configuration
st.set_page_config(page_title="RAG Chatbot Tutorial", page_icon="📚", layout="wide")

st.title("📚 RAG Chatbot Tutorial")
st.markdown("Upload a document and ask questions about it!")

# Sidebar for file upload
with st.sidebar:
    st.header("📄 Document Upload")

    files = st.file_uploader(
        label="Upload PDF, text, or markdown files",
        type=["txt", "pdf", "md"],
        accept_multiple_files=True,
        help="Upload one or more documents to populate the knowledge base"
    )

    if files:
        st.success(f"✅ Loaded {len(files)} file(s):")
        for f in files:
            st.write(f"  • {f.name}")

        # Add a button to process the files
        if st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                try:
                    all_documents = []

                    # Process each file
                    for file in files:
                        st.info(f"Processing {file.name}...")
                        raw_docs = read_file(file)
                        docs = split_docs(raw_docs)
                        all_documents.extend(docs)

                    st.info(f"Total: {len(all_documents)} chunks from {len(files)} file(s)")

                    # Populate the vector database with all documents
                    vdb.populate_db(all_documents)
                    st.session_state['db_populated'] = True
                    st.session_state['file_count'] = len(files)
                    st.session_state['file_names'] = [f.name for f in files]
                    st.success("Documents processed and ready for questions!")

                except Exception as e:
                    st.error(f"Error processing documents: {e}")
                    st.session_state['db_populated'] = False

    st.divider()
    st.markdown("### About")
    st.markdown("""
    This RAG (Retrieval Augmented Generation) chatbot:
    - Supports **PDF, TXT, and Markdown** files
    - Accepts **multiple file uploads**
    - Uses **pgvector** for document storage
    - Runs **Phi4-mini** via ramalama
    - Retrieves relevant context before answering
    """)

# Main chat interface
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! Upload a document to get started, then ask me questions about it."}
    ]

if 'db_populated' not in st.session_state:
    st.session_state['db_populated'] = False

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your document..."):
    if not st.session_state.get('db_populated', False):
        st.warning("⚠️ Please upload and process a document first!")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Get response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Initialize LLM
                    llm = ChatOpenAI(
                        base_url=model_service,
                        api_key="EMPTY",
                        model=model_name,
                        streaming=False,
                        temperature=0.7
                    )

                    # Get retriever
                    retriever = vdb.get_retriever()

                    # Test retrieval to see what context is being used
                    retrieved_docs = retriever.get_relevant_documents(prompt)
                    print(f"\n📚 Retrieved {len(retrieved_docs)} relevant chunks:")
                    for i, doc in enumerate(retrieved_docs, 1):
                        preview = doc.page_content[:100].replace('\n', ' ')
                        print(f"  {i}. {preview}...")

                    # Create RAG prompt
                    rag_prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:

{context}

Question: {input}

Answer: Let me help you with that based on the document.""")

                    # Create chain
                    chain = (
                        {"context": retriever, "input": RunnablePassthrough()}
                        | rag_prompt
                        | llm
                    )

                    # Get response
                    response = chain.invoke(prompt)
                    st.write(response.content)

                    # Add to chat history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response.content
                    })

                except Exception as e:
                    error_msg = f"Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
