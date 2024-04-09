# git

## Local auth

The easiest way to avoid creating a token.
```
brew install gh

gh auth login
```

## Branches
| description | command|
| --- | --- |
| checkout branch | `git checkout <branch name>` |
| create branch | `git branch <branch name>` |
| remove branch | `git branch --delete <branch name>` |
| list branch | `git branch` |
| sync local branch to remote origin/main | `git fetch origin && git merge origin/main` |

## Commits

| description | command|
| --- | --- |
| take the most recent commit and add new staged change to it | `git commit --amend` |
| remove all untracked files including ignored | `git clean --fdx` |
| uncommit change but keep files | `git reset --soft HEAD^` |
| remove all untracked files | `git restore .` |
| move head to a commit and discard changes after | `git reset --hard <COMMIT_ID>` |
| force syncing remote to local | `git push --force` |

## Files
| description | command|
| --- | --- |
| move changes to stash | `git stash` |
| move changes out of stash | `git stash pop` |
| revert a file to its state in main | `git checkout origin/main [filename]` |

## Misc

| description | command|
| --- | --- |
| pretty log | `git log --all --decorate --oneline --graph` |
| emoji | https://gitmoji.dev/ | 