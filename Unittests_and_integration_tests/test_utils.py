#!/usr/bin/env python3
"""
Unit tests for utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map with various inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
        self, nested_map,
        path, expected_exception
    ):
        """
        Test that accessing a nested key raises the expected exception
        """

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


class TestGetJson(unittest.TestCase):
    """
    Test case for get_json function
    """
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, expected_payload, mock_get):
        """
        Test case for get_json function
        """
        mock_json = Mock(return_value=expected_payload)
        mock_get.return_value = Mock(json=mock_json)

        result = get_json(test_url)

        self.assertEqual(result, expected_payload)


class TestClass:
    """
    Test class for memoize decorator
    """
    def a_method(self):
        """
        Test method
        """
        return 42

    @memoize
    def a_property(self):
        """
        Test property decorated with memoize
        """
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """
    Test case for memoize decorator
    """
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test that memoize decorator caches the result
        """
        test_obj = TestClass()
