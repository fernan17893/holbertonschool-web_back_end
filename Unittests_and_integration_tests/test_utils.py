#!/usr/bin/env python3
"""Unittest"""

from utils import access_nested_map
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 1),
        ({"a": 1}, ("a", "b"), 2),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access nested map exception"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get json class"""

    @patch('requests.get')
    def test_get_json(self, mock_get):
        """Test get json"""

        test_urls = [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False}),
        ]
        for test_url, test_payload in test_urls:
            mock_get.return_value = requests.Response()
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = test_payload

            respone = get_json(test_url)

            self.assertEqual(respone, test_payload)
