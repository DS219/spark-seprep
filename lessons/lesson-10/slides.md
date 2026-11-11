---
theme: default
title: DS 219 - Choose Your Project
info: |
  Lesson 10: pick a project and create its repo, plus two local AI activities: Whisper speech-to-text and a RAG chatbot.
author: Sally O'Malley
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-10
lineNumbers: true
---

<div class="eyebrow">Fall 2026 · Lesson 10</div>

# Choose your project,<br><span class="accent">create its repo</span>

<p class="lede">Plus two more local AI tools: speech-to-text and a RAG chatbot</p>

<div class="footer-note">Sally O'Malley · DS 219</div>

<!--
Students need laptops with llmman (gemma3:4b), Podman, and Python. The RAG app image should already be built at home: it is about 2.2 GB.
-->

---

# Today's class

| Time | Work |
| --- | --- |
| 10 min | The project: where we are and what's due |
| 25 min | Activity: speech to text with Whisper |
| 30 min | Activity: chat with your documents (RAG) |
| 10 min | Break |
| 25 min | Choose your project and create its repo |
| 5 min | **Exit ticket:** your repo link in Blackboard |

<!--
Assumes the usual 105-minute meeting. Protect the last 30 minutes: every student must leave with a repo link submitted. If an activity runs long, shorten the RAG activity, not the project time.
-->

---

# Where we left off

Last week we started the project but didn't finish:

- What employers look for: **plan, direct an agent, check its work, ship**
- The project: a small tool that solves a problem **you** have
- Your **scope sentence**

<p class="lede">Today you lock in a project and create its repo.</p>

<!--
Quick recap only. Students who wrote a scope sentence last week keep it. Students who missed the class can still pick an idea today: the Lesson 9 slides have the idea list.
-->

---

# The project

<p class="lede">Build a small tool that solves a problem you actually have,<br>and get at least one person besides you to use it.</p>

> "I noticed X wasted my time. I built Y. My roommate used it, found a bug, and I fixed it."

<!--
One real user who gave feedback makes a better interview story than a long feature list.
-->

---

# The new timeline

| When | What |
| --- | --- |
| **Today** | Choose your project. Create its repo. Submit the link. |
| **Next 2 weeks** | Build the smallest version that works (your MVP) |
| **Next class** | Your project **works**. We add GitHub Actions and more. |
| **Last class** | 2-minute presentations |

<p class="lede">MVP: minimum viable product, the smallest version someone can actually use.</p>

<!--
This replaces the four-class schedule from the Lesson 9 slides: we lost a week, so the MVP gets two weeks. Next class is two weeks from today.
-->

---

# Your scope sentence

**[Who]** wastes time on **[task]**.<br>
The smallest version is **[one screen or one command]**<br>
that **[does one thing]**.

Example:

> Students in my classes waste time copying deadlines from syllabi into their calendars. The smallest version is a command that reads a pasted syllabus and outputs a calendar file of the due dates.

<!--
Students who already wrote one keep it. Ask: could this be built in one afternoon? Who besides you would use it? Approve sentences as you walk around.
-->

---

# Activity 1 · Speech to text

Run a speech model on your laptop and transcribe a short recording.

- **Activity:** [`class-practice/whisper-transcription-activity.md`](https://github.com/DS219/spark-seprep/blob/main/class-practice/whisper-transcription-activity.md)
- You need: Python 3.9+, a 10 to 30 second recording
- Compare the transcript with what was actually said

<p class="question">Project idea: voice memo to action items?</p>

<!--
Whisper is a speech model; it pairs well with an LLM for summaries or to-dos. Point out project ideas as students work.
-->

---

# Activity 2 · Chat with your documents

A **RAG** chatbot: it finds the parts of your document that match your question, then sends them to the model.

- **Activity:** [`class-practice/rag-chatbot-tutorial`](https://github.com/DS219/spark-seprep/tree/main/class-practice/rag-chatbot-tutorial)
- Start the model first: `llmman serve`
- Then: `./start.sh`, and open `http://localhost:8501`
- Model: `gemma3:4b`, or Phi-4-mini

<p class="question">Does it answer from your document, or make something up?</p>

<!--
RAG means retrieval augmented generation. The app runs in a Podman pod with pgvector; the model runs on the laptop with llmman. If a student did not build the image at home, pair them with someone who did: the build is about 2.2 GB. Windows students follow MANUAL_SETUP.md in PowerShell.
-->

---
layout: center
class: text-center
---

# Break · 10 minutes

---

# Create your project repo

1. On GitHub, create a **new repo** with a name that describes the tool.
2. Add a `README.md` with your **scope sentence** at the top.
3. Clone it and open it in OpenCode.
4. Optional: plan `SPEC.md`, `AGENTS.md`, and 3 to 5 issues with the Lesson 9 starter prompt.

<p class="lede">On a résumé, <code>syllabus-to-calendar</code> beats <code>my-project</code>.</p>

<!--
Same steps as the OpenCode activity. The repo must be public or shared with the instructor. Students who finish early start planning with the Lesson 9 starter prompt.
-->

---

# Your MVP in 2 weeks

By the next class:

- It **runs** by following only your README
- It does **the one thing** in your scope sentence
- One person besides you has **tried it**
- Your to-do list lives in **GitHub Issues**

<p class="lede">Working beats finished. Keep it small.</p>

<!--
Next class adds GitHub Actions, so a project with even one test is ahead. Remind students: OpenCode writes the code; if they use llmman, use it inside the app, and read its address from a setting like MODEL_URL.
-->

---
layout: center
class: text-center
---

# Exit ticket

<p class="lede" style="margin: 1.5rem auto">Before you leave, submit your<br><strong>project repo link</strong> in the Blackboard form.</p>

<!--
Check that each link opens and the README has a scope sentence. Students without a repo do not leave until they have one.
-->
