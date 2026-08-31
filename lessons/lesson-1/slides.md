---
theme: default
title: DS 219 — Welcome and Open Source
info: |
  Lesson 1 for DS 219, Software Engineering Career Prep Practicum.
author: Sally O'Malley
keywords: open source, licenses, governance, foundations, DS219
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-1
lineNumbers: true
---

<div class="eyebrow">Boston University · Fall 2026</div>

# Software Engineering<br><span class="accent">Career Prep Practicum</span>

<p class="lede">DS 219 · Lesson 1 · Welcome and Open Source</p>

<div class="footer-note">September 2, 2026 · Sally O'Malley</div>

<!--
Welcome students as they arrive. Ask them to introduce themselves to one person nearby before class begins.
-->

---

<div class="eyebrow">Start here</div>

# Meet someone new

<p class="question">What is one technology you are curious about right now?</p>

<div class="grid two" style="margin-top: 2rem">
  <div class="card"><h2>1 minute</h2><p>Introduce yourself to someone nearby.</p></div>
  <div class="card red"><h2>Then switch</h2><p>Listen for the thing they want to learn.</p></div>
</div>

<!--
Use this as the room settles. Invite two or three volunteers to introduce their partner and name the technology they mentioned.
-->

---

<div class="eyebrow">Tonight's route</div>

# From course mechanics to open-source ecosystems

<div class="timeline">
  <div><strong>4:30</strong><span class="muted">Welcome + how the course works</span></div>
  <div><strong>4:55</strong><span class="muted">Open source + licenses</span></div>
  <div><strong>5:15</strong><span class="muted">Repository investigation</span></div>
  <div><strong>5:35</strong><span class="muted">10-minute break</span></div>
  <div><strong>5:45</strong><span class="muted">Foundations + open AI</span></div>
  <div><strong>6:05</strong><span class="muted">Next week + assignment</span></div>
</div>

<!--
Set the expectation that breaks are real and that the class will mix discussion with hands-on work.
-->

---

<div class="eyebrow">Your instructor</div>

# Sally O'Malley

<div class="grid two">
  <div class="card red">
    <h2>Now</h2>
    <p>Principal Software Engineer<br>Emerging Technologies<br>Red Hat, Office of the CTO</p>
  </div>
  <div class="card">
    <h2>The scenic route</h2>
    <p>Chemical engineering + biology → information technology → software engineering</p>
  </div>
</div>

<p class="lede" style="margin-top: 1.4rem">I teach what I use, what I am learning, and what surprised me in real engineering work.</p>

<!--
Tell the personal version, not a résumé recital. Explain that this semester is solo-instructed, while guests from industry may join particular classes.
-->

---

<div class="eyebrow">The course promise</div>

# Practice the work around the code

<div class="grid three">
  <div class="card"><h2>Operate</h2><p>Terminal, Linux, SSH, containers, cloud environments</p></div>
  <div class="card"><h2>Collaborate</h2><p>Git, GitHub, branches, reviews, open-source communities</p></div>
  <div class="card"><h2>Explore</h2><p>Local AI, models, agents, and fast-changing engineering tools</p></div>
</div>

<p class="lede" style="margin-top: 1.25rem">The topics will evolve. The habits transfer.</p>

<!--
Emphasize that this is a practicum. Students are not expected to arrive with experience in every area.
-->

---

<div class="eyebrow">By December</div>

# You should be able to…

<div class="grid two">
  <div class="card"><span class="number">01</span><p>Work confidently in a terminal and on a remote Linux system.</p></div>
  <div class="card"><span class="number">02</span><p>Use Git and GitHub to collaborate without fear.</p></div>
  <div class="card"><span class="number">03</span><p>Build, run, inspect, and explain containers.</p></div>
  <div class="card"><span class="number">04</span><p>Evaluate and experiment with local AI and agents.</p></div>
</div>

<!--
The goal is not memorizing commands. It is knowing how to investigate, ask for help, and recover when an unfamiliar tool fails.
-->

---

<div class="eyebrow">Weekly rhythm</div>

# Show up. Try things. Ask questions. Reflect.

<div class="grid four">
  <div class="card"><h2>Discuss</h2><p>Concepts and current industry context</p></div>
  <div class="card"><h2>Watch</h2><p>Short live demonstrations</p></div>
  <div class="card"><h2>Practice</h2><p>Hands-on work, usually with a partner nearby</p></div>
  <div class="card"><h2>Submit</h2><p>Evidence of effort and what you learned</p></div>
