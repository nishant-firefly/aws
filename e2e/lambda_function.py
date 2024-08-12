import json
import requests

def lambda_handler(event, context):
    url = event['url']
    method = event['method']
    headers = event.get('headers', {})
    body = event.get('body', None)

    try:
        response = requests.request(method, url, headers=headers, data=body)
        return {
            'statusCode': response.status_code,
            'body': response.text
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
