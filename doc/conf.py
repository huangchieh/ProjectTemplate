# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fatastic Project'
copyright = '2026, SIN group, Aalto University.'
author = 'Jie Huang'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add custom extensions path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / '_extensions'))


extensions = ['myst_parser', 'sphinx.ext.mathjax', 'sphinx_molview', 'sphinxcontrib.bibtex',
              'per_page_numfig']
bibtex_bibfiles = ["_static/ref.bib"]
myst_enable_extensions = [
    'colon_fence',
    'amsmath',
    'dollarmath',]
# Enable automatic figure numbering
# Note: numfig counts figures across ALL documents, not per-page
# Set to False if you want per-page numbering (must be done manually)
numfig = True
numfig_format = {
    'figure': 'Fig. %s.',
    'table': 'Tab. %s.',
    'section': 'Sec. %s.'
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
