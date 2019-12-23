import argparse

from github_status_checker.controllers.commands import Commands


def main():
    argparser = argparse.ArgumentParser(prog="GitHub Status Checker 0.1.0",
                                        description="Check the status of various GitHub services.")

    argparser.add_argument("component",
                           help="Component to check",
                           choices=["webhooks","actions"],
                           action="store",
                           type=str)

    args = argparser.parse_args()
    Commands.check(component=args.component)


if __name__ == "__main__":
    main()
