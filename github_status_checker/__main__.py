import argparse

from github_status_checker.controllers.commands import Commands


def main():
    argparser = argparse.ArgumentParser(
        prog="github-status <component>",
        epilog="Version 1.0.0",
        description="Check the status of various GitHub services.")

    argparser.add_argument("component",
                           help="Component to check",
                           choices=["git",
                                    "api",
                                    "webhooks",
                                    "issues_prs_projects",
                                    "actions",
                                    "packages",
                                    "pages",
                                    "other"],
                           action="store",
                           type=str)

    args = argparser.parse_args()
    Commands.check(component_arg=args.component)


if __name__ == "__main__":
    main()
