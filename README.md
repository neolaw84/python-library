# python-library

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for production-ready Python libraries with full CI/CD, automated versioning, PyPI publishing, and MkDocs documentation.

---

## What you get

| Area | Details |
|---|---|
| **Project structure** | `src/`, `tests/`, `scripts/`, `notebooks/`, `configs/`, `docs/` |
| **Packaging** | `pyproject.toml` (no `requirements.txt`) with setuptools build backend |
| **Testing** | pytest + pytest-cov pre-configured |
| **Documentation** | MkDocs Material with auto-generated API docs and README included on the home page |
| **CI/CD** | Four GitHub Actions workflows (see below) |

## GitHub Actions workflows

| Workflow | Trigger | What it does |
|---|---|---|
| `ci-dev.yml` | PR → `dev` | Runs tests; enforces ≥ 80% coverage when `src/` has > 1 000 LOC, otherwise ≥ 60% |
| `version-bump.yml` | PR → `dev` opened/re-labelled | Auto-bumps version in `pyproject.toml` on the feature branch (`bump:major` / `bump:minor` / `bump:patch` label; default **minor**) |
| `ci-main.yml` | PR → `main` | Rejects PRs whose source branch is not `dev` |
| `release.yml` | PR `dev → main` merged | Builds `.whl` + `.tar.gz`, creates a GitHub Release, publishes to PyPI via OIDC |
| `docs.yml` | PR `dev → main` merged | Builds MkDocs site and deploys to `gh-pages` branch |

## Usage

### Option A — Cookiecutter CLI (recommended)

```bash
pip install cookiecutter
cookiecutter gh:neolaw84/python-library
```

Answer the prompts and your new project is ready.

### Option B — GitHub Template

Click **"Use this template"** on the repository page to create a new repo.  
Then rename `{{cookiecutter.project_name}}/` to your actual package name and replace all `{{cookiecutter.*}}` placeholders.

---

## Branch protection rules

See [BRANCH_RULES.md](BRANCH_RULES.md) for the step-by-step GitHub UI setup guide to lock down `main` and `dev`.

## PyPI Trusted Publisher setup

Before the `release.yml` workflow can publish to PyPI, you must configure a **Trusted Publisher** in your PyPI project settings:

1. Go to **pypi.org → Your account → Publishing**.
2. Add a new Trusted Publisher:
   - **Owner**: your GitHub username / organisation
   - **Repository**: your repo name
   - **Workflow filename**: `release.yml`
   - **Environment**: *(leave blank)*
3. No API token is needed — PyPI uses OIDC automatically.
