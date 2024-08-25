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
        mock_method.return_value = TEST_PAYLOAD
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), TEST_PAYLOAD)
        mock_method.assert_called_once()

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


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient."""

    @parameterized.expand([("google"), ("abc")])
    def test_public_repos(self, org):
        """Integration test: public_repos."""
        client = GithubOrgClient(org)
        response = client.public_repos()
        self.assertIsInstance(response, list)
        self.assertTrue(all(isinstance(repo, dict) for repo in response))
        self.assertTrue(all("name" in repo for repo in response))
        self.assertTrue(all("license" in repo for repo in response))
