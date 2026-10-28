---
theme: default
title: DS 219 - Run an LLM on Your Laptop
info: |
  Lesson 8: what an LLM is, Hugging Face, model servers, and serving an open model locally with llmman.
author: Sally O'Malley
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-8
lineNumbers: true
---

<div class="eyebrow">Fall 2026 · Lesson 8</div>

# Run an LLM<br>on <span class="accent">your laptop</span>

<p class="lede">Models, Hugging Face, and model servers</p>

<div class="footer-note">Sally O'Malley · DS 219</div>

<!--
Lesson 7 used free hosted models inside OpenCode. Today the model runs on the student's own machine. Students were asked to install llmman and download gemma3:4b before class. Check who still needs to download before you start talking; start that now, on the best network available.
-->

---

# Today's class

| Time | Work |
| --- | --- |
| 30 min | LLMs, Hugging Face, and model servers |
| 10 min | Demo: one model, four clients |
| 10 min | Break |
| 50 min | Hands-on activity, ending with cleanup |
| 5 min | Exit ticket |

<p class="lede">Not downloaded yet? Start <code>llmman pull gemma3:4b</code> now.</p>

<!--
Assumes the usual 105-minute meeting. The download is about 3.3 GB plus about 0.5 GB of runtime helpers on first use. On a fast connection that is two minutes; on shared Wi-Fi with thirty laptops it can be much longer. Pair students who could not download in advance.
-->

---

# Where the model lived last week

**Lesson 7:** OpenCode sent your prompts to a hosted model on someone else's servers.

**Today:** the model file is on your disk, and your laptop does the math.

| | Hosted | Local |
| --- | --- | --- |
| Your prompts go to | A company's servers | Nowhere |
| Cost | Free tier, subscription, or per token | Your electricity |
| Works offline | No | Yes |
| Model size and quality | Very large models | Small enough for your RAM |

<!--
Connect to Lesson 6's split between a model and a harness. The harness (OpenCode, a chat app) is the same kind of software either way. Only where the model runs changes. Neither column is "better": it is a set of tradeoffs.
-->

---

# What is a large language model?

A program that **predicts the next token** of text, over and over.

1. Your text is split into **tokens**: words and word pieces.
2. The model scores every possible next token.
3. One is chosen, appended, and the process repeats.

<p class="question">If it only predicts the next word, how can it answer questions?</p>

<!--
Keep this intuitive. Training on enormous amounts of text makes "a plausible continuation of a question" usually look like an answer. Chat models get extra training so they follow instructions. This also sets up the hallucination discussion: plausible is not the same as true.
-->

---

# What is inside a model file?

| Term | Meaning | gemma3:4b |
| --- | --- | --- |
| Parameters | Numbers (weights) learned in training | 3.9 billion |
| Quantization | How compressed each number is | About 4 bits |
| Context length | Most tokens it can consider at once | 131,072 |
| Template | How a chat is formatted for this model | Gemma's format |

<p class="lede">You will read these values yourself with <code>llmman show</code>.</p>

<!--
Values are from llmman show gemma3:4b on the tested setup. Parameter counts are why people say "a 4B model" or "a 70B model". The template is a detail students rarely see: each model family expects chat turns marked up in its own way, and the server applies it.
-->

---

# Why a 4B model fits on a laptop

| Precision | Bytes per parameter | 4B model |
| --- | --- | --- |
| 16-bit (original) | 2 | About 8 GB |
| 8-bit | 1 | About 4 GB |
| **4-bit (today)** | **About 0.5** | **About 2.5–3 GB** |

**Quantization** trades a little quality for a lot less memory.

<p class="question">How much memory would a 70B model need at 4 bits?</p>

<!--
Answer: about 35–40 GB, beyond most laptops. That is roughly why frontier-scale models live in data centers. The download listed as 3.3 GB includes a vision component (the mmproj file) alongside the language weights.
-->

---

# Open models and hosted models

**Open-weight models:** you can download the weights.
Gemma (Google), Phi (Microsoft), Llama (Meta), Qwen (Alibaba), Mistral, and more.

**Hosted-only models:** you send requests to the company's API.
GPT (OpenAI), Claude (Anthropic), Gemini (Google).

<p class="lede">"Open weights" is not always "open source." Read the license.</p>

<!--
Link back to Lesson 1's open-source licensing. Some open-weight models use OSI-style licenses (Phi-4-mini is MIT); others use custom terms with use restrictions (Gemma has its own terms of use). Having the weights is different from having the training data and code.
-->

---

# Hugging Face

The "GitHub of machine learning."

| On Hugging Face | Like on GitHub |
| --- | --- |
| Model repositories, named `org/model` | Code repositories, named `owner/repo` |
| Model cards (README) | README files |
| Datasets | Test fixtures and data |
| Spaces: hosted demos | Pages sites |

Example: `unsloth/gemma-3-4b-it-GGUF`

