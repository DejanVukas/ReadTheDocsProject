Introduction
+++++++++++++

`Tutorial <https://www.youtube.com/watch?v=vFAkt_N6yuk&list=PLPDCBPbzk1AYghqYazE7Cxt3p7edml8I7&index=1>`_

ReadTheDocs provides:

#. free hosting,
#. automated integration with GitHub, GitLab, and BitBucket, and
#. you can host documentation locally.

ReStructured Text markup syntax

On premises readthedocs.org hosting

Prerequisities:

#. Python,
#. Sphinx, (pip install sphinx)
#. ReadTheDocs theme (pip install sphinx_rtd_theme)

https://readthedocs.org/ will host our documentation.

How to use it - documentation is here: https://docs.readthedocs.io/en/stable/tutorial/

Create Documentation project
=============================

Create a documentation project using the sphinx-quickstart command.
You will need to define whether it is:

#. Standalone docs or inside a code project, and
#. project name and authors name

Create documentation folder and navigate in CMD window to it.
Type in:

.. code-block::
    
    sphinx-quickstart

Answer the questions.
This command has created the necessary folders and files.
Populate master file index.rst and create other documentation
.rst stands for ReStructured Text

Use the Make file to build the docs, like so:
make <builder>
where <builder> is one of the supported builders, e.g. html, latex, or linkcheck.
We will use:

.. code-block::

    make html

In CMD prompt type in:
make html

Now run index.html file which is in html folder:

.. code-block::

    path ... \_build\html\index.html

and you will get the documentation page.

Visual Studio Code
====================

Editor for creating documentation: Visual Studio Code

Open the folder containing our documentation.

Apply Read The Documentation theme
-------------------------------------

Open conf.py file in Visual Studio Code

set html_theme to sphinx_rtd_theme (default was "alabaster")

.. code-block::

    html_theme = 'sphinx_rtd_theme'

Save the file.
View - Terminal

Make the documentation page
------------------------------

Navigate to the project folder (e.g. ReadTheDocsProject) and type in:

.. code-block::

    make html

(it did not work for me from VS code terminal, but only from CMD prompt terminal)
We have to specify the root directory, and then it will work from VS Code terminal:

.. code-block::

    ./make html

Open index file
-----------------

Then we will open the index.html page to confirm that Read The Docs theme has been applied:

.. code-block::

    <path to project folder> .\_build\html\index.html

Visual Studio Extension for reStructuredText
---------------------------------------------

Let's now edit index.rst file in Visual Studio Code.

As we can see, sphinx syntax has not been highlighted. Let's insall add-in reStructuredText extension in Visual Studio Code.

In the upper-right corner of the Visual Studio Code we can select a screen button for the page preview.

(it does not work for me?!)

Let's add "Hello World" to index.rst file, just below the title. Save.

Run in Terminal window command:

.. code-block::

    ./make html

Open file

.. code-block::

    .\_build\html\index.html

Creating content with ReStructured Text
========================================

For more information visit: http://www.sphinx-doc.org/en/stable/contents.html

Make a plan about documentation structure (chapters, subchapters).

To add items to the TOC (Table Of Contents), go below content of ".. toctree::" and type new chapter/subchapter names (start typing below :, i.e. three spaces at the beginning of the line):

Uvod/Introduction
Uvod/Guidelines

Make sure that documents Introduction.rst and Guidelines.rst are in folder Uvod.

Documents Introduction.rst and Guidelines.rst should have sections (otherwise they do not appear in TOC section).

When we preview index.rst file, TOC shows up. In order to hide it, type in "hidden" in TOC section of index.rst file.

Also, delete "Indices and Tables" section in index.rst file.

In the TOC section change caption to name of the folder (Uvod).

Add more documents (Komponenete.rst and Hostovanje.rst) in new folder (Razrada):

* Razrada/Komponente
* Razrada/Hostovanje

Copy TOC section above section with new files in index.rst