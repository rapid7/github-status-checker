from dataclasses import dataclass
from typing import Optional

from github_status_checker.models.incident_update import IncidentUpdate


@dataclass
class Incident:
    created_at: str
    id: str
    impact: str
    incident_updates: [IncidentUpdate]
    monitoring_at: Optional[str]
    name: str
    page_id: str
    resolved_at: Optional[str]
    shortlink: str
    status: str
    updated_at: str

    @classmethod
    def from_json(cls, json_: dict):
        incident = cls(**json_)
        incident.incident_updates = \
            [IncidentUpdate.from_json(json_=iu) for iu in json_.get("incident_updates")]

        return incident
