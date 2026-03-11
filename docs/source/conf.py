# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'tfg-kpm'
copyright = 'Except where otherwise noted, content on this site is licensed under a Creative Commons Attribution-Noncommercial-ShareAlike 4.0 License.'
author = 'Glitch714'

release = ''
version = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sphinx_clarity_theme"

html_theme_options = {
    "header_menu": [
        {
            "label": "Getting Started",
            "url": "https://tfg-kpm.glitchpdev.com/en/latest/tutorials/getting-started.html",
        },
        {
            "label": "Github",
            "url": "https://github.com/glitchplaysgames714/tfg-kpm",
            "as": "button",
        },
    ],
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_favicon = "favicon.png"
