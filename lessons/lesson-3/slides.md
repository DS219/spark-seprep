---
theme: default
title: DS 219 - Git and GitHub
info: |
  Lesson 3 for DS 219, Software Engineering Career Prep Practicum.
author: Sally O'Malley
keywords: Git, GitHub, branches, commits, pull requests, DS219
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-3
lineNumbers: true
---

<div class="eyebrow">Fall 2026</div>

# Branching Out<br><span class="accent">with Git and GitHub</span>

<p class="lede">DS 219 · Lesson 3 · Your first repository and contribution</p>

<div class="footer-note">Sally O'Malley</div>

<!--
Open with the concrete outcome: every student will create and push to a repository they own, then use those same mechanics to prepare a contribution to the class repository. Git is not a quiz vocabulary list tonight.
-->

---

<div class="eyebrow">Last week → this week</div>

# The same key.<br>A new computer.

<div class="connection-flow">
  <div class="connection-node"><h2>Last week</h2><p>Your SSH key identified you to the class Linux VM.</p></div>
  <div class="connection-arrow">→</div>
  <div class="connection-node"><h2>Tonight</h2><p>Your public key lets GitHub recognize your computer.</p></div>
</div>

<p class="question">What stays private? What gets shared?</p>

<!--
Answer: the private key stays only on their computer. The public key can go to GitHub. Students who created an SSH key in Lesson 2 should reuse it rather than create more keys.
-->

---

<div class="eyebrow">Quick setup check</div>

# Prove GitHub knows your key

<div class="command-stack">
<div class="terminal-window"><div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div><div class="terminal-body"><span class="prompt-local">$</span> cat ~/.ssh/id_ed25519.pub
<span class="terminal-output">ssh-ed25519 AAAA... your_email@example.com</span></div></div>
<div class="terminal-window"><div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div><div class="terminal-body"><span class="prompt-local">$</span> ssh -T git@github.com
<span class="terminal-output">Hi USERNAME! You've successfully authenticated.</span></div></div>
</div>

<p class="lede">Add only the <strong>public</strong> key in GitHub: Settings → SSH and GPG keys.</p>

<!--
Skim the class activity. Students add their existing public key, then run ssh -T git@github.com. The success message also says GitHub does not provide shell access; that is expected. Do not ask students to paste keys into Blackboard or chat.
-->

---

<div class="eyebrow">Identity matters</div>

