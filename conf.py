# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Linear Algebra'
copyright = '2020, Yong Yang'
author = 'Yong Yang'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
'sphinxcontrib.tikz',
'sphinxcontrib.contentui'
]

tikz_proc_suite = 'pdf2svg'

mathjax_config = '''
        loader: {load: ['a11y/semantic-enrich']},
        options: {
            enrichSpeech: 'shallow',  // one of: 'deep', 'shallow', or 'none'
            renderActions: {
                //
                // Force speech enrichment regardless of the menu settings
                //
                enrich: {'[+]': [
                function (doc) {doc.enrich(true)},
                function (math, doc) {math.enrich(doc, true)}  
                ]}
            }
        },
        tex: {
            tags: 'ams'  // should be 'ams', 'none', or 'all'
        }
'''

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

primary_domain = 'js'
rst_prolog = """
.. |-----| raw:: html

   <hr>
"""

numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_show_sourcelink = False