<!--
Today's gemma3:4b file came from unsloth/gemma-3-4b-it-GGUF, according to llmman show. Google publishes the original weights at google/gemma-3-4b-it; community groups such as unsloth and ggml-org publish quantized GGUF versions. Hugging Face repos are Git repos with large-file storage. You can browse without an account; some models require accepting a license first.
Source: https://huggingface.co/docs/hub/index
-->

---

# Reading a model card

Before you run a model, find:

- **Who made it** and what it was trained to do
- **License** and any use restrictions
- **Size:** parameters and file sizes for each quantization
- **Limitations:** languages, known failure modes, safety notes

<p class="question">Would you use a model whose card has none of these?</p>

<!--
Show a real card live if time allows: https://huggingface.co/google/gemma-3-4b-it. Treat the card as the model's documentation and a source of evidence, not marketing.
-->

---

# Two common file formats

| Format | Typical use | Served by |
| --- | --- | --- |
| **safetensors** | Original full-precision weights | vLLM, SGLang, Transformers |
| **GGUF** | Single file, often quantized for laptops | llama.cpp and tools built on it |

<p class="lede">Today: a GGUF file, served by llama.cpp, managed by llmman.</p>

<!--
Repos ending in -GGUF usually hold several quantization levels (Q4_K_M, Q8_0, and so on). Students do not need to choose today: llmman picks a default. Apple's MLX format also exists for Mac-specific serving.
Source: https://huggingface.co/docs/hub/gguf
-->

---

# What is a model server?

A program that:

1. **Loads** model weights into memory (GPU when it can)
2. **Listens** on an HTTP port for requests
3. **Generates** tokens and sends them back

<p class="lede">One server, many clients: a terminal, a browser, a script, an app.</p>

<!--
Analogy from the website lesson: python3 -m http.server served files on localhost; a model server serves model output on localhost. Loading takes seconds and lots of memory, so the server keeps the model loaded between requests, then unloads it when idle.
-->

---

# One server, many clients

```text
 terminal     browser     curl / ask.py     NextChat
    └────────────┴─────────────┴──────────────┘
                       │  HTTP, port 17434
                 llmman serve       routes requests, loads models
                       │
                 llama-server       does the math
                       │
                 gemma3:4b          the weights on disk
```

<p class="lede">Every client uses the same HTTP API.</p>

<!--
This is the shape of the activity. llmman serve is the front door: it routes requests, loads and unloads models, and keeps logs. It runs llama.cpp's llama-server as the engine that does the math. Containers reach the laptop through host.containers.internal.
-->

---

# The API most AI apps speak

```bash
curl http://127.0.0.1:17434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gemma3:4b",
       "messages": [{"role": "user", "content": "Say hello"}]}'
```

Reply: `choices[0].message.content`, plus token `usage`.

<p class="lede">OpenAI's format became the common standard. Change the URL, keep the app.</p>

<!--
Most servers on the next slide, and most hosted providers, accept this request shape. That is why the same chat app can talk to OpenAI, to a hosted open model, or to your laptop. Messages have roles: system (instructions), user, and assistant.
-->

---

# Model servers for your laptop

| Server | Best known for |
| --- | --- |
| **llama.cpp** | The engine for GGUF models; powers many other tools |
| **Ollama** | Easy setup, its own model library, a background service |
| **LM Studio** | Desktop app with a graphical model browser |
| **RamaLama** | Runs models in Podman/Docker containers |
| **llmman** | Pulls from Hugging Face or any OCI registry; launches agents |
| **MLX-LM** | Apple's framework for Apple Silicon |

<!--
These are laptop/desktop tools; the next slide covers data center servers (vLLM, SGLang). Several tools sit on top of others: Ollama, RamaLama, and llmman can all use llama.cpp for GGUF; llmman can also hand safetensors models to vLLM, SGLang, or MLX-LM. We tested RamaLama for this class; llmman downloaded faster and used the Mac GPU.
Sources: see sources.md.
-->

---

# Model servers for the data center

| Server | Best known for |
| --- | --- |
| **vLLM** | High-throughput serving on large GPUs |
| **SGLang** | Fast serving for many users, structured and agent workloads |

| | Laptop | Data center |
| --- | --- | --- |
| Users | One | Thousands at once |
| Goal | Easy and private | Throughput and cost per token |

<p class="lede">Same idea, different scale: load weights, serve tokens over HTTP.</p>

<!--
vLLM's PagedAttention and SGLang's RadixAttention manage GPU memory so many conversations can share hardware. Students only need the intuition: serving one person is easy; serving millions cheaply is an engineering field. This is a real career area.
Sources: https://arxiv.org/abs/2309.06180; https://arxiv.org/abs/2312.07104
-->

---

# Today's tool: llmman

