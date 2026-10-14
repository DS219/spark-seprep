# Lesson 7: Coding Agents with OpenCode

Continuation of Lesson 6. A short foundations recap leads into a Desktop demo,
a 45-minute guided website activity, and a locally served website assignment.
Uses the same Slidev tooling and shared visual system as the other course lessons.

## Present

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-7
npm ci
npm run dev
```

Press `P` for presenter mode. Build or export for offline use:

```bash
npm run build
npm run export
```

## Materials

- [Slides](slides.md), with speaker notes and activity/homework links
- [45-minute class activity](../../class-practice/opencode-tutorial/README.md)
- [Website homework and 20-point rubric](../../assignments/assignment-5-build-a-website.md)
- [Instructor guide](../../class-practice/opencode-tutorial/INSTRUCTOR.md)
- [Sources and refresh notes](sources.md)

## Relationship to the supplied slides

The [reference deck](https://docs.google.com/presentation/d/1MXWC4O2VE90mp_0QGOILiTrrzz8WZcAi/edit)
contains 25 slides. Slides 1–10 cover foundations, 11–14 survey courses, and
15 surveys frameworks. Slide 16 begins **Running Agents Locally**. This lesson
condenses 1–15 and continues into OpenCode practice. The reference deck is unchanged.

If using the reference live, cover 1–10, skim 11–15, and switch to this deck's
OpenCode section (slide 10). Skip the later local-model and NPS exercise today.

## Before class

- Verify Desktop downloads and a currently free model on an actual student-like setup.
- Prepare your demo folder and confirm Python local serving works.
- Announce the homework deadline and submission destination; those remain unspecified.
- Activity links target the `main` branch. Until changes are published, open the
  local activity or use the current review branch's GitHub URL.
- The Pages workflow includes Lesson 7. Publishing requires committing and merging
  these changes to `main`; the local work alone does not publish it.
