from github_status_checker.api import API
from github_status_checker.models.summary import Summary


class Commands(object):

    @staticmethod
    def _get_component_by_arg(component: str) -> str:
        """
        Lookup a component ID based on command line arg
        :param component: Component
        :return: Component ID
        """

        # map component arguments to component IDs
        map_ = {
            "git": "8l4ygp009s5s",
            "api": "brv1bkgrwx7q",
            "webhooks": "4230lsnqdsld",
            "issues_prs_projects": "kr09ddfgbfsf",
            "actions": "br0l2tvcx85d",
            "packages": "st3j38cctv9l",
            "pages": "vg70hn9s2tyj",
            "other": "5l5rlzqm4yzy"
        }

        try:
            component_id: str = map_[component]
        except KeyError as e:
            raise Exception(f"Error: No component ID found for component '{component}'") from e

        return component_id

    @staticmethod
    def check(component_arg: str) -> None:
        """
        Check the operational status of a GitHub component
        :param component_arg: Component to check, received via command line arg
        :return: None
        """
        component_id: str = Commands._get_component_by_arg(component=component_arg)

        api: API = API.new()
        summary: Summary = api.get_summary()

        for component in summary.components:
            if component.id == component_id:
                print(f"Service '{component.name}' is currently {component.status.value}!")
                return

        raise Exception(f"Error: Component ID '{component_id}' matched to arg '{component_arg}' not found in GitHub "
                        f"status summary!")
