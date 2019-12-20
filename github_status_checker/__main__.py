from github_status_checker.models.summary import Summary
from github_status_checker.models.component import Component
from github_status_checker.api import API
from pkg_resources import get_distribution

import argparse


def _get_component(component: str) -> Component:
    api = API.new()
    summary: Summary = api.get_summary()

    for c in summary.components:
        if component in c.name.lower():
            return c


def check(component: str) -> None:
    comp: Component = _get_component(component=component)
    print(f"{comp.name} is currently {comp.status.value}!")


def main():
    version_string = get_distribution('insightconnect-integrations-validators')
    argparser = argparse.ArgumentParser(epilog=version_string,
                                        description="Status checker for GitHub")

    argparser.add_argument("component",
                           help="Component to check",
                           choices=["webhooks", "api"],
                           action="store",
                           type=str)

    args = argparser.parse_args()
    check(component=args.component)

if __name__ == "__main__":
    main()