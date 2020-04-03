
# GitHub Status Checker

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Tests](https://github.com/rapid7/github-status-checker/workflows/Tests/badge.svg)
![Python Lint](https://github.com/rapid7/github-status-checker/workflows/Python%20Lint/badge.svg)
![Markdown Lint](https://github.com/rapid7/github-status-checker/workflows/Markdown%20Lint/badge.svg)

## What this is

A tool and Python module for checking the status of GitHub.

## Installation

### Install the module via `pip`

```
moose@rapid7:~$ pip install github-status-checker
...
```

## Usage

```
moose@rapid7:~$ github-status webhooks
Service 'Webhooks' is currently operational!
```

## Contributions

Contributions are welcome! This project utilizes [black](https://github.com/psf/black)
and [pre-commit](https://pre-commit.com/) for handling code
style. Simply follow the instructions for installing pre-commit and 
run `pre-commit install` in the repository after cloning and you will
be on your way to contributing!

## Changelog

* 1.0.2 - Update to handle crash on outage report | Code style: black
| Add contribution section
* 1.0.1 - Update homepage and author name
* 1.0.0 - Swap dataclasses for traditional classes for greater Python version 
compatibility (Python 3.x+)
* 0.1.0 - Initial development, support Summary 

