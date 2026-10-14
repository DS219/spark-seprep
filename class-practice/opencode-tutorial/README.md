# Class activity: Build with OpenCode

**Time: 45 minutes.** Companion to [Lesson 7](../../lessons/lesson-7/README.md).
You will use a coding agent to build a small website, serve it on your laptop,
and improve it after checking its behavior yourself.

This is a classroom adaptation of [OpenCode School](https://opencode.school),
especially Installation, Models, Permissions, Instructions, Agents, and
[Build a website](https://opencode.school/exercises/build-a-website/).
Our version uses ordinary HTML, CSS, and JavaScript so we can focus on the agent
workflow. The school exercise uses Hono and Cloudflare Workers. **We serve locally:
no Cloudflare account, deployment, domain, or payment is required.**

## Checkpoints

| Minutes | Work | Evidence you can show |
| --- | --- | --- |
| 0–8 | Create and clone your GitHub repo, open it in OpenCode | Your cloned repo and a short model reply |
| 8–15 | Interview and plan | Your brief and a plan you understand |
| 15–27 | Build and serve | A page at `http://localhost:8000` |
| 27–37 | Inspect and improve | One observed problem and a verified fix |
| 37–45 | Review changes and capture evidence | Git commit, screenshot, short reflection |

## 1. Create your assignment repo and connect (0–8 minutes)

1. Download **OpenCode Desktop** from [the official download page](https://opencode.ai/download).
   Choose your OS and chip. On macOS, check Apple menu > About This Mac for Apple
   Silicon or Intel. Install and launch the app. Windows users can use the Windows
   Desktop app; use WSL for the terminal commands below if that is your usual setup.
2. In the **GitHub website**, sign in and open [New repository](https://github.com/new).
   Select your personal account as the owner and name the repo `opencode-website`
   (or another available name). This is **the repo you will use for homework**.
   Choose Public, or Private if you will give the instructor access. Enable
   **Add a README file**, then click **Create repository**. You do not need
   to fork `spark-seprep` or enable GitHub Pages.
3. On your new repo's page, click **Code** and copy its clone URL. Use **SSH**
   if you configured a GitHub SSH key earlier in the course; otherwise use
   HTTPS with your existing GitHub authentication. In a macOS, Linux, or WSL
   terminal, replace the example URL with the one you copied:

   ```bash
   mkdir -p ~/projects
   cd ~/projects
   git clone git@github.com:YOUR-USERNAME/opencode-website.git
   cd opencode-website
   git switch -c website
   git remote -v
   ```

   If you chose HTTPS, use `git clone https://github.com/YOUR-USERNAME/opencode-website.git`
   instead. If you chose a different repo name, use that name in the `cd` command.
   Confirm `origin` points to **your** new repo. Cloning already sets up Git:
   do not run `git init` or create another repo inside this folder.
4. In OpenCode Desktop, select **Open Project** and choose the **cloned folder**
   `~/projects/opencode-website`. Opening that folder gives OpenCode access to
   the local project files; pasting a GitHub link alone does not open the clone.
   Do not open your home folder or the entire class repo. If using WSL, make
   sure Desktop and your terminal operate on the same folder. An instructor
   can help select the WSL folder or use the terminal interface inside WSL.
5. Click the model name below the prompt and select an available **free** model.
   Model names and availability change. Use the label and current price in the
   picker rather than assuming a particular model is free. You may connect your
   own supported subscription/provider if you already have one. A chat subscription
   does not automatically include API credits. Purchasing anything is optional.
6. Send: `Reply with a short hello. Which model am I using?`
   Confirm the model in the **picker**, since a model can misidentify itself.

**Checkpoint:** `origin` points to your GitHub repo, OpenCode has the cloned
folder open, and everyone has a reply. If a model is busy or rate limited, choose
another free option. If setup takes longer than eight minutes, pair with a
classmate for the remaining steps and finish your individual setup afterward.
No Gemini API key is required for this activity.

## 2. Interview and plan (8–15 minutes)

Select **Plan** in the agent dropdown below the prompt. Plan is useful for
discussion, but it is not a security sandbox. Continue to read any requested actions.

Paste this prompt, replacing the bracketed text:

```text
I'm learning to use a coding agent. Help me plan a one-page website about
[a hobby, student club, project, or fictional business].
Ask me at most three short questions about the audience, content, and look.
Then propose a small plan. Explain each file you would create.
Use only index.html, style.css, and script.js, with no dependencies or CDN.
Include a heading, short introduction, two content sections, and one useful
interaction, such as filtering project items or switching the color theme.
The site must work at narrow and wide browser widths and with a keyboard.
Keep all work inside this project. Serve only on localhost.
Do not build yet, install packages, create accounts, or deploy anything.
```

Answer the questions. Give concrete content, such as two project names and their
descriptions, instead of asking for a generic site. Read the plan and adjust it.
Explain to a partner which files will change and what the interaction should do.

**Connection to the slides:** your brief supplies context. The agent decomposes
your goal into steps. You decide whether the plan meets your requirements.

## 3. Build and serve (15–27 minutes)

Switch to **Build**, then send:

```text
Implement the plan we agreed on. Also create AGENTS.md containing our project
constraints, and update the existing README.md with exact local run instructions.
Use semantic HTML, readable CSS, and a small script. Explain the interaction.
Add .gitignore entries for .env, node_modules/, and .DS_Store.
Check the file paths and JavaScript syntax if tools are available.
Tell me what you checked and what still needs a human browser check.
Do not commit, push, install anything, or start a server for me.
```

Watch at least one tool action. What file or command did the agent use? What
result came back? Permissions depend on configuration: the app may allow an
action, ask you, or deny it. Read requests and approve only actions that fit
this project. You do not need to grant broad access to keep up with class.

In a **separate terminal**, from your website folder, run:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [http://localhost:8000](http://localhost:8000) in your browser. Keep the
terminal running. Stop the server with `Ctrl+C` when you finish.

If `python3` is unavailable, Windows with Python installed can use
`py -m http.server 8000 --bind 127.0.0.1`. Ask the instructor for help if neither
works. A port conflict can be resolved by changing `8000` to `8001` in both
the command and browser URL. Seeing the page via `file://` does not meet the
local-serving checkpoint.

**Checkpoint:** the page loads over HTTP, and the interaction responds.

## 4. Inspect and improve (27–37 minutes)

Check the actual page yourself:

- Resize to about 375 pixels wide. Is text readable without horizontal scrolling?
- Press `Tab` to move through links and buttons. Is focus visible?
- Activate the interaction with the keyboard. Does it do what the brief promised?
- Open browser developer tools > Console. Are there errors?

Choose **one observed issue** or a concrete improvement. Use text to describe
what you see; free models may not support screenshots. For example:

```text
At a narrow browser width, the project titles extend past the right edge.
Inspect the relevant CSS and explain the cause. Fix the layout while preserving
the current content and interaction. Tell me which files changed and how to
check the result. Do not commit or push.
```

Refresh and repeat the same check. If the first page passes all checks, make a
small intentional improvement, such as clearer button text or a useful empty
state for a filter. Record the before/after behavior.

**Connection to the slides:** this is the observe-and-repeat part of the loop.
A confident agent reply is a claim. Your browser check supplies evidence.

## 5. Review and save evidence (37–45 minutes)

Run these in another terminal, leaving your server running:

```bash
git status
git diff
git ls-files --others --exclude-standard
```

On a new repo, `git diff` does not show untracked files. Open the files listed
by the last command in your editor and read them. Ask OpenCode to explain a
line you do not understand. Confirm there are no credentials or unrelated files.

After review, stage the intended files:

```bash
git add index.html style.css script.js README.md AGENTS.md .gitignore
git diff --cached
git commit -m "Build a locally served website with an interactive feature"
```

Take a screenshot of the **served page with the address bar visible**, showing
`localhost:8000` or `127.0.0.1:8000` (or the port you used).
Write a short note in `REFLECTION.md`: model used, one tool action you observed,
and one change you verified in the browser. Commit the note too. After reviewing your commits, push your work branch yourself:

```bash
git push -u origin website
```

Open your GitHub repo and select the `website` branch to confirm your files
appear. Save that branch URL for homework. If authentication blocks the push,
ask for help and finish it before submitting homework.

**Class exit ticket:** show your local page and explain one tool action and one
verified improvement. If pairing, both partners should explain part of the work.
Continue in this same repository for [Build a Website homework](../../assignments/assignment-5-build-a-website.md).

## If something goes wrong

| Symptom | Next step |
| --- | --- |
| Clone or push fails | Check the copied URL, account access, and SSH/authentication setup. Ask for help; do not paste a token into OpenCode. |
| Free model unavailable | Try a different currently free model, shorten the prompt, or pair temporarily. |
| Model requests Cloudflare setup | Restate: “This class requires localhost only. Stop deployment steps.” |
| Directory listing instead of page | Start the server in the folder containing `index.html`. |
| Styling or script missing | Check file names and relative paths. Read the Console/Network errors. |
| Server exits immediately | Read the terminal error; check Python and the port. |
| WSL files differ from app files | Verify the same folder in Desktop and the terminal before generating more files. |
| Agent says it tested the browser | Ask what tool and result support that claim. Perform your own browser check. |

## Optional OpenCode School practice

You may enroll yourself and explore individual lessons after class. Enrollment
and school completion badges are optional. If you use a school-provided prompt,
use **your own** enrollment prompt and explicitly replace deployment with local
serving. Our class instructions and homework requirements define the deliverable.

GitHub setup reference: [Create and clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories).
