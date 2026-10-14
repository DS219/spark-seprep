# Assignment 5: Build a Website with OpenCode

Continue your [class activity](../class-practice/opencode-tutorial/README.md)
in the GitHub repository you created in class. Use OpenCode to create a site you can run locally and
explain. Use currently available free models, or your own supported provider
if you already have access. A paid subscription is not required.

Inspired by [OpenCode School: Build a website](https://opencode.school/exercises/build-a-website/).
The original exercise uses Hono, Tailwind, and Cloudflare Workers. **For this
assignment, serve your website locally. Cloudflare deployment and an account
are not required.** Plain HTML/CSS/JavaScript is enough. Hono or another
framework is welcome if you document its dependencies and local run commands.

**Deadline and submission location:** the instructor will announce these in class/Blackboard.

## Website requirements

- A clear purpose and audience: personal homepage, hobby guide, student club,
  project showcase, or fictional business are all fine.
- A heading, introduction, and at least two meaningful content sections with
  your own content. Replace generated placeholders.
- At least one working interaction, such as a theme switch, filter, quiz, or
  expandable details. A link by itself does not count as the interaction.
- A layout that works at narrow and wide browser widths, with readable text
  and keyboard-operable controls.
- A local HTTP server. Your site must load at `http://localhost:PORT` or
  `http://127.0.0.1:PORT`. Opening an HTML file via `file://` is insufficient.

You may expand the site you started in class. You should direct the agent,
review its output, and verify the result yourself.

## Repository requirements

Use the **GitHub repository you created and cloned during the class activity**.
If you missed class, follow the activity’s GitHub setup steps first. Keep its source and
evidence there rather than adding your website to the shared class repo.
Use a work branch and a descriptive commit message, following our class Git
practices. Push your final branch and provide a link to that branch, or merge
your own reviewed PR and link the default branch. A PR to `spark-seprep` is
not required. Make sure the instructor can access the repository.

Include:

- Website source and any assets needed to run it. Include dependency manifests
  and lockfiles if you use a framework. Exclude `node_modules/`, generated
  build output, credentials, and unrelated files.
- `README.md` with the site's purpose, prerequisites, exact setup and local
  server commands, browser URL, and how to stop the server.
- `AGENTS.md` with the project constraints you gave the agent.
- `REFLECTION.md` containing the model/provider you used, one useful prompt,
  one observed tool action, one issue or improvement you checked before and
  after a change, and a short explanation of how the interaction works.
- A screenshot, for example `evidence/site-localhost.png`, showing your site
  served in a browser **with the localhost address bar visible**.

Use invented or public content as appropriate. Do not include keys, tokens,
private conversations, or passwords in prompts, commits, or screenshots.

## Submit

1. **Your GitHub repository/branch URL** containing the final source.
2. **Your screenshot of the locally served site**. Attach it with the submission
   as well as including it in the repo, if the submission system supports it.

Before submitting, follow your README from a fresh terminal and check that
the site loads. Test the interaction with a keyboard and check a narrow width.
The instructor should be able to reproduce your result using those instructions.

## Grading rubric (20 points)

| Criterion | Points | Evidence |
| --- | ---: | --- |
| Local serving and reproducibility | 5 | README commands work; screenshot shows local HTTP URL and rendered site |
| Content and working interaction | 5 | Original content meets the requirements; interaction works |
| Layout and usability | 3 | Narrow/wide layouts, readable text, keyboard controls and visible focus |
| Agent use and verification | 4 | Constraints and reflection describe a tool action and verified improvement |
| Git repository quality | 3 | Accessible source, descriptive commits, needed assets/dependencies, no junk or secrets |
| **Total** | **20** | |

Visual complexity, paid model access, public hosting, and school completion
badges do not earn extra points. A small working site you can explain meets
the goal of this assignment.
