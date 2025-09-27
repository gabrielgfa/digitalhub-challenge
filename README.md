# MAN DigitalHub Challenge

Hello, CCE team!  
This project implements a **serverless API on AWS** to handle vehicle data. The API accepts JSON payloads, stores them in DynamoDB, and provides endpoints to create, list, and delete vehicles. To fulfill the optional requirement, it also creates weekly a summary file containing the total number of vehicles is generated and stored in an S3 bucket.

Each vehicle record includes:
- `vin` (string) – unique vehicle identifier
- `noOfAxles` (integer) – number of axles
- `fuelType` (string) – allowed values: `"electric"` or `"gaseous"`
- `timestamp` (string) – ISO timestamp when the record was created  

And always following your advice in the interview guideline: when in doubt, simplify! :)  

## Deployment

### Prerequisites
- AWS account with Free Tier
- AWS system variables configured with your AWS Free Tier credentials:
```
    aws configure
```
- [Docker](https://docs.docker.com/engine/install/) installed.

### Deploying

Now, all we gotta do is run:
```
docker compose up --build
```

This Docker compose will be responsible to install all the dependencies, and run [AWS SAM](https://aws.amazon.com/serverless/sam/) to bundle the code and deploy the application to AWS.