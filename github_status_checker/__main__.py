import argparse

from pkg_resources import get_distribution

from github_status_checker.controllers.commands import Commands


def main():
    version_string = get_distribution('insightconnect-integrations-validators')
    argparser = argparse.ArgumentParser(epilog=version_string,
                                        description="Status checker for GitHub")

    argparser.add_argument("component",
                           help="Component to check",
                           choices=["webhooks","actions"],
                           action="store",
                           type=str)

    args = argparser.parse_args()
    Commands.check(component=args.component)


if __name__ == "__main__":
    main()
