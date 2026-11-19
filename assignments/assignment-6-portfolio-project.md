# Assignment 6: Portfolio Project

Build a small tool that solves a problem you actually have, and get at least
one person besides you to use it. This builds on the idea you chose and the
repository you created in [Lesson 10](../lessons/lesson-10/slides.md).

> "I noticed X wasted my time. I built Y. My roommate used it, found a bug, and I fixed it."

**Total: 50 points**, submitted in four checkpoints. Each checkpoint has its own
Blackboard form. Submit your **repository URL** in every form, and make sure
the repository is public or shared with the instructor.

## Checkpoints

| # | Checkpoint | Due | Points |
| --- | --- | --- | ---: |
| 1 | Idea and plan | **Wednesday, Dec 2, before class** | 5 |
| 2 | Repository structure | **Wednesday, Dec 2, before class** | 5 |
| 3 | It works, and someone else tried it | **Friday, Dec 4** | 20 |
| 4 | 2-minute presentation | **Wednesday, Dec 9, last class** | 20 |
| | **Total** | | **50** |

Work on branches and merge to `main` through pull requests, following our
[class Git practices](../README.md). 

## Ground rules

1. **Keep it small.** Your project does one thing, described by your scope sentence.
2. **Use an AI coding agent** (OpenCode or another agent) to plan and write
   code. You direct it, review its output, and verify the result.
3. **If you use an LLM inside the app,** read its address from a setting such
   as `MODEL_URL` so it works with llmman, Ollama, or a hosted provider.
4. **No secrets in the repo.** Do not commit API keys, tokens, passwords, or
   `.env` files. Commit a `.env.example` with placeholder values instead.

---

## Checkpoint 1: Idea and plan (5 points)

**Due Wednesday, Dec 2, before class.**

Use an AI coding agent to turn your idea into a plan. A good starting prompt
is the Lesson 9 starter prompt: describe your idea, ask the agent to question
you until the scope is clear, then ask it to write the files below.

Add to your repository:

- `README.md` with your **scope sentence** at the top:
  > **[Who]** wastes time on **[task]**. The smallest version is
  > **[one screen or one command]** that **[does one thing]**.
- `SPEC.md`: what the MVP does, what it does not do, how a user runs it, and
  the language/framework you chose.
- `AGENTS.md`: the instructions and constraints you gave the agent, for
  example language, framework, "no secrets in code", "keep it small".

In the Blackboard form, name the agent and model you used and paste one prompt
that shaped your plan.

| Points | Criteria |
| ---: | --- |
| 5 | Clear scope sentence; `SPEC.md` describes a small, buildable MVP with what's in and out of scope; `AGENTS.md` has real constraints; agent use described |
| 3 | Plan is present but vague, too large, or missing one of the items above |
| 2 | Only a scope sentence or a minimal README; little evidence of planning |
| 0 | Not submitted |

---

## Checkpoint 2: Repository structure (5 points)

**Due Wednesday, Dec 2, before class.**

Your repository should look like a real project someone could clone and run.

Required:

- `README.md` with:
  - the scope sentence
  - prerequisites
  - exact commands to build and run the project, both with and without the container
  - how to use it, with an example input and output or a screenshot
  - any settings, such as `MODEL_URL`, and their defaults
- **Source files** organized in a sensible layout, for example `src/` or a single
  well-named script for a small tool.
- A **`Containerfile`** that builds and runs your project (optional):
  ```bash
  podman build -t my-project .
  podman run --rm my-project        # add -p PORT:PORT for a web app
  ```
- A **`.gitignore`** that excludes `node_modules/`, virtual environments, build
  output, `.env`, and other generated files.
- **Commit history** with descriptive messages, and work merged through PRs.

| Points | Criteria |
| ---: | --- |
| 5 | README is complete and accurate; source is organized; `.gitignore` present; no secrets or junk files; descriptive commits |
| 3 | One or two items missing or incomplete |
| 2 | Repository has code but little structure or documentation |
| 0 | Not submitted, or the repository is not accessible |

---

## Checkpoint 3: It works, and someone else tried it (10 points)

**Due Friday, Dec 4.**

### Does it work? (10 points)

Before submitting, test it yourself: clone your repo into a new folder, follow
your README step by step, and fix anything that is missing.

In the Blackboard form, include a screenshot or short screen recording of the
project working.

| Points | Criteria |
| ---: | --- |
| 10 | Runs by following the README; does the one thing in the scope sentence; handles a bad input or missing setting without crashing |
| 7 | Works, but the README needed fixes to get there, or the core feature only partly works |
| 4 | Runs but does not do what the scope sentence describes |
| 0 | Does not run, or not submitted |

### Did anyone else try it? (10 points)

Get at least **one person besides you** (a classmate, roommate, friend, or family
member) to use your project by following your README.

- Record their feedback in the Blackboard form.

| Points | Criteria |
| ---: | --- |
| 10 | At least one outside tester; feedback recorded as an issue; a PR fixes it and closes the issue, or a reasoned reply explains why not |
| 7 | Feedback recorded, but nothing was changed or answered |
| 4 | Someone tried it, but there is no issue or written record |
| 0 | No outside tester, or not submitted |

---

## Checkpoint 4: 2-minute presentation (20 points)

**Wednesday, Dec 9, last class.**

Suggestion:

| Time | Part |
| --- | --- |
| 20 sec | **Problem:** what did you build? |
| 60 sec | **Demo:** describe how it works |
| 20 sec | **What a user told me:** one piece of feedback and the change it led to |
| 20 sec | **Next:** one tradeoff you made and what you'd build next |

If you will demo, have your demo running before your
turn.

In the Blackboard form, submit your repository URL and presentation notes (include the 4 points above) 

| Points | Criteria |
| ---: | --- |
| 20 | Covers all four parts within about 2 minutes; working demo; can answer a question about how it works |
| 15 | Missing one part or well over time; demo partly works |
| 10 | Presented, but no demo and most of the parts are missing |
| 0 | Did not present |

---

## What does not earn extra points

A long feature list, a polished UI, paid models, and public hosting do not
earn extra points. A small tool that works, that someone else used, and that you
can explain meets the goal of this assignment.
