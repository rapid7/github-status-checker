class Page:

    def __init__(self,
                 id: str,
                 name: str,
                 url: str,
                 updated_at: str,
                 time_zone: str):

        self.id = id
        self.name = name
        self.url = url
        self.updated_at = updated_at
        self.time_zone = time_zone

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
