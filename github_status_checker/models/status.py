class Status:

    def __init__(self,
                 indicator: str,
                 description: str):
        self.indicator = indicator
        self.description = description

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
