# Instructor guide

## Recommendation

Teach a guided adaptation rather than asking students to complete the full
OpenCode School course in class. Its lessons are personalized and self-paced,
and the original website exercise introduces deployment setup. A common small
project gives you visible checkpoints while students learn the agent workflow.
Keep the school links as optional follow-up.

Use Desktop to match the school's installation tutorial. The CLI is an option
for students already comfortable in WSL, not an additional required install.
Use currently free models. No required Gemini key, API billing, or subscription.

## Suggested 105-minute meeting

| Minutes | Teaching |
| --- | --- |
| 0–20 | Foundations recap; students download Desktop in parallel |
| 20–40 | GitHub create/clone demo, model picker, Plan/Build, website demo |
| 40–50 | Break |
| 50–95 | [Guided class activity](README.md), with its own 45-minute clock |
| 95–105 | Student examples, exit ticket, homework requirements |

Lesson 7 has 19 slides. Slides 14–17 support the activity. Leave the checkpoint
slide up during work and revisit the local-server/browser-check slides as needed.

## Demo preparation

Create a personal GitHub repo in the browser and clone it outside the shared
class repo. Open that clone in Desktop to show how the project connects to
OpenCode. Use a fictional student club
as the subject. Run through the activity prompts once with an available free
model before class. Prepare a working copy to show if model availability fails.
Keep the demo to a tiny page rather than asking for a complete application.

Show the actual model picker, one file edit/tool result, Plan/Build switching,
and your browser check. Explain an approval request if one occurs. Do not
promise that default settings ask for every action.

## Help students finish the core loop

- At eight minutes, pair students blocked on cloning, downloads, or model availability.
- At 15 minutes, ask them to explain the plan before building.
- At 27 minutes, prioritize the local server over extra design changes.
- At 37 minutes, move to review and evidence rather than another feature.

Pairing is a temporary class fallback. Homework should be an individual site
unless you decide otherwise. If Python is absent, help install it from the
official source or use an already installed framework's local dev server.
Students should document whichever server they use.

## Reference-deck notes

The supplied deck has 25 slides; Local LLMs start at 16. Covering 1–15 is a
reasonable boundary, but the course survey can be brief. Lesson 7 condenses
that material so today's practice has enough time.

When teaching the reference, clarify two points: product categories overlap
(chat tools can have agent modes), and persistent context can live in ordinary
files, not only vector databases. Skip its NPS activity today.

## Homework decisions to confirm

Students create their personal website repo during class and continue in that
same repo for homework. The draft uses a 20-point rubric. Students
submit a repo/branch link and a screenshot with the local HTTP address visible.
Source, README commands, AGENTS.md, and a short reflection make the screenshot
reproducible and show what the student checked. Frameworks are optional.

You still need to announce the deadline and Blackboard submission location.
This is Assignment 5.

## Publication

Slides link to the activity/homework paths on `main`. Preview locally first,
then commit and merge through the normal course workflow. Before merge, use
local files or substitute a review-branch URL for class sharing. This preparation
does not push or publish the materials.
