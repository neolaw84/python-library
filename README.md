# python-library

A production-ready [Cookiecutter](https://cookiecutter.readthedocs.io/) template for Python libraries. It provides a robust, modern foundation with CI/CD, automated versioning, documentation generation, and GitHub repository configuration.

## Features

- **Standardised Structure**: Ready-to-go `src/`, `tests/`, `scripts/`, `notebooks/`, `configs/`, and `docs/` directories.
- **Modern Packaging**: Configured with `pyproject.toml` (no `requirements.txt`) using the standard setuptools build backend.
- **Testing**: Pre-configured testing suite with `pytest` and `pytest-cov`.
- **Documentation**: MkDocs Material setup with auto-generated API docs and README integration.
- **Comprehensive CI/CD**: High-quality GitHub Actions for automated testing, coverage enforcement, version bumping, OIDC-based PyPI releases, and GitHub Pages deployment.
- **Repository Setup Script**: Included utility to seamlessly lock down repository branches (main/dev), configure PR labels, and align security permissions.

---

## Bootstrapping a New Project

### 1. Create a GitHub Repository

Before generating the project locally, create a new, empty repository on GitHub. Do not initialize it with a README, license, or `.gitignore`—the template handles everything.

### 2. Generate the Project

Use the `cookiecutter` CLI to generate a new library codebase from this template:

```bash
pip install cookiecutter
cookiecutter gh:neolaw84/python-library
```

You will be prompted to supply several properties. Once finished, navigate to the generated directory, track it in Git, and push it to your newly created GitHub repository:

```bash
cd <your_project_name>
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

### 3. Run the Repository Setup Script

Your new codebase includes `scripts/setup_github_rules.py` which utilizes the GitHub API to automate repository configurations that are critical for your CI/CD workflows. 

**Summary of what the script does:**
- **Creates branches**: Ensures a `dev` branch exists (created from `main` if it's missing).
- **Sets branch protections**: Locks down `main` and `dev` branches, enforcing strict required status checks ("Enforce source branch is dev" for `main`, "Tests & Coverage" for `dev`).
- **Enforces PR reviews**: Requires at least 1 approval for pull requests targeting `main` and `dev`.
- **Configures labels**: Creates the repository labels `bump:major`, `bump:minor`, and `bump:patch` required by the automated version bumping workflow.
- **Secures workflows**: Sets the default `GITHUB_TOKEN` Actions permissions to read/write, preventing workflows from bypassing PR approvals.

#### A. Create a Personal Access Token (PAT)

The setup script requires a **Fine-grained Personal Access Token** with specific permissions.

1. Go to your GitHub account settings -> **Developer settings** -> **Personal access tokens** -> **Fine-grained tokens**.
2. Click **Generate new token**.
3. **Token name/Expiration**: Choose a name (e.g. "Repo Setup Script") and a short expiration span (e.g. 7 days).
4. **Repository access**: Strictly limit your token's reach by choosing **Only select repositories** and picking your newly created specific repository.
5. **Required Permissions**: Ensure the following scopes are strictly set to **`Read and write`**:
   - **Administration** *(Required to apply branch protection rules and workflow permissions)*
   - **Contents** *(Required to access branches and create the `dev` branch if it doesn't already exist)*
   - **Issues** *(Required to manage PR labels, as GitHub categorizes labels under the Issues scope)*
   
*(All other permissions can remain as `No access` or default.)*

#### B. Execute the Script

Ensure you are inside the generated project directory and that you have the required `requests` library installed. 
Simply export the token as an environment variable and run the setup script. It will intelligently infer your repository based on Git configurations:

```bash
pip install requests
export GITHUB_TOKEN="github_pat_11..."
python scripts/setup_github_rules.py
```

Once executed, your repository rules will be fully configured per the summary above.

---

### 4. PyPI Trusted Publisher Setup

Before your automated release pipeline (`release.yml`) can seamlessly publish to PyPI, you must configure a **Trusted Publisher** in PyPI to authenticate via OIDC instead of insecure tokens:

1. Log in to [pypi.org](https://pypi.org).
2. Navigate to **Your account** -> **Publishing** -> **Add a new Trusted Publisher**.
3. Provide the binding details:
   - **Owner**: Your GitHub username or organization
   - **Repository**: Your repository name
   - **Workflow filename**: `release.yml`
   - **Environment**: *(leave blank)*

No API token needs to be stored on GitHub. The GitHub Actions workflows will dynamically and securely authenticate!

---

## Included GitHub Actions Workflows

Your generated repository features the following CI/CD automation automatically configured out of the box:

| Workflow | Trigger | What it does |
|---|---|---|
| `ci-dev.yml` | PR → `dev` | Runs tests; strictly enforces ≥ 80% coverage when `src/` exceeds > 1,000 LOC, otherwise enforces ≥ 60%. |
| `version-bump.yml` | PR → `dev` opened/re-labelled | Auto-bumps version inside `pyproject.toml` based on the PR labels (`bump:major`, `bump:minor`, `bump:patch`). Default is **minor**. |
| `ci-main.yml` | PR → `main` | Validates PR integrity: Actively rejects pull requests whose source origin branch isn't `dev`. |
| `release.yml` | PR `dev → main` merged | Builds the distribution `.whl` + `.tar.gz`, creates a GitHub Release entity, and publishes securely to PyPI via OIDC. |
| `docs.yml` | PR `dev → main` merged | Compiles the comprehensive MkDocs Material site and deploys it effortlessly to the `gh-pages` branch. |
