import boto3
import json
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("vehicle-demo")
s3 = boto3.client("s3")

BUCKET_NAME = "vehicle-summary"

def lambda_handler(event, context):
    response = table.scan()
    count = len(response.get("Items", []))

    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "totalVehicles": count,
    }
    body = json.dumps(summary)

    filename = f"summary_{datetime.utcnow().strftime('%Y%m%d')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=body,
        ContentType="application/json"
    )

    return {"statusCode": 200, "body": body}