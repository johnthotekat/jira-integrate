# Jira Integrate [🚧 NOT READY 🚧]

## 🚨 Overview

The **Jira Integrate** is a Python module designed to interact with Jira's REST API to create issues. It uses Jinja2 templates to dynamically generate the issue data payload based on the provided templates. This module allows you to programmatically create Jira tickets based on various input data and is part of a larger workflow engine that integrates with different tools and systems.

**⚠️ Please note:** This module is currently in development and may not be fully functional or stable. Use with caution and verify its compatibility with your Jira instance before relying on it for production use.

## 🔧 Features

- Create Jira tickets using the Jira REST API.
- Utilizes Jinja2 templates for flexible and dynamic issue creation.
- Configurable for different Jira instances and user credentials.
- Useful for integration with alert handling systems.

## 🚧 Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- Access to a Jira instance with appropriate permissions to create issues.
- Jira credentials (username and API token).
- Jinja2 templates for defining the issue data structure.

## 🛠️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/johnthotekat/jira-integrate.git
   cd jira-integrate
   ```

2. **Install Dependencies**

   Create a virtual environment (optional but recommended) and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## ⚠️ Configuration

1. **Environment Variables**

   Set up environment variables for Jira connection. You can add these to your `.env` file or set them directly in your environment.

   ```bash
   export JIRA_URL="https://yourcompany.atlassian.net"
   export USERNAME="your-email@example.com"
   export API_TOKEN="your-api-token"
   ```

2. **Template Files**

   Place your Jinja2 template files in the `templates` directory. The module will use these templates to generate the issue data.

   Example of a Jinja2 template (`issue_template.j2`):

   ```jinja2
   {
     "fields": {
       "project": {
         "key": "{{ project_key }}"
       },
       "summary": "{{ summary }}",
       "description": "{{ description }}",
       "issuetype": {
         "name": "{{ issue_type }}"
       }
     }
   }
   ```

## 🚀 Usage

Here is a basic example of how to use the Jira Integrate module with Jinja2 templates:

```python
from jira_integrate import JiraClient, TemplateManager

# Initialize the JiraClient
jira_url = "https://yourcompany.atlassian.net"
username = "your-email@example.com"
api_token = "your-api-token"
ticket_creator = JiraClient(jira_url, username, api_token)

# Initialize the TemplateManager
template_path = "templates/issue_template.j2"
template_manager = TemplateManager(template_path)

# Define the data for the issue
issue_data = {
    "project_key": "PROJ",
    "summary": "Test Issue",
    "description": "This is a description for the test issue.",
    "issue_type": "Task"
}

# Render the template with the issue data
rendered_issue_data = template_manager.render_template(issue_data)

# Create a ticket
response = ticket_creator.create_ticket(rendered_issue_data)

# Print response
print(response)
```

### 🛠️ Constructor

#### `JiraClient`

```python
JiraClient(jira_url: str, username: str, api_token: str)
```

- **`jira_url`**: URL of your Jira instance.
- **`username`**: Jira username or email address.
- **`api_token`**: Jira API token.

#### `create_ticket(issue_data: dict) -> dict`

Creates a Jira ticket with the provided issue data.

- **`issue_data`**: JSON-formatted string containing the issue details. Must be generated using a Jinja2 template.

- **Returns**: A dictionary with the response from the Jira API.

### 🛠️ TemplateManager

#### `TemplateManager`

```python
TemplateManager(template_path: str)
```

- **`template_path`**: Path to the Jinja2 template file.

#### `render_template(data: dict) -> str`

Renders the Jinja2 template with the provided data.

- **`data`**: Dictionary containing data to populate the template.

- **Returns**: A JSON-formatted string with the rendered issue data.

## ⚠️ Error Handling

The module will raise exceptions for issues such as invalid credentials, template errors, or network errors. Ensure to handle these exceptions in your implementation.

## 🤝 Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your changes and create a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.