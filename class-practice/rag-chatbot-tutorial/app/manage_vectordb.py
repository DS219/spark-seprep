from langchain_community.vectorstores import PGVector
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os


class VectorDB:
    def __init__(self, host, port, database, user, password, collection_name, embedding_model):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

    def connect(self):
        """Connect to PostgreSQL with pgvector extension"""
        print(f"Connecting to PostgreSQL at {self.host}:{self.port}...")
        return self.connection_string

    def populate_db(self, documents):
        """Populate the vector database with document embeddings"""
        print(f"Populating VectorDB with {len(documents)} document chunks...")

        # Initialize embeddings model
        embeddings = SentenceTransformerEmbeddings(model_name=self.embedding_model)

        # Create or connect to existing PGVector store
        db = PGVector.from_documents(
            documents=documents,
            embedding=embeddings,
            collection_name=self.collection_name,
            connection_string=self.connection_string,
            pre_delete_collection=True  # Clear existing collection on new upload
        )

        print(f"✅ VectorDB populated with {len(documents)} chunks")
        return db

    def get_retriever(self):
        """Get a retriever for an existing collection"""
        print(f"🔍 Getting retriever for collection: {self.collection_name}")
        embeddings = SentenceTransformerEmbeddings(model_name=self.embedding_model)

        db = PGVector(
            connection_string=self.connection_string,
            collection_name=self.collection_name,
            embedding_function=embeddings
        )

        retriever = db.as_retriever(search_kwargs={"k": 4})
        print(f"✅ Retriever ready - will fetch top 4 relevant chunks")
        return retriever

    def clear_db(self):
        """Clear the vector database collection"""
        print(f"Clearing VectorDB collection: {self.collection_name}...")
        try:
            embeddings = SentenceTransformerEmbeddings(model_name=self.embedding_model)

            # Connect and delete collection
            PGVector.from_documents(
                documents=[],
                embedding=embeddings,
                collection_name=self.collection_name,
                connection_string=self.connection_string,
                pre_delete_collection=True
            )
            print("✅ VectorDB cleared")
        except Exception as e:
            print(f"Note: Couldn't clear collection (may not exist yet): {e}")
