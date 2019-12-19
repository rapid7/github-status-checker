from dataclasses import dataclass

from github_status_checker.models.incident_update import IncidentUpdate


@dataclass
class ScheduledMaintenance:
    created_at: str
    id: str
    impact: str
    incident_updates: [IncidentUpdate]
    monitoring_at: str
    name: str
    page_id: str
    resolved_at: str
    scheduled_for: str
    scheduled_until: str
    shortlink: str
    status: str
    updated_at: str

    @classmethod
    def from_json(cls, json_: dict):
        scheduled_maintenance = cls(**json_)
        scheduled_maintenance.incident_updates = \
            [IncidentUpdate.from_json(json_=iu) for iu in json_.get("incident_updates")]

        return scheduled_maintenance
