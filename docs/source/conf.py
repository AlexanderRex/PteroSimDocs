# Configuration file for the Sphinx documentation builder.

from __future__ import annotations

import sys
from pathlib import Path

# When Docs is a nested submodule of PteroSimScripting:
#   .../PteroSimScripting/PteroSimDocs/docs/source/conf.py
# parents[3] == PteroSimScripting root (SDK/python lives there).
_SCRIPTING_ROOT = Path(__file__).resolve().parents[3]
_SDK_PYTHON = _SCRIPTING_ROOT / "SDK" / "python"
if _SDK_PYTHON.is_dir():
    sys.path.insert(0, str(_SDK_PYTHON))
else:
    raise RuntimeError(
        f"PteroSim Python SDK not found at {_SDK_PYTHON}. "
        "Build docs from PteroSimScripting with the PteroSimDocs submodule "
        "(Option A / nested layout)."
    )

# -- Project information

project = "PteroSim"
copyright = "2024, AlexanderRex"
author = "AlexanderRex"

release = ""
version = ""

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_timeout = 5
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Autodoc: document public Python API only (skip gRPC stubs / private attrs)
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": False,
}
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"
