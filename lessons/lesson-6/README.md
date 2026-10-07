# Lesson 6: What Is a Coding Agent?

Lesson 6 introduces coding agents conceptually before students touch one. It separates "LLM" from "reasoning model" from "agent," walks through the agent loop and the six harness ingredients behind tools like Claude Code, Codex, and OpenCode, and previews two things students do before next class: get a free Gemini API key and prepare to install OpenCode.

Lessons 4 and 5 are not in this repository.

## Run the presentation

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-6
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
- `npm run export` creates `lesson-6.pdf` for Blackboard or offline use.

## Teaching flow

| Time | Activity |
| --- | --- |
| 4:30–4:40 | Reconnect: bridge from Assignment 4 to "code that runs itself" |
| 4:40–5:00 | Chatbot vs. agent, the three terms, the agent loop |
| 5:00–5:30 | The six harness ingredients, tool approval example |
| 5:30–5:40 | Break |
| 5:40–5:55 | Claude Code, Codex, and OpenCode as real examples; OpenCode install preview |
| 5:55–6:10 | Class activity preview: Gemini API key, one plain model call vs. an agent loop |
| 6:10–6:15 | Checkpoint, exit ticket, next time |

## Instructor preparation

- There is no hands-on repository work tonight; the exit ticket is a written sentence, not a screenshot.
- Confirm the Google AI Studio API key flow still matches `sources.md` before class, since provider UIs change.
- Confirm the OpenCode install command still matches `sources.md`; project install methods can change between releases.
- Next class requires every student to arrive with a free Gemini API key already created. Remind them in the prior session or an announcement, not just in these slides.
- Do not demo running an untrusted shell script live without first explaining what `curl | bash` does.

## Files

- `slides.md`: student-facing slides and presenter notes
- `style.css`: imports the shared DS 219 visual system from `lesson-3`
- `sources.md`: source and refresh notes