# A commit records who made it

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --list
```

<p class="lede">This labels commits on this computer. It is different from GitHub authentication.</p>

<!--
Git's author identity is metadata recorded in commits. SSH keys prove access to GitHub. They are related in the workflow but solve different problems.
-->

---
layout: center
class: text-center
---

<div class="section-number">01</div>
<div class="eyebrow">Version control</div>

# Save history.<br><span class="accent">Work without fear.</span>

<!--
Ask what students currently do before changing a document or code file: copy it, rename it final-final, email it to themselves. Git gives a better record of intentional save points.
-->

---

<div class="eyebrow">Why Git exists</div>

# A project changes over time

<div class="timeline">
  <div><strong>Commit A</strong><span class="muted">first working version</span></div>
  <div><strong>Commit B</strong><span class="muted">add a feature</span></div>
  <div><strong>Commit C</strong><span class="muted">fix a problem</span></div>
  <div><strong>Today</strong><span class="muted">inspect, compare, recover</span></div>
</div>

<div class="grid three" style="margin-top: 1.5rem">
  <div class="card"><h2>History</h2><p>Know what changed and why.</p></div>
  <div class="card red"><h2>Safety</h2><p>Try a change without losing the last working state.</p></div>
  <div class="card"><h2>Collaboration</h2><p>Coordinate work without emailing files around.</p></div>
</div>

---

<div class="eyebrow">Two related tools</div>

# Git ≠ GitHub

<div class="grid two">
  <div class="card"><h2>Git</h2><p>A free, open-source version-control system. It tracks history in a repository on your computer.</p></div>
  <div class="card red"><h2>GitHub</h2><p>A service for hosting Git repositories and collaborating through issues, reviews, and pull requests.</p></div>
</div>

<p class="question">Git works without GitHub. GitHub uses Git.</p>

<!--
Avoid calling GitHub “the cloud version of Git.” It is a hosting and collaboration service built around Git repositories. GitLab and Codeberg are other examples.
-->

---

<div class="eyebrow">One repository, four states</div>

# Your work travels through states

<div class="git-flow">
  <div><strong>Working tree</strong><span>Files you are editing locally.</span></div>
  <div><strong>Staging area</strong><span>Changes selected for the next commit.</span></div>
  <div><strong>Commit</strong><span>An intentional local history entry.</span></div>
  <div><strong>Remote</strong><span>A shared repository such as GitHub.</span></div>
</div>

```bash
git status
git add yourname.md
git commit -m "Add your name: Assignment 3"
git push
```

<!--
Git status is the recurring orientation command, analogous to whoami/pwd/ls in Lesson 2. Git add does not upload. Git commit does not upload. Git push sends committed history to a remote.
-->

---
layout: center
class: text-center
---

<div class="section-number">02</div>
<div class="eyebrow">Guided practice</div>

# Create a repository.<br><span class="accent">Then make it yours.</span>

<!--
The first activity is deliberately a personal sandbox. Students own this repository and may safely push directly to main. It gives them a complete, low-stakes loop before we introduce forks and pull requests.
-->

---

<div class="eyebrow">In-class activity · Step 1</div>

# Create a small GitHub repository

<div class="grid two">
  <div class="card red"><h2>In the browser</h2><p>GitHub → <strong>New repository</strong></p><p>Choose a short name, make it public, and initialize it with a README.</p></div>
  <div class="card"><h2>Why start here?</h2><p>You own this repository. It is a safe place to learn the full Git loop.</p></div>
</div>

<p class="lede">This is your personal practice repository, not Assignment 3.</p>

<!--
Follow class-practice/git-create-repo.md. A public repository lets students see that a remote is a shared, inspectable copy. If a student has a privacy concern, let them use a private repository for this practice activity and verify it with you.
-->

---

<div class="eyebrow">In-class activity · Step 2</div>

# Clone your repository locally

```bash
cd ~
mkdir -p github
cd github
git clone git@github.com:YOUR-GITHUB-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
ls
```

<p class="lede">Use the SSH URL from GitHub’s <strong>Code</strong> menu. You should see <code>README.md</code>.</p>

<!--
This repeats the same clone pattern students will use later. Pause to connect the browser repository (remote) to the folder on their computer (local clone). Do not introduce upstream yet.
-->

---

<div class="eyebrow">In-class activity · Step 3</div>

# Make your first change<br>and push it

```bash
touch git-practice.md
# Write a few lines, save, then:
git status
git add git-practice.md
git commit -m "Add Git practice file"
git push origin main
```

<p class="lede">Refresh GitHub. Your file should be visible in <strong>your</strong> repository.</p>

<!--
This is the first complete loop: working tree, staging area, local commit, remote push. It is okay to push to main here because students own this sandbox repository. Ask them to run git status after the push and observe a clean working tree.
-->

---

<div class="eyebrow">The bridge</div>

# Same Git loop.<br><span class="accent">Different collaboration rules.</span>

<div class="grid two">
  <div class="card"><h2>Your practice repository</h2><p>You own it. A direct push to <code>main</code> is fine.</p></div>
  <div class="card red"><h2>Course repository</h2><p>It is shared. Work on a branch in your fork, then open a pull request.</p></div>
</div>

<p class="question">The commands are familiar. The responsibility changes.</p>

<!--
This is the conceptual hinge of the lesson. The fork/branch/PR sequence is not ceremony: it protects a shared project and creates a reviewable conversation around a proposed change.
-->

---
layout: center
class: text-center
---

<div class="section-number">03</div>
<div class="eyebrow">Your copy of a shared project</div>

# Fork. Clone. Branch.<br><span class="accent">Then contribute.</span>

---

<div class="eyebrow">Fork first</div>

# A fork is your GitHub copy

<div class="remote-map">
  <div><strong>DS219 / spark-seprep</strong><span>The maintained course repository.</span></div>
  <div class="arrow">→</div>
  <div style="border-color: var(--red-bright)"><strong>Your fork</strong><span>Your GitHub copy. You can push here.</span></div>
  <div class="arrow">→</div>
  <div><strong>Your computer</strong><span>Your local clone, where you edit and commit.</span></div>
</div>

<p class="lede">Fork in the browser. Clone to your computer.</p>

<!--
Use the course repository as the live example. A fork records a relationship to the upstream repository and is the normal contribution route for people without write access.
-->

---

<div class="eyebrow">Clone second</div>

# Clone makes a local working copy

```bash
mkdir -p ~/github
cd ~/github
git clone git@github.com:YOUR-GITHUB-USERNAME/spark-seprep.git
cd spark-seprep
git remote -v
```

<p class="lede">Use the SSH clone URL. It uses the GitHub key you just verified.</p>

<!--
Have students replace only their GitHub username. Pause at git remote -v: origin should point to their fork. Do not use a global insteadOf setting; cloning the SSH URL is sufficient and explicit.
-->

---

<div class="eyebrow">Name the source</div>

# <code>origin</code> is yours.<br><code>upstream</code> is the source.

```bash
git remote add upstream git@github.com:DS219/spark-seprep.git
git remote -v
```

<div class="grid two" style="margin-top: 1rem">
  <div class="card red"><h2><code>origin</code></h2><p>Your fork. Push your branch here.</p></div>
  <div class="card"><h2><code>upstream</code></h2><p>The DS219 repository. Fetch updates from here.</p></div>
</div>

<!--
Remote is Git's name for another copy of the repository. The words origin and upstream are conventions, not magic. We use them because conventions make team instructions readable.
-->

---

<div class="eyebrow">Before making changes</div>

# Check your starting state

```bash
git checkout main
git fetch upstream
git rebase upstream/main
git status
```

<p class="lede">Start the assignment from the current course version, then create your branch.</p>

<!--
Explain this sequence slowly. Fetch downloads knowledge of the upstream history. Rebase brings the local main branch up to date. If students have conflicts, stop and ask for help. This is not the night to speed-run conflict resolution.
-->

---

<div class="eyebrow">A branch is a safe workspace</div>

# Change the branch,<br>not <code>main</code>

```bash
git checkout -b assignment-3
git branch --show-current
```

<div class="grid two" style="margin-top: 1.1rem">
  <div class="card"><h2><code>main</code></h2><p>The stable starting point.</p></div>
  <div class="card red"><h2><code>assignment-3</code></h2><p>Your proposed change, isolated until review.</p></div>
</div>

<!--
A branch is not a folder and not a second copy of every file. It is a named line of development. The point is reversible, reviewable work.
-->

---

<div class="eyebrow">Guided practice</div>

# Make one small, visible change

```bash
cd student-work/assignment-3
touch yourname.md
# Open it in your editor, write content, then save.
git status
```

<p class="lede">Create a Markdown file with your name, favorite language, code sample, and an explanation.</p>

<!--
This is the middle of Assignment 3. The class goal is to get every student to a clean starting point and a saved file; faster students can format and preview their Markdown. Do not have students commit directly to main.
-->

---

<div class="eyebrow">Markdown is source text</div>

# Write once. Render everywhere.

```md
# Your Name

