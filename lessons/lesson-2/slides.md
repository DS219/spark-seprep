---
theme: default
title: DS 219 - Command Line and SSH
info: |
  Lesson 2 for DS 219, Software Engineering Career Prep Practicum.
author: Sally O'Malley
keywords: Linux, terminal, shell, SSH, filesystems, DS219
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
presenter: true
browserExporter: true
exportFilename: ds219-lesson-2
lineNumbers: true
---

<div class="eyebrow">Boston University · Fall 2026</div>

# Your First Remote<br><span class="accent">Linux Session</span>

<p class="lede">DS 219 · Lesson 2 · Command Line and SSH</p>

<div class="footer-note">September 9, 2026 · Sally O'Malley</div>

<!--
Welcome students back. Ask them to open Blackboard, the class repository, and a terminal before class begins.
-->

---

<div class="eyebrow">Warm-up</div>

# Where is your code running?

<div class="grid three" style="margin-top: 1.5rem">
  <div class="card"><h2>Your laptop</h2><p>Local files, local programs, your operating system</p></div>
  <div class="card red"><h2>A remote VM</h2><p>Another computer, reached over a network</p></div>
  <div class="card"><h2>The cloud</h2><p>Still somebody's computers</p></div>
</div>

<p class="question">How can one keyboard control all three?</p>

<!--
Take two or three answers. The point is not to define cloud computing yet. Establish that remote systems are real computers with their own users, files, processes, and permissions.
-->

---

<div class="eyebrow">Tonight's mission</div>

# Connect. Orient. Change. Verify. Exit.

<div class="timeline">
  <div><strong>4:30</strong><span class="muted">Terminal + shell mental model</span></div>
  <div><strong>4:50</strong><span class="muted">Navigate the Linux filesystem</span></div>
  <div><strong>5:15</strong><span class="muted">Command-line practice</span></div>
  <div><strong>5:35</strong><span class="muted">10-minute break</span></div>
  <div><strong>5:45</strong><span class="muted">SSH + key authentication</span></div>
  <div><strong>6:05</strong><span class="muted">Class VM mission + debrief</span></div>
</div>

<!--
Tell students that the goal is one successful remote workflow, not memorizing a command dictionary.
-->

---

<div class="eyebrow">By the end</div>

# You should be able to…

<div class="grid two">
  <div class="card"><span class="number">01</span><p>Explain the difference between a terminal, shell, command, and remote host.</p></div>
  <div class="card"><span class="number">02</span><p>Navigate Linux paths and inspect files without a graphical interface.</p></div>
  <div class="card"><span class="number">03</span><p>Use an SSH key pair without exposing the private key.</p></div>
  <div class="card"><span class="number">04</span><p>Connect to your class account, complete a task, verify it, and exit.</p></div>
</div>

<!--
Confidence comes from knowing what state you are in and how to verify it. Accuracy is more valuable than speed tonight.
-->

---
layout: center
class: text-center
---

<div class="section-number">01</div>
<div class="eyebrow">The interface</div>

# Terminal ≠ shell ≠ operating system

<p class="lede" style="margin: 1rem auto">Three layers that are often casually called “the terminal.”</p>

<!--
Ask students which word they normally use. Explain that casual usage is fine, but the distinction helps when debugging.
-->

---

<div class="eyebrow">The layers</div>

# What happens after you type a command?

<div class="grid three">
  <div class="card"><h2>Terminal</h2><p>The window that displays text and sends keystrokes.</p></div>
  <div class="card red"><h2>Shell</h2><p>The command interpreter. Tonight, usually Bash.</p></div>
  <div class="card"><h2>Operating system</h2><p>Runs programs and manages users, files, processes, and devices.</p></div>
</div>

<div class="terminal-window" style="margin-top: 1.35rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">sally@laptop ~ $</span> whoami
<span class="terminal-output">sally</span></div>
</div>

<!--
GNU describes a shell as both a command interpreter and a programming language. Bash means Bourne Again Shell. Do not spend time on shell history beyond the pun.
-->

---

<div class="eyebrow">Open a terminal</div>

# Different window, same goal

