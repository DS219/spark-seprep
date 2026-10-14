---
theme: default
title: DS 219 - Coding Agents with OpenCode
info: |
  Lesson 7: agent foundations, OpenCode tutorial, and a locally served website.
author: Sally O'Malley
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-7
lineNumbers: true
---

<div class="eyebrow">Fall 2026 · Lesson 7</div>

# Coding Agents<br>with <span class="accent">OpenCode</span>

<p class="lede">A website you can run, inspect, and explain</p>

<div class="footer-note">Sally O'Malley · DS 219</div>

<!--
This continues Lesson 6. Students use hosted free models today. Local LLMs belong to a later class. This deck adapts the foundations from the supplied Intro to AI Agents deck, then replaces its local-model/NPS exercise with OpenCode website practice.
Source: https://docs.google.com/presentation/d/1MXWC4O2VE90mp_0QGOILiTrrzz8WZcAi/edit
-->

---

# Today's class

| Time | Work |
| --- | --- |
| 20 min | Agent foundations and the loop |
| 20 min | OpenCode demonstration and setup |
| 10 min | Break |
| 45 min | Guided website activity |
| 10 min | Share results and homework |

<p class="lede">Download OpenCode Desktop while we begin.</p>

[Official download](https://opencode.ai/download)

<!--
Assumes the previous class's 105-minute meeting. Installation can happen during the discussion. At the activity start, leave eight minutes for setup checks. If the session is shorter, shorten discussion and the framework survey while protecting the 45-minute practice block.
Source: https://opencode.ai/download
-->

---

# Chat, assistance, and action

**Chat:** responds to a question or conversation.

**Assistance:** suggests changes for a person to apply or approve.

**Agent workflow:** selects tools, takes actions, reads results, and continues.

<p class="question">What evidence would show that a tool actually changed a file?</p>

<!--
Reconnect to the reference deck's slides 2–4. These describe workflows, not permanent product categories. Modern chat apps and coding assistants can also have agent modes. Ask for a file diff, tool result, or observed changed behavior as evidence.
Source: supplied deck, slides 2–4.
-->

---

# The pieces of a coding agent

| Piece | In today's project |
| --- | --- |
| Model | Interprets the request and proposes next actions |
| Tools | Read files, edit code, run commands |
| Context | Brief, files, conversation, project instructions |
| Planning | Break the website into manageable changes |

<p class="lede">OpenCode supplies the workflow around the model.</p>

<!--
Adapted from reference slide 5, the agent formula. Connect to Lesson 6's distinction between a model and a harness. The formula is a teaching shorthand, not a literal software architecture shared by every agent.
Sources: supplied deck, slide 5; https://opencode.ai/docs/
-->

---

# The agent loop in a website task

1. Inspect the brief and existing files.
2. Choose a change and use a tool to make it.
3. Read the tool result and check the page.
4. Continue if the result does not meet the goal.

<p class="question">“The site is finished” is a claim. A working page is evidence.</p>

<!--
Adapt the reference deck's ReAct slide 6 to an observable coding workflow. Do not imply we can see the model's private reasoning. Students will observe tool requests, file changes, and results. Ask what happens if a command fails: the loop should incorporate the error.
Source: supplied deck, slide 6; https://arxiv.org/abs/2210.03629
-->

---

# Agentic design patterns

| Pattern | What it looks like |
| --- | --- |
| Planning | A proposed file list and implementation steps |
| Tool use | Editing CSS or checking JavaScript syntax |
| Reflection | Reviewing a result and revising it |
| Multiple agents | Dividing work among specialized assistants |

<p class="lede">Today's practice uses one agent and a human reviewer.</p>

<!--
Reference slide 7. Multiple agents are an option, not a requirement. We are practicing planning, tool use, and improvement. Human browser feedback helps the agent revise a result.
Source: supplied deck, slide 7.
-->

---

# Tools and permissions

Tools can read files, write code, and execute commands.

| Permission | What happens |
| --- | --- |
| Allow | The action proceeds |
| Ask | You review an approval request |
| Deny | The action is blocked |

<p class="lede">Read the command, its target, and its effect before approving.</p>

<!--
Reference slide 8 introduces tools. Add the OpenCode permission levels. Demonstrate reading an approval prompt if one appears; do not promise every edit will ask. Avoid global config changes in this short class. Students stay in one new project folder.
Source: https://opencode.school/lessons/permissions/
-->

---

# Context across sessions

**Conversation:** the current brief, feedback, and tool results.

**Project files:** source code and README instructions that future sessions can read.

**AGENTS.md:** written project constraints for the agent.

<p class="question">Which requirement would you want a new session to remember?</p>

<!--
Reference slide 9 covers memory. Clarify that long-term context need not be a vector database, and saving a session differs from including its entire transcript in every model request. Today students persist constraints in AGENTS.md. Do not claim files automatically enter the model's context without being read.
Sources: supplied deck, slide 9; https://opencode.ai/docs/rules/
-->

---

# Coding agents and frameworks

**A coding agent** gives you a ready-to-use workflow for working on a project.

**An agent framework** helps a developer build an agent application.

Examples to explore later: LangGraph, smolagents, and other course frameworks.

<p class="lede">Today we use OpenCode to build a website.</p>

<!--
This condenses reference slides 10–15. If presenting the original instead, teach slides 1–10 and skim 11–15. Stop before slide 16, Running Agents Locally. Do not repeat the reference's maturity rankings or dated model recommendations. The NPS exercise in the reference does not apply today.
Source: supplied deck, slides 10–15.
-->

---

# OpenCode Desktop

1. Download for your operating system and chip.
2. Create your website repo on GitHub and clone it locally.
3. Open the cloned folder as your OpenCode project.
4. Select a free model and confirm it responds.

[Download](https://opencode.ai/download) · [Installation walkthrough](https://opencode.school/lessons/installation/)

<!--
Demo Desktop to match OpenCode School. The terminal interface is a fallback for students already using WSL. Avoid mixing V1 and V2 installation instructions: the official download page and older docs currently differ. No CLI install is required for the primary Desktop route.
Sources: https://opencode.ai/download; https://opencode.school/lessons/installation/
-->

---

# Free models for today's work

Choose a model currently labeled free in the picker.

If it is busy, try another free model or pair temporarily.

Your own supported subscription or provider is optional.

<p class="lede">Model availability changes. Check the picker before sending.</p>

<!--
No fixed model name is required. OpenCode School describes built-in free models but says they change. Some lack vision, so the activity uses text feedback instead of requiring screenshot input. Do not send students to a billing setup flow. A general chat subscription does not guarantee API access. No Gemini key is required today.
Source: https://opencode.school/lessons/models/
-->

---

# Plan and Build

**Plan:** discuss the goal, inspect context, and refine the approach.

**Build:** implement the agreed changes with tools.

In Desktop, use the agent dropdown below the prompt.

<p class="lede">Plan helps structure the work. Permissions still matter.</p>

<!--
Demo switching modes. The school warns that Plan is not a hard sandbox, so avoid claiming it guarantees zero side effects. Ask students to explain the intended file changes before switching to Build.
Source: https://opencode.school/lessons/agents/
-->

---

# Instructor demonstration

Plan a small student club homepage.

Build the files, then serve the page on localhost.

Inspect the page and request one concrete improvement.

<p class="question">Where did the agent use a tool? Where did you verify its claim?</p>

<!--
Use the exact prompts from the class activity. Keep the live demo to 10–12 minutes inside the 20-minute demo/setup block. Prepare a working project in advance. Show a file edit, the local HTTP URL, and an improvement after browser feedback. Keep advanced school configuration, plugins, and workspaces for optional follow-up.
-->

---
layout: center
class: text-center
---

# Class activity · 45 minutes

[Open the guided OpenCode activity](https://github.com/DS219/spark-seprep/blob/main/class-practice/opencode-tutorial/README.md)

<p class="lede" style="margin: 1.5rem auto">One small website. One working interaction.<br>One improvement you can verify.</p>

<!--
This link points to the eventual main-branch location. Before publication, open the local README or link to the review branch. See the lesson README for the absolute local file path and publishing checklist. Pause here to confirm students have the activity open, then start the timer.
-->

---

# Practice checkpoints

| Elapsed time | Checkpoint |
| --- | --- |
| 8 min | Your repo is cloned and OpenCode replies |
| 15 min | You understand the plan and file list |
| 27 min | Site and interaction work on localhost |
| 37 min | You have checked an improvement |
| 45 min | Changes reviewed, screenshot and reflection saved |

<!--
Leave this slide visible while students work. At minute eight, pair anyone still blocked on installation or free-model availability. At minute 27, help students start their local server rather than expanding scope.
-->

---

# Serving locally

From the folder containing `index.html`:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open **http://localhost:8000** in your browser.

Keep the terminal running. Use `Ctrl+C` to stop.

<p class="lede">The browser loads the site from your laptop over HTTP.</p>

<!--
Windows Python launcher fallback: py -m http.server 8000 --bind 127.0.0.1. WSL users use their WSL terminal and the same project folder. For a port conflict, use 8001 in both command and URL. Binding to 127.0.0.1 keeps this classroom server on the local machine. No public tunnel is needed.
Source: https://docs.python.org/3/library/http.server.html
-->

---

# Browser checks

- Narrow and wide layouts remain readable.
- Keyboard focus is visible on controls.
- The interaction produces the expected result.
- The browser Console shows no unexplained errors.

<p class="question">Describe what you observed before asking the agent to change it.</p>

<!--
Human verification is required even when the agent reports success. Free models may not accept images. Encourage exact text feedback: browser width, control used, expected behavior, actual behavior. If no bug appears, students can make and verify a deliberate improvement.
-->

---

# Homework · Build a Website

Continue today's site in the same GitHub repository.

Submit **your Git repository link** and a **screenshot of the served site**.

The screenshot must include the localhost address bar.

[Homework requirements and rubric](https://github.com/DS219/spark-seprep/blob/main/assignments/assignment-5-build-a-website.md)

<!--
Students use their own website repo, with source, README run instructions, AGENTS.md, reflection, and screenshot. No PR to the shared course repo is required. Rubric is 20 points. Deadline/submission destination still need instructor confirmation. Public hosting and paid models are not grading criteria.
-->

---
layout: center
class: text-center
---

# Exit ticket

<p class="lede" style="margin: 1.5rem auto">Show your local site.<br>Explain one agent tool action.<br>Describe one improvement you checked.</p>

<div class="footer-note">Next topic: local LLMs</div>

<!--
Ask for concrete evidence rather than a general reaction to AI. Let a few students share, then remind everyone that homework is the local website plus the repo and screenshot. Save local-model installation and the reference deck's NPS activity for another class.
-->
