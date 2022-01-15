import json

# import requests


def lambda_handler(message, context):
    
    print(message['pathParameters']['id'])
    print(json.loads(message['body']))

    return {
        "statusCode": 200,
        "body": json.dumps({
          "message": "hello world",
        }),
    } 

