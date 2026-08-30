# Lesson 1: Welcome and Open Source

The first DS 219 class introduces the course, establishes expectations, and gives students a practical framework for understanding open-source software, licenses, governance, and foundations.

## Learning objectives

By the end of class, students should be able to:

- explain why visible source code is not automatically open source;
- distinguish a project, license, governance model, community, and foundation;
- compare permissive and copyleft licenses at a high level;
- identify basic health and governance signals in a GitHub repository; and
- describe how the Linux Foundation, CNCF, PyTorch Foundation, and OpenClaw Foundation relate to open-source ecosystems; and
- trace how products, services, integrations, standards, and jobs can grow around an open-source project.

## Run the presentation

Requires Node.js 20.12 or newer.

```bash
cd lessons/lesson-1
npm install
npm run dev
```

Slidev opens the presentation in a browser. Press `P` for presenter mode, which includes speaker notes and the next-slide preview.

## Published presentation

GitHub Pages is the primary classroom and student-facing host:

- Course lessons: <https://ds219.github.io/spark-seprep/>
- Lesson 1 slides: <https://ds219.github.io/spark-seprep/lesson-1/>
- Lesson 1 presenter mode: <https://ds219.github.io/spark-seprep/lesson-1/presenter/>

Pushing lesson changes to `main` automatically rebuilds the site through `.github/workflows/pages.yml`.
The workflow also creates a static presenter entry point because GitHub Pages does not provide the development server's single-page-app fallback.

GitHub Pages still requires internet access. Before class, export the PDF and keep it on the presentation laptop as the offline fallback.

## Build and export

```bash
npm run build
npm run export
```

- `npm run build` creates a static HTML presentation in `dist/`.
- `npm run export` creates `lesson-1.pdf` for Blackboard or offline use.

Generated files are intentionally excluded by the repository's existing `dist/` rule. Do not commit `node_modules/`, `dist/`, or the exported PDF.

## Suggested class plan

| Time | Activity |
| --- | --- |
| 4:30–4:40 | Welcome and student introductions |
| 4:40–4:55 | Course structure, expectations, and outcomes |
| 4:55–5:15 | What open source means |
| 5:15–5:35 | License overview and repository investigation |
| 5:35–5:45 | Break |
| 5:45–6:05 | Governance, foundation case studies, and the infrastructure beneath AI |
| 6:05–6:15 | Week 2 preview, Week 1 assignment, exit ticket |

## Before class

- Confirm that the Week 1 assignment is visible in Blackboard.
- Confirm the published late-work policy before discussing it.
- Confirm office-hours details and the VM onboarding plan.
- Open the course repository in a separate browser tab for the live investigation.
- Export a fresh PDF after changing the slides.

## Files

- `slides.md`: student-facing slides and speaker notes
- `style.css`: local presentation theme
- `assignment.md`: Blackboard-ready Week 1 assignment copy
- `sources.md`: authoritative sources and refresh guidance