<div class="grid three">
  <div class="card"><h2>macOS</h2><p>Spotlight → Terminal<br><span class="muted">or a terminal you already use</span></p></div>
  <div class="card red"><h2>Windows</h2><p>Open your WSL distribution<br><span class="muted">not Command Prompt</span></p></div>
  <div class="card"><h2>Linux</h2><p>Open Terminal from your application menu.</p></div>
</div>

<p class="lede" style="margin-top: 1.4rem">VS Code's integrated terminal is convenient. It is still a terminal connected to a shell.</p>

<!--
Pause and make sure every student has a usable shell. Pair students by platform. Windows students should use WSL for course commands.
-->

---

<div class="eyebrow">Read the prompt</div>

# Your prompt is a status display

<div class="terminal-window" style="margin-top: 1.3rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">sally@macbook</span> <span style="color: var(--gold)">~/projects</span> $</div>
</div>

<div class="grid three" style="margin-top: 1.2rem">
  <div class="card"><h2>Who?</h2><p><code>sally</code>, the current user</p></div>
  <div class="card"><h2>Where?</h2><p><code>macbook</code>, the current computer</p></div>
  <div class="card"><h2>Which directory?</h2><p><code>~/projects</code>, the current location</p></div>
</div>

<!--
Prompts vary, so students should not expect this exact shape. The reliable commands are whoami, hostname, and pwd.
-->

---

<div class="eyebrow">Orient first</div>

# Ask the system where you are

<div class="grid four">
  <div class="card"><h2><code>whoami</code></h2><p>Which user am I?</p></div>
  <div class="card"><h2><code>hostname</code></h2><p>Which computer am I using?</p></div>
  <div class="card"><h2><code>pwd</code></h2><p>Which directory am I in?</p></div>
  <div class="card"><h2><code>ls</code></h2><p>What is here?</p></div>
</div>

<p class="question">Before changing anything: Who am I, where am I, and what is here?</p>

<!--
Have everyone run all four commands locally. This four-command sequence becomes the class's recovery pattern whenever someone feels lost.
-->

---

<div class="eyebrow">Command anatomy</div>

# Most commands follow a recognizable shape

<div class="command-shape">
  <div><code>ls</code><strong>Command</strong><br><span class="muted">the action</span></div>
  <div><code>-la</code><strong>Options</strong><br><span class="muted">change behavior</span></div>
  <div><code>~/projects</code><strong>Argument</strong><br><span class="muted">the target</span></div>
</div>

<div class="terminal-window" style="margin-top: 1.4rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">$</span> ls -la ~/projects</div>
</div>

<!--
Not every command uses this exact grammar, but it is a useful starting pattern. Encourage students to read commands left to right before running them.
-->

---
layout: center
class: text-center
---

<div class="section-number">02</div>
<div class="eyebrow">The filesystem</div>

# One tree, many paths

<p class="lede" style="margin: 1rem auto">Your current directory changes how relative paths are interpreted.</p>

<!--
The key mental model is a tree rooted at slash. Students do not need a tour of every top-level Linux directory tonight.
-->

---

<div class="eyebrow">A small filesystem</div>

# Paths identify locations

<div class="grid two">
  <pre class="path-tree" aria-label="Example filesystem hierarchy">/
└── home
    └── sally
        ├── notes.txt
        └── ds219
            └── practice.txt</pre>
  <div>
    <div class="card red"><h2>Absolute path</h2><p><code>/home/sally/ds219/practice.txt</code><br>Starts at <code>/</code>.</p></div>
    <div class="card" style="margin-top: 1rem"><h2>Relative path</h2><p><code>ds219/practice.txt</code><br>Starts where you are now.</p></div>
  </div>
</div>

<!--
Explain slash as the filesystem root, tilde as the current user's home, dot as the current directory, and dot-dot as the parent directory.
-->

---

<div class="eyebrow">Navigate</div>

# Move deliberately

<div class="grid two">
  <div class="card"><h2><code>cd directory</code></h2><p>Move into a directory.</p></div>
  <div class="card"><h2><code>cd ..</code></h2><p>Move to the parent directory.</p></div>
  <div class="card"><h2><code>cd ~</code></h2><p>Return to your home directory.</p></div>
  <div class="card red"><h2><code>pwd</code></h2><p>Verify the result. Never navigate by vibes.</p></div>
