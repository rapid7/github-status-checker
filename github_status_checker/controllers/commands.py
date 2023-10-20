from github_status_checker.api import API
from github_status_checker.models.summary import Summary


class Commands(object):

    # map component arguments to component IDs
    _COMPONENT_MAP = {
        "git": "8l4ygp009s5s",
        "api": "brv1bkgrwx7q",
        "webhooks": "4230lsnqdsld",
        "issues_prs_projects": "kr09ddfgbfsf",
        "actions": "br0l2tvcx85d",
        "packages": "st3j38cctv9l",
        "pages": "vg70hn9s2tyj",
        "other": "5l5rlzqm4yzy",
    }

    @staticmethod
    def _get_component_by_arg(component: str) -> str:
        """
        Lookup a component ID based on command line args
        :param component: Component
        :return: Component ID
        """

        try:
            component_id: str = Commands._COMPONENT_MAP[component]
        except KeyError as e:
            raise Exception(
                f"Error: No component ID found for component '{component}'"
            ) from e

        return component_id

    @staticmethod
    def check(component_arg: str, verbose: bool = False) -> None:
        """
        Check the operational status of a GitHub component
        :param component_arg: Component to check, received via command line arg
        :param verbose: Whether or not to print the status verbosely
        :return: None
        """
        component_id: str = Commands._get_component_by_arg(component=component_arg)

        api: API = API.new()
        summary: Summary = api.get_summary()

        for component in summary.components:
            if component.id == component_id:
                if verbose:
                    print(
                        f"Report for service '{component.name}':\n"
                        f"- Description: {component.description}\n"
                        f"- Status: {component.status.value}\n"
                        f"- Last status update: {component.updated_at}"
                    )
                else:
                    print(
                        f"Service '{component.name}' is currently {component.status.value}!"
                    )
                return

        raise Exception(
            f"Error: Component ID '{component_id}' matched to arg '{component_arg}' not found in GitHub "
            f"status summary!"
        )

    @staticmethod
    def summary() -> None:
        """
        Print a summary of the status of all GitHub services
        :return: None
        """

        api: API = API.new()
        summary: Summary = api.get_summary()

        statuses = [
            f"Service '{c.name}' is currently {c.status.value}!"
            for c in summary.components
        ]
        print("\n".join(statuses))
