import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(message, context):
    
  app_table = boto3.resource('dynamodb', region_name='us-east-1')
  table = app_table.Table('App')

  response = table.query( 
    KeyConditionExpression=Key('PK').eq('users'),
  );  

  return {
    'statusCode': 200,
    'body': json.dumps(response['Items'])
  }
