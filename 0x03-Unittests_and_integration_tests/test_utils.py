#!/usr/bin/env python3
"""Test utils
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Test get_json"""
        mock_requests_get.return_value = Mock()
        mock_requests_get.return_value.json.return_value = test_payload

        self.assertEqual(get_json(test_url), test_payload)
        mock_requests_get.assert_called_once_with(test_url)


# 3. Parameterize and patch
# mandatory
# Read about memoization and familiarize yourself with the utils.memoize decorator.

# Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

# Inside test_memoize, define following class

# class TestClass:

#     def a_method(self):
#         return 42

#     @memoize
#     def a_property(self):
#         return self.a_method()
# Use unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.


class TestMemoize(unittest.TestCase):
    """TestMemoize"""

    def test_memoize(self):
        """Test memoize"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test = TestClass()

        with patch.object(test, "a_method") as mock_a_method:
            mock_a_method.return_value = 42

            assert test.a_property == 42
            assert test.a_property == 42

            mock_a_method.assert_called_once()
