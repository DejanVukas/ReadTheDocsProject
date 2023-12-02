Hostovanje
+++++++++++

GitHub workflow
=================

Git is distributed version control system.
Repository is one code "project".
GitHub is git hosting platform.
If you need more information about git, have a look at "How Git Works" by Paolo Perrotta.

To install git, visit https://git-scm.com/
Once we install git, git commands will be available.

Create new repository on GitHub
------------------------------------

Initialize Git in local folder
--------------------------------

Create gitignore file and add _build folder to it.

We can do it from CMD terminal with git init command, but let's do it from VS Code.
Click on Source Control tab in VS Code (or Ctrl+Shift+G)
Click on "Initialize Repository"
All files in our folder are marked as the one needed to be commited to new repository.
Type a commit note (e.g. initial commit) and press button Commit.
Now we have created **local** git repository.



Hook up local folder to GitHub project
---------------------------------------

Now we should connect to the remote repository and push the files to it.
We have to do it from the terminal:
Define the remote repository:
git remote add origin <link to repository copied from GitHub>

Push content of the local folder to GitHub
----------------------------------------------

git branch -M main
git push -u origin main


Read The Docs hosting
=======================

Let's hook up Read the Docs to GitHub project folder.

Log in to readthedocs.org.
Click on the "Connect your Accounts"
Click on Connect to GitHub. Consent window pops-up. Give your consent.

Then click on the your user ID in the upper right corner.
Click on "Import a Project"
Click on the Refresh icon. Then we get the list of our repositories on the GitHub.
Click on "+" symbol next to the repository you would like to publish on Read the Docs.
Click Next.
Wait for a while while documentation is building.
Click on the ViewDocs.




Lokalni racunar
================


Intranet
============

Use some web server e.g. IIS

Internet
============

Read the Documents
-------------------

Podnaslov2.1.1
~~~~~~~~~~~~~~~

Podnaslov2.1.2
~~~~~~~~~~~~~~~~


Podnaslov2.2
----------------

Јеш текста на ову тему ...