</div>

<p class="question">Confusion is expected. Silence is optional.</p>

<!--
Explain how students should ask questions in class and where to ask between classes. Blackboard is the source of truth for announcements and due dates; GitHub holds technical materials.
-->

---

<div class="eyebrow">Grades</div>

# Effort and participation are the point

<div class="grid two">
  <div class="card red"><div class="number">50%</div><h2>Attendance + participation</h2><p>Be present, engage, collaborate, and contribute to the room.</p></div>
  <div class="card"><div class="number">50%</div><h2>Assignments</h2><p>Try the work, document the process, and submit evidence of learning.</p></div>
</div>

<p class="lede" style="margin-top: 1.2rem">Blackboard is the source of truth for grades, deadlines, and the published late-work policy.</p>

<!--
Make the attendance stakes explicit without sounding punitive. Explain how students should communicate when illness or emergencies affect attendance. Do not improvise a late policy here; use the published Blackboard language.
-->

---

<div class="eyebrow">Support</div>

# You are not expected to get stuck alone

<div class="grid two">
  <div class="card red"><h2>Office hours</h2><p>Wednesdays at 3:15 PM<br>CDS 206 C</p></div>
  <div class="card"><h2>Course systems</h2><p><strong>Blackboard:</strong> announcements, submissions, grades<br><strong>GitHub:</strong> code, lessons, technical resources</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">Ask early. Debugging is easier before the deadline.</p>

<!--
Mention that changes or cancellations to office hours will be announced through Blackboard.
-->

---
layout: center
class: text-center
---

<div class="section-number">01</div>
<div class="eyebrow">The first big idea</div>

# What is open source?

<p class="lede" style="margin: 1rem auto">A development model, a legal framework, and a community practice.</p>

<!--
Ask for definitions before advancing. Capture a few phrases verbally: free, public, collaborative, GitHub, modifiable.
-->

---

<div class="eyebrow">Discuss</div>

# Which one is open source?

<div class="grid three">
  <div class="card"><h2>A</h2><p>The source is on GitHub. No license file.</p></div>
  <div class="card"><h2>B</h2><p>The code is downloadable, but the terms prohibit commercial use.</p></div>
  <div class="card green"><h2>C</h2><p>The code has an OSI-approved license granting use, modification, and redistribution.</p></div>
</div>

<p class="question" v-click>Only <strong>C</strong> clearly meets the open-source standard.</p>

<!--
Let students vote before revealing the answer. A public repository without a license remains under ordinary copyright. “Source available” can be useful, but it is not necessarily open source.
-->

---

<div class="eyebrow">Definition</div>

# Open source is about permission

<p class="big-idea">People must be allowed to <span class="accent">use, study, modify, and share</span> the software.</p>

<div class="grid two" style="margin-top: 1.5rem">
  <div class="card"><h2>Source code</h2><p>The preferred form for understanding and changing the software</p></div>
  <div class="card red"><h2>License</h2><p>The explicit legal grant that makes collaboration possible</p></div>
</div>

<div class="footer-note">Source: Open Source Initiative, The Open Source Definition</div>

<!--
“Free” describes freedoms, not necessarily price. Open-source companies can sell software, hosted services, training, support, and expertise.
-->

---

<div class="eyebrow">An open-source ecosystem</div>

# Five layers, five different questions

<div class="grid three">
  <div class="card"><h2>Code</h2><p>What does it do?</p></div>
  <div class="card"><h2>License</h2><p>What may I do with it?</p></div>
  <div class="card"><h2>Governance</h2><p>Who decides?</p></div>
  <div class="card"><h2>Community</h2><p>Who contributes and participates?</p></div>
  <div class="card"><h2>Foundation</h2><p>Who stewards shared infrastructure and assets?</p></div>
</div>

<!--
This distinction is the organizing framework for the rest of the lesson. A project can be open source without belonging to a foundation. A foundation does not write every line of a project.
-->

---

<div class="eyebrow">Licenses</div>

# Every license makes tradeoffs

<div class="spectrum"></div>
<div class="spectrum-labels">
  <span>Permissive<br><small>Few redistribution conditions</small></span>
  <span style="text-align:center">Reciprocal<br><small>Share some changes</small></span>
  <span style="text-align:right">Strong copyleft<br><small>Share derivative source</small></span>
