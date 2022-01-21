import json
from urllib import response
import boto3
from ulid import ULID
import json

def lambda_handler(message, context):
    
  user = json.loads(message['body'])

  app_table = boto3.resource('dynamodb', region_name='us-east-1')
  table = app_table.Table('App')

  params = {
    'PK': 'users',
    'SK': str(ULID()),
    'name': user['name'],
    'city': user['city'],
  }

  table.put_item(TableName='App', Item=params)

  return {
    'statusCode': 201,
  }
