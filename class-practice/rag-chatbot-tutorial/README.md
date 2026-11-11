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

This tutorial runs two containers in a single pod. The model runs on your laptop with
[llmman](../llmman-tutorial/README.md), outside the pod:

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
└─────────────────────────────────────────────────┘
                       ↓  host.containers.internal:17434
┌─────────────────────────────────────────────────┐
│  Your laptop: llmman serve (Port 17434)         │
│  - Serves gemma3:4b (or Phi-4-mini)             │
│  - Uses your laptop's GPU                       │
│  - OpenAI-compatible API                        │
└─────────────────────────────────────────────────┘
```

### Components

1. **PostgreSQL with pgvector**: Vector database that stores document embeddings and performs similarity search
2. **Streamlit Application**: Web UI for uploading documents and chatting
3. **llmman** (on your laptop, not in the pod): Serves the model with an OpenAI-compatible API.
   Inside a container, `127.0.0.1` means the container itself, so the app reaches your
   laptop at `host.containers.internal`, Podman's name for the host.

## Prerequisites

- **Podman** installed, with a Podman machine running: see
  [Install Podman on Mac or Windows](../podman-install.md)
- **llmman** installed, with `gemma3:4b` downloaded: see
  [step 0 of the llmman tutorial](../llmman-tutorial/README.md#0-before-class-install-and-download-about-10-minutes).
  Optional: Phi-4-mini, from step 5 of that tutorial.
- About 3 GB of free disk space for the app image
- 8GB+ RAM recommended
- Works on Apple Silicon Macs and Windows 11. llmman has no Intel Mac build.

> **Before class:** run `podman build -t rag-chatbot-app:latest ./app` from this folder.
> The image is about 2.2 GB (mostly PyTorch for the embedding model) and took about
> 4 minutes to build on our test Mac. Classroom Wi-Fi is much slower.

## Two Ways to Learn

This tutorial offers two approaches:

1. **Quick Start** (recommended for demos): Use `start.sh` to automate everything
2. **Manual Setup** (recommended for learning): Follow step-by-step to understand each component

Choose your path below!

---

## Quick Start (Automated)

### 1. Start llmman and Navigate to This Directory

In one terminal, start the model server and leave it running:

```bash
llmman serve
```

In a second terminal:

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

The script will:
- Check that `llmman serve` is running
- Build the chatbot application container (fast if you already built it)
- Start both containers in a pod

`start.sh` is a bash script. On Windows, follow [MANUAL_SETUP.md](MANUAL_SETUP.md)
in PowerShell instead, joining each multi-line command into one line.

### 4. Access the Chatbot

Once you see "✅ RAG Chatbot is ready!", open your browser to:

```
http://localhost:8501
```

### 5. Use the Chatbot

1. Click "Browse files" in the sidebar
2. Upload a PDF or text file (try a technical document, article, or book chapter)
3. Click "Process Documents"
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
7. **Generation**: The relevant chunks are sent to the model (Gemma 3 or Phi-4-mini) as context
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

### Clean Up Everything

```bash
./stop.sh
podman rmi rag-chatbot-app:latest  # Removes the app image (about 2.2 GB)
```

Then stop llmman with Ctrl+C. To remove llmman and its models, follow
[step 7 of the llmman tutorial](../llmman-tutorial/README.md#7-remove-everything-4550-minutes).

## Troubleshooting

### `start.sh` Says llmman Is Not Running

Start it in another terminal with `llmman serve`, then run `./start.sh` again.

### Connection Errors in Chatbot

Make sure both containers are running:

```bash
podman ps --pod
```

You should see 3 containers running (including the pod infra container). Then check
that llmman is still running: `curl http://127.0.0.1:17434/v1/models`.

### "model not found" Error

`MODEL_NAME` must match a model llmman has downloaded. Run `llmman ls`. Use `gemma3:4b`,
or `hf.co/unsloth/Phi-4-mini-instruct-GGUF` for Phi-4-mini (the short name `phi4-mini`
does not work).

### Out of Memory

Close other apps, or switch to Phi-4-mini, which is smaller (2.5 GB vs 3.3 GB).

### Port Already in Use

If port 8501 is already in use, change `--publish 8501:8501` in `start.sh`, for example
to `--publish 8502:8501`, and open `http://localhost:8502`.

## Learning Objectives

By completing this tutorial, students will learn:

1. **Container Orchestration**: How to run multiple containers as a cohesive application using pods
2. **Vector Databases**: How embeddings work and why they're useful for semantic search
3. **RAG Architecture**: How to combine retrieval with generation for better AI responses
4. **LangChain**: Using LangChain for document processing and retrieval chains
5. **Local AI Models**: Running AI models locally without cloud dependencies
6. **API Integration**: How containers communicate within a pod, and with a server on the host

## Customization Ideas

### Try Different Models

Edit `MODEL_NAME` in `.env`, then run `./start.sh` again:

```bash
# Google Gemma 3, 4B parameters (default)
MODEL_NAME=gemma3:4b

# Microsoft Phi-4-mini, 3.8B parameters
# First run: llmman pull hf.co/unsloth/Phi-4-mini-instruct-GGUF
MODEL_NAME=hf.co/unsloth/Phi-4-mini-instruct-GGUF
```

Ask both models the same question about the same document and compare. In our test,
Phi-4-mini answered in about 8 seconds and Gemma in about 18.

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
- [llmman](https://github.com/llmmanorg/llmman)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Understanding RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/)

## FAQ

**Q: Can I use this with proprietary documents?**
A: Yes! Everything runs locally. Your documents never leave your machine.

**Q: How much does this cost?**
A: Nothing! All components are open source and run locally.

**Q: Will this work on my Mac M1/M2/M3?**
A: Yes. Intel Macs are not supported because llmman has no Intel Mac build.

**Q: Does this use GPU acceleration?**
A: Yes, for the model. llmman runs on your laptop, not in a container, so it can use
the Mac's GPU (Metal). The embedding model inside the app container runs on CPU,
which is fine for small documents.

**Q: How accurate is it?**
A: The quality depends on:
- How well your question relates to the document content
- The chunk size (too small = missing context, too large = irrelevant info)
- The model's capabilities (small 4B models are good but not perfect)

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
