
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

## CLI Usage

```console
moose@rapid7:~$ github-status check -c webhooks
Service 'Webhooks' is currently operational!
```

```console
moose@rapid7:~$ github-status check -c git -v
Report for service 'Git Operations':
- Description: Performance of git clones, pulls, pushes, and associated operations
- Status: operational
- Last status update: 2020-04-21T16:48:14.527Z
```

```console
moose@rapid7:~$ github-status summary
Service 'Git Operations' is currently operational!
Service 'API Requests' is currently operational!
Service 'Webhooks' is currently operational!
Service 'Visit www.githubstatus.com for more information' is currently operational!
Service 'Issues, PRs, Projects' is currently operational!
Service 'GitHub Actions' is currently operational!
Service 'GitHub Packages' is currently operational!
Service 'GitHub Pages' is currently operational!
Service 'Other' is currently operational!
```

## Programmatic Usage

In addition to being a functional command line tool, github-status-checker
can also be used programmatically
to interact with [https://www.githubstatus.com/](https://www.githubstatus.com/)
in a Pythonic fashion.

```python
from github_status_checker.api import API

api = API.new()
summary = api.get_summary()
print(f"Component '{summary.components[0].name}' is for {summary.components[0].description}")
```

## Contributions

Contributions are welcome! This project utilizes [black](https://github.com/psf/black)
and [pre-commit](https://pre-commit.com/) for handling code
style. Simply follow the instructions for installing pre-commit and
run `pre-commit install` in the repository after cloning and you will
be on your way to contributing!

## Changelog

* 2.0.0 - Updated CLI grammar to add "check" and "summary" commands
| Added option to get verbose status report with "check" command
* 1.0.2 - Update to handle crash on outage report | Code style: black
| Add contribution section
* 1.0.1 - Update homepage and author name
* 1.0.0 - Swap dataclasses for traditional classes for greater Python version
compatibility (Python 3.x+)
* 0.1.0 - Initial development, support Summary

