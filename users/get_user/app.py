import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(message, context):
    
  user_id = message['pathParameters']['id']

  app_table = boto3.resource('dynamodb', region_name='us-east-1')
  table = app_table.Table('App')

  response = table.get_item( 
    Key={
      'PK': 'users',
      'SK': user_id,
    },
  )

  return {
    'statusCode': 200,
    'body': json.dumps({
      'name': response['Item']['name'],
      'city': response['Item']['city'],
    })
  }