My favorite language is **Python** because...

## Example code

```python
print("Hello, DS 219")
```

### Code explanation

Run this with `python hello.py`.
```

<p class="lede">Preview the file before you commit it.</p>

<!--
The assignment is a small public contribution, so avoid overly personal information. Students should use a code sample they understand and can explain. The outer code fence is shown as a Markdown example; point out the indentation is presentation-only.
-->

---

<div class="eyebrow">Create history</div>

# Stage. Commit. Push.

```bash
git add yourname.md
git status
git commit -m "Add Your Name: Assignment 3"
git push -u origin assignment-3
```

<p class="lede">Read <code>git status</code> before and after each transition.</p>

<!--
Tell students to use a descriptive message, not “update.” Commit creates a local checkpoint. The -u option remembers this remote branch so future git push commands are shorter.
-->

---

<div class="eyebrow">The pull request</div>

# A PR asks for review<br>before a change lands

<div class="remote-map">
  <div><strong>Your branch</strong><span><code>assignment-3</code> on your fork.</span></div>
  <div class="arrow">→</div>
  <div style="border-color: var(--red-bright)"><strong>Pull request</strong><span>Explain the proposed change and invite review.</span></div>
  <div class="arrow">→</div>
  <div><strong>DS219 main</strong><span>Merge only after review.</span></div>
</div>

<p class="question">A pull request is a conversation around a proposed change.</p>

<!--
Demo opening a PR from the GitHub banner, choosing the upstream DS219 repository as the base. Point out the changed-files view. Students do not merge their own PRs.
-->

---

<div class="eyebrow">Class checkpoint</div>

# You are ready when…

<div class="grid two">
  <div class="card"><h2>GitHub access</h2><p><code>ssh -T git@github.com</code> succeeds.</p></div>
  <div class="card"><h2>Correct remotes</h2><p><code>origin</code> is your fork; <code>upstream</code> is DS219.</p></div>
  <div class="card"><h2>Correct branch</h2><p><code>git branch --show-current</code> prints <code>assignment-3</code>.</p></div>
  <div class="card red"><h2>Visible work</h2><p><code>git status</code> tells you exactly what will be committed.</p></div>
</div>

<!--
Have students partner-check the four states. This catches wrong remotes and work on main before they become frustrating.
-->

---
layout: center
class: text-center
---

<div class="section-number">04</div>
<div class="eyebrow">Assignment 3</div>

# Make a contribution<br><span class="accent">someone else can review.</span>

---

<div class="eyebrow">Assignment 3 · 25 points</div>

# A small public contribution

<div class="grid five">
  <div class="card"><span class="number">01</span><p>GitHub SSH access</p></div>
  <div class="card"><span class="number">02</span><p>Fork, clone, and remotes</p></div>
  <div class="card"><span class="number">03</span><p>Clear Markdown content</p></div>
  <div class="card"><span class="number">04</span><p>Branch, commit, and push</p></div>
  <div class="card red"><span class="number">05</span><p>Pull request and Blackboard form</p></div>
</div>

<p class="lede" style="margin-top: 1.25rem"><a href="https://github.com/DS219/spark-seprep/blob/main/assignments/assignment-3.md">Open Assignment 3 in the course repository</a>, then submit your PR link through Blackboard.</p>

<!--
State the grading standard: effort and a traceable workflow matter. Do not require a single commit; real contributions often develop through multiple commits. Verify the Blackboard form fields before class.
-->

---

<div class="eyebrow">When something breaks</div>

# Diagnose the state.<br>Then ask a precise question.

<div class="grid three">
  <div class="card"><h2>Access</h2><p>Run <code>ssh -T git@github.com</code>.</p></div>
  <div class="card"><h2>Repository</h2><p>Run <code>git remote -v</code>.</p></div>
  <div class="card red"><h2>Changes</h2><p>Run <code>git status</code>.</p></div>
</div>

<p class="question">“Here is the command, here is the output, here is what I expected.”</p>

<!--
This is the same orientation technique as Lesson 2. Normalize errors as information. Tell students never to paste tokens, private keys, or their full configuration files into a public issue or PR.
-->

---

<div class="eyebrow">Exit ticket</div>

# Show your work<br><span class="accent">in GitHub.</span>

<div class="grid two">
  <div class="card red"><h2>Submit one screenshot</h2><p>Show your in-class GitHub repository with <code>git-practice.md</code> visible.</p></div>
  <div class="card"><h2>Why this matters</h2><p>It confirms you created a repository, pushed a file, and can find the result on GitHub.</p></div>
</div>

<p class="lede" style="margin-top: 1.4rem">Upload the screenshot through the Blackboard exit-ticket form before you leave.</p>

<!--
Use the screenshot as lightweight participation and attendance evidence. Keep “choose one transition and explain it” as an in-class discussion prompt instead of a written exit-ticket question. If the file is not visible yet, accept a screenshot of the repository page plus the student's current command/error as an honest effort record.
-->

---

<div class="eyebrow">Next time</div>

# Your history is<br><span class="accent">a shared artifact.</span>

<p class="lede">Bring your pull request, questions, and one thing Git made clearer or more confusing.</p>

<div class="footer-note">DS 219 · Git, GitHub, and responsible collaboration</div>

<!--
Close by reminding students that their contribution will be visible to the class repository. Encourage modest, understandable changes and honest questions.
-->
