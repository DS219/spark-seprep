# RAG Chatbot - Manual Step-by-Step Setup

This guide walks you through setting up the RAG chatbot **manually**, explaining each step. This helps you understand exactly what the `start.sh` script does automatically.

Use this guide to learn the internals, then use `start.sh` for quick deployment!

---

## Overview

We will:
1. Create a Podman pod with port mappings
2. Start PostgreSQL with pgvector extension
3. Start the ramalama model server
4. Build the chatbot application container
5. Start the chatbot application
6. Test the complete system

**Time**: ~10-15 minutes (first time, including model download)

---

## Step 1: Clean Up Any Existing Setup

First, remove any existing `rag-chatbot` pod to start fresh:

```bash
podman pod rm rag-chatbot --force -t 0 2>/dev/null || true
```

**What this does**: Removes the pod and all its containers if they exist. The `|| true` prevents errors if nothing exists.

**Check**: Run `podman pod ps` - you should NOT see `rag-chatbot` listed.

---

## Step 2: Create a Volume for Model Storage

Create a persistent volume to store the AI model:

```bash
podman volume create rag-models
```

**What this does**: Creates a named volume that persists even when containers are removed. The model (~2.4GB) will be stored here and reused across restarts.

**Check**: Run `podman volume ls` - you should see `rag-models` listed.

---

## Step 3: Create the Pod

Create a pod with the ports we need exposed:

```bash
podman pod create \
    --name rag-chatbot \
    --publish 8501:8501 \
    --publish 8888:8888
```

**What this does**:
- Creates a pod named `rag-chatbot`
- Maps port 8501 (Streamlit UI) from the pod to your host
- Maps port 8888 (model server) from the pod to your host
- All containers in this pod share the same network namespace (they can talk via localhost)

**Check**: Run `podman pod ps` - you should see the `rag-chatbot` pod with STATUS "Created" and 0/0 containers.

---

## Step 4: Start PostgreSQL with pgvector

Start the vector database:

```bash
podman run -d --rm \
    --pod rag-chatbot \
    --name rag-chatbot-pgvector \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=ragdb \
    pgvector/pgvector:pg16
```

**What this does**:
- Runs PostgreSQL 16 with the pgvector extension
- Attaches it to our pod (so it shares the network)
- Sets up database credentials
- Creates a database named `ragdb`
- The `-d` flag runs it in detached mode (background)

**Check**:
```bash
podman ps --pod
```
You should see `rag-chatbot-pgvector` running in the `rag-chatbot` pod.

**Test the database** (wait ~5 seconds for startup):
```bash
podman exec rag-chatbot-pgvector psql -U postgres -d ragdb -c "SELECT version();"
```
You should see PostgreSQL version information.

---

## Step 5: Start the Ramalama Model Server

Start the AI model server:

```bash
podman run -d --rm \
    --pod rag-chatbot \
    --name rag-chatbot-model \
    -v rag-models:/models:Z \
    quay.io/ramalama/ramalama:latest \
    ramalama --store /models serve \
    --port 8888 \
    --host 0.0.0.0 \
    ollama://phi4-mini:latest
```

**What this does**:
- Runs ramalama (a tool for serving AI models)
- Attaches to our pod
- Mounts the `rag-models` volume to `/models` in the container
- Downloads Phi4-mini-instruct model from Hugging Face (first time only)
- Serves the model on port 8888 with an OpenAI-compatible API
- The `:Z` flag sets proper SELinux labels (safe to use even on non-SELinux systems)

**This step takes the longest on first run** (~5-10 minutes to download 2.4GB model)

**Check progress**:
```bash
podman logs -f rag-chatbot-model
```
Press `Ctrl+C` to stop following logs.

Look for messages like:
- "Downloading model..."
- "Loading model..."
- "Uvicorn running on http://0.0.0.0:8888"

**Test when ready**:
```bash
curl http://localhost:8888/v1/models
```

You should see JSON output with model information. If you get "connection refused", wait a bit longer.

---

## Step 6: Build the Chatbot Application

Build the Streamlit chatbot container from the Containerfile:

```bash
podman build -t rag-chatbot-app:latest ./app
```

**What this does**:
- Reads the `app/Containerfile`
- Creates a Python 3.11 environment
- Installs dependencies from `requirements.txt`
- Copies `rag_app.py` and `manage_vectordb.py`
- Tags the image as `rag-chatbot-app:latest`

**Check**:
```bash
podman images | grep rag-chatbot-app
```
You should see `localhost/rag-chatbot-app` with tag `latest`.

