import requests
from jinja2 import FileSystemLoader, Environment
from requests.auth import HTTPBasicAuth
import json
import os

#https://www.postman.com/api-evangelist/atlassian-jira/request/fasib33/create-issue?tab=body
# Replace with your Jira instance details
JIRA_URL = os.getenv('JIRA_URL')
USERNAME = os.getenv('USERNAME')
API_TOKEN = os.getenv('API_TOKEN')

print(JIRA_URL)

API_ENDPOINT = '/rest/api/2/issue'
PROJECT_KEY = 'SUP'  # Replace with your project key
ISSUE_TYPE = 'Task'  # Replace with the issue type you want to create

# Create the issue data payload

# Path to the directory containing your Jinja2 template
TEMPLATE_PATH = 'templates'

# Load the Jinja2 template from the specified path
file_loader = FileSystemLoader(TEMPLATE_PATH)
env = Environment(loader=file_loader)
template = env.get_template('issue_template.j2')

# Define the data for the issue
issue_data = {
    "project_key": "SUP",  # Replace with your project key
    "summary": "This is a test issue created via Python",
    "description": "Detailed description of the issue",
    "issue_type": "Task"  # Replace with the issue type you want to create
}

# Render the template with the data
rendered_issue_data = template.render(issue_data)

# Send the request to Jira
response = requests.post(
    f'{JIRA_URL}{API_ENDPOINT}',
    auth=HTTPBasicAuth(USERNAME, API_TOKEN),
    headers={
        'Content-Type': 'application/json'
    },
    data=rendered_issue_data
)

# Print the response
if response.status_code == 201:
    print('Issue created successfully!')
    print('Issue key:', response.json().get('key'))
else:
    print('Failed to create issue')
    print('Response:', response.json())