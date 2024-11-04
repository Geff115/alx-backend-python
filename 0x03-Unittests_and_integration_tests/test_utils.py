#!/usr/bin/env python3
"""
This script contains a unit test for the utils.access_nested_map
function.
"""

import unittest
import requests
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Testing access nested map with different nested maps and path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Testing that KeyError is raised for non-existent paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test class"""
    @parameterized.expand([
        ("https://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_requests: Any) -> None:
        """Testing the requests.get object"""
        # Mock the response object
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response

        # Call get_json and assert its output
        self.assertEqual(get_json(test_url), test_payload)

        # Assert that requests.get was called once with test_url
        mock_requests.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test class"""

    def test_memoize(self):
        """This method tests the utils.memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_instance = TestClass()

            # Checking that the output of a_property is as expected
            result = test_instance.a_property
            self.assertEqual(result, 42)

            result = test_instance.a_property
            self.assertEqual(result, 42)

            # Verify that a_method was called once due to memoization (caching)
            mock_method.assert_called_once()