</div>

<div class="grid two" style="margin-top: 1.8rem">
  <div class="card cyan"><h2>Permissions</h2><p>Use, copy, modify, distribute, and sometimes patent rights</p></div>
  <div class="card gold"><h2>Conditions</h2><p>Preserve notices, disclose source, use the same license, or offer network users source</p></div>
</div>

<!--
This is a conceptual map, not a legal ranking or legal advice. The right license depends on the project's goals and dependencies.
-->

---

<div class="eyebrow">Permissive licenses</div>

# Broad reuse, limited obligations

<div class="grid three">
  <div class="card"><h2>MIT</h2><p>Short, permissive, widely used</p></div>
  <div class="card red"><h2>Apache 2.0</h2><p>Permissive with an explicit patent grant and notice requirements</p></div>
  <div class="card"><h2>BSD</h2><p>A family of permissive licenses with attribution conditions</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">Derivative work may usually be distributed under different terms, if the original conditions are followed.</p>

<!--
Point ahead to this course repository, which uses Apache 2.0. Avoid attempting detailed legal interpretation in class.
-->

---

<div class="eyebrow">Copyleft licenses</div>

# Keep shared work shareable

<div class="grid two">
  <div class="card red"><h2>GPL</h2><p>Distribution of a covered derivative work generally requires corresponding source under the GPL.</p></div>
  <div class="card gold"><h2>AGPL</h2><p>Adds a source-offer obligation for users who interact with modified software over a network.</p></div>
</div>

<p class="question">Copyleft is not “no commercial use.” Companies build businesses with copyleft software.</p>

<!--
Keep this high-level. The point is reciprocity, not a complete licensing seminar.
-->

---

<div class="eyebrow">10-minute investigation</div>

# Read a repository before you run it

<p><a href="https://github.com/DS219/spark-seprep">github.com/DS219/spark-seprep</a></p>

<div class="grid two">
  <div class="card"><h2>Find</h2><ul class="checklist"><li>The license</li><li>The latest commit</li><li>Contributors</li><li>Open issues and pull requests</li></ul></div>
  <div class="card red"><h2>Discuss</h2><ul class="checklist"><li>What may you do with this code?</li><li>Who appears to make decisions?</li><li>What looks active or stale?</li><li>What evidence is missing?</li></ul></div>
</div>

<!--
Students may work in pairs. Ask them not to clone anything yet; this is about learning to read a repository in the browser. Circulate and ask what evidence supports each conclusion.
-->

---

<div class="eyebrow">Debrief</div>

# What did the repository tell us?

<div class="grid three">
  <div class="card red"><h2>Apache 2.0</h2><p>Permissions and conditions are explicit.</p></div>
  <div class="card"><h2>History</h2><p>Commits and contributors show activity, not quality by themselves.</p></div>
  <div class="card"><h2>Governance</h2><p>GitHub signals influence, but formal decision rules may live elsewhere.</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">A repository is evidence. Interpretation still requires context.</p>

<!--
Ask each pair for one concrete observation and one uncertainty. Model evidence-based language: “The latest commit was…” rather than “This project is healthy.”
-->

---
layout: center
class: text-center
---

<div class="section-number">02</div>
<div class="eyebrow">The second big idea</div>

# Why do foundations exist?

<p class="lede" style="margin: 1rem auto">Open code still needs durable stewardship.</p>

<!--
Resume after the break here. Ask: what problems appear when a widely used project is controlled by one company or one person?
-->

---

<div class="eyebrow">Neutral stewardship</div>

# A foundation can hold the commons together

<div class="grid four">
  <div class="card"><h2>Assets</h2><p>Trademarks, funds, and shared infrastructure</p></div>
  <div class="card"><h2>Governance</h2><p>Charters, boards, and transparent processes</p></div>
  <div class="card"><h2>Operations</h2><p>Events, training, legal help, and administration</p></div>
  <div class="card"><h2>Neutrality</h2><p>A home broader than one vendor or employer</p></div>
</div>

<p class="question">A foundation supports a project. It does not replace its maintainers or community.</p>

<!--
“Foundation” is not one legal or governance model. Each foundation has its own structure, membership, and relationship to technical decision-making.
-->

---

<div class="eyebrow">A small ecosystem map</div>

# Related, but not the same organization

