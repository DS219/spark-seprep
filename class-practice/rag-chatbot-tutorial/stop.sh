#!/bin/bash

# RAG Chatbot Tutorial - Stop Script
# This script stops and removes the RAG chatbot pod and all its containers

POD_NAME="rag-chatbot"

echo "Stopping $POD_NAME pod..."
podman pod stop $POD_NAME 2>/dev/null || echo "Pod not running"

echo "Removing $POD_NAME pod and containers..."
podman pod rm $POD_NAME --force 2>/dev/null || echo "Pod not found"

echo "✅ RAG Chatbot stopped and removed"
echo ""
echo "Note: llmman is still running on your laptop."
echo "Stop it with Ctrl+C in its terminal."