</div>

<!--
Demo cd, pwd, and ls as a repeating loop. Show that cd with no argument also returns home, but teach cd ~ because its intent is visible.
-->

---

<div class="eyebrow">Create and inspect</div>

# Small commands compose into a workflow

```bash {1|2|3|4|5|all}
mkdir ds219
cd ds219
touch notes.txt
echo "first remote session" > notes.txt
cat notes.txt
```

<p class="lede">Create → move → write → inspect.</p>

<!--
Run this live. Explain that greater-than redirects command output and replaces the destination file. Double greater-than appends. Students will practice both later.
-->

---

<div class="eyebrow">From commands to scripts</div>

# Save the workflow. Run it again.

<div class="grid two">
  <div>

```bash
#!/usr/bin/env bash
echo "Hello, $USER"
date
pwd
```

<p class="small muted">A Bash script is a plain-text file containing commands Bash can run.</p>

  </div>
  <div class="card red" style="align-self: center">
    <h2>Run the file with Bash</h2>
    <div class="terminal-window" style="margin: 0.75rem 0 1rem">
      <div class="terminal-body"><span class="prompt-local">$</span> bash hello.sh</div>
    </div>
    <p>The shell reads each command in order, just as if you typed it yourself.</p>
  </div>
</div>

<!--
Connect this directly to the previous slide: we just ran several commands one at a time. If the sequence is useful enough to repeat, we can save those commands in a text file.

"Script" is the broad term for a small program used to automate a task. A Bash script is specifically written for the Bash shell. It often begins as a list of commands that run from top to bottom, then grows to include variables, conditions, loops, and reusable functions.

Point out the first line, called a shebang. It identifies Bash as the intended interpreter when the file is later made executable and run directly. For now, `bash hello.sh` works without changing file permissions. We will connect the executable bit to scripts on the permissions slide.

Emphasize that a script is executable instructions, not inert notes. Read and understand scripts before running them, especially scripts copied from the internet.
-->

---

<div class="eyebrow">Streams</div>

# Output can become input

<div class="grid three">
  <div class="card"><h2><code>></code></h2><p>Write output to a file, replacing its contents.</p></div>
  <div class="card"><h2><code>>></code></h2><p>Append output to the end of a file.</p></div>
  <div class="card red"><h2><code>|</code></h2><p>Send one command's output into another command.</p></div>
</div>

```bash
date > session.txt
whoami >> session.txt
cat session.txt | wc -l
```

<!--
This is the first glimpse of composition. Do not explain file descriptors yet. Ask students to predict the line count before running the final command.
-->

---

<div class="eyebrow">Permissions</div>

# Linux asks who may do what

<div class="terminal-window" style="margin-top: 1.2rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">$</span> ls -l joke.sh
<span class="terminal-output">-rw-r--r--  1 sally students  84 Sep 9 17:12 joke.sh</span></div>
</div>

<div class="grid three" style="margin-top: 1.1rem">
  <div class="card"><h2><code>r</code></h2><p>read</p></div>
  <div class="card"><h2><code>w</code></h2><p>write</p></div>
  <div class="card red"><h2><code>x</code></h2><p>execute</p></div>
</div>

<!--
Keep the owner/group/other model high-level. Tonight students only need to recognize whether their script is executable.
-->

---

<div class="eyebrow">Make a script executable</div>

# Permission is part of the file

```bash {1|2|3|all}
chmod u+x joke.sh
ls -l joke.sh
./joke.sh
```

<p class="question">Why <code>./joke.sh</code> instead of just <code>joke.sh</code>?</p>

<!--
Explain that dot-slash names a file in the current directory. The shell otherwise searches directories listed in PATH. Avoid a deep PATH discussion tonight.
-->

---

<div class="eyebrow">Editors</div>

# Choose a tool. Know the escape hatch.

