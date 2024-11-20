# Setup Instructions (Using Locally Hosted LLAMA)

1. Download the [zipped lecture folder](https://drive.google.com/file/d/1s3an7jfe4upxEZhvoLSsnK2I8bzKYYOd/view?usp=drive_link) onto your laptop.
2. Unzip the folder, navigate to the root, and open it in either VSCode or Jupyter Lab.
3. To host the LLAMA model locally, download the quantized model from Hugging Face.
4. Install Hugging Face Hub:
   ```
   pip3 install huggingface-hub
   ```
   ```
   brew install huggingface-cli
   ```
5. Download the model:
   ```
   huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF mistral-7b-instruct-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
   ```
6. Install LLAMA-CPP in one of two ways:
   * First option:
     ```
     git clone https://github.com/ggerganov/llama.cpp
     cd llama.cpp
     make
     ```
   * Second option:
     ```
     pip install sse-starlette starlette_context pydantic-settings
     pip install llama-cpp-python
     ```
7. Host the model:
   ```
   python3 -m llama_cpp.server --model ./mistral-7b-instruct-v0.1.Q4_K_M.gguf --host 0.0.0.0 --port 8000 --n_gpu_layers 0
   ```
