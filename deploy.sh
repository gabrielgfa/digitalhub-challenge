#!/bin/bash
set -e

STACK_NAME="vehicle-demo-stack"
REGION="eu-west-1"

sam build

sam deploy --stack-name $STACK_NAME \
           --region $REGION \
           --capabilities CAPABILITY_IAM \
           --no-confirm-changeset \
           --resolve-s3