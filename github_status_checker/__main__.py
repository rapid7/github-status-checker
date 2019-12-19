import json

import click
import requests

from github_status_checker.models.summary import Summary


@click.option("--name", envvar="some_awesome_name")
def main():
    pass


if __name__ == "__main__":
    ENDPOINT = "https://kctbh9vrtdwd.statuspage.io/api/v2"

    url = f"{ENDPOINT}/summary.json"

    resp = requests.get(url)

    j = json.dumps(resp.json(), default=lambda o: o.__dict__)
    summary: Summary = Summary.from_json(json_=resp.json())
    for c in summary.components:
        print(f"{c.name} is currently {c.status.value}")
