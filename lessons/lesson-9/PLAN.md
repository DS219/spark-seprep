# Lesson 9 Plan: Build Something People Use

Week 1 of a four-class project. Classes 1 to 3 are build sessions. Class 4 is
for 2-minute student presentations.

**Class goal:** students leave with a scoped project idea, a spec and issue
list written with an AI coding agent, and a first working version started.

**The theme of the class:** employers now expect new developers to have
worked with AI tools. They don't just want someone who can prompt. They want
someone who can **plan, design, direct an agent, and check what it produced**.
This project gives students evidence they can point to.

## Project brief (tell students this first)

> **Build a small tool that solves a problem you actually have, and get at
> least one person besides you to use it.**

Students should start from something they do every day that could be
automated or made faster. One real user who gave feedback makes a better
interview story than a long feature list:

> "I noticed X wasted my time. I built Y. My roommate used it, found a bug,
> and I fixed it."

### The four classes

| Class | Focus | Due before next class |
| --- | --- | --- |
| **1 (this class)** | Scope, spec, issues, first build, partner test | Smallest working version pushed. Partner's issue fixed in a PR |
| **2** | Real users and quality: one test, GitHub Actions, feedback to issue to fix | Two users from outside the class. Their feedback saved as issues, at least one fixed |
| **3** | Ship and rehearse: `v0.1.0` release, README with screenshot or GIF, GitHub Pages if possible, timed practice pitches | Release tagged. Slide and demo GIF added to the shared deck |
| **4** | Presentations | — |

## Part 1: What employers look for (12 min)

Start by asking: *"If you were hiring a junior developer now that everyone
has AI coding tools, what would you want to see?"* Collect answers on the board,
then fill in what's missing.

**Talking points**

- **Writing code is no longer the scarce skill.** Agents write code quickly.
  The valuable skills are deciding what to build, breaking it into parts,
  giving an agent clear constraints, and catching its mistakes.
- **Experience with AI tools.** Students have now used OpenCode, local
  models with llmman, and Whisper. Encourage them to name these tools
  on a résumé, along with what they did with each one.
- **Planning and design.** A spec, a scoped list of issues, and an
  `AGENTS.md` show that the student was making the decisions and the agent
  was doing the typing.
- **Verification.** Tests, CI, and "I checked X before and after the change"
  separate engineers from people who accept whatever the agent produces.
- **Shipping and users.** Something real people used, a release, and feedback
  they acted on.
- **Communication.** A README a stranger can follow, and a 2-minute pitch.

**Show the checklist** (this is what interviewers and recruiters notice in a
GitHub repo):

- [ ] README: why the app exists, a screenshot or GIF, setup steps that work
- [ ] `SPEC.md` and `AGENTS.md`: the plan and the instructions given to the agent
- [ ] GitHub Issues as the to-do list, with changes made in small PRs
- [ ] At least one test, run automatically by GitHub Actions
- [ ] Feedback from a real user, saved as an issue and then fixed
- [ ] A tagged release, such as `v0.1.0`
- [ ] A 2-minute pitch: the problem, a demo, one tradeoff, what's next

> **Instructor prep:** bring two or three real job postings for junior or new
> grad roles that mention AI tools, coding assistants, or LLMs. Read one line
> from each out loud. Real postings are more convincing than any slide.

## Part 2: Ground rules and ideas (13 min)

### Four recommendations

1. **Use OpenCode to write the code. If you use llmman, use it inside the
   app.** Writing code through OpenCode with a 4B local model is slow and
   frustrating, so use OpenCode's free hosted models to write the code.
   llmman works well as a feature of the app itself: summarizing, sorting,
   or pulling details out of messy text. It also gives students something to say
   in an interview: *"no user data leaves the laptop."*
2. **Make the LLM optional, or let users choose where it runs.** If the app
   needs llmman, every user needs llmman too, which makes it hard to get
   users. Read the model's address from a setting such as `MODEL_URL`. Then
   the app works with llmman, Ollama, or a hosted provider. This is a real
   design decision that students can explain in an interview.
3. **Start a new repo for the app.** A repo named `opencode-website` says
   little on a résumé. Give the new repo a name that describes the tool.
   The website from Assignment 5 can become their portfolio page and link to
   the new app.
4. **Keep the scope small.** Most student projects that fail were too big.
   Nobody writes code until they've written their scope sentence (Part 3).

### Ideas from a student's daily life

