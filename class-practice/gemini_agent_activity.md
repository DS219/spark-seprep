# Class Activity: Your First Agent Loop (Gemini API)

Companion activity for Lesson 6. We go from one plain model call to a model
that can take an action on its own, the same "observe, inspect, choose, act"
loop from tonight's slides, built with about 20 lines of Python.

Bring: a free Gemini API key (Google AI Studio). If you don't have one yet,
stop here and create one first: https://aistudio.google.com/apikey

Windows: use your WSL terminal, same as Lesson 2. Every command below is
bash and works there unchanged.

## 0. Create a working directory

```bash
mkdir ~/Desktop/gemini-agent-activity
cd ~/Desktop/gemini-agent-activity
```

Open this folder in VS Code (`code .`) and open its integrated terminal for
every step below.

## 1. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your prompt. Install the SDK:

```bash
pip install -U google-genai
```

## 2. Set your API key as an environment variable

Never paste your key into a script or commit it to Git. Set it for this
terminal session only:

```bash
export GEMINI_API_KEY="paste-your-key-here"
```

This variable disappears when you close the terminal, which is fine for
tonight. Check it worked:

```bash
python3 -c "import os; print('set' if os.environ.get('GEMINI_API_KEY') else 'missing')"
```

That only confirms the variable is set, not that the key is valid. Check the
key itself against the real API:

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

A JSON list of model objects means the key works. A `400` or `403` means the
key is wrong, not yet active, or billing/terms were never accepted in AI
Studio, fix that now before moving on.

That raw JSON is a lot to read in a hurry. For a clean list of just the
model names you can actually call, create `list_models.py`:

```python
from google import genai

client = genai.Client()

for model in sorted(client.models.list(), key=lambda m: m.name):
    if "generateContent" not in (model.supported_actions or []):
        continue
    name = model.name.removeprefix("models/")
    print(f"{name:28} {model.display_name}")
```

```bash
python3 list_models.py
```

This filters out embedding, image, and video-only models and prints just
the ones you can drop into `model=` for the rest of this activity.

One more check, specific to the model this activity actually uses
(`gemini-3.5-flash-lite`):

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"contents":[{"parts":[{"text":"Say hello in five words or fewer."}]}]}'
```

A short reply in the JSON `text` field means this exact model works for your
key. If this 404s but the step 2 `models` list still shows
`gemini-3.5-flash-lite`, double-check you typed the model name correctly in
the URL, no typos, no extra spaces.

## 3. Stage 1 — one plain call

Create `stage1_plain_call.py`:

```python
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain what a coding agent is, in two sentences, for a beginner.",
)

print(response.text)
```

Run it:

```bash
python3 stage1_plain_call.py
```

This is the whole LLM: text in, text out, one call, no memory, no tools.
Everything after this is the harness we built around it.

## 4. Stage 2 — a loop (still just an LLM)

Create `stage2_chat_loop.py`:

```python
from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-3.5-flash-lite")

print("Chat with Gemini. Type 'quit' to stop.")
while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() == "quit":
        break
    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}")
```

Run it and have a short back-and-forth. `chat.send_message` keeps the prior
turns in context for you. This is the "observe, choose, act" loop, except
the only action the model can take is replying with more text. It still
cannot look at your files, do math reliably, or check anything real.

## 5. Stage 3 — give it a tool (this is the agent moment)

Create `stage3_agent.py`:

```python
import os
from google import genai

def list_files() -> str:
    """Lists the files in the current working directory."""
    return "\n".join(os.listdir("."))

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What files are in my current directory?",
    config={"tools": [list_files]},
)

print(response.text)
```

Run it:

```bash
python3 stage3_agent.py
```

Nothing in your prompt told the model what files exist. It read the
`list_files` function's name, type hints, and docstring, decided to call it,
the SDK ran your Python function locally, and the result went back to the
model before it wrote an answer. That decide-then-call step is the agent
loop from tonight's slides, running for real.

### Give it a second tool

Add this function above `response = ...` and add it to the `tools` list:

```python
def add_numbers(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b
```

```python
    config={"tools": [list_files, add_numbers]},
```

Change the prompt to `"What is 482 plus 919, and what files are in my
directory?"` and run it again. One call, two tool uses, same loop.

## What just happened, in harness terms

| Stage | What the model can do | Harness ingredient from tonight |
| --- | --- | --- |
| 1 | Answer from training data only | None, just the raw LLM |
| 2 | Answer using the conversation so far | Memory / transcript |
| 3 | Decide to run your code, then answer using the result | Structured tools |

Real coding agents like Claude Code, Codex, and OpenCode use this same
decide-call-respond loop, just with dozens of tools (read file, edit file,
run shell command, search the web) and an approval step before anything
risky runs.

## Troubleshooting

- `API key not valid`: re-check the `export` command ran in *this* terminal
  tab; a new tab needs it set again. Re-run the step 2 `curl` check to
  confirm.
- `404` / model not found: Gemini model names change over time. Re-run the
  step 2 `curl` check, it returns a JSON list of every model your key can
  currently use, and swap the right name into the `model=` argument.
- `429` rate limited: the free tier has a requests-per-minute cap. Wait a
  minute and try again; this is expected under classroom load.
- Nothing happens / hangs: check your wifi; the call goes out to Google's
  servers, not a local model.
- `Warning: there are non-text parts in the response: ['thought_signature']`:
  harmless. The model does some internal "thinking" before answering, and
  the SDK is noting it skipped that part when it gave you `.text`. Your
  answer printed anyway; nothing to fix.

## Stretch, if time allows

- Add a third tool of your own, for example one that returns the current
  time or reverses a string.
- Ask the model a question that needs *both* tools in one sentence and watch
  it choose correctly.
- Preview for next week: OpenCode gives a model dozens of tools like this
  automatically, and adds the approval step before anything risky runs.
