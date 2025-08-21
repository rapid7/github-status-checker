import unittest
from github_status_checker.controllers.commands import Commands

COMPONENT_TARGETS = [
    "git",
    "api",
    "webhooks",
    "issues_prs_projects",
    "actions",
    "packages",
    "pages"
]

class TestComponentCheck(unittest.TestCase):
    def test_check_runs_for_all_components(self):
        for component in COMPONENT_TARGETS:
            with self.subTest(component=component):
                # Should not raise for valid components, will reach out to the real API
                Commands.check(component_arg=component)
