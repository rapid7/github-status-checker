from dataclasses import dataclass


@dataclass
class Page:
    id: str
    name: str
    url: str
    updated_at: str
    time_zone: str

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
