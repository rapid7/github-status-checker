from typing import Optional

from github_status_checker.models.incident_update import IncidentUpdate
from github_status_checker.models.component import Component


class Incident:
    def __init__(
        self,
        created_at: str,
        id: str,
        impact: str,
        incident_updates: [IncidentUpdate],
        components: [Component],
        monitoring_at: Optional[str],
        name: str,
        page_id: str,
        resolved_at: Optional[str],
        shortlink: str,
        status: str,
        started_at: str,
        updated_at: str,
    ):
        self.created_at = created_at
        self.id = id
        self.impact = impact
        self.incident_updates = incident_updates
        self.components = components
        self.monitoring_at = monitoring_at
        self.name = name
        self.page_id = page_id
        self.resolved_at = resolved_at
        self.shortlink = shortlink
        self.status = status
        self.started_at = started_at
        self.updated_at = updated_at

    @classmethod
    def from_json(cls, json_: dict):
        incident = cls(**json_)
        incident.incident_updates = [
            IncidentUpdate.from_json(json_=iu) for iu in json_.get("incident_updates")
        ]

        return incident
