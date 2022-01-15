import json

# import requests


def lambda_handler(message, context):
    

    return {
        "statusCode": 200,
        "body": json.dumps({
          "message": "hello world",
        }),
    }
