# Sources and refresh notes

## Course-owned sources

- `../../assignments/assignment-4.md`: the script/Containerfile assignment this lesson bridges from
- `../../class-practice/setup_local_llm.md`: prior local-LLM activity, related background for students

## External references

- [Components of a Coding Agent — Sebastian Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent): primary source for the six-ingredient breakdown and the LLM/reasoning-model/agent framing. Simplified from six named components into two groups of three for a beginner audience.
- [Mini Coding Agent (reference implementation)](https://github.com/rasbt/mini-coding-agent/blob/main/mini_coding_agent.py): the from-scratch example Raschka's article annotates; not shown to students, kept here for instructor reference.
- [OpenCode](https://opencode.ai/): open-source, model-agnostic terminal coding agent. Install command verified via web search at authoring time: `curl -fsSL https://opencode.ai/install | bash`, with `npm install -g opencode-ai` and `brew install anomalyco/tap/opencode` as alternatives.
- [OpenCode GitHub repository](https://github.com/opencode-ai/opencode)
- [Google AI Studio](https://ai.google.dev/aistudio): free-tier Gemini API key creation flow referenced on the "Get a free Gemini API key" slide.
- [Gemini API Python quickstart](https://ai.google.dev/gemini-api/docs/get-started): source for the `google-genai` SDK install and minimal `generate_content` example shown in slides.

## Refresh before teaching

- Re-check the OpenCode install command and supported package managers; these change across releases.
- Re-check the Google AI Studio key-creation flow (menu labels and steps); provider UIs change more often than APIs.
- Re-verify the `google-genai` Python example still matches the current SDK (model name, import path, client construction).
- If Claude Code or Codex CLI documentation changes how they describe themselves, confirm the one-line descriptions on the "three agent harnesses" slide are still accurate and even-handed.
