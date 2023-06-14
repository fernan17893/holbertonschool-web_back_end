#!/usr/bin/env python3
"""Client test"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
import client
from fixtures import TEST_PAYLOAD


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Github Org"""

    @parameterized.expand([
        ("google", {}),
        ("abc", {}),
    ])
    def test_org(self, org, result):
        """Test org"""
        with patch('client.get_json') as mock_get:
            mock_get.return_value = {}
            test_client = client.GithubOrgClient(org)
            self.assertEqual(test_client.org, result)
            mock_get.assert_called_once_with()
