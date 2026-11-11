#!/bin/bash

# RAG Chatbot Tutorial - Startup Script
# This script creates a pod with 2 containers:
# 1. PostgreSQL with pgvector extension
# 2. RAG chatbot UI (Streamlit)
# The model runs on your laptop with llmman, outside the pod.

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
MODEL_NAME="${MODEL_NAME:-gemma3:4b}"
LLMMAN_PORT="${LLMMAN_PORT:-17434}"
# Leave APP_IMAGE empty to build the app from ./app
APP_IMAGE="${APP_IMAGE:-}"

echo "================================================"
echo "RAG Chatbot Tutorial - Starting..."
echo "================================================"

# Check that llmman is serving on the laptop
echo "Checking for the llmman model server on port ${LLMMAN_PORT}..."
if ! curl -s "http://127.0.0.1:${LLMMAN_PORT}/v1/models" >/dev/null 2>&1; then
    echo "❌ Error: llmman is not running"
    echo "Start it in another terminal with: llmman serve"
    exit 1
fi
echo "✅ llmman is running"

# Clean up any existing pod
echo "Cleaning up any existing $POD_NAME pod..."
podman pod rm $POD_NAME --force -t 0 2>/dev/null || true

# Create pod with port mappings
echo "Creating $POD_NAME pod..."
podman pod create \
    --name $POD_NAME \
    --publish 8501:8501

# Start PostgreSQL with pgvector
echo "Starting PostgreSQL with pgvector extension..."
podman run -d --rm \
    --pod $POD_NAME \
    --name $POD_NAME-pgvector \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e POSTGRES_DB=${POSTGRES_DB} \
    docker.io/pgvector/pgvector:pg16

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
sleep 5

# Get the chatbot app image
if [ -n "$APP_IMAGE" ]; then
    echo "Pulling chatbot application image ${APP_IMAGE}..."
    podman pull ${APP_IMAGE}
else
    echo "Building chatbot application container..."
    echo "⏳ This takes a few minutes on first run..."
    APP_IMAGE="rag-chatbot-app:latest"
    podman build -t ${APP_IMAGE} ./app
fi

# Start chatbot application
# host.containers.internal is Podman's name for your laptop
echo "Starting RAG chatbot application..."
podman run -d --rm \
    --pod $POD_NAME \
    --name $POD_NAME-app \
    -e MODEL_ENDPOINT=http://host.containers.internal:${LLMMAN_PORT} \
    -e MODEL_NAME=${MODEL_NAME} \
    -e POSTGRES_HOST=127.0.0.1 \
    -e POSTGRES_PORT=5432 \
    -e POSTGRES_DB=${POSTGRES_DB} \
    -e POSTGRES_USER=${POSTGRES_USER} \
    -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
    -e EMBEDDING_MODEL=BAAI/bge-small-en-v1.5 \
    -e COLLECTION_NAME=documents \
    ${APP_IMAGE}

echo ""
echo "================================================"
echo "✅ RAG Chatbot is ready!"
echo "================================================"
echo ""
echo "Access the chatbot at: http://localhost:8501"
echo ""
echo "The pod contains 2 containers:"
echo "  • PostgreSQL + pgvector (database)"
echo "  • Streamlit chatbot UI"
echo "The model (${MODEL_NAME}) runs on your laptop with llmman."
echo ""
echo "Useful commands:"
echo "  podman logs $POD_NAME-app          # View chatbot logs"
echo "  podman logs $POD_NAME-pgvector     # View database logs"
echo "  podman pod stop $POD_NAME          # Stop all containers"
echo "  ./stop.sh                          # Stop and remove pod"
echo ""
