---
theme: default
title: DS 219 - What Is a Coding Agent?
info: |
  Lesson 6 for DS 219, Software Engineering Career Prep Practicum.
author: Sally O'Malley
keywords: coding agents, LLM, agent harness, Claude Code, Codex, OpenCode, Gemini, DS219
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-6
lineNumbers: true
---

<div class="eyebrow">Fall 2026 · Lesson 6</div>

# What Is a<br><span class="accent">Coding Agent?</span>

<p class="lede">DS 219 · Part 1: concepts before we touch one</p>

<div class="footer-note">Sally O'Malley</div>

<!--
Bridge from Assignment 4: everyone wrote a script and packaged it in a container. Tonight is about code that writes, runs, and checks itself.
-->

---

<div class="eyebrow">Tonight's route</div>

# From chatbot to agent, one layer at a time

<div class="timeline">
  <div><strong>4:30</strong><span class="muted">Chatbot vs. agent, three terms</span></div>
  <div><strong>5:00</strong><span class="muted">Six harness ingredients, as two groups of three</span></div>
  <div><strong>5:40</strong><span class="muted">Break</span></div>
  <div><strong>5:55</strong><span class="muted">Claude Code, Codex, OpenCode preview</span></div>
  <div><strong>6:10</strong><span class="muted">Gemini API key + exit ticket</span></div>
</div>

<!--
Next week: install and run OpenCode hands-on. Tonight stays conceptual, no terminal work required.
-->

---

<div class="eyebrow">Start here</div>

# Have you used a chatbot that "did" something?

<p class="question">Not just answered a question. Edited a file, ran a command, looked something up, and kept going.</p>

<!--
Take a few answers. Steer toward: ChatGPT with code interpreter, Claude Code, Copilot, Cursor, a browser agent. Don't define "agent" yet, just collect examples.
-->

---
layout: center
class: text-center
---

<div class="section-number">01</div>
<div class="eyebrow">The first big idea</div>

# Three words, three different things

<p class="lede" style="margin: 1rem auto">LLM. Reasoning model. Agent.</p>

<!--
This confusion is common even among working engineers. Clearing it up now makes the rest of the lesson land.
-->

---

<div class="eyebrow">Definitions</div>

# The engine, the upgraded engine, the driver

<div class="grid three">
  <div class="card"><h2>LLM</h2><p>The core model. Given text, it predicts the next token.</p></div>
  <div class="card red"><h2>Reasoning model</h2><p>Still an LLM, but trained or prompted to "think" longer before answering.</p></div>
  <div class="card cyan"><h2>Agent</h2><p>A loop around a model that decides what to check, which tools to use, and when to stop.</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">An agent is software wrapped around a model, not a bigger or smarter model.</p>

<div class="footer-note">Source: Sebastian Raschka, "Components of a Coding Agent," 2026</div>

<!--
Analogy: LLM is the engine, a reasoning model is a beefed-up engine, an agent harness is the car and driver built around either engine. The analogy is imperfect since LLMs still work standalone in a chat box, but it conveys the layering.
-->

---

<div class="eyebrow">Zoom in</div>

# An agent is a loop, not a single call

<div class="grid four">
  <div class="card"><h2>Observe</h2><p>Gather information from the environment</p></div>
  <div class="card"><h2>Inspect</h2><p>Make sense of what came back</p></div>
  <div class="card red"><h2>Choose</h2><p>Decide the next action</p></div>
  <div class="card"><h2>Act</h2><p>Execute it, then observe again</p></div>
</div>

<p class="question">A chatbot answers once. An agent repeats this loop until the task is done.</p>

<div class="footer-note">Source: Sebastian Raschka, "Components of a Coding Agent," 2026</div>

<!--
This loop is the heart of every agent harness discussed tonight, including Claude Code, Codex, and OpenCode. A coding harness is simply this loop specialized for software work.
-->

---
layout: center
class: text-center
---

<div class="section-number">02</div>
<div class="eyebrow">The second big idea</div>

# What makes an agent work

<p class="lede" style="margin: 1rem auto">Six ingredients, simplified into two groups of three.</p>

<!--
Raschka's article names six components. For a beginner audience, group them as "knowing where you are" and "working carefully." Mini Coding Agent on GitHub shows all six in plain Python, for instructor reference only.
-->

---

<div class="eyebrow">Group one</div>

# Knowing where you are

