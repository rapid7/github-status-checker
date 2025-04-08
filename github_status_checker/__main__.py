import argparse
from argparse import Namespace

from github_status_checker import VERSION
from github_status_checker.controllers.commands import Commands


def main():
    argparser = argparse.ArgumentParser(
        prog="github-status <component> | <summary>",
        epilog=f"Version {VERSION}",
        description="Check the status of various GitHub services",
    )

    subparsers = argparser.add_subparsers(help="Commands")

    # Summary
    summary_command = subparsers.add_parser(
        "summary", help="Print a summary of the status of all GitHub services"
    )
    summary_command.set_defaults(func=summary)

    # Individual components
    check_command = subparsers.add_parser(
        "check", help="Print the status of an individual GitHub service"
    )
    check_command.add_argument(
        "-c",
        "--component",
        action="store",
        help="GitHub service to print the status of",
        choices=[
            "git",
            "api",
            "webhooks",
            "issues_prs_projects",
            "actions",
            "packages",
            "pages",
            "other",
        ],
    )
    check_command.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Toggle verbosity of the status check",
    )
    check_command.set_defaults(func=check)

    args = argparser.parse_args()
    args.func(args)


def check(args: Namespace) -> None:
    """
    Print a summary of the status of all GitHub services.
    :param args: Individual GitHub service to inspect.
    :return: None
    """
    Commands.check(component_arg=args.component, verbose=args.verbose)


def summary(args: Namespace) -> None:
    """
    Print a summary of the status of all GitHub services.
    :param args: None
    :return: None
    """
    Commands.summary()


if __name__ == "__main__":
    main()
