---
theme: default
title: DS 219 - Build Something People Use
info: |
  Lesson 9: what employers look for now that everyone has AI coding tools, and week 1 of a four-class portfolio project.
author: Sally O'Malley
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-9
lineNumbers: true
---

<div class="eyebrow">Fall 2026 · Lesson 9</div>

# Build something<br><span class="accent">people use</span>

<p class="lede">What employers look for, and a project that shows it</p>

<div class="footer-note">Sally O'Malley · DS 219</div>

<!--
Week 1 of a four-class project. Classes 1 to 3 are build sessions; class 4 is 2-minute presentations. Students need laptops with OpenCode Desktop working. llmman is optional.
-->

---

# Today's class

| Time | Work |
| --- | --- |
| 12 min | What employers look for |
| 13 min | The project, ground rules, and ideas |
| 13 min | Your scope sentence and a partner check |
| 20 min | Plan with the agent |
| 10 min | Break |
| 25 min | Build the smallest version that works |
| 12 min | Laptop swap and close |

<!--
Assumes the usual 105-minute meeting. The scope sentence is the most important 13 minutes of the class. Protect it even if the discussion runs long.
-->

---
layout: center
class: text-center
---

# If you were hiring a junior developer

<p class="lede" style="margin: 1.5rem auto">Everyone has AI coding tools now.<br>What would you want to see?</p>

<!--
Collect answers on the board for 3 to 4 minutes before showing the next slide.
-->

---

# [Data and AI Engineer](https://www.indeed.com/viewjob?jk=6f672b26044ae87c) · The Brattle Group

Boston · early career, 0 to 3 years · $91k to $115k

| The posting says | The skill |
| --- | --- |
| "Use AI-assisted development responsibly without treating generated output as automatically correct" | Verification |
| "Comfort working in ambiguous problem spaces where the task may need to be clarified, decomposed, and revised" | Planning |
| "Git, notebooks, code review, documentation, testing, and reproducible workflows" | Your repo |
| "Explain technical work, assumptions, limitations, and next steps clearly" | Your pitch |

<p class="lede">"Project-based experience may also be considered."</p>

<!--
Start date July 2027: this is a role current students could apply for. Read the last line slowly: the project they start today counts. Ask: which of these lines could you show evidence for right now? Postings expire; replace before reusing this deck.
-->

---

# [AI Engineer](https://www.indeed.com/viewjob?jk=04b24d10854e0c3e) · Boston contract

| The posting says | The skill |
| --- | --- |
| "Build AI agents and integrate AI models with enterprise applications" | AI tools |
| "Support the full AI development lifecycle, from solution design to deployment and monitoring" | Plan, build, ship |
| "Strong problem-solving, documentation, and communication skills" | README and pitch |

<!--
Senior contract role ($68/hour), included to show the same skills appear above entry level.
-->

---

# [Product Manager Intern](https://redhat.wd5.myworkdayjobs.com/en-US/jobs/details/Product-Manager-Intern_R-059060) · Red Hat

Raleigh and Boston · internship

| The posting says | In this project |
| --- | --- |
| "Collect and document input from technology users, customers, and other stakeholders" | Your partner's issue; outside users in week 2 |
| "Develop and prioritize and document requirements, epics, and user stories" | `SPEC.md` and your GitHub issues |
| "Collaborate with engineering teams… to solve business problems" | Directing the agent |

<!--
Not every tech job is writing code. This internship is almost exactly today's class: talk to users, write requirements, prioritize, work with engineers. Postings expire; replace before reusing this deck.
-->

---

# [Technical Product Intern](https://redhat.wd5.myworkdayjobs.com/en-US/jobs/details/Technical-Product-Intern_R-059526-1) · Red Hat

Raleigh · internship

| The posting says | In this course |
| --- | --- |
| "Own a meaningful project end to end" | This project |
| "Use AI tools to work smarter and faster" | OpenCode, llmman, Whisper |
| "Build an automation demo that shows how teams simplify repetitive IT tasks" | Automate something you do daily |
| "Familiarity with Linux, containers (Docker, Podman, Kubernetes)" | Earlier lessons |
| "…project work where you created technical content, demos, or tutorials" | README, demo GIF, pitch |

<!--
Internal title is Technical Marketing Manager. Point out that students have already used Linux, Podman, and AI tools in this course; they can list those today. Postings expire; replace before reusing this deck.
-->

---

# [Software Engineer Intern](https://redhat.wd5.myworkdayjobs.com/en-US/jobs/details/Software-Engineer-Intern_R-059038) · Red Hat

Boston, Lowell, Raleigh, Durham · internship

| The posting says | In this project |
| --- | --- |
| "Design, develop, and maintain code in Python, Golang or similar" | Your app |
| "Add new features, debug, identify, and track issues" | GitHub issues and PRs |
| "Collaborate with… Quality Engineering, Designers, Product Management or Documentation" | Partner swap, README |
| "Passion, curiosity, and desire to create new things" | Something you'd use yourself |

