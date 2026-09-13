# Lesson 3: Git and GitHub

Lesson 3 turns last week's SSH-key setup into two complete Git workflows: create and push to a small repository they own, then fork the course repository, make a change on a branch, and open a pull request.

## Run the presentation

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-3
npm install
npm run dev
```

Press `P` for presenter mode, including speaker notes and the next-slide preview.

## Build and export

```bash
npm run build
npm run export
```

- `npm run build` creates the static presentation in `dist/`.
- `npm run export` creates `lesson-3.pdf` for Blackboard or offline use.

## Teaching flow

| Time | Activity |
| --- | --- |
| 4:30–4:40 | Reconnect: GitHub SSH key and identity |
| 4:40–4:55 | Why version control, Git versus GitHub |
| 4:55–5:20 | Guided activity: create, clone, and push to a personal repository |
| 5:20–5:30 | Bridge: direct push versus shared-project contribution |
| 5:30–5:40 | Break |
| 5:40–6:05 | Fork, clone, branch, Markdown, and pull request workflow |
| 6:05–6:15 | Assignment 3, exit ticket, troubleshooting |

## Instructor preparation

- Verify the GitHub SSH-key walkthrough and the `ssh -T git@github.com` success message.
- Follow `class-practice/git-create-repo.md` for the personal-repository activity before introducing the course fork.
- Do not ask students to post private keys, passphrases, tokens, or personal contact details in the public repository.
- Export a fresh PDF after content changes.

## Files

- `slides.md`: student-facing slides and presenter notes
- `style.css`: shared DS 219 visual system plus Git diagrams
- `sources.md`: source and refresh notes
- `source/lesson-3-original.pptx`: retained reference deck
