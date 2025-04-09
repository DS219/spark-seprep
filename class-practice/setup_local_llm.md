# Setup Instructions (Using Locally Hosted LLAMA)

1. Download the [zipped lecture folder](https://drive.google.com/file/d/1s3an7jfe4upxEZhvoLSsnK2I8bzKYYOd/view?usp=drive_link) onto your laptop.
      * `mkdir ~/Desktop/local-llm-practice`
      * Download to your `~/Desktop/local-llm-practice/` directory.
      * You should now have `~/Desktop/local-llm-practice/LLM_Infrastructure_Class_Exercise.zip`
3. Unzip the folder, navigate to the root, and open it in either VSCode or Jupyter Lab.
      * To unzip, navigate to the folder from your laptop's file finder app, then click on the zip file. This should unzip the file.
5. To host the LLAMA model locally, download the quantized model from Hugging Face.
6. Install Hugging Face Hub:
   ```
   cd ~/Desktop/local-llm-practice
   python3 -m venv venv-local-llm
   source venv-local-llm/bin/activate
   # you should now be in a virtual env
   pip3 install huggingface-hub huggingface-hub[cli] uvicorn fastapi
   ```
7. Download the model:
   ```
   huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.1-GGUF mistral-7b-instruct-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
   ```
8. Install LLAMA-CPP in one of two ways:
   * First option:
     ```
     git clone https://github.com/ggerganov/llama.cpp
     cd llama.cpp
     make
     ```
   * Second option (probably what you want):
     ```
     pip install sse-starlette starlette_context pydantic-settings
     pip install llama-cpp-python
     ```
9. Host the model:
   ```
   python3 -m llama_cpp.server --model ./mistral-7b-instruct-v0.1.Q4_K_M.gguf --host 0.0.0.0 --port 8000 --n_gpu_layers 0
   ```

10. Start a simple chatbot:
    * Open a new terminal
    * Follow the chatbot [README](../local-chatbot/README.md)
    * visit your browser at `localhost:8501`
