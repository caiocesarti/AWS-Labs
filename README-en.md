<div align="center">
  <img src="./assets/banner.png" alt="AWS Cloud Labs" width="100%"/>

  <br/>

  ![Labs](https://img.shields.io/badge/labs-29-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
  ![Domains](https://img.shields.io/badge/domains-6-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
  ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
  ![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
  ![CI](https://img.shields.io/github/actions/workflow/status/caiocesarti/AWS-Labs/validate.yml?style=flat-square&logo=github&label=CI)

  <p>
    <a href="./README-en.md">🇺🇸 English</a> &nbsp;|&nbsp;
    <a href="./README.md">🇧🇷 Português</a>
  </p>
</div>

---

## About

Repository with practical AWS labs organized by product domain. Each lab documents provisioning, the scripts used, and validation evidence. Under continuous expansion.

---

## Covered Domains

| Domain                  | Labs | Technologies                                    |
| ----------------------- | ---- | ----------------------------------------------- |
| ⚡ Serverless            | 7    | Lambda, API Gateway, SNS, SQS, DLQ, EventBridge |
| 🔒 Security & Compliance | 8    | IAM, STS, KMS, CloudWatch, CloudTrail, SSM      |
| 🌐 Network & Delivery    | 3    | VPC, CloudFront, API Gateway                    |
| 📦 Storage               | 4    | S3, EBS, Bucket Policy, Lifecycle, DLM          |
| 🗄️ Database              | 3    | DynamoDB, LSI, GSI, Boto3                       |
| 🖥️ Compute               | 4    | EC2, Elastic Beanstalk, Auto Scaling, ALB       |

---

## Labs

### ⚡ Serverless

| #   | Lab                                                                        | Description                                             | Level          |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------- | -------------- |
| 01  | [AWS Lambda Introduction](./labs/6-serverless/01-lambda-introduction/)     | Automatic image resizing with S3 Triggers               | 🔴 Advanced     |
| 02  | [Lambda Aliases + API Gateway](./labs/6-serverless/02-lambda-api-gateway/) | dev/prod stage isolation with aliases and `$LATEST`     | 🟡 Intermediate |
| 03  | [Lambda + EventBridge](./labs/6-serverless/03-lambda-eventbridge/)         | Cron scheduler for automated EC2 instance shutdown      | 🔴 Advanced     |
| 04  | [Lambda + S3 + API Gateway](./labs/6-serverless/04-lambda-s3-game/)        | Serverless full-stack web app — guessing game           | 🟡 Intermediate |
| 05  | [SNS + SQS + DLQ](./labs/6-serverless/05-sns-sqs-dlq/)                     | Pub/Sub with failure isolation via Dead-Letter Queue    | 🟡 Intermediate |
| 06  | [Fan-Out SNS → SQS](./labs/6-serverless/06-sns-sqs-fanout/)                | Fan-out topology with attribute-based message filtering | 🔴 Advanced     |
| 07  | [S3 Event Notifications](./labs/6-serverless/07-s3-sns-sqs-events/)        | Audit triggered by native bucket events                 | 🔴 Advanced     |

### 🔒 Security, Identity, and Compliance

| #   | Lab                                                                                        | Description                                                    | Level          |
| --- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | -------------- |
| 01  | [Introduction to AWS IAM](./labs/5-security-identity-compliance/01-iam-introduction/)      | User, group, and access policy management (least privilege)    | 🟢 Foundational |
| 02  | [AWS STS: Temporary Credentials](./labs/5-security-identity-compliance/02-aws-sts/)        | Programmatic `AssumeRole` for access without permanent keys    | 🟢 Foundational |
| 03  | [IAM: S3 ReadOnly](./labs/5-security-identity-compliance/03-iam-s3-readonly/)              | Least privilege with Managed Groups for restricted access      | 🟢 Foundational |
| 04  | [AWS Budgets](./labs/5-security-identity-compliance/04-aws-budgets/)                       | Expense control with threshold alerts via email                | 🟢 Foundational |
| 05  | [CloudWatch + CloudTrail](./labs/5-security-identity-compliance/05-cloudwatch-cloudtrail/) | EC2 monitoring under load + API call auditing                  | 🟡 Intermediate |
| 06  | [SSM Parameter Store + KMS](./labs/5-security-identity-compliance/06-ssm-parameter-store/) | Secret management with AES-256 encryption via KMS              | 🟡 Intermediate |
| 07  | [Basic Environment Audit](./labs/5-security-identity-compliance/07-aws-basic-audit/)       | IAM, VPC Security analysis, and log auditing in CloudTrail/S3  | 🟡 Intermediate |
| 08  | [AWS KMS: Key Management](./labs/5-security-identity-compliance/08-aws-kms-introduction/)  | Symmetric key lifecycle, SSE-KMS, and auditing with CloudTrail | 🟡 Intermediate |

### 🌐 Network and Content Delivery

| #   | Lab                                                                                      | Description                                       | Level          |
| --- | ---------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------- |
| 01  | [Amazon VPC](./labs/4-network-and-content-delivery/01-vpc-introduction/)                 | Public/private subnets, NAT Gateway, IGW, and AZs | 🟢 Foundational |
| 02  | [Amazon CloudFront](./labs/4-network-and-content-delivery/02-cloudfront-introduction/)   | CDN with distribution via Edge Locations          | 🟢 Foundational |
| 03  | [Amazon API Gateway](./labs/4-network-and-content-delivery/03-api-gateway-introduction/) | Serverless microservice with Lambda integration   | 🟢 Foundational |

### 📦 Storage

| #   | Lab                                                                    | Description                                                                    | Level          |
| --- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------- |
| 01  | [S3: Introduction and Policies](./labs/2-storage/01-s3-introduction/)  | Bucket Policies (JSON), Block Public Access (BPA), and Recovery via Versioning | 🟡 Intermediate |
| 02  | [S3: Advanced Management](./labs/2-storage/02-s3-advanced-management/) | Versioning, Lifecycle, Pre-signed URLs, and Server Access Logs                 | 🟢 Foundational |
| 03  | [S3: Basic & Advanced](./labs/2-storage/03-s3-basic-advanced/)         | Storage class automation and temporary URLs                                    | 🟢 Foundational |
| 04  | [EBS: Volumes and Snapshots](./labs/2-storage/04-ebs-mount-snapshots/) | ext4 mount via CLI and retention policies with DLM                             | 🟡 Intermediate |

### 🗄️ Database

| #   | Lab                                                                                   | Description                                                  | Level          |
| --- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------- |
| 01  | [Introduction to Amazon DynamoDB](./labs/3-database/01-amazon-dynamodb-introduction/) | Table creation, item insertion, and Query vs Scan operations | 🟢 Foundational |
| 02  | [DynamoDB Serverless CRUD](./labs/3-database/02-dynamodb-lambda-crud/)                | REST API with Lambda + Boto3 on NoSQL table                  | 🟡 Intermediate |
| 03  | [DynamoDB LSI & GSI](./labs/3-database/03-dynamodb-lsi-gsi/)                          | Query optimization — Scan vs Query and index rotation        | 🟡 Intermediate |

### 🖥️ Compute

| #   | Lab                                                                 | Description                                                     | Level          |
| --- | ------------------------------------------------------------------- | --------------------------------------------------------------- | -------------- |
| 01  | [Introduction to Amazon EC2](./labs/1-compute/01-ec2-introduction/) | Lifecycle: Launch, Monitoring, Security, and Vertical Resize    | 🟢 Foundational |
| 02  | [EC2 + CloudShell](./labs/1-compute/02-ec2-console-cloudshell/)     | Web instances with User Data via Console and CLI                | 🟢 Foundational |
| 03  | [Elastic Beanstalk](./labs/1-compute/03-elastic-beanstalk/)         | PaaS deployment with IAM Instance Profile                       | 🟢 Foundational |
| 04  | [Auto Scaling + ALB](./labs/1-compute/04-auto-scaling-alb/)         | High availability with Launch Templates, ASG, and Load Balancer | 🟡 Intermediate |

---

## Lab Structure
```text
<lab-name>/
├── README.md      # Architecture context and technical decisions
├── README-en.md   # English version
├── src/           # Scripts (Python / Bash / Boto3)
└── assets/        # Diagrams and validation evidence
```

> **Note:** Infrastructure as Code (Terraform/CDK) scripts are centralized in the root `/iac` directory, organized by lab.

---

## Author

**Caio Cesar**
IT Graduate, AWS re/Start Graduate. Certifications: CLF-C02 · DVA-C02 · SAA-C03 · AIF-C01.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-caiocesardev-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/caiocesardev/)
[![GitHub](https://img.shields.io/badge/GitHub-caiocesarti-181717?style=flat-square&logo=github)](https://github.com/caiocesarti)
