# RAG Chatbot - Manual Step-by-Step Setup

This guide walks you through setting up the RAG chatbot **manually**, explaining each step. This helps you understand exactly what the `start.sh` script does automatically.

Use this guide to learn the internals, then use `start.sh` for quick deployment!

---

## Overview

We will:
1. Create a Podman pod with port mappings
2. Start PostgreSQL with pgvector extension
3. Start the llmman model server on your laptop
4. Build the chatbot application container
5. Start the chatbot application
6. Test the complete system

**Time**: ~10-15 minutes (first time, including the app image build)

**Before you start**: you need Podman ([Install Podman on Mac or Windows](../podman-install.md))
and llmman with `gemma3:4b` downloaded ([llmman tutorial](../llmman-tutorial/README.md)).

**Windows**: these commands work in PowerShell, but PowerShell does not use `\` to
continue a line. Join each multi-line command into one line, or replace each `\`
with a backtick (`` ` ``).

---

## Step 1: Clean Up Any Existing Setup

First, remove any existing `rag-chatbot` pod to start fresh:

```bash
podman pod rm rag-chatbot --force -t 0 2>/dev/null || true
```

**What this does**: Removes the pod and all its containers if they exist. The `|| true` prevents errors if nothing exists.

**Check**: Run `podman pod ps` - you should NOT see `rag-chatbot` listed.

---

## Step 2: Create the Pod

Create a pod with the ports we need exposed:

```bash
podman pod create \
    --name rag-chatbot \
    --publish 8501:8501
```

**What this does**:
- Creates a pod named `rag-chatbot`
- Maps port 8501 (Streamlit UI) from the pod to your host
- All containers in this pod share the same network namespace (they can talk via localhost)

**Check**: Run `podman pod ps` - you should see the `rag-chatbot` pod with STATUS "Created" and 0/0 containers.

---

## Step 3: Start PostgreSQL with pgvector

Start the vector database:

```bash
podman run -d --rm \
    --pod rag-chatbot \
    --name rag-chatbot-pgvector \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=ragdb \
    docker.io/pgvector/pgvector:pg16
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

## Step 4: Start the llmman Model Server

Open a **new terminal** and start llmman on your laptop:

```bash
llmman serve
```

Leave this terminal open. The model does **not** run in the pod: llmman runs directly
on your laptop, where it can use your GPU. You set it up in the
[llmman tutorial](../llmman-tutorial/README.md).

**Test it** from your first terminal:
```bash
curl http://127.0.0.1:17434/v1/models
```

You should see JSON that lists `docker.io/ai/gemma3:4b`. If you get "connection refused",
check that `llmman serve` is still running.

---

## Step 5: Build the Chatbot Application

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

The image is about 2.2 GB, mostly PyTorch for the embedding model. It took about
4 minutes to build on our test Mac, so do this step at home if you can.

**Check**:
```bash
podman images | grep rag-chatbot-app
```
You should see `localhost/rag-chatbot-app` with tag `latest`.

---

## Step 6: Start the Chatbot Application

Start the Streamlit UI:

```bash
podman run -d --rm \
    --pod rag-chatbot \
    --name rag-chatbot-app \
    -e MODEL_ENDPOINT=http://host.containers.internal:17434 \
    -e MODEL_NAME=gemma3:4b \
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
- Attaches to our pod (can reach the database via localhost)
- Configures environment variables:
  - `MODEL_ENDPOINT`: Where to find the AI model. Inside a container, `127.0.0.1`
    means the container itself, so we use `host.containers.internal`, Podman's name
    for your laptop.
  - `MODEL_NAME`: Which llmman model to use. For Phi-4-mini, use
    `hf.co/unsloth/Phi-4-mini-instruct-GGUF`.
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

## Step 7: Verify Everything is Running

Check all containers in the pod:

```bash
podman ps --pod
```

You should see **3 containers** running:
1. Pod infra container (infrastructure)
2. `rag-chatbot-pgvector` (database)
3. `rag-chatbot-app` (Streamlit UI)

The model server, llmman, runs on your laptop, so it is not in this list.

**Pod status**:
```bash
podman pod ps
```
Should show `rag-chatbot` with `3/3` containers running.

---

## Step 8: Access the Chatbot

Open your browser to:

```
http://localhost:8501
```

You should see the RAG Chatbot interface!

---

## Step 9: Test with a Document

1. **Upload a document**:
   - Click "Browse files" in the sidebar
   - Select `sample-document.txt` (or any PDF/text file)
   - Click "Process Documents"

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
2. **Host Services**: How a container reaches a server on your laptop with `host.containers.internal`
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

# Stop llmman: press Ctrl+C in its terminal

# Now follow steps 2-6 again
```

---

## Next Steps

Now that you understand the manual process:

1. **Use the automation**: Try `./start.sh` and see how it does all this for you!
2. **Experiment**: Modify the model, chunk size, or embedding model
3. **Monitor**: Watch logs while using the chatbot to see what happens
4. **Compare models**: Run the app once with `gemma3:4b` and once with Phi-4-mini

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

# Test model server (llmman on your laptop)
curl http://127.0.0.1:17434/v1/models

# Stop everything
podman pod stop rag-chatbot

# Remove everything
podman pod rm rag-chatbot --force
```

**Recommendation**: Do the manual setup once to learn, then use `start.sh` for convenience!
