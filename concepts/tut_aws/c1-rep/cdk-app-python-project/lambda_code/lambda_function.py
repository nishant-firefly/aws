import os
import requests
from jinja2 import Template

# Define Lambda handler function
def lambda_handler(event, context):
    # Extract parameters from event
    template = event.get('template', {})  # Template should be passed from Step Functions
    params = event.get('params', {})      # Dynamic parameters for the template

    # Validate template structure
    if 'url' not in template or 'method' not in template or 'payload' not in template:
        return {
            'statusCode': 400,
            'body': 'Invalid template format. Missing url, method, or payload.'
        }
    
    # Construct the API URL (base URL can be passed as an environment variable)
    base_url = os.environ.get('API_BASE_URL', '')
    full_url = f"{base_url}{template['url']}"

    # Prepare the headers (if any)
    headers = template.get('headers', {})

    # Render the payload using Jinja2 template
    jinja_template = Template(template.get('payload', ''))
    rendered_payload = jinja_template.render(params)

    # Call the API based on the method (GET, POST, etc.)
    try:
        if template['method'].upper() == 'POST':
            response = requests.post(full_url, headers=headers, json=eval(rendered_payload))
        elif template['method'].upper() == 'GET':
            response = requests.get(full_url, headers=headers, params=params)
        else:
            return {
                'statusCode': 400,
                'body': f'Unsupported HTTP method: {template["method"]}'
            }

        # Return the API response
        return {
            'statusCode': response.status_code,
            'body': response.json()
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error calling the API: {str(e)}'
        }
