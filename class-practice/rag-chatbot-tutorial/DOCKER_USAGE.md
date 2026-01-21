# Docker Usage Guide

This project supports both **CPU-only** and **NVIDIA GPU-accelerated** deployments using Docker or Podman.

## Quick Start

### CPU-Only Version (Lightweight)
```bash
docker compose -f docker-compose.cpu.yml up
```

### NVIDIA GPU Version (Requires NVIDIA GPU)
```bash
docker compose -f docker-compose.nvidia.yml up
```

Access the chatbot at: **http://localhost:8501**

---

## Understanding the Two Versions

### CPU Version (`Dockerfile.cpu`)
- **Image Size**: ~2-3 GB (much lighter!)
- **No CUDA dependencies** - uses PyTorch CPU-only
- **Best for**:
  - Development on laptops
  - Machines without NVIDIA GPUs
  - Testing and learning
  - Budget-conscious deployments

### NVIDIA GPU Version (`Dockerfile.nvidia`)
- **Image Size**: ~3-4 GB (slightly larger due to CUDA-enabled PyTorch)
- **Uses host GPU** via NVIDIA Container Runtime (no full CUDA toolkit in container!)
- **Best for**:
  - Production deployments with NVIDIA GPUs
  - Faster embedding generation
  - Larger datasets

**Important**: The NVIDIA version does NOT install the full CUDA toolkit in the container. It uses CUDA-enabled PyTorch libraries but relies on the host's NVIDIA drivers and CUDA installation through the NVIDIA Container Runtime. This keeps the image much smaller than traditional GPU containers.

---

## Prerequisites

### For CPU Version
- Docker or Podman installed
- That's it!

### For NVIDIA GPU Version
1. **NVIDIA GPU** on your host machine
2. **NVIDIA Drivers** installed on host
3. **NVIDIA Container Runtime** installed ([Installation Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html))
4. Docker configured to use NVIDIA runtime

#### Verify GPU Setup
```bash
# Test that Docker can access your GPU
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
```

---

## Build and Run Options

### Option 1: Docker Compose (Recommended)

#### CPU Version
```bash
# Create .env file (optional - uses defaults if not present)
cp env.template .env

# Start all services
docker compose -f docker-compose.cpu.yml up

# Run in background
docker compose -f docker-compose.cpu.yml up -d

# View logs
docker compose -f docker-compose.cpu.yml logs -f app

# Stop services
docker compose -f docker-compose.cpu.yml down
```

#### NVIDIA GPU Version
```bash
# Create .env file (optional - uses defaults if not present)
cp env.template .env

# Start all services
docker compose -f docker-compose.nvidia.yml up

# Run in background
docker compose -f docker-compose.nvidia.yml up -d

# View logs
docker compose -f docker-compose.nvidia.yml logs -f app

# Stop services
docker compose -f docker-compose.nvidia.yml down
```

### Option 2: Manual Docker Build

#### CPU Version
```bash
# Build
cd app
docker build -f Dockerfile.cpu -t rag-chatbot:cpu .

# Run (requires running PostgreSQL and model server separately)
docker run -p 8501:8501 \
  -e MODEL_ENDPOINT=http://model-server:8888 \
  -e POSTGRES_HOST=pgvector \
  # ... other env vars ...
  rag-chatbot:cpu
```

#### NVIDIA GPU Version
```bash
# Build
cd app
docker build -f Dockerfile.nvidia -t rag-chatbot:nvidia .

# Run with GPU access
docker run --gpus all -p 8501:8501 \
  -e MODEL_ENDPOINT=http://model-server:8888 \
  -e POSTGRES_HOST=pgvector \
  # ... other env vars ...
  rag-chatbot:nvidia
```

---

## Environment Variables

Create a `.env` file based on `env.template`:

```bash
# Database Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ragdb

# Model Configuration
MODEL_NAME=phi4-mini-instruct
MODELSERVER_PORT=8888

# Embedding Model (used by app)
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
COLLECTION_NAME=documents
```

---

## Performance Comparison

### Embedding Generation (1000 documents)
- **CPU**: ~30-60 seconds
- **GPU**: ~5-10 seconds (5-6x faster)

### First Run Model Download
Both versions download the same model (~2.5 GB for Phi-4-mini). The model is cached in a Docker volume.

---

## Image Size Comparison

```bash
# Check image sizes
docker images | grep rag-chatbot

# Example output:
# rag-chatbot:cpu      ~2.1 GB
# rag-chatbot:nvidia   ~3.2 GB
```

The CPU version saves **~1 GB** by using PyTorch CPU-only builds!

---

## Troubleshooting

### NVIDIA GPU Not Detected
```bash
# Check NVIDIA runtime is installed
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi

# If fails, install NVIDIA Container Runtime:
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html
```

### Out of Memory (GPU)
Reduce batch size or use CPU version for development.

### Model Server Takes Long to Start
First run downloads ~2.5 GB model. Subsequent runs are fast (model is cached).

---

## Switching Between CPU and GPU

You can switch versions at any time:

```bash
# Stop current version
docker compose -f docker-compose.cpu.yml down

# Start GPU version (shares same volumes!)
docker compose -f docker-compose.nvidia.yml up
```

The database and model volumes are shared between versions.

---

## For Students Using Podman

If you prefer Podman, replace `docker` with `podman` in all commands:

```bash
# CPU version
podman compose -f docker-compose.cpu.yml up

# GPU version (requires crun runtime for GPU support)
podman compose -f docker-compose.nvidia.yml up
```

**Note**: For GPU support with Podman, you need the `crun` runtime with NVIDIA support.

---

## Summary

✅ **Use CPU version** for development, testing, and non-GPU machines
✅ **Use NVIDIA version** for production with GPUs and faster performance
✅ **Both versions are lightweight** - no bloated CUDA toolkit in containers!
✅ **Easy to switch** between versions using docker-compose files
