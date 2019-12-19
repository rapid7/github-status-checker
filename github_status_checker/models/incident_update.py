from dataclasses import dataclass


@dataclass
class IncidentUpdate:
    body: str
    created_at: str
    display_at: str
    id: str
    incident_id: str
    status: str
    updated_at: str

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
