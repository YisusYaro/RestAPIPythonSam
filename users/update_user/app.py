import json
import boto3

# import requests


def lambda_handler(message, context):
    
  user_id = message['pathParameters']['id']
  user = json.loads(message['body'])
  app_table = boto3.resource('dynamodb', region_name='us-east-1')
  table = app_table.Table('App')

  keys = {
    'PK': 'users',
    'SK': user_id
  }

  table.update_item(
    Key=keys,
    UpdateExpression='set #name = :n, city = :c',
    ExpressionAttributeValues={
      ':n': user['name'],
      ':c': user['city'],
    },
    ExpressionAttributeNames={
      '#name': 'name'
    },
    ReturnValues="UPDATED_NEW"
  )

  return {
    "statusCode": 200,
  } 