<div class="foundation-map">
  <div class="foundation-parent">
    <h2>Linux Foundation</h2>
    <p class="muted">A neutral home for many open-technology ecosystems</p>
    <div class="foundation-children">
      <div class="foundation-child"><h3>CNCF</h3><p>Cloud-native projects</p></div>
      <div class="foundation-child"><h3>PyTorch Foundation</h3><p>Open-source AI projects</p></div>
    </div>
  </div>
  <div class="foundation-independent">
    <h2>OpenClaw Foundation</h2>
    <p>An independent nonprofit stewarding the OpenClaw personal-agent project and community.</p>
  </div>
</div>

<!--
The key contrast: CNCF and the PyTorch Foundation operate within the Linux Foundation ecosystem. The OpenClaw Foundation is an independent nonprofit, not a Linux Foundation project.
-->

---

<div class="eyebrow">Case study 1</div>

# CNCF: the infrastructure beneath modern AI

<div class="grid two">
  <div>
    <p class="big-idea">The AI boom did not replace infrastructure. Models still have to run somewhere.</p>
    <span class="tag">Kubernetes</span><span class="tag">OpenTelemetry</span><span class="tag">Envoy</span>
  </div>
  <div class="card red">
    <h2>From OpenShift to AI</h2>
    <p><strong>82%</strong> of surveyed container users run Kubernetes in production.</p>
    <p><strong>66%</strong> of surveyed organizations hosting generative AI use Kubernetes for at least some inference workloads.</p>
  </div>
</div>

<div class="footer-note">Source: CNCF 2025 Annual Cloud Native Survey</div>

<!--
Keep this to about five minutes. Personal bridge: when Sally first taught this material, CNCF was central because her work focused on OpenShift and Kubernetes. AI changed the headline, but not the need for scheduling, networking, observability, security, and scaling. CNCF is part of the Linux Foundation and provides a vendor-neutral home for many projects that supply those layers. Note that the percentages come from CNCF's own ecosystem survey, so treat them as evidence rather than universal measurements. The course will return to this ecosystem when students reach containers and Kubernetes.
-->

---

<div class="eyebrow">Case study 2</div>

# PyTorch Foundation: open-source AI grows up

<div class="grid two">
  <div class="card red"><h2>Origin</h2><p>PyTorch moved from Meta to a vendor-neutral foundation within the Linux Foundation in 2022.</p></div>
  <div class="card"><h2>Today</h2><p>The foundation hosts an expanding family of AI projects, including PyTorch, vLLM, DeepSpeed, Ray, and Safetensors.</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">Technical maintainers still own technical decisions; the foundation supplies a durable, multi-stakeholder home.</p>

<div class="footer-note">Sources: PyTorch Foundation and PyTorch Foundation Projects</div>

<!--
This is the bridge from traditional open-source infrastructure to modern AI. Ask why neutrality might matter when multiple cloud and hardware companies depend on the same framework.
-->

---

<div class="eyebrow">Case study 3 · New in 2026</div>

# OpenClaw: independent by design

<div class="grid two">
  <div>
    <p class="big-idea" style="font-size: 1.75rem !important">A nonprofit home for an open-source personal AI assistant.</p>
    <p class="lede">Independent. Neutral. Community-driven.</p>
  </div>
  <div class="lobster-panel">
    <img class="lobster-mark" src="/lobster.webp" alt="Red low-poly lobster">
    <p class="lobster-caption">Why the lobster?<br><strong>Nobody knows.</strong></p>
  </div>
</div>

<div class="footer-note">Source: OpenClaw Foundation · openclaw.org</div>

<!--
Frame this as a current case study, not a product pitch. OpenClaw Foundation is an independent nonprofit created to keep the project open, neutral, and community-driven. Sally can briefly connect it to current work and explain why foundation formation changes project stewardship.
-->

---

<div class="eyebrow">Compare the models</div>

# Ask the same questions every time

| Question | CNCF | PyTorch Foundation | OpenClaw Foundation |
| --- | --- | --- | --- |
| Primary domain | Cloud native | Open-source AI | Personal AI agents |
| Organizational home | Linux Foundation | Linux Foundation | Independent nonprofit |
| Example project | Kubernetes | PyTorch | OpenClaw |
| What to inspect next | Charter + project maturity | Charter + technical governance | Nonprofit mission + project governance |

<!--
The table is intentionally incomplete. It models the next questions students should ask rather than declaring one governance structure “best.”
-->

---

<div class="eyebrow">Open-source AI</div>

