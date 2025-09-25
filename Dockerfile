FROM python:3.11-slim

RUN apt-get update && apt-get install -y unzip zip curl jq groff less && \
    pip install awscli boto3 && \
    apt-get clean

WORKDIR /app

COPY template.yaml .
COPY deploy.sh .

WORKDIR /lambda
COPY lambda/vehicle_handler.py .

WORKDIR /app
CMD ["bash", "deploy.sh"]