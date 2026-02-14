"""Configuration file for the Sphinx documentation builder."""  # noqa: INP001
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / ".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "turnq"
copyright = "2026, Kyle Benesch"  # noqa: A001
author = "Kyle Benesch"

release = subprocess.check_output(("git", "describe", "--always", "--abbrev=0"), text=True).strip()
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}
