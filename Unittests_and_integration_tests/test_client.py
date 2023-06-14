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
        ("google"),
        ("abc"),
    ])
    def test_org(self, org):
        """Test org"""
        with patch('client.get_json') as mock_get:
            mock_get = {}
            mock_get.return_value = {"payload": True}
            test_class = GithubOrgClient(org)
            self.assertEqual(test_class.org, mock_get.return_value)
            mock_get.assert_called_once_with("https://api.github.com/orgs/" + org)
