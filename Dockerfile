FROM python:3.11-slim

RUN apt-get update && apt-get install -y unzip curl zip jq groff less git && \
    pip install awscli boto3 aws-sam-cli && \
    apt-get clean

WORKDIR /app

COPY template.yaml .
COPY deploy.sh .

CMD ["bash", "deploy.sh"]