<div class="grid three">
  <div class="card"><h2>VS Code</h2><p>Comfortable for local project work and integrated terminals.</p></div>
  <div class="card red"><h2><code>nano</code></h2><p>Friendly for a quick edit on a remote machine.</p></div>
  <div class="card"><h2><code>vi</code> / <code>vim</code></h2><p>Common on servers. Know <code>Esc</code>, <code>:wq</code>, and <code>:q!</code>.</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">The best editor is the one you can exit.</p>

<!--
Do not make editor preference a culture war. If time allows, open a tiny file in vi and demonstrate insert mode, Escape, save, and quit.
-->

---

<div class="eyebrow">Safety</div>

# The shell assumes you meant it

<div class="grid two">
  <div class="card green"><h2>Before acting</h2><p>Run <code>pwd</code> and <code>ls</code>. Read the command left to right. Check the target.</p></div>
  <div class="card red"><h2>Before deleting</h2><p>Remember: <code>rm</code> has no trash can. Use <code>rm -i</code> while learning.</p></div>
</div>

<p class="big-idea" style="margin-top: 1.4rem">Copying commands is not the same as understanding them.</p>

<!--
Never demo destructive recursive commands for shock value. The habit is inspect, predict, run, verify.
-->

---
layout: center
class: text-center
---

<div class="section-number">03</div>
<div class="eyebrow">Remote access</div>

# SSH: a secure conversation between computers

<p class="lede" style="margin: 1rem auto">Your terminal stays local. Your shell can run somewhere else.</p>

<!--
Return to the warm-up. Students are about to control the class VM from their own keyboards.
-->

---

<div class="eyebrow">Client and server</div>

# What SSH connects

<div class="connection-flow">
  <div class="connection-node"><div class="number">01</div><h2>Your laptop</h2><p>SSH client<br>Your private key</p></div>
  <div class="connection-arrow">⇄</div>
  <div class="connection-node"><div class="number">02</div><h2>Class VM</h2><p>SSH server<br>Your Linux account</p></div>
</div>

<p class="lede" style="margin-top: 1.3rem">SSH encrypts the connection and authenticates both sides.</p>

<!--
The client initiates a connection to the server, normally on TCP port 22. Avoid a protocol deep dive. The two identities matter: the server proves which machine it is, and the user proves which account they may use.
-->

---

<div class="eyebrow">The command</div>

# Name the user and the host

<div class="terminal-window" style="margin-top: 1.5rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">$</span> ssh YOUR_USERNAME@VM_ADDRESS</div>
</div>

<div class="grid two" style="margin-top: 1.2rem">
  <div class="card"><h2><code>YOUR_USERNAME</code></h2><p>Your BU email name without <code>@bu.edu</code>.</p></div>
  <div class="card red"><h2><code>VM_ADDRESS</code></h2><p>The class VM address provided in Blackboard.</p></div>
</div>

<!--
Do not place the public VM address in the public deck. Put it in Blackboard. Confirm the username convention before class.
-->

---

<div class="eyebrow">The first connection</div>

# “Authenticity can't be established” is a question

