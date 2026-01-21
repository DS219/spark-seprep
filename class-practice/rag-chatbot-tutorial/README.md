# RAG Chatbot Tutorial

A hands-on tutorial for building a Retrieval Augmented Generation (RAG) chatbot using containers and local AI models.

## What is RAG?

RAG (Retrieval Augmented Generation) is a technique that enhances Large Language Models (LLMs) by giving them access to external knowledge. Instead of relying only on the model's training data, RAG:

1. Takes your documents and converts them into searchable embeddings
2. Stores these embeddings in a vector database
3. When you ask a question, finds the most relevant parts of your documents
4. Sends that context to the LLM along with your question
5. The LLM generates an accurate answer based on YOUR documents

## Architecture

This tutorial runs three containers in a single pod:

```
┌─────────────────────────────────────────────────┐
│                  RAG Chatbot Pod                │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌──────────────────────────────────────────┐   │
│  │  Streamlit UI (Port 8501)                │   │
│  │  - File upload interface                 │   │
│  │  - Chat interface                        │   │
│  │  - Document processing                   │   │
│  └──────────────────────────────────────────┘   │
│                      ↓                          │
│  ┌──────────────────────────────────────────┐   │
│  │  PostgreSQL + pgvector                   │   │
│  │  - Stores document embeddings            │   │
│  │  - Vector similarity search              │   │
│  └──────────────────────────────────────────┘   │
│                      ↓                          │
│  ┌──────────────────────────────────────────┐   │
│  │  Ramalama Model Server (Port 8888)       │   │
│  │  - Serves Phi4-mini-instruct             │   │
│  │  - OpenAI-compatible API                 │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### Components

1. **PostgreSQL with pgvector**: Vector database that stores document embeddings and performs similarity search
2. **Ramalama Model Server**: Serves the Phi4-mini-instruct model with an OpenAI-compatible API
3. **Streamlit Application**: Web UI for uploading documents and chatting

## Prerequisites

- **Podman** installed ([Get Podman](https://podman.io/getting-started/installation))
- At least 8GB of free disk space (for the model)
- 8GB+ RAM recommended
- Works on:
  - macOS (Intel or Apple Silicon - M-series Macs will use Metal GPU acceleration automatically)
  - Linux (with or without NVIDIA GPU)
  - Windows with WSL2

Note: Ramalama automatically detects and uses available GPUs for better performance!

## Two Ways to Learn

This tutorial offers two approaches:

1. **Quick Start** (recommended for demos): Use `start.sh` to automate everything
2. **Manual Setup** (recommended for learning): Follow step-by-step to understand each component

Choose your path below!

---

## Quick Start (Automated)

### 1. Clone or Navigate to This Directory

```bash
cd rag-chatbot-tutorial
```

### 2. (Optional) Configure Environment

Copy the template and customize if needed:

```bash
cp env.template .env
# Edit .env if you want to change defaults
```

### 3. Start the RAG Chatbot

Make the script executable and run it:

```bash
chmod +x start.sh
./start.sh
```

The first run will:
- Download the Phi4-mini-instruct model (~2.4GB) - this takes a few minutes
- Build the chatbot application container
- Start all three containers in a pod

Subsequent runs will be much faster since the model is cached.

### 4. Access the Chatbot

Once you see "✅ RAG Chatbot is ready!", open your browser to:

```
http://localhost:8501
```

### 5. Use the Chatbot

1. Click "Browse files" in the sidebar
2. Upload a PDF or text file (try a technical document, article, or book chapter)
3. Click "Process Document"
4. Wait for processing to complete
5. Ask questions about your document in the chat!

Example questions:
- "What is the main topic of this document?"
- "Summarize the key points"
- "What does the document say about [specific topic]?"

---

## Manual Setup (Educational)

Want to understand what's happening under the hood?

**👉 See [MANUAL_SETUP.md](MANUAL_SETUP.md)** for a complete step-by-step guide that walks through:
- Creating pods and volumes manually
- Starting each container individually
- Understanding networking and configuration
- Debugging and troubleshooting techniques

**This is highly recommended for students learning container orchestration!**

The manual setup teaches you exactly what `start.sh` does automatically, one command at a time.

---

## How It Works

### Step-by-Step Flow

1. **Upload**: You upload a document (PDF or text)
2. **Chunking**: The document is split into smaller chunks (default 512 characters)
3. **Embedding**: Each chunk is converted to a vector using a sentence transformer model
4. **Storage**: Vectors are stored in PostgreSQL with the pgvector extension
5. **Query**: When you ask a question, it's also converted to a vector
6. **Retrieval**: The database finds the most similar document chunks
7. **Generation**: The relevant chunks are sent to Phi4-mini-instruct as context
8. **Response**: The model generates an answer based on YOUR document

## Project Structure

```
rag-chatbot-tutorial/
├── README.md              # This file - Quick start guide
├── MANUAL_SETUP.md        # Step-by-step manual setup guide
├── start.sh              # Script to start the pod (automated)
├── stop.sh               # Script to stop the pod
├── env.template          # Environment configuration template
├── sample-document.txt   # Example document for testing
└── app/
    ├── Containerfile     # Container image definition
    ├── requirements.txt  # Python dependencies
    ├── rag_app.py       # Main Streamlit application
    └── manage_vectordb.py # Vector database management
