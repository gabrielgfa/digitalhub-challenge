#!/bin/bash
set -e

STACK_NAME="vehicle-demo-stack"
BUCKET_NAME="vehicle-demo-lambda"

LAMBDA_ZIP="vehicle_handler_$(date +%s).zip"

echo "📦 Packaging Lambda..."
cp /lambda/vehicle_handler.py .
zip $LAMBDA_ZIP vehicle_handler.py

echo "☁️ Uploading to S3..."
aws s3 mb s3://$BUCKET_NAME 2>/dev/null || echo "Bucket exists"
aws s3 cp $LAMBDA_ZIP s3://$BUCKET_NAME/$LAMBDA_ZIP

echo "🚀 Deploying CloudFormation..."
aws cloudformation deploy \
  --stack-name $STACK_NAME \
  --template-file template.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides LambdaS3Key=$LAMBDA_ZIP

echo "✅ Deployment complete!"
aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query "Stacks[0].Outputs"