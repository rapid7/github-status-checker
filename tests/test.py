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

