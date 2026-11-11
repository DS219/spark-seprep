# Lesson 10: Choose Your Project

Week 2 of the portfolio project. Students review the project and its new
timeline, run two local AI activities (Whisper speech-to-text and a RAG
chatbot), then choose a project and create its repo. The exit ticket is the
repo link, submitted in a Blackboard form. Students have two weeks to build a
working MVP before the next class, which adds GitHub Actions.
Uses the same Slidev tooling and shared visual system as the other course lessons.

## Present

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-10
npm ci
npm run dev
```

Press `P` for presenter mode. Build or export for offline use:

```bash
npm run build
npm run export
```

## Materials

- [Slides](slides.md), with speaker notes
- [Whisper activity](../../class-practice/whisper-transcription-activity.md)
- [RAG chatbot activity](../../class-practice/rag-chatbot-tutorial/README.md)

## Before class

- Create the Blackboard form for the exit ticket.
- Remind students to bring laptops with llmman (`gemma3:4b`) and Podman working,
  and to build the RAG app image at home: `podman build -t rag-chatbot-app:latest ./app`
  from `class-practice/rag-chatbot-tutorial`. It is about 2.2 GB.