```text
The authenticity of host 'VM_ADDRESS' can't be established.
ED25519 key fingerprint is SHA256:...
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

<div class="grid two" style="margin-top: 1.1rem">
  <div class="card green"><h2>Verify</h2><p>Compare the fingerprint with the trusted value in Blackboard.</p></div>
  <div class="card red"><h2>Then trust</h2><p>Type <code>yes</code> only after the fingerprint matches.</p></div>
</div>

<!--
This prompt protects against connecting to the wrong machine. Publish the VM host-key fingerprint in Blackboard before class. Do not teach students to click through it blindly.
-->

---

<div class="eyebrow">User authentication</div>

# Passwords work. Keys scale better.

<div class="key-pair">
  <div class="key-card public"><span class="key-icon">🔓</span><h2>Public key</h2><p>Copy it to systems that should recognize you.</p><p><code>id_ed25519.pub</code></p></div>
  <div class="key-card private"><span class="key-icon">🔐</span><h2>Private key</h2><p>Keep it on your device. Never paste, upload, or share it.</p><p><code>id_ed25519</code></p></div>
</div>

<!--
Avoid saying that SSH encrypts a login by “encrypting with the public key.” Modern SSH authentication is a challenge-and-signature protocol. The safe beginner model is that the private key proves possession without being sent to the server.
-->

---

<div class="eyebrow">Check before creating</div>

# You may already have a key

```bash
ls -la ~/.ssh
```

<div class="grid two" style="margin-top: 1.3rem">
  <div class="card"><h2>Look for a pair</h2><p><code>id_ed25519</code> and <code>id_ed25519.pub</code></p></div>
  <div class="card red"><h2>Do not overwrite</h2><p>If a key already exists, stop and inspect before generating another.</p></div>
</div>

<!--
Walk the room before generating keys. Students may already have a GitHub key, a course key, or multiple named keys.
-->

---

<div class="eyebrow">Generate a key</div>

# Use Ed25519 for a new key

```bash
ssh-keygen -t ed25519 -C "YOUR_BU_EMAIL"
```

<div class="grid two" style="margin-top: 1.2rem">
  <div class="card"><h2>File location</h2><p>Accept the default only if it will not overwrite an existing key.</p></div>
  <div class="card red"><h2>Passphrase</h2><p>Add one. Your SSH agent can remember it during your session.</p></div>
</div>

<!--
GitHub and Google Cloud both document Ed25519 as the normal modern choice, with RSA as a legacy compatibility option. Do not ask students to reveal the generated key material.
-->

---

<div class="eyebrow">Install the public key</div>

# Copy only the file ending in <code>.pub</code>

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub YOUR_USERNAME@VM_ADDRESS
```

<p class="lede" style="margin-top: 1.4rem">The temporary password authorizes this one-time setup. Future logins use the key.</p>

<div class="card red" style="margin-top: 1rem; min-height: auto"><strong>Platform note:</strong> if <code>ssh-copy-id</code> is unavailable, use the course's platform-specific fallback.</div>

<!--
Do not put the shared temporary password on public slides. Provide it in Blackboard or verbally. Windows and some macOS setups may not include ssh-copy-id, so the in-class activity needs a tested fallback before publication.
-->

---

<div class="eyebrow">Connect with the key</div>

# Same command, different proof

```bash
ssh -i ~/.ssh/id_ed25519 YOUR_USERNAME@VM_ADDRESS
```

<div class="terminal-window" style="margin-top: 1.2rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-local">sally@laptop ~ $</span> ssh sally@VM_ADDRESS
<span class="prompt-remote">sally@class-vm ~ $</span> <span class="terminal-output"># now remote</span></div>
</div>

<!--
Have students compare the prompt before and after connecting. If the default key name is used, -i may be unnecessary; showing it makes the selected identity explicit.
-->

---

<div class="eyebrow">Same tool, different destination</div>

# SSH can authenticate to GitHub too

<div class="grid two">
  <div class="card red"><h2>Class VM</h2><p><code>ssh user@host</code><br>opens a remote shell for your Linux account.</p></div>
  <div class="card"><h2>GitHub</h2><p>Your key authenticates Git operations. GitHub does not provide an interactive shell.</p></div>
</div>

```bash
ssh -T git@github.com
```

<!--
This is the bridge to the Git lesson. A successful GitHub test intentionally reports that GitHub does not provide shell access and may return exit status 1.
-->

---
layout: center
class: text-center
---

<div class="section-number">04</div>
<div class="eyebrow">In-class practice</div>

# The class VM mission

<p class="lede" style="margin: 1rem auto">Use your own account. Ask a neighbor for reasoning, never for credentials.</p>

<!--
Move students into the activity. Pair by platform where possible. The activity details may change after instructor review, so keep this slide focused on the success condition.
-->

---

<div class="eyebrow">Mission checklist</div>

# Leave evidence that you were here

<div class="status-strip">
  <div><strong>1 · Connect</strong><span>SSH into your account</span></div>
  <div><strong>2 · Orient</strong><span>whoami, hostname, pwd</span></div>
  <div><strong>3 · Create</strong><span>directory + session file</span></div>
  <div><strong>4 · Verify</strong><span>inspect, then exit</span></div>
</div>

```bash
mkdir -p ~/commandline-practice
date > ~/commandline-practice/session.txt
whoami >> ~/commandline-practice/session.txt
hostname >> ~/commandline-practice/session.txt
cat ~/commandline-practice/session.txt
```

