from dataclasses import dataclass

from github_status_checker.models.component import Component
from github_status_checker.models.incident import Incident
from github_status_checker.models.page import Page
from github_status_checker.models.scheduled_maintenance import ScheduledMaintenance
from github_status_checker.models.status import Status


@dataclass
class Summary:
    page: Page
    components: [Component]
    incidents: [Incident]
    scheduled_maintenances: [ScheduledMaintenance]
    status: Status

    @classmethod
    def from_json(cls, json_: dict):
        page = Page.from_json(json_=json_.get("page"))
        components = [Component.from_json(json_=c) for c in json_.get("components")]
        status = Status.from_json(json_=json_.get("status"))
        scheduled_maintenances = [ScheduledMaintenance.from_json(json_=sm) for sm in
                                  json_.get("scheduled_maintenances")]
        incidents = [Incident.from_json(json_=i) for i in json_.get("incidents")]

        return cls(page=page,
                   components=components,
                   incidents=incidents,
                   scheduled_maintenances=scheduled_maintenances,
                   status=status)
