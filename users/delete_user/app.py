import boto3

def lambda_handler(message, context):
    
  print(message['pathParameters']['id'])

  user_id = message['pathParameters']['id']

  app_table = boto3.resource('dynamodb', region_name='us-east-1')
  table = app_table.Table('App')

  keys = {
    'PK': 'users',
    'SK': user_id,
  }

  table.delete_item(Key=keys)
    
  return {
      "statusCode": 200,
  }