# Source code is only one layer

<div class="grid four">
  <div class="card"><h2>Code</h2><p>Training and inference software</p></div>
  <div class="card"><h2>Weights</h2><p>Learned model parameters</p></div>
  <div class="card"><h2>Data information</h2><p>What shaped the system?</p></div>
  <div class="card"><h2>License terms</h2><p>What can users actually do?</p></div>
</div>

<p class="question">“Open weights” and “open source AI” are not automatically the same claim.</p>

<div class="footer-note">Source: Open Source Initiative, Open Source AI Definition 1.0</div>

<!--
Do not turn this into a model-licensing deep dive. The goal is to show why software-era vocabulary becomes harder when the artifact is produced through training.
-->

---

<div class="eyebrow">The industry view</div>

# Follow one project through the stack

<div class="grid three">
  <div class="card"><h2>Build</h2><p>Models, frameworks, runtimes, and agent applications</p></div>
  <div class="card red"><h2>Run</h2><p>Containers, orchestration, networking, and observability</p></div>
  <div class="card"><h2>Build around it</h2><p>Products, services, integrations, standards, and jobs</p></div>
</div>

<p class="question">The project is only the center. The ecosystem is the story.</p>

<!--
This reframes the old CNCF-only assignment. A project may live in CNCF, the PyTorch Foundation, another foundation, a company, or an independent community. The investigation asks students to distinguish repository popularity from evidence that people actually build products, services, integrations, standards, and careers around the project.
-->

---

<div class="eyebrow">One personal story</div>

# How has open source changed my life?

<p class="big-idea">It turned learning in public into a career, and coworkers into a worldwide community.</p>

<div class="grid two" style="margin-top: 1.5rem">
  <div class="card"><h2>Technical leverage</h2><p>I can inspect the systems I depend on and contribute improvements.</p></div>
  <div class="card red"><h2>Human leverage</h2><p>I can learn from maintainers, users, and contributors far beyond one company.</p></div>
</div>

<!--
Replace these general lines with a specific story from Sally's career: a first contribution, a community connection, or a project that changed an opportunity.
-->

---

<div class="eyebrow">Our shared workspace</div>

# DS 219 on GitHub

<p class="big-idea"><a href="https://github.com/DS219/spark-seprep">github.com/DS219/spark-seprep</a></p>

<div class="grid three" style="margin-top: 1.5rem">
  <div class="card"><h2>Lessons</h2><p>Slides, notes, and links</p></div>
  <div class="card"><h2>Assignments</h2><p>Hands-on work and instructions</p></div>
  <div class="card"><h2>Resources</h2><p>References and troubleshooting guides</p></div>
</div>

<!--
Show the repository live. Point out that the presentation itself is HTML generated from Markdown in Git.
-->

---

<div class="eyebrow">Next week</div>

# Your first remote Linux machine

<div class="grid three">
  <div class="card red"><h2>Terminal</h2><p>Navigate, inspect, and redirect output</p></div>
  <div class="card"><h2>SSH</h2><p>Connect securely to your account on the class VM</p></div>
  <div class="card"><h2>Keys</h2><p>Understand public and private key roles</p></div>
</div>

<p class="question">Never share a private key, password, API key, or access token in chat, Git, or an assignment.</p>

<!--
Preview that each student already has a separate VM login. Tell students what, if anything, they must install before class.
-->

---

<div class="eyebrow">Week 1 assignment</div>

# Introduce yourself

<div class="grid two" style="margin-top: 1.5rem">
  <div class="card red"><h2>Google Form</h2><p>Tell me about your experience, interests, learning goals, and what you want to explore.</p></div>
  <div class="card"><h2>25 points</h2><p>Open and submit the assignment through Blackboard.</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">This helps me shape the course around the class. There are no trick questions.</p>

<!--
Open the Blackboard assignment live if useful. State the due date exactly as published there, then show students that Blackboard links to the Google Form.
-->

---
layout: center
class: text-center
---

<div class="eyebrow">Exit ticket</div>

# One idea. One question.

<p class="lede" style="margin: 1rem auto 2rem">Before you leave, name one idea you are taking with you and one question you still have.</p>

<span class="tag">Use</span>
<span class="tag">Study</span>
<span class="tag">Modify</span>
<span class="tag">Share</span>

<!--
Take responses aloud or through the Blackboard exit-ticket mechanism. Use unanswered questions to tune Lesson 2.
-->
