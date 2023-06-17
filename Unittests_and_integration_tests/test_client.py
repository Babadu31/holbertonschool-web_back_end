#!/usr/bin/env python3
"""
Mocking a property
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """
    def test_public_repos_url(self):
        """
        Test case to verify the behavior of the _public_repos_url property.
        The test mocks the GithubOrgClient.org property and verifies that the
        _public_repos_ur property returns the expected URL based on the
        mocked payload.
        """
        mock_payload = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
                }
        expected_result = mock_payload['repos_url']

        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock,
                return_value=mock_payload
                ):
            client = GithubOrgClient('Google')
            result = client._public_repos_url
            self.assertEqual(result, expected_result)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Mocking the get_json metho
        """
        mock_get_json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]

        with patch.object(
                GithubOrgClient, '_public_repos_url',
                return_value='https://api.github.com/orgs/testorg/repos'
                ):
            client = GithubOrgClient('testorg')
            repos = client.public_repos()
            self.assertEqual(repos, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        [{'license': {'key': 'my_license'}}, 'my_license'],
        [{'license': {'key': 'other_license'}}, 'my_license'],
        ])
    def test_has_license(self, repo, license_key):
        """
        Test case to verify the behavior of the has_license method.
        The test parametrizes the repo and license_key inputs and verifies
        the result of the has_license method.
        """
        client = GithubOrgClient('testorg')
        result = client.has_license(repo, license_key)

        if license_key == repo.get('license', {}).get('key'):
            self.assertTrue(result)
        else:
            self.assertFalse(result)
