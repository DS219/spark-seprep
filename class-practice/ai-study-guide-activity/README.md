# Class activity: Turn a study guide into flashcards with your local LLM

**Time: 50 minutes.** Builds on the [llmman tutorial](../llmman-tutorial/README.md).
You will connect a real app, Pete Cheslock's
[ai-study-guide](https://github.com/petecheslock/ai-study-guide), to the model
server running on your laptop. The app reads a study guide, asks the model to
write flashcards, asks it again to fact-check them, and then quizzes you.

Nothing in this activity needs an account or a payment.
Your study guide never leaves your laptop.

## What you need

| | Requirement |
| --- | --- |
| llmman | Installed, with `gemma3:4b` downloaded. If you deleted it at the end of the llmman tutorial, redo [step 0](../llmman-tutorial/README.md#0-before-class-install-and-download-about-10-minutes) **before class**. |
| Node.js | Version 20.6 or newer. Check with `node --version`. Install from [nodejs.org](https://nodejs.org/) (choose the LTS version) if needed. |
| git | Check with `git --version`. |
| Memory | Same as the llmman tutorial: 8 GB RAM or more. |

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
git clone https://github.com/petecheslock/ai-study-guide
cd ai-study-guide
npm install
```

`npm install` downloads the libraries the app needs into a `node_modules`
folder inside `ai-study-guide`. Nothing is installed anywhere else.

Look around before you run it:

| Path | What it is |
| --- | --- |
| `server/llm.js` | The code that talks to the model server. |
| `server/prompts.js` | The instructions the app gives the model. |
| `web/` | The web page you will use. |
| `.env.example` | The settings file template. |

## 3. Point the app at your model (10–15 minutes)

Copy the settings template:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` in an editor and change these lines:

```
LLM_BASE_URL=http://127.0.0.1:17434/v1
LLM_MODEL=gemma3:4b
LLM_API_KEY=fake-api-key
VISION_MODEL=
PORT=8888
CARD_COUNT=15
```

| Setting | Why |
| --- | --- |
| `LLM_BASE_URL` | The same server you called with `curl` and `ask.py` in the llmman tutorial. `/v1` is where the OpenAI-format API lives. |
| `LLM_MODEL` | The model the server should use. |
| `LLM_API_KEY` | Cloud services like OpenAI require a secret key. llmman ignores it, so any text works. We use `fake-api-key` to show where a real key would go. |
| `VISION_MODEL` | Left empty, the app uses `LLM_MODEL` for photos too. Gemma 3 can read images. |

> **Never put a real API key in a file you push to GitHub.** `.env` is listed
> in the app's `.gitignore` for exactly that reason.

**Checkpoint:** your `.env` points at `127.0.0.1:17434`.

## 4. Run the app (15–20 minutes)

```bash
npm start
```

You should see:

```text
Flashcard Studio listening on http://0.0.0.0:8888
LLM endpoint: http://127.0.0.1:17434/v1 (model: gemma3:4b, vision model: gemma3:4b)
```

Open [http://localhost:8888](http://localhost:8888) in your browser.

**Checkpoint:** the upload page loads.

## 5. Make a lobster deck (20–35 minutes)

Open [`lobster-study-guide.md`](lobster-study-guide.md) from this folder, copy
all of it, and paste it into the app. Click **Generate**.

Watch both terminals while you wait. The model makes **two passes**:

1. It writes flashcards from the guide.
2. It checks each card against the guide and fixes or drops any card the
   guide does not support.

On our test laptop, a 10-card deck took about 30 seconds.

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

Stop the app: press **Ctrl+C** in its terminal. Stop the model server: press
**Ctrl+C** in the `llmman serve` terminal.

Your saved decks are in `ai-study-guide/data/decks.json`. To remove the app,
delete the whole `ai-study-guide` folder:

```bash
cd ..
rm -rf ai-study-guide
```

Windows PowerShell:

```powershell
cd ..
Remove-Item -Recurse -Force ai-study-guide
```

To remove llmman and the model too, follow
[step 7 of the llmman tutorial](../llmman-tutorial/README.md#7-remove-everything-4550-minutes).

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| `node: command not found`, or a version below 20.6 | Install the LTS version from [nodejs.org](https://nodejs.org/), then reopen the terminal. |
| `npm start` says `node: .env: not found` | You skipped `cp .env.example .env`. Run it from inside the `ai-study-guide` folder. |
| App starts but Generate fails with a connection error | The model server is not running. Start `llmman serve` in another terminal. |
| `curl` to port 17434 says connection refused | Same as above. |
| Generate takes several minutes | The model is loading into memory, or your laptop is busy. Close other apps. Lower `CARD_COUNT` to `8` in `.env` and restart the app. |
| "We can't see any study material there" | Your guide is too short. The app needs at least 80 characters and 12 words. |
| Browser cannot reach `localhost:8888` | Check the app terminal for the port it printed. Another program may already use 8888: change `PORT` in `.env`. |
