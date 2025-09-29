## Fork-and-PR Workflow

### Prerequisites
- GitHub account; `git` installed. Optional: GitHub CLI `gh` (`gh auth login`).

### 1) Fork and clone
- On GitHub, fork the upstream repository (the original project).
- Clone your fork:
  - HTTPS: `git clone https://github.com/<your-username>/<repo>.git`
  - SSH: `git clone git@github.com:<your-username>/<repo>.git`
  - `cd <repo>`

### 2) Add upstream remote
- Add the original project as `upstream` to sync later:
  - `git remote add upstream https://github.com/<upstream-owner>/<repo>.git`
  - Verify: `git remote -v`

### 3) Create a feature branch
- Start from latest `main` (or default branch):
  - `git fetch upstream`
  - `git checkout main && git merge upstream/main` (or `git rebase upstream/main`)
  - `git checkout -b <type>/<short-topic>` (e.g., `feat/login-form`)

### 4) Make changes locally
- Implement changes and add tests/docs as required by the project.
- Run local checks (examples): `npm test`, `make test`, `cargo test`, or project-specific commands.

### 5) Commit with clear messages
- Example: `git add -A && git commit -m "feat(auth): add login form validation"`

### 6) Push and open a PR to upstream
- Push branch to your fork: `git push -u origin <branch>`
- Open a pull request targeting the upstream repo’s base branch (`main` unless specified):
  - Web UI: choose base = `upstream/<base-branch>`, compare = `<your-username>:<branch>`.
  - GitHub CLI: `gh pr create --fill --base <base-branch> --head <your-username>:<branch> --repo <upstream-owner>/<repo>`
- Include a clear description, linked issues, and screenshots/logs if UI or behavior changes.

### 7) Keep your PR up to date
- Sync with upstream and update your branch:
  - `git fetch upstream && git rebase upstream/<base-branch>`
  - Resolve conflicts, then `git rebase --continue`
  - Update the PR: `git push --force-with-lease`

### 8) Reviews and merging into upstream
- As contributor (no write access): respond to review comments; reviewers/maintainers will merge via squash/rebase/merge.
- As maintainer (has write access): ensure checks pass, then merge in the upstream repo:
  - Squash merge for clean history; rebase-merge to preserve commits when appropriate.
  - After merging, delete the feature branch in upstream and your fork.

### 9) After merge: clean up and sync
- `git checkout main && git fetch upstream && git merge upstream/main`
- `git push origin main`
- Optionally prune local branch: `git branch -D <branch>`
