# Sources and refresh notes

Reviewed October 27, 2026.

## Tested on macOS 26.2, Apple Silicon, 32 GB RAM

- llmman `v0.1.586`, installed with `LLMMAN_VERSION=v0.1.586` (installs to
  `~/.local/bin`; without the pin, Macs that have Homebrew get a Homebrew install instead).
- `llmman pull gemma3:4b` resolved to `docker.io/ai/gemma3:4b` (3.3 GB, 3.9B
  parameters, Q4_K, repo label `unsloth/gemma-3-4b-it-GGUF`). `ai/gemma3` without
  the `docker.io/` prefix failed with a Hugging Face `401`.
- `hf.co/unsloth/Phi-4-mini-instruct-GGUF` (2.5 GB) pulled and ran. Its answer to
  "In one sentence, what is a local LLM?" is the hallucination quoted on the slides.
- First run also downloaded llama.cpp (Metal build) and, on macOS, mlx-lm and uv
  (about 450 MB) into `~/.local/share/llmman`.
- Built-in web UI at `http://127.0.0.1:17434/`, OpenAI API (`/v1/chat/completions`),
  `ask.py`, and NextChat (`docker.io/yidadaa/chatgpt-next-web:latest`, 199 MB) via
  `host.containers.internal:17434` from a libkrun Podman machine all worked.
  The NextChat page and API proxy responded; the Masks UI was not clicked through.
- RamaLama 0.25 was evaluated as an alternative. It worked, but in our test it took
  about 6 minutes to download a 2.5 GB file that llmman fetched in 33 seconds,
  and its container ran on CPU on macOS.

## References

- [llmman](https://github.com/llmmanorg/llmman): commands, store locations,
  serve API, web UI (`docs/webui.md`), configuration (`docs/configuration.md`).
- [Hybrid inference with llmman](https://llmmanorg.github.io/blog/hybrid-inference/)
- [Hugging Face Hub documentation](https://huggingface.co/docs/hub/index)
- [GGUF on Hugging Face](https://huggingface.co/docs/hub/gguf)
- [Gemma 3 4B model card](https://huggingface.co/google/gemma-3-4b-it)
- [Phi-4-mini-instruct model card](https://huggingface.co/microsoft/Phi-4-mini-instruct) (MIT license)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Ollama](https://ollama.com)
- [LM Studio](https://lmstudio.ai)
- [RamaLama](https://github.com/containers/ramalama)
- [vLLM](https://github.com/vllm-project/vllm) and the
  [PagedAttention paper](https://arxiv.org/abs/2309.06180)
- [SGLang](https://github.com/sgl-project/sglang) and the
  [SGLang paper](https://arxiv.org/abs/2312.07104)
- [MLX-LM](https://github.com/ml-explore/mlx-lm)
- [NextChat](https://github.com/ChatGPTNextWeb/NextChat)

## Course context

The Udemy course "Zero to Hero in Ollama" (Start-Tech Academy) was used only as a
topic outline (install, CLI, web UI, vision models, custom models, Python and the
OpenAI-compatible API). No course content was purchased, viewed, or reused.
