FROM python:3.13-slim

RUN apt-get update && apt-get install -y unzip curl zip jq groff less git && \
    pip install --no-cache-dir awscli boto3 aws-sam-cli && \
    apt-get clean

WORKDIR /app

COPY template.yaml .
COPY deploy.sh .
COPY lambda/ lambda/

CMD ["bash", "deploy.sh"]