| Idea | LLM role | How others could use it |
| --- | --- | --- |
| **Syllabus to calendar:** paste a syllabus, get a calendar file of all deadlines | Finds the dates and assignments in the text | Share the script with classmates |
| **Commit message writer:** writes a commit message from `git diff` | Summarizes the code change | A small command-line tool other developers can install |
| **Job application tracker** with a résumé-to-job-posting match check | Compares the résumé to the posting, privately | Personal use, or the tracker alone on GitHub Pages |
| **Lecture notes to flashcards** | Writes the questions and answers | Classmates in the same course |
| **Voice memo to action items** | Turns a transcript into a summary and to-dos | Club officers, study groups. Builds on the Whisper activity |
| **Roommate expense splitter** | None needed | Can be put on GitHub Pages for anyone |
| **Club or event sign-up page** with a waitlist | Optional | Real users right away |
| **Study timer and habit tracker** | Optional weekly summary | Can be put on GitHub Pages for anyone |

**Point this out:** apps that don't need a model can be published on GitHub
Pages for free. That's the easiest way to get real users, because nothing
needs to run on the user's laptop.

Students may use their own idea instead. These are starting points.

## Part 3: Scope sentence and partner check (13 min)

Each student fills in this sentence and writes it down:

> ***[Who]*** wastes time on ***[task]***. The smallest version is ***[one
> screen or one command]*** that ***[does one thing]***.

Example: *"Students in my classes waste time copying deadlines from syllabi
into their calendars. The smallest version is a command that reads a pasted
syllabus and outputs a calendar file of the due dates."*

**Partner check (5 min):** students swap sentences and answer two questions:

1. Could this be built in one afternoon? If not, what can you remove?
2. Who besides the author would actually use this?

Walk around and approve each sentence before students move on. Projects
that are too big are the biggest risk to this project, so this is the most
useful moment for you to step in.

## Part 4: Plan with the agent (20 min)

Students create their new repo (same steps as the
[OpenCode activity](../../class-practice/opencode-tutorial/README.md)) and
open it in OpenCode Desktop.

**Planning comes from the prompt, not from a button.** The starter prompt
tells the agent not to create or change files yet, so this works in any mode.
If students want the Plan agent anyway: Desktop hides the Plan/Build picker by
default. Turn on **Settings → General → Show agent** and the picker appears
below the prompt. (In the terminal version, `Shift+Tab` switches agents.)
Don't spend class time on it if the picker doesn't appear. Some Desktop
versions have a bug where it never shows.

**Starter prompt:**

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

Students answer the agent's questions, **cut anything that goes beyond the
scope sentence**, then reply "Now write SPEC.md and AGENTS.md as we agreed."
(If they used the Plan agent, they switch back to **Build** first.) They
create the issues by hand on GitHub, which helps them see the list as their
own plan rather than the agent's.

**Check before the break:** each repo has `SPEC.md`, `AGENTS.md`, and 3 to 5
issues.

## Break (10 min)

## Part 5: Build the smallest version that works (25 min)

Students pick their first issue, create a branch, and build.

Coaching points while you walk around:

- One issue, one branch, one PR. Don't let them combine everything.
- **Run it yourself after each agent change.** If you can't explain what
  changed, ask the agent before you accept it.
- Write the run command into the README as soon as it works.
- If the app uses an LLM, call it through `MODEL_URL` from day one.

The goal is something that runs, not something finished.

## Part 6: Laptop swap (12 min)

Students swap laptops (or repo links) with a partner. The partner:

1. Follows **only the README** to run the app
2. Tries the one thing it is supposed to do
3. Files **one real GitHub issue** on the author's repo: a bug, a confusing
   step, or a missing feature

Every student leaves with their first piece of real user feedback. They
will also see how much the README matters.

**Close (last 2 minutes):** preview the Class 4 pitch so students know where
this is going:

1. **Problem (20 sec):** who wastes time on what
2. **Demo (60 sec):** show it working
3. **What a user told me (20 sec):** one piece of feedback and the change it led to
4. **Next (20 sec):** one tradeoff they made and what they'd build next

## Due before Class 2

- [ ] New GitHub repo shared with the instructor
- [ ] `SPEC.md` (with the scope sentence at the top) and `AGENTS.md`
- [ ] 3 to 5 GitHub issues
- [ ] Smallest working version on `main`, with README run steps that work
- [ ] The partner's issue fixed in a PR that closes it

## Instructor prep checklist

- [ ] Two or three real job postings for Part 1
- [ ] Decide the Week 1 checkpoint points (suggested: 10 of 50, with 10 / 10
      / 10 for checkpoints and 20 for the presentation)
- [ ] Decide where students submit their repo link
- [ ] Remind students to bring laptops with OpenCode working. llmman is optional
- [ ] Pair students without a working setup in advance

## Timing

| Time | Part | Minutes |
| --- | --- | ---: |
| 0:00 | 1. What employers look for | 12 |
| 0:12 | 2. Ground rules and ideas | 13 |
| 0:25 | 3. Scope sentence and partner check | 13 |
| 0:38 | 4. Plan with the agent | 20 |
| 0:58 | Break | 10 |
| 1:08 | 5. Build the smallest version | 25 |
| 1:33 | 6. Laptop swap and close | 12 |
| 1:45 | End | |
