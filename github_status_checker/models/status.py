from dataclasses import dataclass


@dataclass
class Status:
    indicator: str
    description: str

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