```bash
llmman pull gemma3:4b     # download from a registry
llmman run gemma3:4b      # chat (starts the server)
llmman show gemma3:4b     # read the model's details
llmman ps                 # what is loaded right now
llmman rm gemma3:4b       # delete the model
```

No account. No startup service. One program and one data folder.

<!--
Why llmman for this class: no login item or service on Mac or Windows; the files live in one folder; we pinned v0.1.586, the version these instructions were tested on. The server keeps running until stopped, and cleanup is part of the activity. Intel Macs are not supported: pair those students.
Source: https://github.com/llmmanorg/llmman
-->

---

# Demo: one model, four clients

1. `llmman run gemma3:4b` in the terminal
2. The built-in chat page at `http://127.0.0.1:17434`
3. `curl` and a 30-line Python script
4. NextChat in a Podman container

<p class="question">Which of these needed the internet after the download?</p>

<!--
Answer: none, except pulling the NextChat image. Show Wi-Fi off during the browser chat if comfortable. Show gemma3 describing an image. Keep the demo under ten minutes.
-->

---
layout: center
class: text-center
---

# Class activity · 50 minutes

[Open the llmman activity](https://github.com/DS219/spark-seprep/blob/main/class-practice/llmman-tutorial/README.md)

<p class="lede" style="margin: 1.5rem auto">Serve a model. Connect four clients.<br>Catch a mistake. Remove everything.</p>

<!--
The link targets the main branch; until the changes are merged, open the local README or a review branch URL. Confirm students have the activity open, then start the timer.
-->

---

# Practice checkpoints

| Elapsed | Checkpoint |
| --- | --- |
| 10 min | Terminal reply; you know your model's parameter count |
| 20 min | Reply in the browser chat |
| 30 min | `curl` JSON and `ask.py` with your own system message |
| 40 min | A NextChat persona you created |
| 45 min | One confidently wrong answer |
| 50 min | Cleanup checks print nothing |

<!--
Leave this up while students work. Students without Podman skip the NextChat step; everything else works without containers. Protect the last five minutes for cleanup: it is part of the lesson, not an afterthought.
-->

---

# A container talking to your laptop

```bash
podman run -d --name nextchat -p 127.0.0.1:3000:3000 \
  -e BASE_URL=http://host.containers.internal:17434 \
  -e OPENAI_API_KEY=sk-local \
  -e CUSTOM_MODELS=-all,+gemma3:4b \
  docker.io/yidadaa/chatgpt-next-web:latest
```

`host.containers.internal` is the container's name for your laptop.

<!--
Ties back to the containers lesson. The NextChat image is about 200 MB. The API key is a placeholder that llmman does not check. Masks in NextChat are system prompts with a friendly interface: the same idea as editing the system message in ask.py.
Source: https://github.com/ChatGPTNextWeb/NextChat
-->

---

# Small models make things up

When we asked Phi-4-mini "What is a local LLM?" it said:

<p class="lede">"A model trained on a dataset specific to a particular region or community."</p>

Confident, fluent, and wrong. This is a **hallucination**.

<p class="question">How would you check an answer you cannot verify yourself?</p>

<!--
This happened in our own test run of the activity. A local model has no web search and no clock; it only knows its training data. Smaller models hallucinate more. Relate to Lesson 7: an agent's claim is not evidence; a working page is.
-->

---

# Always clean up

| What | How |
| --- | --- |
| Chat app | `podman rm -f nextchat`, then `podman rmi` the image |
| Model server | `pkill -f "llmman serve"` (Windows: `Stop-Process`) |
| Program | Delete `llmman` from `~/.local/bin` |
| Models and data | Delete `~/.local/share/llmman` |

<p class="lede">Know what you installed, where it lives, and how to remove it.</p>

<!--
Full Mac and Windows commands, plus checks that should print nothing, are in step 8 of the activity. This is a professional habit: every tool you install on a work machine is something you are responsible for.
-->

---

# Where this goes next

**Local models in a coding agent:** `llmman launch opencode --model gemma3:4b`

**Hybrid:** keep small requests local and send oversized ones to a hosted model.

<p class="lede">The harness from Lesson 7, with the model from today.</p>

[Hybrid inference with llmman](https://llmmanorg.github.io/blog/hybrid-inference/)

<!--
Optional, not part of today's activity. launch needs the OpenCode command-line tool installed, not only OpenCode Desktop. A 4B model is a weak coding agent; the point is the architecture, not the quality. The hybrid blog post describes routing by request size, never by guessing difficulty.
Sources: https://github.com/llmmanorg/llmman; https://llmmanorg.github.io/blog/hybrid-inference/
-->

---
layout: center
class: text-center
---

# Exit ticket

<p class="lede" style="margin: 1.5rem auto">How many parameters does your model have?<br>Name one model server besides llmman.<br>Show that your cleanup checks print nothing.</p>

<!--
Quick verbal round or a show of terminals. Remind students that they can reinstall llmman any time with the pinned command in the activity.
-->
