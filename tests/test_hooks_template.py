from pathlib import Path


def test_post_gen_project_uses_repo_dir_for_pre_commit_template() -> None:
    source = Path("hooks/post_gen_project.py").read_text(encoding="utf-8")

    assert "{{ cookiecutter._repo_dir }}" in source
    assert "__file__" not in source