<p class="question">What's the same in all five postings?</p>

<!--
Even the software engineering internship lists design, issue tracking, and collaboration alongside writing code. Its curriculum also includes AI, GitHub, and Agile. Expected answers to the question: planning and design, AI tools, communication and documentation, working with others. Nobody is asking for "can type code fast." Postings expire; replace before reusing this deck.
-->

---

# Writing code is no longer the scarce skill

Agents write code quickly. What's valuable now:

- **Deciding** what to build, and what not to build
- **Breaking it down** into small pieces of work
- **Directing** an agent with clear constraints
- **Checking** what it produced before you accept it

<p class="lede">The agent does the typing. You make the decisions.</p>

<!--
This is the main idea of the whole project. Every artifact students produce over the next three weeks is evidence of one of these four skills.
-->

---

# What employers look for

| Skill | What it looks like |
| --- | --- |
| Experience with AI tools | OpenCode, llmman, Whisper: what you did with each |
| Planning and design | A spec, scoped issues, an `AGENTS.md` |
| Verification | Tests, CI, "I checked X before and after" |
| Shipping and users | Real people used it; you acted on their feedback |
| Communication | A README a stranger can follow; a 2-minute pitch |

<!--
Encourage students to name the AI tools on their résumé along with what they did with each one. "Used OpenCode" is weak; "planned and built a syllabus-to-calendar tool with OpenCode, reviewed every change" is strong.
-->

---

# What a reviewer notices in your repo

- README: **why** it exists, a screenshot or GIF, setup steps that work
- `SPEC.md` and `AGENTS.md`: your plan and your instructions to the agent
- GitHub Issues as the to-do list; changes made in small PRs
- At least one test, run automatically by GitHub Actions
- A real user's feedback, filed as an issue and then fixed
- A tagged release, such as `v0.1.0`

<p class="lede">You'll have every item on this list by Class 4.</p>

<!--
Most student portfolios have none of the last three. A test running in GitHub Actions alone puts a student ahead of most applicants for internships.
-->

---

# The project

<p class="lede">Build a small tool that solves a problem you actually have,<br>and get at least one person besides you to use it.</p>

Start from something you do every day that could be automated or made faster.

> "I noticed X wasted my time. I built Y. My roommate used it, found a bug, and I fixed it."

<!--
One real user who gave feedback makes a better interview story than a long feature list.
-->

---

# Four classes

| Class | Focus | Due before next class |
| --- | --- | --- |
| **1** | **Today:** scope, spec, issues, first build | Smallest working version; partner's issue fixed |
| **2** | Real users, a test, GitHub Actions | Two outside users; their feedback filed and one fixed |
| **3** | Release `v0.1.0`, README, practice pitch | Release tagged; slide and demo GIF in shared deck |
| **4** | **2-minute presentations** | — |

<!--
Each week adds one thing employers look for: something that works, then real users, then a release and a pitch. A student who falls behind still has something to show at each stage.
-->

---

# Four ground rules

1. **OpenCode writes the code.** If you use llmman, use it *inside* the app.
2. **Make the LLM optional,** or read its address from a setting like `MODEL_URL`.
3. **Start a new repo** with a name that describes the tool.
4. **Keep it small.** No code until your scope sentence is approved.

<!--
1. A 4B local model is a slow, frustrating coding agent. Use OpenCode's free hosted models for coding. llmman is a good feature: summarize, sort, or extract from messy text. Interview line: "no user data leaves the laptop."
2. If the app needs llmman, every user needs llmman. A MODEL_URL setting lets it work with llmman, Ollama, or a hosted provider. That's a design decision they can explain.
3. "opencode-website" says little on a résumé. The Assignment 5 site can become their portfolio page and link to the new app.
4. Most student projects that fail were too big.
-->

---

# Ideas that use an LLM

| Idea | LLM role |
| --- | --- |
| Syllabus to calendar file | Finds dates and assignments |
| Commit message writer from `git diff` | Summarizes the change |
| Job application tracker with résumé match | Compares résumé to posting, privately |
| Lecture notes to flashcards | Writes questions and answers |
| Voice memo to action items | Summary and to-dos (builds on Whisper) |

<!--
Starting points only; students may use their own idea. Ask who already has one before showing these.
-->

---

# Ideas with no model: free hosting

| Idea | LLM role |
| --- | --- |
| Roommate expense splitter | None needed |
| Club sign-up page with a waitlist | Optional |
| Study timer and habit tracker | Optional weekly summary |

Apps that don't need an LLM can go on **GitHub Pages** for free.

<p class="lede">The easiest way to get real users: nothing runs on their laptop.</p>

