"""{{cookiecutter.project_name}} - {{cookiecutter.project_description}}."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{cookiecutter.project_name}}")
except PackageNotFoundError:  # package not installed (e.g. running from source)
    __version__ = "unknown"

__author__ = "{{cookiecutter.author_name}}"
__email__ = "{{cookiecutter.author_email}}"