<div class="grid three">
  <div class="card"><h2>Repo context</h2><p>Which branch, which files, what AGENTS.md or README says to do</p></div>
  <div class="card red"><h2>Reusable prompt</h2><p>Stable instructions and tool descriptions get cached, not rebuilt every turn</p></div>
  <div class="card cyan"><h2>Memory</h2><p>A running summary of the task, separate from the full transcript</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">"Fix the tests" only works if the agent already knows which repo, which branch, which test command.</p>

<div class="footer-note">Source: Sebastian Raschka, "Components of a Coding Agent," 2026</div>

<!--
Connect to assignment-4 and the local-LLM activity: students already saw that a model without context has to guess. This is the same problem, solved by the harness instead of the user.
-->

---

<div class="eyebrow">Group two</div>

# Working carefully

<div class="grid three">
  <div class="card"><h2>Structured tools</h2><p>A fixed list of actions the model can request, each checked before it runs</p></div>
  <div class="card red"><h2>Approval</h2><p>Risky actions pause for a human yes before executing</p></div>
  <div class="card cyan"><h2>Context limits</h2><p>Old file reads and long outputs get trimmed so the model doesn't drown</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">The harness gives the model less freedom. That restriction is what makes it usable.</p>

<div class="footer-note">Source: Sebastian Raschka, "Components of a Coding Agent," 2026</div>

<!--
Emphasize: "less freedom, more reliability" is the core design tradeoff of every agent harness in this lesson, including the one running this very class session.
-->

---

<div class="eyebrow">Walk through it</div>

# One tool call, start to finish

<div class="grid two">
  <div class="card"><h2>1. Model proposes</h2><p>"Run the test suite" as a structured action, not free text</p></div>
  <div class="card"><h2>2. Harness checks</h2><p>Known tool? Valid arguments? Inside the workspace? Needs approval?</p></div>
  <div class="card red"><h2>3. Human approves</h2><p>If the action is risky, a person says yes first</p></div>
  <div class="card cyan"><h2>4. Result returns</h2><p>Trimmed output goes back into the loop, and the model decides what's next</p></div>
</div>

<div class="footer-note">Source: Sebastian Raschka, "Components of a Coding Agent," 2026</div>

<!--
This is the approval prompt students have likely already seen in any AI coding tool, Copilot included. Naming the four steps demystifies the pause-and-confirm moment.
-->

---
layout: center
class: text-center
---

<div class="section-number">03</div>
<div class="eyebrow">Meeting the tools</div>

# Three harnesses you'll hear about

<p class="lede" style="margin: 1rem auto">Same six ingredients, different companies.</p>

<!--
Keep these descriptions even-handed. None of these is being sold as "the best." Confirm against sources.md before class, since product positioning changes fast.
-->

---

<div class="eyebrow">Compare</div>

# Claude Code, Codex, OpenCode

<div class="grid three">
  <div class="card"><h2>Claude Code</h2><p>Anthropic's terminal coding agent, built around Claude models</p></div>
  <div class="card red"><h2>Codex</h2><p>OpenAI's terminal coding agent, built around GPT models</p></div>
  <div class="card cyan"><h2>OpenCode</h2><p>Open-source and model-agnostic; works with Claude, GPT, Gemini, and local models</p></div>
</div>

<p class="question">We'll install and run OpenCode next week, since it doesn't lock us into one provider.</p>

<div class="footer-note">Sources: Anthropic, OpenAI, opencode.ai</div>

<!--
This is a one-line, non-promotional comparison. Do not go deep on pricing or feature races; that content ages out fast.
-->

---

<div class="eyebrow">Preview, don't run yet</div>

# Next week: installing OpenCode

<div class="command-stack">
<div class="terminal-window"><div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div><div class="terminal-body"><span class="prompt-local">$</span> curl -fsSL https://opencode.ai/install | bash<br><span class="terminal-output"># install script</span></div></div>
<div class="terminal-window"><div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div><div class="terminal-body"><span class="prompt-local">$</span> npm install -g opencode-ai<br><span class="terminal-output"># Node.js package manager</span></div></div>
</div>

<p class="lede" style="margin-top: 1.3rem">A third option, a package-manager install, also exists. We'll pick one together next week.</p>

<div class="footer-note">Source: opencode.ai/docs, verified 2026-10-07</div>

<!--
Do not run curl | bash live without explaining what it does first: it downloads a script and executes it immediately, so only run it from a source you trust. Re-verify this command right before class; install scripts change across releases.
-->

