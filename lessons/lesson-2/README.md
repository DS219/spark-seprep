# Lesson 2: Command Line and SSH

Lesson 2 gives students a practical mental model for terminals, shells, Linux filesystems, permissions, and SSH


## Learning objectives

By the end of class, students should be able to:

- distinguish a terminal, shell, command, operating system, and remote host;
- navigate Linux paths and inspect files from a shell;
- explain the roles of SSH clients, servers, host keys, public keys, and private keys;
- connect to their non-root account on the class VM; and
- make, verify, and safely exit a small remote workflow.

## Run the presentation

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-2
npm install
npm run dev
```

Press `P` for presenter mode, which includes speaker notes and the next-slide preview.

Lesson 2 is intentionally not included in the GitHub Pages workflow until the instructor approves the draft.

## Build and export

```bash
npm run build
npm run export
```

- `npm run build` creates a static HTML presentation in `dist/`.
- `npm run export` creates `lesson-2.pdf` for Blackboard or offline use.

## Suggested class plan

| Time | Activity |
| --- | --- |
| 4:30–4:50 | Terminal, shell, prompt, and command mental model |
| 4:50–5:15 | Filesystem navigation, streams, permissions, and editors |
| 5:15–5:35 | Guided local command-line practice |
| 5:35–5:45 | Break |
| 5:45–6:05 | SSH, host verification, and key authentication |
| 6:05–6:15 | Class VM mission, troubleshooting, and exit ticket |

## Instructor preparation

- Put the VM address, temporary password, and verified host-key fingerprint in Blackboard, not the public deck.
- Confirm every student account exists and has no root or `sudo` access.
- Test the SSH flow from macOS, Windows WSL, and Linux.
- Decide and document the fallback when `ssh-copy-id` is unavailable.
- Finalize the in-class activity and Blackboard assignment after reviewing this draft.
- Export a fresh PDF after changing the slides.

## Files

- `slides.md`: student-facing slides and speaker notes
- `style.css`: Lesson 1 visual system plus Lesson 2 diagrams
- `sources.md`: authoritative sources and refresh guidance
