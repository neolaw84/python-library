# Branch Protection Rules

Follow these steps in the GitHub repository **Settings → Branches** UI to protect the two sacred branches (`main` and `dev`).

> Prefer automation? In repositories generated from this template, run `scripts/setup_github_rules.py` to apply the same branch protections, labels, and workflow-permission defaults via GitHub API.

---

## 1 · Protect `main`

1. Open **Settings → Branches** and click **"Add branch ruleset"** (or **"Add rule"** on the classic UI).
2. Set **Branch name pattern**: `main`
3. Enable the following options:

| Option | Value |
|---|---|
| Require a pull request before merging | ✅ Enabled |
| Required number of approvals | `1` (adjust to taste) |
| Dismiss stale pull request approvals when new commits are pushed | ✅ Enabled |
| Require status checks to pass before merging | ✅ Enabled |
| Status checks required | `Enforce source branch is dev` (from `ci-main.yml`) |
| Require branches to be up to date before merging | ✅ Enabled |
| Restrict who can push to matching branches | ✅ Enabled — add only maintainers |
| Do not allow bypassing the above settings | ✅ Enabled |
| Allow force pushes | ❌ Disabled |
| Allow deletions | ❌ Disabled |

> **Tip**: The `Enforce source branch is dev` check is the job name inside `ci-main.yml`. GitHub will block the merge if it fails (i.e., the head branch is not `dev`).

---

## 2 · Protect `dev`

1. Click **"Add branch ruleset"** again.
2. Set **Branch name pattern**: `dev`
3. Enable the following options:

| Option | Value |
|---|---|
| Require a pull request before merging | ✅ Enabled |
| Required number of approvals | `1` (adjust to taste) |
| Dismiss stale pull request approvals when new commits are pushed | ✅ Enabled |
| Require status checks to pass before merging | ✅ Enabled |
| Status checks required | `Tests & Coverage` (from `ci-dev.yml`) |
| Require branches to be up to date before merging | ✅ Enabled |
| Do not allow bypassing the above settings | ✅ Enabled |
| Allow force pushes | ❌ Disabled |
| Allow deletions | ❌ Disabled |

> **Tip**: The version-bump workflow (`version-bump.yml`) commits back to the feature branch. Make sure the default `GITHUB_TOKEN` has write access to repository contents — this is set in **Settings → Actions → General → Workflow permissions → Read and write permissions**.

---

## 3 · Create required labels

The `version-bump.yml` workflow reads these PR labels to decide the semver increment:

| Label | Meaning |
|---|---|
| `bump:major` | Increment the **major** version (breaking change) |
| `bump:minor` | Increment the **minor** version (default when no label is set) |
| `bump:patch` | Increment the **patch / micro** version (bug fix) |

Create them in **Issues → Labels → New label** (or via the GitHub CLI):

```bash
gh label create "bump:major" --color "E11D48" --description "Breaking change — bump major version"
gh label create "bump:minor" --color "0EA5E9" --description "New feature — bump minor version (default)"
gh label create "bump:patch" --color "22C55E" --description "Bug fix — bump patch version"
```

---

## 4 · Enable GitHub Pages

1. Go to **Settings → Pages**.
2. Set **Source** to **"Deploy from a branch"**.
3. Select the `gh-pages` branch and `/` (root) folder.
4. Save.

The `docs.yml` workflow will create and populate `gh-pages` automatically on the first merge to `main`.

---

## 5 · Configure PyPI Trusted Publisher

See the [README](README.md#pypi-trusted-publisher-setup) for the one-time setup required before `release.yml` can publish to PyPI.

---

## 6 · Mark the repository as a GitHub Template

Once the repo is in the desired state:

1. Go to **Settings → General**.
2. Under **Repository** (top section), tick **"Template repository"**.
3. Save.

Users can now click **"Use this template"** to scaffold new projects from this repository.
