## Codex CLI

### Pick a Model
- Choose based on task complexity vs speed.
  - Fast iteration: `codex --provider openai --model gpt-4o-mini`
  - Deeper reasoning: `codex --provider openai --model gpt-4o`
- Set credentials via env vars (example): `export OPENAI_API_KEY=...`.

### Create a Prompt File
- Keep prompts short, specific, and actionable. Store under `prompts/`.
- Example (`prompts/bugfix.md`):
  ```md
  # Goal
  Fix intermittent timeout in API client.

  # Context
  Files: `src/client/*`; tests in `tests/client/`.

  # Constraints
  - Minimal diff; preserve public API.
  - Add a failing test first.

  # Acceptance Criteria
  - Tests pass locally and in CI.

  # Deliverables
  - Patch implementing fix + test.
  - Brief summary of approach.
  ```
- Run with prompt file: `codex --prompt prompts/bugfix.md`.

### Running in a Repo
- Start from project root so Codex can index files: `cd <repo> && codex`.
- Limit scope with working dir: `codex --cwd path/to/subdir`.
- Ask Codex to propose a plan before editing; iterate on the plan if needed.

### Approvals & Sandbox
- Codex may request approval for risky actions:
  - Destructive commands, dependency installs, network access, or writing outside the workspace.
- Prefer small, reviewable patches; verify with local tests before broader changes.

### Good Practices
- Reference exact paths and commands in prompts.
- Provide acceptance criteria and non-goals.
- Use task branches (e.g., `feat/search-filter`, `fix/api-timeout`).
- Save useful prompts with the codebase for reuse.

### Troubleshooting
- Model errors: verify `--provider/--model` and API keys.
- Missing context: run from correct directory; include file paths in the prompt.
- Slow iterations: narrow the task or switch to a faster model.
