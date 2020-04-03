from github_status_checker.models.affected_component import AffectedComponent


class IncidentUpdate:
    body: str
    created_at: str
    display_at: str
    id: str
    incident_id: str
    status: str
    updated_at: str

    def __init__(
        self,
        body: str,
        created_at: str,
        display_at: str,
        affected_components: [AffectedComponent],
        deliver_notifications: bool,
        custom_tweet: str,
        tweet_id: str,
        id: str,
        incident_id: str,
        status: str,
        updated_at: str,
    ):

        self.body = body
        self.created_at = created_at
        self.display_at = display_at
        self.affected_components = affected_components
        self.deliver_notifications = deliver_notifications
        self.custom_tweet = custom_tweet
        self.tweet_id = str(tweet_id)
        self.id = id
        self.incident_id = incident_id
        self.status = status
        self.updated_at = updated_at

    @classmethod
    def from_json(cls, json_: dict):
        return cls(**json_)