```

## Useful Commands

### View Logs

```bash
# Chatbot application logs
podman logs rag-chatbot-app

# Model server logs
podman logs rag-chatbot-model

# Database logs
podman logs rag-chatbot-pgvector
```

### Stop the Chatbot

```bash
./stop.sh
# or
podman pod stop rag-chatbot
podman pod rm rag-chatbot
```

### Check Running Containers

```bash
podman pod ps
podman ps --pod
```

### Clean Up Everything (Including Model)

```bash
./stop.sh
podman volume rm rag-models  # Removes downloaded model
```

## Troubleshooting

### Model Server Taking Too Long

The first run downloads ~2.4GB. Check progress:

```bash
podman logs -f rag-chatbot-model
```

### Connection Errors in Chatbot

Make sure all containers are running:

```bash
podman ps --pod
```

You should see 4 containers running (including the pod infra container).

### Out of Memory

Reduce the model context or use a smaller model. Edit `start.sh` and change the model to:

```bash
huggingface://TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

### Port Already in Use

If port 8501 or 8888 is already in use, edit `.env`:

```bash
MODELSERVER_PORT=8889  # Change to different port
```

Then modify `start.sh` to change the UI port if needed.

## Learning Objectives

By completing this tutorial, students will learn:

1. **Container Orchestration**: How to run multiple containers as a cohesive application using pods
2. **Vector Databases**: How embeddings work and why they're useful for semantic search
3. **RAG Architecture**: How to combine retrieval with generation for better AI responses
4. **LangChain**: Using LangChain for document processing and retrieval chains
5. **Local AI Models**: Running AI models locally without cloud dependencies
6. **API Integration**: How containers communicate within a pod

## Customization Ideas

### Try Different Models

Edit `start.sh` and change the model URL:

```bash
# Mistral 7B (larger, slower, potentially better)
huggingface://TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_M.gguf

# Llama 3 8B
huggingface://QuantFactory/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct.Q4_K_M.gguf
```

### Modify Chunk Size

Edit `app/rag_app.py` and change `chunk_size`:

```python
chunk_size = int(os.getenv("CHUNK_SIZE", "512"))  # Try 256, 1024, etc.
```

### Add More File Types

Extend `read_file()` in `app/rag_app.py` to support:
- Word documents (`.docx`)
- Markdown (`.md`)
- CSV files (`.csv`)

Look into LangChain's document loaders: `Docx2txtLoader`, `CSVLoader`, etc.

### Improve Retrieval

Modify `get_retriever()` in `app/manage_vectordb.py`:

```python
# Retrieve more chunks
return db.as_retriever(search_kwargs={"k": 8})  # Default is 4

# Use different search type
return db.as_retriever(search_type="mmr", search_kwargs={"k": 4, "fetch_k": 10})
```

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [Ramalama Project](https://github.com/containers/ramalama)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Understanding RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/)

## FAQ

**Q: Can I use this with proprietary documents?**
A: Yes! Everything runs locally. Your documents never leave your machine.

**Q: How much does this cost?**
A: Nothing! All components are open source and run locally.

**Q: Will this work on my Mac M1/M2/M3?**
A: Yes! Ramalama automatically detects and uses Metal acceleration on Apple Silicon for significantly better performance.

**Q: Does this use GPU acceleration?**
A: Yes! Ramalama automatically detects available GPUs:
- On Apple Silicon Macs: Uses Metal (automatic, no configuration needed)
- On Linux with NVIDIA GPUs: Uses CUDA if drivers are available
- On systems without GPUs: Falls back to CPU (still works fine)

**Q: How accurate is it?**
A: The quality depends on:
- How well your question relates to the document content
- The chunk size (too small = missing context, too large = irrelevant info)
- The model's capabilities (Phi4-mini is good but not perfect)

## Next Steps

After completing this tutorial, consider:

1. Building a web API instead of Streamlit UI
2. Adding user authentication
3. Supporting multiple documents in the database
4. Implementing citation/source tracking
5. Deploying to a server with Kubernetes
6. Adding evaluation metrics for answer quality

## License

This tutorial is part of the AI Lab Recipes project and follows the same license.

## Contributing

Found an issue or want to improve this tutorial? Contributions welcome!
