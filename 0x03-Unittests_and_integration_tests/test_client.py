#!/usr/bin/env python3
"""Unittests for the client module."""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class."""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """Test that GithubOrgClient.org returns the correct value."""
        mock.return_value = TEST_PAYLOAD
        client = GithubOrgClient(org)
        self.assertEqual(client.org, TEST_PAYLOAD)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one."""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock:
            org = GithubOrgClient("google")
            org._public_repos_url = "https://api.github.com/orgs/google/repos"
            self.assertEqual(org._public_repos_url, mock.return_value)

    @patch("client.get_json")
    def test_public_repos(self, mock_method):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        payload = [{"name": "google"}, {"name": "abc"}]
        mock_method.return_value = payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            org = GithubOrgClient("google")
            self.assertEqual(org.public_repos(), ["google", "abc"])
            mock_method.assert_called_once()
            mock_url.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


# We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.

# Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

# Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py. The file contains the following fixtures:

# org_payload, repos_payload, expected_repos, apache2_repos
# The setupClass should mock requests.get to return example payloads found in the fixtures.

# Use patch to start a patcher named get_patcher, and use side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.

# Implement the tearDownClass class method to stop the patcher.


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class."""
        cls.get_patcher = patch("client.get_json")
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class."""
        cls.get_patcher.stop()

    @parameterized.expand(
        [("org_payload", "repos_payload", "expected_repos", "apache2_repos")],
        testcase_func_name=parameterized.to_safe_name,
    )
    def test_public_repos(
        self, org_payload, repos_payload, expected_repos, apache2_repos
    ):
        """Test public_repos method."""
        org_payload = getattr(self, org_payload)
        repos_payload = getattr(self, repos_payload)
        expected_repos = getattr(self, expected_repos)
        apache2_repos = getattr(self, apache2_repos)

        self.mock_get.side_effect = [org_payload, repos_payload]
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), apache2_repos)
