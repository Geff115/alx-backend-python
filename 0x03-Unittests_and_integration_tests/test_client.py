#!/usr/bin/env python3
"""This script contains a unit tests for the
client.GithubOrgClient class.
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, MagicMock
from utils import get_json
from parameterized import parameterized, parameterized_class
from typing import Any, Dict
from fixtures import TEST_PAYLOAD
from functools import wraps


class TestGithubOrgClient(unittest.TestCase):
    """Test class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mocked_request: Any) -> None:
        """Testing org to return expected results"""
        # Defining a mock response for get_json
        mock_response = {"mock_key": "mock_value"}
        mocked_request.return_value = mock_response

        # Instantiate GithubOrgClient with the given org
        test_client = GithubOrgClient(org)

        # Calling the org method and capturing the result
        result = test_client.org

        self.assertEqual(result, mock_response)
        mocked_request.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns the expected repos_url"""
        with patch.object(GithubOrgClient, 'org',
             new_callable=PropertyMock) as mock_org:
            # Define the mock payload
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"
            }
            # Instantiate the client and call the _public_repos_url property
            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            # Assert that _public_repos_url matches repos_url in mock payload
            self.assertEqual(
                result, "https://api.github.com/orgs/test_org/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Any) -> None:
        """Unit-test for public_repos"""
        # Mock response payload from get_json
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_repos_payload

        # Mock _public_repos_url to return a test URL
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as url:
            url.return_value = "https://api.github.com/orgs/test_org/repos"

            # Instantiate the client
            client = GithubOrgClient("test_org")

            # Call public_repos and check the result
            expected_repos = ["repo1", "repo2", "repo3"]
            result = client.public_repos()

            # Assert the returned repo list is as expected
            self.assertEqual(result, expected_repos)

            # Assert that _public_repos_url and get_json were each called once
            url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict,
                         license_key: str, expected: bool) -> None:
        """Unit-test for has_license"""
        # Call the static method has_license
        # with the given repo and license_key
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)


@parameterized_class([
    ({"org_payload": {**TEST_PAYLOAD[0][0], "login": "test_org"},
      "repos_payload": TEST_PAYLOAD[0][1],
      "expected_repos": ["episodes.dart"],
      "apache2_repos": ["episodes.dart"]})
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class-level patches and mocks"""
        # Mock requests.get and set side_effect to return fixtures based on URL
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set side_effect to return different responses based on URL
        def get_json_side_effect(func):
            @wraps(func)
            def wrapper(url):
                if "orgs" in url:
                    return cls.org_payload
                elif "repos" in url:
                    return cls.repos_payload
                return {}
            return wrapper

        cls.mock_get.return_value.json.side_effect = get_json_side_effect(
            cls.mock_get.return_value.json
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class-level patches"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repos"""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repos by license"""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
