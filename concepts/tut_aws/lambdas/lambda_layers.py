"""
Lambda Layers allow you to reuse dependencies or code across multiple Lambda functions. 
Here's an example where we use a Lambda Layer to include an external Python library like requests.
"""
# Create a directory for the layer:
# mkdir -p python/lib/python3.8/site-packages/
# Install requests into the directory:
# pip install requests -t python/lib/python3.8/site-packages/
# zip the folder
# zip -r layer.zip python/

import requests

def lambda_handler(event, context):
    # Use the requests library (from the layer)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    return {
        'statusCode': 200,
        'body': response.text
    }
