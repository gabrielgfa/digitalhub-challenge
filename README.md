# MAN DigitalHub Challenge

## Introduction

Hi CCE Team! 👋  

For this challenge, I followed your advice: *"Have fun and when in doubt, simplify!"*. I focused on a clean, serverless design using high-level AWS services and infrastructure-as-code, keeping the implementation straightforward while demonstrating automation, cloud-native best practices, and maintainable code.

## Project overview  

### Key Features:
- REST API for CRUD operations on vehicles (`POST /vehicle`, `GET /vehicles`, `DELETE /vehicle`)  
- Persistence in DynamoDB (`vehicle-demo` table)  
- Weekly summary of vehicle count generated and stored in S3 (`vehicle-summary` bucket)  
- Fully automated deployment using AWS SAM  

### Tech Stack:
- AWS Lambda (Python 3.13)  
- DynamoDB  
- S3  
- API Gateway 
- AWS SAM / CloudFormation  
- Docker

## Architecture & Design  

### Architecture Diagram:
```
[API Gateway] --> [VehicleLambda] --> [DynamoDB]
[SummaryLambda] (triggered by CloudWatch Event) --> [DynamoDB] --> [S3 Bucket]
```

### Design Decisions:
- **Serverless:** Lambda functions for event-driven, scalable endpoints  
- **High-level AWS Services:** DynamoDB used instead of custom databases for simplicity and managed scalability  
- **Infrastructure-as-Code:** SAM chosen for reproducibility and ease of deployment  
- **Validation & Data Modeling:** `VehicleModel` ensures data integrity before persisting  
- **Decoupling:** Separate Lambda for weekly summary to reduce load on main API  

### Considerations:  
- Free Tier compatible  
- Schedule for summary can be adjusted (currently daily)  
- Error handling included for common DynamoDB conflicts (e.g., duplicate VIN)  

## Deployment  

### Requirements
- AWS account (also works on free tier version)
- Docker  
- [AWS CLI](https://aws.amazon.com/cli/)
- AWS credentials configured (`~/.aws/credentials`)

### Deployment Steps

All you need to do is run:
```
docker compose up --build
```
This Docker compose will be responsible to install all dependencies, and run AWS SAM to bundle the code and deploy the application to AWS.

## High-level CI/CD Strategy

I noticed in your interview guideline that GitLab is the platform you use, which I know well. For this project, I replicated the level of automation I aim for in any stack, using Docker to manage the build environment and create the application image through the [Gitlab Container Registry](https://docs.gitlab.com/user/packages/container_registry/), while leveraging [GitLab CI](https://docs.gitlab.com/ci/) to automate the build and deployment process from start to finish.  

### Pipeline Flow:  

1. **Source Control:** Developer pushes code → [GitLab CI](https://docs.gitlab.com/ci/) triggers pipeline  
2. **Linting & Unit Tests:** Python tests + code quality checks  
3. **Approval Gate:** Manual approval before production deploy  
4. **Build & Package:** SAM build and package commands  
5. **Deployment:** Deploy to environment  
6. **Monitoring:** CloudWatch logs and metrics (maybe with a Datadog integration for better monitoring)


## Wrap-up

Thanks for the fun challenge! I really enjoyed putting this together.  
I’m looking forward to chatting with you in the interview and hearing your thoughts. 🙂