<!--
These commands are safe to rerun except the first date line will be replaced. Decide during the activity revision whether students should also download and execute joke.sh.
-->

---

<div class="eyebrow">Know your boundaries</div>

# Your account is yours, not the whole server

<div class="grid two">
  <div class="card green"><h2>You can</h2><p>Create files in your home directory, run ordinary commands, and inspect your own work.</p></div>
  <div class="card red"><h2>You cannot</h2><p>Use <code>sudo</code>, become <code>root</code>, modify system configuration, or access another student's home.</p></div>
</div>

<p class="question">A permission error is information, not a request to force harder.</p>

<!--
Demonstrate one harmless permission denial if useful. Explain least privilege: students have the access required for the course, not administrative control of a shared machine.
-->

---

<div class="eyebrow">When it fails</div>

# Read the error before changing the command

<div class="grid two">
  <div class="card"><h2>Permission denied (publickey)</h2><p>Wrong user, wrong key, or public key not installed.</p></div>
  <div class="card"><h2>No such file or directory</h2><p>Wrong path, wrong working directory, or typo.</p></div>
  <div class="card"><h2>Connection timed out</h2><p>Network, address, firewall, or server availability.</p></div>
  <div class="card red"><h2>Host key changed</h2><p>Stop. Verify with the instructor. Do not blindly delete the warning.</p></div>
</div>

<!--
Model debugging out loud: observe exact error, identify the failing layer, test one hypothesis, then retry. Use ssh -v only if the class is ready for verbose output.
-->

---

<div class="eyebrow">Finish cleanly</div>

# Verify, then exit

```bash
whoami
hostname
cat ~/commandline-practice/session.txt
exit
```

<div class="terminal-window" style="margin-top: 1.2rem">
  <div class="terminal-bar"><span class="terminal-dot red-dot"></span><span class="terminal-dot gold-dot"></span><span class="terminal-dot green-dot"></span></div>
  <div class="terminal-body"><span class="prompt-remote">sally@class-vm ~ $</span> exit
<span class="terminal-output">Connection to VM_ADDRESS closed.</span>
<span class="prompt-local">sally@laptop ~ $</span></div>
</div>

<!--
Ask students to say which computer their prompt represents after exit. This catches the most important state transition in the lesson.
-->

---

<div class="eyebrow">Exit ticket</div>

# Explain one transition

<div class="grid three">
  <div class="card"><h2>Local → remote</h2><p>How did you know the SSH connection worked?</p></div>
  <div class="card"><h2>Private → public</h2><p>Which key may be copied, and which must remain secret?</p></div>
  <div class="card red"><h2>Lost → oriented</h2><p>Which commands tell you who you are, where you are, and what is here?</p></div>
</div>

<!--
Take responses aloud or in Blackboard. Listen for prompt changes plus whoami/hostname/pwd, not merely “the command worked.”
-->

---

<div class="eyebrow">Next</div>

# From remote access to collaboration

<p class="big-idea">Next we use these same habits to understand <span class="accent">Git</span>: state, history, identity, and verification.</p>

<div class="grid two" style="margin-top: 1.5rem">
  <div class="card"><h2>Before next class</h2><p>Complete <a href="https://github.com/DS219/spark-seprep/blob/main/assignments/assignment-2.md" target="_blank">Assignment 2 on GitHub</a>, then submit the form in Blackboard.</p></div>
  <div class="card red"><h2>Keep safe</h2><p>Know where your private key lives. Never submit or share it.</p></div>
</div>

<!--
Open the GitHub assignment briefly so students recognize the page they will use. Blackboard remains the source of truth for the due date, submission form, and grade.
-->

---
layout: center
class: text-center
---

<div class="eyebrow">DS 219 · Lesson 2</div>

# You controlled another computer<br>without leaving your chair.

<p class="lede" style="margin: 1rem auto">The command line is not magic. It is a precise conversation.</p>

<!--
Close by normalizing difficulty. Students who connected, recovered from one error, and could identify where their commands ran achieved tonight's core outcome.
-->
