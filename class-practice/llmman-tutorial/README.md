# Class activity: Run an LLM on your laptop

**Time: 50 minutes.** Companion to [Lesson 8](../../lessons/lesson-8/README.md).
You will download an open model from Hugging Face, serve it on your own laptop
with [llmman](https://github.com/llmmanorg/llmman), talk to it four different
ways, and then remove everything you installed.

Nothing in this activity needs an account, an API key, or a payment.
Your prompts never leave your laptop.

## What you need

| | Requirement |
| --- | --- |
| Mac | Apple Silicon (M1 or newer). Check Apple menu > About This Mac. **Intel Macs are not supported:** pair with a classmate. |
| Windows | Windows 10 or 11, PowerShell. |
| Memory | 8 GB RAM or more. 16 GB is comfortable. |
| Disk | About 5 GB free. |
| Podman | Only for step 6. You installed it earlier in the course. |

## Checkpoints

| Minutes | Work | Evidence you can show |
| --- | --- | --- |
| Before class | Install llmman and download the model | `llmman ls` lists `gemma3:4b` |
| 0–10 | Chat in the terminal, inspect the model | A reply, and the model's parameter count |
| 10–20 | Chat in the browser | A reply at `http://127.0.0.1:17434` |
| 20–30 | Call the API with `curl` and Python | JSON from `curl`, an answer from `ask.py` |
| 30–40 | Run a chat app in a container | A persona you created in NextChat |
| 40–45 | Find the model's limits | One confidently wrong answer |
| 45–50 | Remove everything | The cleanup checks print nothing |

## 0. Before class: install and download (about 10 minutes)

The model is a 3 GB download. On shared classroom Wi-Fi this can take a long
time, so **please do this step at home before class.**

All commands pin llmman to version `v0.1.586`, the version these instructions
were tested with. Copy them exactly.

### Mac (Apple Silicon)

Open **Terminal** and run:

```bash
curl -fsSL https://llmmanorg.github.io/install.sh | LLMMAN_VERSION=v0.1.586 sh
```

This places one file, `llmman`, in `~/.local/bin`. If the installer says
`~/.local/bin` is not on your PATH, run the `echo 'export PATH=...'` line it
prints, then **close and reopen Terminal**. Check:

```bash
llmman --version
```

You should see `llmman 0.1.586`.

### Windows

Open **PowerShell** (not WSL) and run:

```powershell
$env:LLMMAN_VERSION = "v0.1.586"
irm https://llmmanorg.github.io/install.ps1 | iex
```

This places `llmman.exe` in `%LOCALAPPDATA%\Microsoft\WindowsApps`, which is
already on your PATH. Close and reopen PowerShell, then check:

```powershell
llmman --version
```

All remaining commands are the same on Mac and Windows unless noted.

### Download the model

```bash
llmman pull gemma3:4b
llmman ls
```

`llmman ls` should list `docker.io/ai/gemma3:4b` at about 3.3 GB.

> **Type the name exactly: `gemma3:4b`.** Other spellings, such as `ai/gemma3`,
> look on Hugging Face instead and fail with a confusing `401` error.

The first time llmman starts, it also downloads its inference engine
(`llama.cpp`) and, on a Mac, a few hundred MB of helper tools. That is
expected. Everything lands in one folder, which you will delete at the end.

**Checkpoint:** `llmman ls` lists `gemma3:4b`.

## 1. Chat in the terminal and inspect the model (0–10 minutes)

```bash
llmman run gemma3:4b
```

The first reply takes a few seconds while the model loads into memory. Try:

```text
In two sentences, what is a large language model?
Write a haiku about debugging.
```

Type `/bye` to exit.

Now look at what you downloaded:

```bash
llmman show gemma3:4b
```

Find these lines and write down the values:

| Field | What it means |
| --- | --- |
| `parameters` | How many numbers (weights) the model learned. `3.9B` is 3.9 billion. |
| `quantization` | How much those numbers were compressed. `Q4_K` is about 4 bits each. |
| `context length` | The most text, in tokens, the model can consider at once. |
| `ai.model.repo` | The **Hugging Face** repository the file came from. |

Open `https://huggingface.co/` followed by the `ai.model.repo` value in your browser.
That page is the model card: who made the model, its license, and how it was trained.

**Checkpoint:** a reply, and you can say how many parameters your model has.

## 2. What just happened: the model server (reading, 1 minute)

`llmman run` did not run the model itself. It quietly started a **model server**,
`llmman serve`, in the background. The server loads the model and answers
requests on `http://127.0.0.1:17434`. The terminal chat was one client.
Next you will connect three more clients to the **same** server.

```bash
llmman ps
```

This shows which models are loaded in memory right now. An idle model unloads
after five minutes. The server itself keeps running until you stop it in step 8.

## 3. Chat in the browser (10–20 minutes)

Open [http://127.0.0.1:17434](http://127.0.0.1:17434) in your browser.
This chat page is built into llmman. Nothing new was installed.

1. Choose `gemma3:4b` in the model picker and send a message.
2. Gemma 3 can also **read images**. Attach a photo or screenshot and ask
   `What is in this image?`
3. Turn off Wi-Fi and send another message. It still works: the model is on
   your laptop. Turn Wi-Fi back on.

**Checkpoint:** a reply in the browser.

## 4. Call the API (20–30 minutes)

A model server speaks an **API**: a fixed format for requests and replies.
llmman speaks the OpenAI format, which most AI apps understand.

### With `curl`

Mac Terminal:

```bash
curl http://127.0.0.1:17434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gemma3:4b", "messages": [{"role": "user", "content": "Say hello in five words."}]}'
```

Windows PowerShell (quoting JSON for `curl` is painful there, so use PowerShell's own command):

```powershell
$body = @{
  model = "gemma3:4b"
  messages = @(@{ role = "user"; content = "Say hello in five words." })
} | ConvertTo-Json -Depth 5
Invoke-RestMethod http://127.0.0.1:17434/v1/chat/completions -Method Post -ContentType "application/json" -Body $body | ConvertTo-Json -Depth 5
```

Read the JSON that comes back. Find the answer inside
`choices` > `message` > `content`. Find `usage`: how many tokens did your
question and the answer use?

### With Python

[`ask.py`](ask.py) sends the same request with Python's standard library,
so there is nothing to `pip install`. From this folder:

```bash
python3 ask.py "What is Hugging Face, in one sentence?"
```

Windows: use `py ask.py "..."` if `python3` is not found.

Open `ask.py` in an editor. Change the **system** message, for example to
`You are a pirate. Answer in pirate speak.`, save, and ask the same question.
The system message is instructions the app gives the model before your question.

**Checkpoint:** an answer from `ask.py` with your own system message.

## 5. Optional: a second model

If you have time and disk space, download Microsoft's Phi-4-mini (2.5 GB):

```bash
llmman pull hf.co/unsloth/Phi-4-mini-instruct-GGUF
llmman run hf.co/unsloth/Phi-4-mini-instruct-GGUF "In one sentence, what is a local LLM?"
```

This name points **directly at a Hugging Face repository**. Ask both models
the same question and compare the answers.

## 6. Find the model's limits (40–45 minutes)

A 4-billion-parameter model is small. Try to catch it being confidently wrong:

```text
What is today's date?
Who won the most recent World Series?
What is the mascot of our school?
How many r's are in "strawberry"?
```

The model has no internet access and no clock. It only knows its training data.
When it does not know, it may still answer fluently. When we tested Phi-4-mini, it
said a "local LLM" is a model trained on a regional dialect. That is a
**hallucination**.

Write down one wrong answer and why you think the model got it wrong.

## 7. Remove everything (45–50 minutes)

Do this even if you plan to use llmman again. You can reinstall in a minute.

### Mac

```bash

# 1. Stop the model server (this also stops the model it loaded)
pkill -f "llmman serve"

# 2. The program, the models, and everything llmman downloaded
rm ~/.local/bin/llmman
rm -rf ~/.local/share/llmman ~/.config/llmman
```

If you added the PATH line during install and want it gone, delete the
`export PATH="$HOME/.local/bin:$PATH"` line from `~/.zshrc`. It is harmless to keep.

Check that nothing is left. **Each command should print nothing:**

```bash
pgrep -fl llmman
ls ~/.local/share/llmman 2>/dev/null
podman ps -a --filter name=nextchat --format '{{.Names}}'
```

### Windows (PowerShell)

```powershell

# 1. Stop the model server and the model it loaded
Stop-Process -Name llmman, llama-server -ErrorAction SilentlyContinue

# 2. The program, the models, and everything llmman downloaded
Remove-Item "$env:LOCALAPPDATA\Microsoft\WindowsApps\llmman.exe*"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\llmman", "$env:APPDATA\llmman" -ErrorAction SilentlyContinue
```

Check. **Each command should print nothing:**

```powershell
Get-Process llmman, llama-server -ErrorAction SilentlyContinue
Test-Path "$env:LOCALAPPDATA\llmman"   # should print False
```

**Checkpoint:** the checks print nothing (or `False`), and about 4 GB of disk is back.

### Things llmman did *not* install

llmman does not add a login item, a startup service, or a background app.
If you restart your computer before cleaning up, the server will not come back
by itself. You still need the delete commands above to free the disk space.

## Privacy note

`llmman serve` keeps a short log of the prompts it has seen in
`prompts.jsonl` inside its data folder, so `llmman log` can show your history.
It stays on your laptop and is deleted in step 8. To turn it off, set
`LLMMAN_NOHISTORY=1` before starting llmman.

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| `llmman: command not found` | Close and reopen the terminal. On Mac, run the PATH line the installer printed. |
| Installer says Intel Mac not supported | Pair with a classmate. llmman has no Intel Mac build. |
| `HTTP 401` from Hugging Face | Check the model name. Use `gemma3:4b` exactly. |
| Download is very slow | Classroom Wi-Fi is shared. Pair with someone who downloaded at home. |
| First reply takes a long time | The model is loading into memory. Later replies are faster. |
| Browser page at port 17434 does not load | Run `llmman run gemma3:4b "hi"` first. That starts the server. |
| Laptop gets slow or hot | That is the model using your GPU. Close other apps. Stop the server with step 7, part 2. |
| Out of disk space | Skip step 5. Run `llmman rm <name>` to delete a model. |
