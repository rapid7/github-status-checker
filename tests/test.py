from unittest import TestCase

import json
from github_status_checker.controllers.commands import Commands
from github_status_checker.models.summary import Summary


class TestCheckInvalidArg(TestCase):
    def setUp(self) -> None:
        pass

    def test_check(self):
        with self.assertRaises(Exception):
            Commands.check(component_arg="onemoose")


class TestJSONDeserializeSummary(TestCase):
    def setUp(self) -> None:
        pass

    def test_deserialize_good(self):
        good_json = """{"page":{"id":"kctbh9vrtdwd","name":"GitHub","url":"https://www.githubstatus.com","time_zone":"Etc/UTC","updated_at":"2019-12-30T08:15:33.297Z"},"components":[{"id":"8l4ygp009s5s","name":"Git Operations","status":"operational","created_at":"2017-01-31T20:05:05.370Z","updated_at":"2019-12-13T18:46:03.911Z","position":1,"description":"Performance of git clones, pulls, pushes, and associated operations","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"brv1bkgrwx7q","name":"API Requests","status":"operational","created_at":"2017-01-31T20:01:46.621Z","updated_at":"2019-12-13T18:46:02.799Z","position":2,"description":"Requests for GitHub APIs","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"4230lsnqdsld","name":"Webhooks","status":"operational","created_at":"2019-11-13T18:00:24.256Z","updated_at":"2019-12-19T23:13:07.086Z","position":3,"description":"Real time HTTP callbacks of user-generated and system events","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"0l2p9nhqnxpd","name":"Visit www.githubstatus.com for more information","status":"operational","created_at":"2018-12-05T19:39:40.838Z","updated_at":"2019-11-13T18:02:47.782Z","position":4,"description":null,"showcase":false,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"kr09ddfgbfsf","name":"Issues, PRs, Projects","status":"operational","created_at":"2017-01-31T20:01:46.638Z","updated_at":"2019-12-13T18:46:06.900Z","position":5,"description":"Web requests for github.com UI and services","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"br0l2tvcx85d","name":"GitHub Actions","status":"operational","created_at":"2019-11-13T18:02:19.432Z","updated_at":"2019-12-13T18:46:01.547Z","position":6,"description":"Workflows, Compute and Orchestration for GitHub Actions","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"st3j38cctv9l","name":"GitHub Packages","status":"operational","created_at":"2019-11-13T18:02:40.064Z","updated_at":"2019-12-10T11:40:31.724Z","position":7,"description":"API requests and webhook delivery for GitHub Packages","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"vg70hn9s2tyj","name":"GitHub Pages","status":"operational","created_at":"2017-01-31T20:04:33.923Z","updated_at":"2019-12-13T18:46:06.226Z","position":8,"description":"Frontend application and API servers for Pages builds","showcase":true,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false},{"id":"5l5rlzqm4yzy","name":"Other","status":"operational","created_at":"2019-11-13T18:03:05.012Z","updated_at":"2019-12-19T23:13:02.972Z","position":9,"description":"Other","showcase":false,"group_id":null,"page_id":"kctbh9vrtdwd","group":false,"only_show_if_degraded":false}],"incidents":[],"scheduled_maintenances":[],"status":{"indicator":"none","description":"All Systems Operational"}}"""

        try:
            Summary.from_json(json_=json.loads(good_json))
        except TypeError:
            self.fail()


