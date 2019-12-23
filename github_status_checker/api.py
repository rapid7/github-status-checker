from json import JSONDecodeError

from requests import Session, Request
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from github_status_checker.models.summary import Summary


class API(object):
    _ENDPOINT = "https://kctbh9vrtdwd.statuspage.io/api/v2"

    def __init__(self, session: Session):
        self.session = session

    @classmethod
    def new(cls):
        """
        Instantiate a new GitHub Status API object
        :return: GitHub Status API object
        """
        session = Session()
        retries = Retry(total=5,
                        backoff_factor=0.2)
        adapter = HTTPAdapter(max_retries=retries)

        session.mount("https://", adapter)

        return cls(session=session)

    def get_summary(self) -> Summary:
        """
        Get a status summary for GitHub services
        :return: Summary
        """
        request = self.session.prepare_request(Request(method="GET",
                                                       url=f"{self._ENDPOINT}/summary.json"))

        response = self.session.send(request)
        response.raise_for_status()

        try:
            summary = Summary.from_json(response.json())
        except (JSONDecodeError, KeyError) as e:
            raise Exception("An error occurred while attempting to"
                            " deserialize the GitHub status summary response!") from e

        return summary
