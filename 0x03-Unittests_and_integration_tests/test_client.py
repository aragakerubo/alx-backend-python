#!/usr/bin/env python3
"""Unittests for the client module."""
import unittest
from unittest.mock import patch
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
    def test_public_repos(self, mock):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        mock.return_value = TEST_PAYLOAD
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public:
            mock_public.return_value = TEST_PAYLOAD
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), TEST_PAYLOAD)
            mock.assert_called_once()
            mock_public.assert_called_once()
