# Sources and refresh notes

Reviewed October 14, 2026.

- [Supplied Intro to AI Agents deck](https://docs.google.com/presentation/d/1MXWC4O2VE90mp_0QGOILiTrrzz8WZcAi/edit):
  inspected in the user's Chrome session via its HTML presentation view. 25 slides;
  foundations 1–10, courses 11–14, framework survey 15, local models begin 16.
  Used as conceptual source, not edited or republished verbatim.
- [OpenCode School](https://opencode.school/): course structure and agent-led lessons.
- [Installation](https://opencode.school/lessons/installation/): Desktop workflow,
  opening a project, and first message. Inspected in the enrolled browser.
- [Models](https://opencode.school/lessons/models/): model picker and built-in free
  offerings. Specific models change; materials deliberately do not require one name.
- [Permissions](https://opencode.school/lessons/permissions/): allow/ask/deny.
- [Agents](https://opencode.school/lessons/agents/): Plan/Build dropdown and the
  limitation that Plan is not a hard sandbox.
- [Build a website](https://opencode.school/exercises/build-a-website/): inspected
  in the enrolled browser. Original uses Hono, Tailwind CDN, and Cloudflare Workers.
  Classroom adaptation uses static files and a local HTTP server. No enrollment
  identifier or school completion requirement is included in course materials.
- [Official downloads](https://opencode.ai/download): Desktop installers for
  macOS, Windows, and Linux. Prefer this over copying older CLI commands: the
  download page currently advertises V2 while `/docs` describes V1 installation.
- [Project instructions](https://opencode.ai/docs/rules/): AGENTS.md convention.
- [Python HTTP server](https://docs.python.org/3/library/http.server.html): local
  serving command and bind option. This is a development server.
- [ReAct paper](https://arxiv.org/abs/2210.03629): reasoning/action/observation
  pattern underlying the reference deck's loop discussion.

- [GitHub repository quickstart](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories):
  browser creation with README, cloning, and the origin remote.

## Recheck before teaching

Check downloads, visible free labels, availability, and Desktop controls.
Test on Windows/WSL if possible, especially matching the app project path to
the terminal path. No live OpenCode generation or student OS matrix has been
validated by preparing the Markdown files alone.
