# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dajngo Sphinx Test'
copyright = '2024, Raphael Baqueta'
author = 'Raphael Baqueta'
release = 'v0.1'

#-- Path setup ---------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.confluencebuilder'
]
# 'sphinxcontrib.confluencebuilder' 

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',
# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',
# Additional stuff for the LaTeX preamble.
    'preamble': '',
# Latex figure (float) alignment
    'figure_align': 'htbp',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
