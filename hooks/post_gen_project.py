#!/usr/bin/env python3
"""Post-generation hook: initialise git repo and install pre-commit hook."""

from __future__ import annotations

import os
import shutil
import stat
import subprocess

PROJECT_DIR = os.getcwd()
PRE_COMMIT_TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pre-commit-template")
PRE_COMMIT_HOOK = os.path.join(".git", "hooks", "pre-commit")


def git_init() -> None:
    subprocess.run(["git", "init"], check=True)
    print("✓ Initialised git repository")


def install_pre_commit_hook() -> None:
    shutil.copy2(PRE_COMMIT_TEMPLATE, PRE_COMMIT_HOOK)
    current = os.stat(PRE_COMMIT_HOOK)
    os.chmod(PRE_COMMIT_HOOK, current.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("✓ Installed pre-commit hook")


def print_next_steps() -> None:
    project_name = os.path.basename(PROJECT_DIR)
    print(f"""
Project '{project_name}' is ready. Next steps:

  1. Create a GitHub repository, then:
       git remote add origin git@github.com:<you>/{project_name}.git

  2. Make an initial commit and push:
       git add .
       git commit -m "Initial commit"
       git push -u origin main

  3. Set up branch protection rules and labels:
       python scripts/setup_github_rules.py
""")


if __name__ == "__main__":
    git_init()
    install_pre_commit_hook()
    print_next_steps()