class TestOutagePayload(TestCase):
    def setUp(self) -> None:
        self.json = """{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2020-04-02T20:37:08.838Z"
  },
  "components": [
    {
      "id": "8l4ygp009s5s",
      "name": "Git Operations",
      "status": "major_outage",
      "created_at": "2017-01-31T20:05:05.370Z",
      "updated_at": "2020-04-02T20:26:21.656Z",
      "position": 1,
      "description": "Performance of git clones, pulls, pushes, and associated operations",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "brv1bkgrwx7q",
      "name": "API Requests",
      "status": "major_outage",
      "created_at": "2017-01-31T20:01:46.621Z",
      "updated_at": "2020-04-02T20:18:20.643Z",
      "position": 2,
      "description": "Requests for GitHub APIs",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "4230lsnqdsld",
      "name": "Webhooks",
      "status": "major_outage",
      "created_at": "2019-11-13T18:00:24.256Z",
      "updated_at": "2020-04-02T20:37:08.834Z",
      "position": 3,
      "description": "Real time HTTP callbacks of user-generated and system events",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "0l2p9nhqnxpd",
      "name": "Visit www.githubstatus.com for more information",
      "status": "operational",
      "created_at": "2018-12-05T19:39:40.838Z",
      "updated_at": "2019-11-13T18:02:47.782Z",
      "position": 4,
      "description": null,
      "showcase": false,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "kr09ddfgbfsf",
      "name": "Issues, PRs, Projects",
      "status": "major_outage",
      "created_at": "2017-01-31T20:01:46.638Z",
      "updated_at": "2020-04-02T20:18:21.177Z",
      "position": 5,
      "description": "Web requests for github.com UI and services",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "br0l2tvcx85d",
      "name": "GitHub Actions",
      "status": "partial_outage",
      "created_at": "2019-11-13T18:02:19.432Z",
      "updated_at": "2020-04-02T20:21:56.716Z",
      "position": 6,
      "description": "Workflows, Compute and Orchestration for GitHub Actions",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "st3j38cctv9l",
      "name": "GitHub Packages",
      "status": "major_outage",
      "created_at": "2019-11-13T18:02:40.064Z",
      "updated_at": "2020-04-02T20:36:52.738Z",
      "position": 7,
      "description": "API requests and webhook delivery for GitHub Packages",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "vg70hn9s2tyj",
      "name": "GitHub Pages",
      "status": "operational",
      "created_at": "2017-01-31T20:04:33.923Z",
      "updated_at": "2020-03-12T15:51:14.866Z",
      "position": 8,
      "description": "Frontend application and API servers for Pages builds",
      "showcase": true,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    },
    {
      "id": "5l5rlzqm4yzy",
      "name": "Other",
      "status": "operational",
      "created_at": "2019-11-13T18:03:05.012Z",
      "updated_at": "2020-03-06T00:22:12.900Z",
      "position": 9,
      "description": "Other",
      "showcase": false,
      "group_id": null,
      "page_id": "kctbh9vrtdwd",
      "group": false,
      "only_show_if_degraded": false
    }
  ],
  "incidents": [
    {
      "id": "80d0cs6kpsps",
      "name": "Incident on 2020-04-02 20:20 UTC",
      "status": "investigating",
      "created_at": "2020-04-02T20:20:54.013Z",
      "updated_at": "2020-04-02T20:26:36.356Z",
      "monitoring_at": null,
      "resolved_at": null,
      "impact": "major",
      "shortlink": "http://stspg.io/n0wskg2n6bvy",
      "started_at": "2020-04-02T20:20:54.005Z",
      "page_id": "kctbh9vrtdwd",
      "incident_updates": [
        {
          "id": "yqsdhyw44qzj",
          "status": "investigating",
          "body": "We are investigating reports of service unavailability.",
          "incident_id": "80d0cs6kpsps",
          "created_at": "2020-04-02T20:26:36.354Z",
          "updated_at": "2020-04-02T20:26:36.354Z",
          "display_at": "2020-04-02T20:26:36.354Z",
          "affected_components": null,
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        },
        {
          "id": "bd69p75gd9y8",
          "status": "investigating",
          "body": "We are investigating reports of degraded performance.",
          "incident_id": "80d0cs6kpsps",
          "created_at": "2020-04-02T20:20:54.071Z",
          "updated_at": "2020-04-02T20:20:54.071Z",
          "display_at": "2020-04-02T20:20:54.071Z",
          "affected_components": [
            {
              "code": "0l2p9nhqnxpd",
              "name": "Visit www.githubstatus.com for more information",
              "old_status": "operational",
              "new_status": "operational"
            }
          ],
          "deliver_notifications": true,
          "custom_tweet": null,
          "tweet_id": null
        }
      ],
      "components": [
        {
          "id": "0l2p9nhqnxpd",
          "name": "Visit www.githubstatus.com for more information",
          "status": "operational",
          "created_at": "2018-12-05T19:39:40.838Z",
          "updated_at": "2019-11-13T18:02:47.782Z",
          "position": 4,
          "description": null,
          "showcase": false,
          "group_id": null,
          "page_id": "kctbh9vrtdwd",
          "group": false,
          "only_show_if_degraded": false
        }
      ]
    }
  ],
  "scheduled_maintenances": [],
  "status": {
    "indicator": "major",
    "description": "Partial System Outage"
  }
}
"""

    def test_serialize(self):
        summary = Summary.from_json(json_=json.loads(self.json))
        print(summary)
