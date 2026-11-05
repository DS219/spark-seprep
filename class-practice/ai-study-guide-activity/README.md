# Class activity: Turn a study guide into flashcards with your local LLM

**Time: 50 minutes.** Builds on the [llmman tutorial](../llmman-tutorial/README.md).
You will connect a real app, Pete Cheslock's
[ai-study-guide](https://github.com/petecheslock/ai-study-guide), to the model
server running on your laptop. The app reads a study guide, asks the model to
write flashcards, asks it again to fact-check them, and then quizzes you.

**App repository:** <https://github.com/petecheslock/ai-study-guide>

Nothing in this activity needs an account or a payment.
Your study guide never leaves your laptop.

## What you need

| | Requirement |
| --- | --- |
| llmman | Installed, with `gemma3:4b` downloaded. If you deleted it at the end of the llmman tutorial, redo [step 0](../llmman-tutorial/README.md#0-before-class-install-and-download-about-10-minutes) **before class**. |
| Podman | Installed, with a Podman machine running. See [Install Podman on Mac or Windows](../podman-install.md). |
| Memory | Same as the llmman tutorial: 8 GB RAM or more. |
| Disk | About 1 GB free for the app's container image. |

You do **not** need Node.js or git. The app comes ready to run as a container image.

## 0. Before class: install Podman (about 20 minutes)

Follow [Install Podman on Mac or Windows](../podman-install.md). If you already
have Podman and `podman machine list` shows a machine, just run
`podman machine start`.

**Checkpoint:** `podman run --rm quay.io/podman/hello` prints the hello message.

## 1. Start the model server (0–5 minutes)

```bash
llmman serve
```

Leave this terminal open. In a **second** terminal, check that the server is up:

```bash
curl http://127.0.0.1:17434/v1/models
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:17434/v1/models
```

You should see `gemma3:4b` in the reply.

**Checkpoint:** the model list includes `gemma3:4b`.

## 2. Download the app (5–10 minutes)

In the second terminal:

```bash
podman pull ghcr.io/petecheslock/ai-study-guide:latest
```

This downloads Pete's app as a **container image** from the GitHub Container
Registry (`ghcr.io`). The image already contains Node.js, the app's libraries,
and its code. Nothing is installed on your laptop outside Podman.

You can read the app's code in
[Pete's repository](https://github.com/petecheslock/ai-study-guide) while it downloads:

| Path | What it is |
| --- | --- |
| [`server/llm.js`](https://github.com/petecheslock/ai-study-guide/blob/main/server/llm.js) | The code that talks to the model server. |
| [`server/prompts.js`](https://github.com/petecheslock/ai-study-guide/blob/main/server/prompts.js) | The instructions the app gives the model. |
| [`web/`](https://github.com/petecheslock/ai-study-guide/tree/main/web) | The web page you will use. |
| [`.env.example`](https://github.com/petecheslock/ai-study-guide/blob/main/.env.example) | The settings file template. |

## 3. Point the app at your model (10–15 minutes)

Make a folder for the app's settings and create a file named `.env` in it.

> **Do not copy Pete's `.env.example`.** It is written for running the app
> without a container. It sets `PORT=8888` and points at `127.0.0.1`, and
> neither works inside a container. Use the settings below.

Mac Terminal:

```bash
mkdir flashcards
cd flashcards
cat > .env <<'EOF'
LLM_BASE_URL=http://host.containers.internal:17434/v1
LLM_MODEL=gemma3:4b
LLM_API_KEY=fake-api-key
CARD_COUNT=15
EOF
```

Windows PowerShell:

```powershell
mkdir flashcards
cd flashcards
@"
LLM_BASE_URL=http://host.containers.internal:17434/v1
LLM_MODEL=gemma3:4b
LLM_API_KEY=fake-api-key
CARD_COUNT=15
"@ | Set-Content -Encoding ascii .env
```

Check the file with `cat .env` (Mac) or `Get-Content .env` (Windows).

| Setting | Why |
| --- | --- |
| `LLM_BASE_URL` | The same llmman server you called with `curl` and `ask.py` in the llmman tutorial. Inside a container, `127.0.0.1` means **the container itself**, not your laptop. `host.containers.internal` is Podman's name for your laptop. `/v1` is where the OpenAI-format API lives. |
| `LLM_MODEL` | The model the server should use. |
| `LLM_API_KEY` | Cloud services like OpenAI require a secret key. llmman ignores it, so any text works. We use `fake-api-key` to show where a real key would go. |
| `CARD_COUNT` | How many cards to write per deck. |

The app also reads `VISION_MODEL` (for photos) and `PORT`. Leave them out.
Without `VISION_MODEL`, the app uses `LLM_MODEL` for photos too, and Gemma 3 can
read images. **Do not set `PORT`:** the run command below expects the app on
port 3000, its default.

> **Never put a real API key in a file you push to GitHub.** Pete's repository
> lists `.env` in its `.gitignore` for exactly that reason.

**Checkpoint:** your `.env` points at `host.containers.internal:17434`.

## 4. Run the app (15–20 minutes)

From the `flashcards` folder, Mac Terminal:

```bash
podman run -d --name flashcards \
  -p 3000:3000 \
  --env-file .env \
  -v flashcard-data:/app/data \
  --restart unless-stopped \
  ghcr.io/petecheslock/ai-study-guide:latest
```

Windows PowerShell (one line):

```powershell
podman run -d --name flashcards -p 3000:3000 --env-file .env -v flashcard-data:/app/data --restart unless-stopped ghcr.io/petecheslock/ai-study-guide:latest
```

| Option | What it does |
| --- | --- |
| `-d` | Runs the container in the background and gives you your terminal back. |
| `--name flashcards` | Names the container so you can refer to it later. |
| `-p 3000:3000` | Connects port 3000 on your laptop to port 3000 in the container. |
| `--env-file .env` | Passes your settings into the container. |
| `-v flashcard-data:/app/data` | Stores saved decks in a Podman **volume** named `flashcard-data`, so they survive if the container is removed. |
| `--restart unless-stopped` | Restarts the app if it crashes, until you stop it yourself. |

Check that it started:

```bash
podman logs flashcards
```

You should see:

```text
Flashcard Studio listening on http://0.0.0.0:3000
LLM endpoint: http://host.containers.internal:17434/v1 (model: gemma3:4b, vision model: gemma3:4b)
```

If the log says `:8888` or `127.0.0.1` instead, your `.env` is wrong. Fix it as
shown in step 3, then recreate the container. The container reads `.env` only
when it is created, so `podman restart` is not enough:

```bash
podman rm -f flashcards
```

Then run the `podman run` command again.

Open [http://localhost:3000](http://localhost:3000) in your browser.

**Checkpoint:** the upload page loads.

## 5. Make a lobster deck (20–35 minutes)

Open [`lobster-study-guide.md`](lobster-study-guide.md) from this folder, copy
all of it, and paste it into the app. Click **Generate**.

While you wait, run `podman logs -f flashcards` to watch the app work
(press Ctrl+C to stop watching). The model makes **two passes**:

1. It writes flashcards from the guide.
2. It checks each card against the guide and fixes or drops any card the
   guide does not support.

On our test laptop, a 10-card deck took 20 to 30 seconds.

Now study:

| Action | Key |
| --- | --- |
| Flip the card | Tap, or press space |
| I got it | → or the green button |
| Still fuzzy | ← or the red button |

Mark at least **three** cards as fuzzy, even if you know them. When the round
ends, the app sends the cards you missed back to the model and asks for **new**
questions on the same ideas.

Compare the follow-up questions to the cards you missed. Are they really about
the same facts? In our test, we missed cards about **claws** and **blood**, and
the follow-up asked about **senses** and **molting** instead. A 4-billion-parameter
model does not always follow instructions exactly. Write down whether yours did.

**Checkpoint:** you finished one round and one follow-up round.

## 6. Check the model's work (35–45 minutes)

The app's fact-check pass is done by the **same small model** that wrote the
cards. Check it yourself:

1. Pick three cards from your deck.
2. Find each answer in `lobster-study-guide.md`.
3. Is each answer supported by the guide, word for word or close to it?

Then try to break it. Start a new deck with a short guide that contains one
false "fact", for example:

```text
Lobsters are mammals. They breathe air with lungs and live in trees.
Lobsters have ten legs, and the front two are claws.
Lobster blood is blue because it contains copper.
```

Does the app turn the false fact into a flashcard? In our test, it made the
card "What class do lobsters belong to?" with the answer "Lobsters are
mammals." That is expected: the fact-check
compares cards to **your guide**, not to the real world. The model is only as
reliable as what you give it.

Optional: write a one-page study guide for another class, paste it in, and
study with it. Or take a photo of handwritten notes and upload it, so Gemma
reads the image.

**Checkpoint:** you found one card that was right and know how you checked it.

## 7. Clean up (45–50 minutes)

Remove the app's container, its saved decks, and its image:

```bash
podman rm -f flashcards
podman volume rm flashcard-data
podman rmi ghcr.io/petecheslock/ai-study-guide:latest
```

Then delete the `flashcards` settings folder: `cd ..` and `rm -rf flashcards`
(Mac) or `Remove-Item -Recurse -Force flashcards` (Windows).

Stop the model server: press **Ctrl+C** in the `llmman serve` terminal.

If you want to keep Podman for later activities, stop the machine with
`podman machine stop`. To remove the Podman machine and its disk entirely:
`podman machine rm`.

To remove llmman and the model too, follow
[step 7 of the llmman tutorial](../llmman-tutorial/README.md#7-remove-everything-4550-minutes).

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| `podman: command not found` | Close and reopen the terminal after installing. |
| `Cannot connect to Podman` | The Podman machine is not running. Run `podman machine start`. |
| `podman run` says the name `flashcards` is already in use | You ran it before. Run `podman rm -f flashcards`, then run it again. Your decks are safe in the volume. |
| `podman run` says `.env` not found | You are in the wrong folder. `cd` into `flashcards`. |
| App starts but Generate fails with a connection error | The model server is not running, or `LLM_BASE_URL` still says `127.0.0.1`. Start `llmman serve`, check `.env`, then `podman rm -f flashcards` and run the container again. |
| `curl` to port 17434 says connection refused | The model server is not running. Start `llmman serve` in another terminal. |
| Browser cannot reach `localhost:3000` | Run `podman logs flashcards`. If it says `listening on ... :8888`, your `.env` sets `PORT`. Delete that line, run `podman rm -f flashcards`, then run the container again. |
| Generate takes several minutes | The model is loading into memory, or your laptop is busy. Close other apps. Lower `CARD_COUNT` to `8` in `.env` and run the container again. |
| "We can't see any study material there" | Your guide is too short. The app needs at least 80 characters and 12 words. |
| You changed `.env` but nothing changed | The container reads `.env` only when it is created. Run `podman rm -f flashcards`, then the `podman run` command again. |