<!--
The job tracker also works on GitHub Pages without the match check. A sign-up page needs somewhere to store data; a shared form or the browser's local storage keeps it simple.
-->

---

# Your scope sentence

**[Who]** wastes time on **[task]**.<br>
The smallest version is **[one screen or one command]**<br>
that **[does one thing]**.

Example:

> Students in my classes waste time copying deadlines from syllabi into their calendars. The smallest version is a command that reads a pasted syllabus and outputs a calendar file of the due dates.

<!--
Give students 8 minutes to write their sentence. Walk around and approve each one before they move on. Projects that are too big are the biggest risk to this project.
-->

---

# Partner check · 5 minutes

Swap sentences with a partner and answer:

1. Could this be built in **one afternoon?** If not, what can you remove?
2. Who besides the author would **actually use** this?

<p class="lede">Raise your hand when your sentence is ready for approval.</p>

<!--
Common problems: "an app that manages my whole life," a login system, anything that needs a database on day one. Push students to the single most useful screen or command.
-->

---

# Plan with the agent

1. Create a new GitHub repo and clone it (same steps as the OpenCode activity).
2. Open the cloned folder in OpenCode Desktop.
3. Paste the starter prompt on the next slide.

**Planning comes from the prompt, not a button.** The prompt tells the agent not to change files yet, so it works in any mode.

**Models:** OpenCode's free models, [TerrierGPT](https://myapps.bu.edu/apps/terriergpt) with your BU login, or your own paid subscription.

<!--
Optional Plan agent: Desktop hides the Plan/Build picker by default. Settings > General > Show agent makes it appear below the prompt. Some Desktop versions never show it (GitHub issue 57812). Terminal version: Shift+Tab. Don't spend class time on the picker.
Source: https://github.com/anomalyco/opencode/issues/59642
-->

---

# Starter prompt

```text
I'm building a small tool. My scope sentence is:
"<paste scope sentence>"

Help me plan the smallest version that works. Propose:
1. A SPEC.md with: problem, target user, up to 3 features for v0.1,
   what's out of scope, tech stack, how to run it, and how to test it.
2. An AGENTS.md with constraints for you: language/framework, no secrets
   in the repo, keep changes small, explain commands before running them.
3. Three to five GitHub issues, each small enough for one PR.
Ask me questions before deciding anything I didn't specify.
Do not create or change any files yet. Just propose the plan.
```

<!--
Students can copy this from the lesson plan in the repo (lessons/lesson-9/PLAN.md) or from the published slides.
-->

---

# You make the decisions

- Answer the agent's questions.
- **Cut anything beyond your scope sentence.**
- Then: *"Now write SPEC.md and AGENTS.md as we agreed."*
- Create the 3 to 5 issues **yourself** on GitHub.

<p class="lede">Before the break: <code>SPEC.md</code>, <code>AGENTS.md</code>, and 3 to 5 issues.</p>

<!--
Creating the issues by hand helps students see the list as their own plan rather than the agent's. If they used the Plan agent, they switch back to Build before asking it to write files.
-->

---
layout: center
class: text-center
---

# Break · 10 minutes

---

# Build the smallest version that works

- **One issue, one branch, one PR.**
- Run it yourself after every agent change.
- Can't explain a change? Ask the agent before you accept it.
- Put the run command in the README as soon as it works.
- Using an LLM? Call it through `MODEL_URL` from day one.

<p class="lede">The goal is something that runs, not something finished.</p>

<!--
25 minutes. Walk around. The most common mistake is letting the agent combine several issues into one giant change.
-->

---

# Laptop swap · your first user

Swap with a partner. As their first user:

1. Follow **only the README** to run the app.
2. Try the one thing it's supposed to do.
3. File **one real GitHub issue**: a bug, a confusing step, or a missing feature.

<p class="question">Could you run it without asking the author anything?</p>

<!--
Every student leaves with their first piece of real user feedback, and sees how much the README matters. If a repo is private, the author adds the partner as a collaborator, or the partner writes the issue and the author files it.
-->

---

# Class 4: your 2-minute pitch

| Time | Part |
| --- | --- |
| 20 sec | **Problem:** who wastes time on what |
| 60 sec | **Demo:** show it working |
| 20 sec | **What a user told me:** one piece of feedback and the change it led to |
| 20 sec | **Next:** one tradeoff you made and what you'd build next |

<p class="lede">The same pitch works in a job interview.</p>

<!--
Preview this now so students know where the project is going. The third part is why collecting feedback in week 2 matters: they can't skip it if they have to talk about it.
-->

---

# Due before Class 2

- New repo shared with the instructor
- `SPEC.md` with your scope sentence at the top, and `AGENTS.md`
- 3 to 5 GitHub issues
- Smallest working version on `main`, with README run steps that work
- Your partner's issue fixed in a PR that closes it

<!--
Announce the submission location and checkpoint points (suggested 10 of 50) here.
-->
