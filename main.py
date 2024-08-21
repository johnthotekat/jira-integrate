# main.py

import os
from jira_operations import JiraClient
from template_manager import TemplateManager


def main():
    # Load environment variables
    JIRA_URL = os.getenv('JIRA_URL')
    USERNAME = os.getenv('USERNAME')
    API_TOKEN = os.getenv('API_TOKEN')
    TEMPLATE_PATH = 'templates'

    # Initialize clients
    jira_client = JiraClient(JIRA_URL, USERNAME, API_TOKEN)
    template_manager = TemplateManager(TEMPLATE_PATH)

    # Choose template and issue data
    template_name = 'issue_template.j2'  # This can be changed based on user input
    issue_data_context = {
        "project_key": "SUP",
        "summary": "This is a test issue created via Python",
        "description": "Detailed description of the issue",
        "issue_type": "Task"
    }

    # Render issue data from template
    rendered_issue_data = template_manager.render_template(template_name, issue_data_context)

    # Print the payload to debug
    print("Payload to Jira:", rendered_issue_data)

    # Create issue
    response = jira_client.create_issue(rendered_issue_data)

    # Print response
    if response['success']:
        print('Issue created successfully!')
        print('Issue key:', response['key'])
    else:
        print('Failed to create issue')
        print('Response:', response['error'])


if __name__ == '__main__':
    main()
