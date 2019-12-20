from github_status_checker.api import API
from github_status_checker.models.component import Component
from github_status_checker.models.summary import Summary


class Commands(object):

    @staticmethod
    def _get_component(component: str) -> Component:
        api = API.new()
        summary: Summary = api.get_summary()

        for c in summary.components:
            if component in c.name.lower():
                return c

    @staticmethod
    def check(component: str) -> None:
        comp: Component = Commands._get_component(component=component)
        print(f"{comp.name} is currently {comp.status.value}!")
