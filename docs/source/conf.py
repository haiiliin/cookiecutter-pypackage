# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'python-package'
copyright = '2022, WANG Hailin'
author = 'WANG Hailin'

# The full version, including alpha/beta/rc tags
_default_version = '0.0.1-unknown'
try:
    version = pkg_resources.get_distribution('python-package').version
except pkg_resources.DistributionNotFound:
    version = _default_version
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.linkcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx_codeautolink',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
