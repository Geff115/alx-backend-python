#!/usr/bin/env python3
"""This script contains a unit tests for the
client.GithubOrgClient class.
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch
from utils import get_json
from parameterized import parameterized
from typing import Any, Dict


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
