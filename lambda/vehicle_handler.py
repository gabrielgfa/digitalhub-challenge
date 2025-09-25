import os
import json
import boto3

TABLE_NAME = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'POST':
        body = json.loads(event['body'])
        vin = body.get('vin')
        noOfAxles = body.get('noOfAxles')
        fuelType = body.get('fuelType')
        
        if fuelType not in ["gaseous", "electric"]:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "fuelType must be 'gaseous' or 'electric'"})
            }
        
        table.put_item(Item={
            "vin": vin,
            "noOfAxles": noOfAxles,
            "fuelType": fuelType
        })
        return {"statusCode": 200, "body": json.dumps({"message": "Vehicle added"})}
    
    elif method == 'GET':
        response = table.scan()
        return {"statusCode": 200, "body": json.dumps(response['Items'])}
    
    elif method == 'DELETE':
        vin = event['queryStringParameters'].get('vin')
        if not vin:
            return {"statusCode": 400, "body": json.dumps({"message": "vin is required"})}
        table.delete_item(Key={"vin": vin})
        return {"statusCode": 200, "body": json.dumps({"message": "Vehicle deleted"})}
    
    else:
        return {"statusCode": 405, "body": json.dumps({"message": "Method not allowed"})}