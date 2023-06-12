#!/usr/bin/env python3
"""Unittest"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b") , 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 1),
        ({"a": 1}, ("a", "b") , 2),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access nested map exception"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)