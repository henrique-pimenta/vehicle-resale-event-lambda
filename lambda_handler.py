import os

import requests


def lambda_handler(event, context):
    inverse_routing_urls = {
        'inventory_service': os.environ["TRANSACTION_SERVICE_URL"],
        'transaction_service': os.environ["INVENTORY_SERVICE_URL"],
    }
    try:
        url = inverse_routing_urls.get(event.get('source', 'unknown'))
        if url is None:
            raise Exception('invalid source')

        response = requests.post(url, json=event)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending event to service: {e}") # for CloudWatch
