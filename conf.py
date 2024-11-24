# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#I HAVE ADDED THIS SECTION BECAUSE SPHINX_RTD_THEME COULD NOT BE FOUND
#import os
#import sys
#error occurs because you are using a normal string as a path. You can put r before your normal string. It converts a normal string to a raw string
#sys.path.insert(0, os.path.abspath(r'C:\Users\Vukas\AppData\Local\Programs\Python\Python311\Lib\site-packages'))
#sys.path.insert(0, os.path.abspath('C:/Users/Vukas/AppData/Local/Programs/Python/Python311/Lib/site-packages'))
#import sphinx_rtd_theme
#END OF MY CHANGES

project = 'ReadTheDocsProject'
copyright = '2023, Dejan Vukas'
author = 'Dejan Vukas'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#I HAVE ADDED 'SPHINX_RTD_THEME' TO EXTENSIONS
extensions = ['sphinx_rtd_theme',]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']
