# Class activity: Run an AI agent from a starter kit

**Time: 40 minutes**, plus a download of about 1.3 GB the first time. Do it in class or on your own.

An **agent** is an app where the model decides which of your code to run. You ask a
question, the model picks a **tool** (a Python function), the app runs it and sends
the result back, and the model answers. You will run a ready-made agent from Red
Hat's [Agentic Starter Kits](https://github.com/RED-HAT-DATA-SERVICES/AGENTIC-STARTER-KITS)
in a Podman container, connect it to the model on your laptop, and give it a new tool.

If your project is a chatbot or an agent, this template can be its starting point.

## What you need

| | Requirement |
| --- | --- |
| Podman | Installed, with a Podman machine running. See [Install Podman on Mac or Windows](podman-install.md). Docker works too: replace `podman` with `docker`. |
| llmman | Installed, with `gemma3:4b` downloaded. See [step 0 of the llmman tutorial](llmman-tutorial/README.md#0-before-class-install-and-download-about-10-minutes). |
| git | Check with `git --version`. |
| Disk | About 2 GB free. |

You do **not** need Python, `uv`, `make`, or OpenShift. Everything the agent needs is
installed inside the container.

## 1. Start the model server (0–5 minutes)

```bash
llmman serve
```

Leave this terminal open. Open a **second** terminal for the rest of the activity.

## 2. Get the starter kit (5–10 minutes)

```bash
git clone https://github.com/RED-HAT-DATA-SERVICES/AGENTIC-STARTER-KITS
cd AGENTIC-STARTER-KITS/agents/vanilla_python/templates/openai_responses_agent
```

The repository has many kits. This one, **OpenAI Responses Agent**, is the simplest: it
uses no agent framework, just the `openai` Python library and a short loop.

> **Skip the OpenShift parts.** The kit's README also covers MLflow tracing, Helm, and
> deploying to OpenShift. You will not use them. Also skip `make build`: it always builds
> for Intel/AMD processors, which is very slow on an Apple Silicon Mac.

Look at the two files that matter:

| File | What it is |
| --- | --- |
| `src/openai_responses_agent/tools.py` | The tools: plain Python functions. Both are fake: they return made-up prices and reviews. |
| `src/openai_responses_agent/agent.py` | The loop. Find `setup_system_prompt`: these are the instructions the model gets. |

`setup_system_prompt` pastes the **source code** of each tool into the instructions.
The model reads your function, including its docstring, to decide when to call it.

## 3. Build the container image (10–15 minutes)

The kit's `Containerfile` is named `Dockerfile`. Make two changes before you build.

**Copy the logo images** into this folder. The image build expects them here.

Mac Terminal:

```bash
cp -r ../../../../images ./images
```

Windows PowerShell:

```powershell
Copy-Item -Recurse ..\..\..\..\images .\images
```

**Turn off tracing** to make the image smaller. Open `Dockerfile` in an editor, find this line:

```dockerfile
RUN uv sync --frozen --no-dev --extra tracing
```

and delete ` --extra tracing`, so it reads:

```dockerfile
RUN uv sync --frozen --no-dev
```

This skips MLflow, which this activity doesn't use. The image drops from about 3.1 GB to 1.3 GB.

Then build:

```bash
podman build -t my-agent .
```

**Checkpoint:** `podman images my-agent` lists the image.

## 4. Run the agent (15–20 minutes)

Mac Terminal:

```bash
podman run -d --name my-agent -p 8080:8080 \
  -e BASE_URL=http://host.containers.internal:17434/v1 \
  -e MODEL_ID=gemma3:4b \
  -e API_KEY=fake-api-key \
  my-agent
```

Windows PowerShell (one line):

```powershell
podman run -d --name my-agent -p 8080:8080 -e BASE_URL=http://host.containers.internal:17434/v1 -e MODEL_ID=gemma3:4b -e API_KEY=fake-api-key my-agent
```

| Setting | Why |
| --- | --- |
| `BASE_URL` | Your llmman server. Inside a container, `127.0.0.1` means the container itself, so we use `host.containers.internal`, Podman's name for your laptop. |
| `MODEL_ID` | The model llmman should use. |
| `API_KEY` | OpenAI requires a key. llmman ignores it, so any text works. |

Open [http://localhost:8080](http://localhost:8080) and ask:

```text
How much does a Dell laptop cost and what are the reviews?
```

In our test, the agent called both tools and answered in about 9 seconds:
*"A Dell laptop costs $400 and the reviews are good."* The $400 comes from the fake
tool, not from the model.

Watch what happened:

```bash
podman logs my-agent
```

**Checkpoint:** an answer that uses the fake tool's price.

## 5. Give the agent a new tool (20–35 minutes)

Small models are bad at date math. Give the agent a tool that does it correctly.

1. Add this function to the end of `src/openai_responses_agent/tools.py`:

   ```python
   def days_until(date: str) -> str:
       """Count the days from today until a date written as YYYY-MM-DD."""
       from datetime import date as Date

       days = (Date.fromisoformat(date) - Date.today()).days
       return f"{days} days until {date}"
   ```

2. In `src/openai_responses_agent/agent.py`, import it. Change:

   ```python
   from openai_responses_agent.tools import search_price, search_reviews
   ```

   to:

   ```python
   from openai_responses_agent.tools import days_until, search_price, search_reviews
   ```

3. In the same file, find `tools=[` and register it:

   ```python
   tools=[
       ("search_price", search_price),
       ("search_reviews", search_reviews),
       ("days_until", days_until),
   ],
   ```

4. Rebuild and restart. The container only has the code it was built with:

   ```bash
   podman rm -f my-agent
   podman build -t my-agent .
   ```

   Then run the `podman run` command from step 4 again.

5. Ask: `How many days until 2026-12-25?` In our test, the agent called `days_until`
   and got the right answer. Ask the same question in llmman's own chat page,
   [http://127.0.0.1:17434](http://127.0.0.1:17434), where the model has no tool. Is it right?

**Checkpoint:** the agent answers with your tool's result.

Now make a tool for **your** project. Some ideas:

| Tool | What it does |
| --- | --- |
| `word_count(text)` | Counts words, which models do badly |
| `read_file(name)` | Reads a file from a folder, such as your notes |
| `next_deadline(course)` | Looks up a due date in a list you write |

Keep each tool small. Give it a clear docstring: the model reads it to decide when to use the tool.

## 6. Clean up (35–40 minutes)

```bash
podman rm -f my-agent
podman rmi my-agent
```

Stop llmman: press **Ctrl+C** in its terminal. To remove the starter kit, delete the
`AGENTIC-STARTER-KITS` folder.

If you use the kit for your project, copy the `openai_responses_agent` folder into your
own repo instead of working inside the starter kits repo. Keep the `LICENSE` file:
the kit is Apache 2.0 licensed.

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| `podman build` fails with `images: no such file or directory` | You skipped copying the images. Run the `cp` or `Copy-Item` command from step 3. |
| `Cannot connect to Podman` | Run `podman machine start`. |
| The page loads, but answers fail with a connection error | llmman is not running. Start `llmman serve` in another terminal. |
| `the container name "my-agent" is already in use` | Run `podman rm -f my-agent`, then run it again. |
| Your new tool is never called | Did you rebuild after editing? Check the import and the `tools=[` list. Then make the docstring clearer. |
| The answer starts with "Thought: …" | That's the model's reasoning, shown before its answer. Small models do this. Read to the end. |
| `500 Compute error` with Phi-4-mini | Use `gemma3:4b`. Phi-4-mini failed with this kit's prompt in our test. |
| Port 8080 is in use | Use `-p 8081:8080` and open `http://localhost:8081`. |
