class AffectedComponent:
    def __init__(self, code: str, name: str, old_status: str, new_status: str):
        self.code = code
        self.name = name
        self.old_status = old_status
        self.new_status = new_status

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
