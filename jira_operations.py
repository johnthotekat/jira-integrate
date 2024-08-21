# jira_operations.py

import requests
from requests.auth import HTTPBasicAuth
import json


class JiraClient:
    def __init__(self, jira_url, username, api_token):
        self.jira_url = jira_url
        self.username = username
        self.api_token = api_token
        self.api_endpoint = '/rest/api/2/issue'

    def create_issue(self, issue_data):
        response = requests.post(
            f'{self.jira_url}{self.api_endpoint}',
            auth=HTTPBasicAuth(self.username, self.api_token),
            headers={'Content-Type': 'application/json'},
            data=json.dumps(issue_data)
        )

        if response.status_code == 201:
            return {'success': True, 'key': response.json().get('key')}
        else:
            return {'success': False, 'error': response.json()}

