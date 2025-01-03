# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ESP32-C3 Breadboard Adapter'
copyright = '2024, Alexander Bobkov'
author = 'Alexander Bobkov'
release = '5.8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_simplepdf',]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
#'sphinx_rtd_theme'
#'alabaster'
html_static_path = ['_static']

latex_elements = {
    'papersize':'letterpaper',
    'pointsize':'8pt'
}

simplepdf_vars = {
    'primary': '#333333',
    'links': '#FF3333',
}
