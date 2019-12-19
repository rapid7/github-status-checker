from dataclasses import dataclass
from typing import Optional, Any

from github_status_checker.models.component_status import ComponentStatus


@dataclass
class Component:
    created_at: str
    description: Optional[str]
    id: str
    name: str
    page_id: str
    position: int
    status: ComponentStatus
    updated_at: str
    showcase: bool
    group_id: Any
    only_show_if_degraded: bool
    group: bool

    @classmethod
    def from_json(cls, json_: dict):
        component = cls(**json_)
        component.status = ComponentStatus(value=json_.get("status"))
        return component
