# digitalhub-challenge

Hello, CCE team! :)
This project implements a **serverless API on AWS** to handle vehicle data. The API accepts JSON payloads, stores them in DynamoDB, and provides endpoints to create, list, and delete vehicles.  

Each vehicle record includes:
- `vin` (string) – unique vehicle identifier
- `noOfAxles` (integer) – number of axles
- `fuelType` (string) – allowed values: `"electric"` or `"gaseous"`
- `timestamp` (string) – ISO timestamp when the record was created  

And to fulfill the optional requirement, it also creates weekly a summary file containing the total number of vehicles could be generated and stored in an S3 bucket.

## Deployment

### Prerequisites
- AWS account with Free Tier
- AWS system variables configured with your AWS Free Tier credentials:
```
    aws configure
```
- [Docker](https://docs.docker.com/engine/install/) installed. 