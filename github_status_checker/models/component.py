from typing import Optional, Any

from github_status_checker.models.component_status import ComponentStatus


class Component:

    def __init__(self,
                 created_at: str,
                 description: Optional[str],
                 id: str,
                 name: str,
                 page_id: str,
                 position: int,
                 status: ComponentStatus,
                 updated_at: str,
                 showcase: bool,
                 group_id: Any,
                 only_show_if_degraded: bool,
                 group: bool):

        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.page_id = page_id
        self.position = position
        self.status = status
        self.updated_at = updated_at
        self.showcase = showcase
        self.group_id = group_id
        self.only_show_if_degraded = only_show_if_degraded
        self.group = group

    @classmethod
    def from_json(cls, json_: dict):
        component = cls(**json_)
        component.status = ComponentStatus(value=json_.get("status"))
        return component
