import json

# import requests


def lambda_handler(message, context):
    
    print(message['pathParameters']['id'])

    return {
        "statusCode": 200,
        "body": json.dumps({
          "message": "hello world",
        }),
    }