---

## Step 7: Start the Chatbot Application

Start the Streamlit UI:

```bash
podman run -d --rm \
    --pod rag-chatbot \
    --name rag-chatbot-app \
    -e MODEL_ENDPOINT=http://127.0.0.1:8888 \
    -e MODEL_NAME=library/phi4-mini \
    -e POSTGRES_HOST=127.0.0.1 \
    -e POSTGRES_PORT=5432 \
    -e POSTGRES_DB=ragdb \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e EMBEDDING_MODEL=BAAI/bge-small-en-v1.5 \
    -e COLLECTION_NAME=documents \
    rag-chatbot-app:latest
```

**What this does**:
- Runs the chatbot container we just built
- Attaches to our pod (can access database and model via localhost)
- Configures environment variables:
  - `MODEL_ENDPOINT`: Where to find the AI model
  - `POSTGRES_*`: Database connection details
  - `EMBEDDING_MODEL`: Which model to use for creating embeddings
  - `COLLECTION_NAME`: Name for the vector collection in the database

**Check**:
```bash
podman logs -f rag-chatbot-app
```

Look for:
- "Connecting to PostgreSQL..."
- "You can now view your Streamlit app in your browser"
- "Network URL: http://0.0.0.0:8501"

Press `Ctrl+C` to stop following logs.

---

## Step 8: Verify Everything is Running

Check all containers in the pod:

```bash
podman ps --pod
```

You should see **4 containers** running:
1. Pod infra container (infrastructure)
2. `rag-chatbot-pgvector` (database)
3. `rag-chatbot-model` (AI model server)
4. `rag-chatbot-app` (Streamlit UI)

**Pod status**:
```bash
podman pod ps
```
Should show `rag-chatbot` with `4/4` containers running.

---

## Step 9: Access the Chatbot

Open your browser to:

```
http://localhost:8501
```

You should see the RAG Chatbot interface!

---

## Step 10: Test with a Document

1. **Upload a document**:
   - Click "Browse files" in the sidebar
   - Select `sample-document.txt` (or any PDF/text file)
   - Click "Process Document"

2. **Wait for processing**:
   - You'll see "Processing document..."
   - Then "Split into X chunks"
   - Finally "Document processed and ready for questions!"

3. **Ask a question**:
   - In the chat input, try: "What are the benefits of containers?"
   - The chatbot will retrieve relevant chunks and answer based on the document

---

## Stopping the Application

### Option 1: Stop the pod (keeps containers for restart)

```bash
podman pod stop rag-chatbot
```

### Option 2: Remove everything

```bash
podman pod rm rag-chatbot --force
```

### Option 3: Use the stop script

```bash
./stop.sh
```

---

## What You Learned

By following these manual steps, you now understand:

1. **Pod Creation**: How to create a pod and map ports
2. **Volume Management**: Using persistent volumes for data
3. **Container Networking**: How containers in a pod communicate via localhost
4. **Service Dependencies**: Starting services in the right order
5. **Environment Configuration**: Passing configuration via environment variables
6. **Image Building**: Creating custom containers from Containerfiles
7. **Logging & Debugging**: Using `podman logs` to troubleshoot

---

## Cleanup and Restart

To completely start over:

```bash
# Remove pod
podman pod rm rag-chatbot --force

# Remove built image (optional)
# Don't remove if you are going to run again
podman rmi rag-chatbot-app:latest

# Remove model volume to free space (optional)
# Don't remove if you are going to run again
podman volume rm rag-models

# Now follow steps 2-7 again
```

---

## Next Steps

Now that you understand the manual process:

1. **Use the automation**: Try `./start.sh` and see how it does all this for you!
2. **Experiment**: Modify the model, chunk size, or embedding model
3. **Monitor**: Watch logs while using the chatbot to see what happens
4. **Scale**: Try running multiple pods with different models

---

## Quick Reference Commands

```bash
# View all pod containers
podman ps --pod

# View pod status
podman pod ps

# Follow logs
podman logs -f rag-chatbot-app

# Test database
podman exec rag-chatbot-pgvector psql -U postgres -d ragdb -c "SELECT version();"

# Test model server
curl http://localhost:8888/v1/models

# Stop everything
podman pod stop rag-chatbot

# Remove everything
podman pod rm rag-chatbot --force

# View volumes
podman volume ls

# Inspect volume
podman volume inspect rag-models
```

**Recommendation**: Do the manual setup once to learn, then use `start.sh` for convenience!
