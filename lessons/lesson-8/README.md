# Lesson 8: Run an LLM on Your Laptop

Follows Lesson 7. Covers what an LLM is, Hugging Face, model files and
quantization, model servers (llama.cpp, Ollama, LM Studio, RamaLama, llmman,
vLLM, SGLang, MLX-LM), and the OpenAI-compatible API. Students serve
`gemma3:4b` locally with llmman, connect four clients, and remove everything.
Uses the same Slidev tooling and shared visual system as the other course lessons.

## Present

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-8
npm ci
npm run dev
```

Press `P` for presenter mode. Build or export for offline use:

```bash
npm run build
npm run export
```

## Materials

- [Slides](slides.md), with speaker notes
- [50-minute class activity](../../class-practice/llmman-tutorial/README.md)
  and its [`ask.py`](../../class-practice/llmman-tutorial/ask.py) script
- [Sources and refresh notes](sources.md)

## Before class

- **Ask students to install llmman and run `llmman pull gemma3:4b` at home.**
  Step 0 of the activity is written to be sent ahead of time. The model is
  3.3 GB, plus about 0.5 GB of runtime helpers on the first Mac run.
- The activity pins llmman `v0.1.586`. That version was tested end to end on
  macOS (Apple Silicon) on October 27, 2026. If you change the pin, rerun the activity.
- Windows commands follow the official installer and docs but were **not**
  tested on a Windows machine. Have a Windows student try step 0 early.
- llmman has no Intel Mac build. Pair those students.
- NextChat (step 6) needs a running Podman machine. Students without Podman
  skip that step.
- Activity links target the `main` branch. Until changes are published, open the
  local activity or use a review branch URL.
- The Pages workflow includes Lesson 8. Publishing requires merging to `main`.
