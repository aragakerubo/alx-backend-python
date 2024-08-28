#!/usr/bin/env python3
"""Unittests for the client module."""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class."""

    @classmethod
    def setUpClass(self):
        """Set up class."""
        self.get_patcher = patch("client.get_json")
        self.mock_get = self.get_patcher.start()
        self.mock_get.side_effect = [
            self.org_payload,
            self.repos_payload,
        ]

    @classmethod
    def tearDownClass(self):
        """Tear down class."""
        self.get_patcher.stop()

    def test_public_repos(self):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos
        returns the correct value with license.
        """
        org = GithubOrgClient("google")
        self.assertEqual(org.public_repos("apache-2.0"), self.apache2_repos)
