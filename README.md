# ANSYS all-members team

[![Ansys](https://img.shields.io/badge/Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://github.com/ansys)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.7-blue)](https://www.python.org/)
[![Team Update](https://github.com/ansys/ansys-all-members/actions/workflows/team_update.yml/badge.svg)](https://github.com/ansys/ansys-all-members/actions/workflows/team_update.yml)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)

Repository for updating the ansys/all-members team automatically.

## Table of contents

<!--ts-->
   * [Introduction](#introduction)
   * [How does it work?](#how-does-it-work)
   * [Requirements](#requirements)
<!--te-->


## Introduction
GitHub organizations do not provide an off-the-shelf capability of creating
and maintaining up-to-date an *all-members* team. The goal of the ``update_team.py`` script
in this repository is to:

* Provided an org and an *all-members* team (i.e. ``@<MY_ORG>/all-members``), update its
members on the execution of this script.
* Provide the capability to automate the update of the members using GitHub Actions.

Feel free to fork this repository for your own application. You are also welcome to help
contribute to it in any possible way! Please submit an issue with any proposal you may have.

## How does it work?
This repository basically contains a simple Python script ``update_team.py``. Within this
script, there are two main variables which a user must take into account:

* ``MY_PAT``: this variable will basically include your personal authentication token in order
to interact with GitHub (using [PyGitHub](https://github.com/PyGithub/PyGithub)). You can also
make use of the automated mechanism, by which the script will search for an environment variable
named ``TOKEN`` which should contain your PAT.
* ``MY_ORG``: the organization whose team *all-members* we want to update.

In order to run it, simply modify these values and run:

```bash
    python update_team.py
```

Bear in mind that this specific version of the script has already set up the ``MY_ORG`` variable
to ``ansys``, since it is the organization for which this repository is oriented.

Furthermore, this repository has a GitHub Actions workflow to automate the update of the team
members on a regular basis (since it has an ``on.schedule`` argument). If you want to make use of
this capability take into account that a PAT must be stored as a repository secret. Check the 
[workflow file](https://github.com/ansys/ansys-all-members/blob/main/.github/workflows/team_update.yml)
for further details.

## Requirements
In order to run the previous script, one only needs to install ``pygithub``. In order to ease the
user its installation, we have created a requirements file: ``requirements.txt``. You can install
the latest version of the package by doing as follows with the ``pip`` package manager:

```bash
    pip install -r requirements.txt
```
