# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import inspect
import sys
import typing

import git
import pkg_resources

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


# linkcode source
def linkcode_resolve(domain: str, info: dict[str, typing.Union[str, list[str]]]):
    """Resolve linkcode source

    Parameters
    ----------
    domain : str
        specifies the language domain the object is in
    info : dict[str, str | list[str]]
        a dictionary with the following keys guaranteed to be present (dependent on the domain)

        - py: module (name of the module), fullname (name of the object)
        - c: names (list of names for the object)
        - cpp: names (list of names for the object)
        - javascript: object (name of the object), fullname (name of the item)

    Returns
    -------
    source url of the object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    filename = modname.replace('.', '/')
    try:
        branch_name = git.repo.Repo('../../').active_branch.name
    except Exception:
        branch_name = f'V{version[:4]}'
    baseurl = f'https://github.com/haiiliin/abqpy/blob/{branch_name}/src/{filename}.py'

    submod = sys.modules.get(modname)
    if submod is None:
        return baseurl

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return baseurl
    try:
        source, lineno = inspect.getsourcelines(obj)
    except TypeError:
        # Find source line for an attribute, the obj is None
        attr = fullname.split('.')[-1]
        obj = submod
        for part in fullname.split('.')[:-1]:
            try:
                obj = getattr(obj, part)
            except Exception:
                return baseurl
        source, lineno = inspect.getsourcelines(obj)
    except Exception:
        return baseurl

    return baseurl + f'#L{lineno}-L{lineno + len(source) - 1}'


templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
