#!/usr/bin/env python3
"""Unittest"""


import unittest
import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path):
        self.assertEqual(access_nested_map
                         (nested_map, path),
                         nested_map[path[-1]])
