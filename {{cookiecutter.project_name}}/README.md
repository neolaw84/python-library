# {{cookiecutter.project_name}}

> {{cookiecutter.project_description}}

[![PyPI version](https://badge.fury.io/py/{{cookiecutter.project_name}}.svg)](https://badge.fury.io/py/{{cookiecutter.project_name}})
[![Documentation](https://img.shields.io/badge/docs-gh--pages-blue)](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repo}}/)

## Installation

```bash
pip install {{cookiecutter.project_name}}
```

Or install the latest development build directly from GitHub Releases:

```bash
pip install https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/releases/latest/download/{{cookiecutter.project_name}}-latest-py3-none-any.whl
```

## Quick Start

```python
import {{cookiecutter.project_name}}

# Your code here
```

## Development

### Set up the environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev,docs]"
```

### Run tests

```bash
pytest
```

### Build documentation locally

```bash
mkdocs serve
```

## Contributing

1. Fork the repository and create your feature branch from **dev**.
2. Add tests for every new behaviour.
3. Open a Pull Request targeting **dev** — CI will gate on tests + coverage.
4. Label your PR with `bump:major`, `bump:minor` (default), or `bump:patch` to control the version bump.

## License

{{cookiecutter.open_source_license}} — see [LICENSE](LICENSE) for details.