---
layout: center
class: text-center
---

<div class="section-number">04</div>
<div class="eyebrow">Before next time</div>

# Get a free Gemini key

<p class="lede" style="margin: 1rem auto">You'll need it for the class activity.</p>

<!--
This is the one piece of required prep. State plainly that this is separate from tonight's exit ticket and from next week's OpenCode install.
-->

---

<div class="eyebrow">Google AI Studio</div>

# Three steps, no credit card

<div class="grid three">
  <div class="card"><h2>1. Sign in</h2><p>Go to Google AI Studio with any Google account</p></div>
  <div class="card red"><h2>2. Create key</h2><p>"Get API key" → create a new key in a new or existing project</p></div>
  <div class="card cyan"><h2>3. Save it</h2><p>Copy it somewhere private; never commit it to Git or paste it in chat</p></div>
</div>

<p class="question">Never share a private key, password, API key, or access token in chat, Git, or an assignment.</p>

<div class="footer-note">Source: ai.google.dev/aistudio, verified 2026-10-07</div>

<!--
Menu labels in Google's UI change more often than the underlying flow. Walk through it live from a screen share if possible, confirming current labels before class.
-->

---

<div class="eyebrow">Checkpoint</div>

# Verify your key works

<div class="terminal-window"><div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div><div class="terminal-body"><span class="prompt-local">$</span> export GEMINI_API_KEY="your-key-here"<br><span class="prompt-local">$</span> curl https://generativelanguage.googleapis.com/v1beta/models \<br>&nbsp;&nbsp;-H "x-goog-api-key: $GEMINI_API_KEY"</div></div>

<p class="lede" style="margin-top: 1.3rem">A JSON list of model names back means your key is live. An error means fix it now, before the activity.</p>

<div class="footer-note">Source: ai.google.dev/api/models, verified 2026-10-07</div>

<!--
Have every student run this before the activity starts. It is faster to catch a bad or not-yet-active key here than to debug it mid-exercise. The response also shows exact current model names, useful if gemini-3.5-flash-lite has since changed.
-->

---

<div class="eyebrow">A glimpse ahead</div>

# What the class activity will look like

<div class="terminal-window">
  <div class="terminal-bar">
    <span class="terminal-dot red-dot"></span>
    <span class="terminal-dot gold-dot"></span>
    <span class="terminal-dot green-dot"></span>
  </div>
  <div class="terminal-body"><span class="prompt-local">$</span> pip install -U google-genai<br><span class="terminal-output">...</span><br><span class="prompt-local">$</span> python ask_gemini.py<br><span class="terminal-output">-> one short answer, one call, no loop</span></div>
</div>

<p class="lede" style="margin-top: 1.1rem">One plain call like this is the LLM. Next class, we wrap it in a loop and watch it become an agent.</p>

<div class="footer-note">Source: ai.google.dev/gemini-api/docs/get-started, verified 2026-10-07</div>

<!--
Do not run this live tonight; it previews the activity so students arrive with a mental model, not cold. The actual activity is a separate session.
-->

---

<div class="eyebrow">Tonight in one line</div>

# A chatbot answers. An agent loops, checks, and acts.

<div class="grid two" style="margin-top: 1.5rem">
  <div class="card"><h2>LLM vs. agent</h2><p>An agent is software wrapped around a model, built to observe, inspect, choose, and act, on repeat</p></div>
  <div class="card red"><h2>Why the harness matters</h2><p>Context, tools, approval, and limits are what make an agent trustworthy enough to use</p></div>
</div>

<!--
Recap before the exit ticket. Ask for one example from the room of each: an LLM used plainly, and an agent-like tool they've touched.
-->

---
layout: center
class: text-center
---

<div class="eyebrow">Exit ticket</div>

# One idea. One question.

<p class="lede" style="margin: 1rem auto 2rem">Name one idea about coding agents you're taking with you, and one question you still have.</p>

<span class="tag">Observe</span>
<span class="tag">Inspect</span>
<span class="tag">Choose</span>
<span class="tag">Act</span>

<div class="footer-note">Before next class: create your free Gemini API key.</div>

<!--
Take responses aloud or through the Blackboard exit-ticket mechanism. Use unanswered questions to tune next week's OpenCode install session. Remind students one more time about the Gemini key requirement before they leave.
-->
