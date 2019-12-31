from github_status_checker.models.incident_update import IncidentUpdate


class ScheduledMaintenance:

    def __init__(self,
                 created_at: str,
                 id: str,
                 impact: str,
                 incident_updates: [IncidentUpdate],
                 monitoring_at: str,
                 name: str,
                 page_id: str,
                 resolved_at: str,
                 scheduled_for: str,
                 scheduled_until: str,
                 shortlink: str,
                 status: str,
                 updated_at: str):

        self.created_at = created_at
        self.id = id
        self.impact = impact
        self.incident_updates = incident_updates
        self.monitoring_at = monitoring_at
        self.name = name
        self.page_id = page_id
        self.resolved_at = resolved_at
        self.scheduled_for = scheduled_for
        self.scheduled_until = scheduled_until
        self.shortlink = shortlink
        self.status = status
        self.updated_at = updated_at

    @classmethod
    def from_json(cls, json_: dict):
        scheduled_maintenance = cls(**json_)
        scheduled_maintenance.incident_updates = \
            [IncidentUpdate.from_json(json_=iu) for iu in json_.get("incident_updates")]

        return scheduled_maintenance
