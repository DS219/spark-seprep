#!/bin/bash

# RAG Chatbot Tutorial - Startup Script
# This script creates a pod with 3 containers:
# 1. PostgreSQL with pgvector extension
# 2. Ramalama model server (Phi4-mini-instruct)
# 3. RAG chatbot UI (Streamlit)

set -e

POD_NAME="rag-chatbot"

# Load environment variables from .env file
if [ -f ".env" ]; then
    echo "Loading configuration from .env file..."
    source .env
else
    echo "⚠️  Warning: .env file not found, using defaults"
    echo "You can create a .env file based on env.template"
fi

# Set defaults if not specified in .env
POSTGRES_USER="${POSTGRES_USER:-postgres}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-postgres}"
POSTGRES_DB="${POSTGRES_DB:-ragdb}"
MODEL_NAME="${MODEL_NAME:-library/phi4-mini}"
MODELSERVER_PORT="${MODELSERVER_PORT:-8888}"

echo "================================================"
echo "RAG Chatbot Tutorial - Starting..."
echo "================================================"

# Clean up any existing pod
echo "Cleaning up any existing $POD_NAME pod..."
podman pod rm $POD_NAME --force -t 0 2>/dev/null || true

# Create volume for models
echo "Creating model volume..."
podman volume create rag-models 2>/dev/null || true

# Create pod with port mappings
echo "Creating $POD_NAME pod..."
podman pod create \
    --name $POD_NAME \
    --publish 8501:8501 \
    --publish ${MODELSERVER_PORT}:${MODELSERVER_PORT}

# Start PostgreSQL with pgvector
echo "Starting PostgreSQL with pgvector extension..."
podman run -d --rm \
    --pod $POD_NAME \
    --name $POD_NAME-pgvector \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e POSTGRES_DB=${POSTGRES_DB} \
    pgvector/pgvector:pg16

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
sleep 5

# Start ramalama model server
echo "Starting ramalama model server with ${MODEL_NAME}..."
echo "⏳ This may take a few minutes to download the model on first run..."

podman run -d --rm \
    --pod $POD_NAME \
    --name $POD_NAME-model \
    -v rag-models:/models:Z \
    quay.io/ramalama/ramalama:latest \
    ramalama --store /models serve \
    --port ${MODELSERVER_PORT} \
    --host 0.0.0.0 \
    ollama://phi4-mini:latest

# Wait for model server to be ready
echo "Waiting for model server to be ready..."
MAX_ATTEMPTS=60
ATTEMPT=0
while [ $ATTEMPT -lt $MAX_ATTEMPTS ]; do
    if curl -s "http://127.0.0.1:${MODELSERVER_PORT}/v1/models" >/dev/null 2>&1; then
        echo "✅ Model server is ready!"
        break
    fi
    ATTEMPT=$((ATTEMPT + 1))
    echo "Attempt $ATTEMPT/$MAX_ATTEMPTS - Waiting for model server..."
    sleep 5
done

if [ $ATTEMPT -eq $MAX_ATTEMPTS ]; then
    echo "❌ Error: Model server did not start within timeout"
    echo "Check logs with: podman logs $POD_NAME-model"
    exit 1
fi

# Build chatbot app container
echo "Building chatbot application container..."
podman build -t rag-chatbot-app:latest ./app

# Start chatbot application
echo "Starting RAG chatbot application..."
podman run -d --rm \
    --pod $POD_NAME \
    --name $POD_NAME-app \
    -e MODEL_ENDPOINT=http://127.0.0.1:${MODELSERVER_PORT} \
    -e MODEL_NAME=${MODEL_NAME} \
    -e POSTGRES_HOST=127.0.0.1 \
    -e POSTGRES_PORT=5432 \
    -e POSTGRES_DB=${POSTGRES_DB} \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e EMBEDDING_MODEL=BAAI/bge-small-en-v1.5 \
    -e COLLECTION_NAME=documents \
    rag-chatbot-app:latest

echo ""
echo "================================================"
echo "✅ RAG Chatbot is ready!"
echo "================================================"
echo ""
echo "Access the chatbot at: http://localhost:8501"
echo ""
echo "The pod contains 3 containers:"
echo "  • PostgreSQL + pgvector (database)"
echo "  • Ramalama model server (${MODEL_NAME})"
echo "  • Streamlit chatbot UI"
echo ""
echo "Useful commands:"
echo "  podman logs $POD_NAME-app          # View chatbot logs"
echo "  podman logs $POD_NAME-model        # View model server logs"
echo "  podman logs $POD_NAME-pgvector     # View database logs"
echo "  podman pod stop $POD_NAME          # Stop all containers"
echo "  ./stop.sh                          # Stop and remove pod"
echo ""
