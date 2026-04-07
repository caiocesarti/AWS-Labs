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

<details>
<summary>👉 <b>⚡ Serverless</b> (7 Labs)</summary>
<br>


- **01. [AWS Lambda Introduction](./labs/6-serverless/01-lambda-introduction/)** | `🔴 Advanced`
  > Automatic image resizing with S3 Triggers


- **02. [Lambda Aliases + API Gateway](./labs/6-serverless/02-lambda-api-gateway/)** | `🟡 Intermediate`
  > dev/prod stage isolation with aliases and `$LATEST`


- **03. [Lambda + EventBridge](./labs/6-serverless/03-lambda-eventbridge/)** | `🔴 Advanced`
  > Cron scheduler for automated EC2 instance shutdown


- **04. [Lambda + S3 + API Gateway](./labs/6-serverless/04-lambda-s3-game/)** | `🟡 Intermediate`
  > Serverless full-stack web app — guessing game


- **05. [SNS + SQS + DLQ](./labs/6-serverless/05-sns-sqs-dlq/)** | `🟡 Intermediate`
  > Pub/Sub with failure isolation via Dead-Letter Queue


- **06. [Fan-Out SNS → SQS](./labs/6-serverless/06-sns-sqs-fanout/)** | `🔴 Advanced`
  > Fan-out topology with attribute-based message filtering


- **07. [S3 Event Notifications](./labs/6-serverless/07-s3-sns-sqs-events/)** | `🔴 Advanced`
  > Audit triggered by native bucket events

</details>
<details>
<summary>👉 <b>🔒 Security, Identity, and Compliance</b> (8 Labs)</summary>
<br>


- **01. [Introduction to AWS IAM](./labs/5-security-identity-compliance/01-iam-introduction/)** | `🟢 Foundational`
  > User, group, and access policy management (least privilege)


- **02. [AWS STS: Temporary Credentials](./labs/5-security-identity-compliance/02-aws-sts/)** | `🟢 Foundational`
  > Programmatic `AssumeRole` for access without permanent keys


- **03. [IAM: S3 ReadOnly](./labs/5-security-identity-compliance/03-iam-s3-readonly/)** | `🟢 Foundational`
  > Least privilege with Managed Groups for restricted access


- **04. [AWS Budgets](./labs/5-security-identity-compliance/04-aws-budgets/)** | `🟢 Foundational`
  > Expense control with threshold alerts via email


- **05. [CloudWatch + CloudTrail](./labs/5-security-identity-compliance/05-cloudwatch-cloudtrail/)** | `🟡 Intermediate`
  > EC2 monitoring under load + API call auditing


- **06. [SSM Parameter Store + KMS](./labs/5-security-identity-compliance/06-ssm-parameter-store/)** | `🟡 Intermediate`
  > Secret management with AES-256 encryption via KMS


- **07. [Basic Environment Audit](./labs/5-security-identity-compliance/07-aws-basic-audit/)** | `🟡 Intermediate`
  > IAM, VPC Security analysis, and log auditing in CloudTrail/S3


- **08. [AWS KMS: Key Management](./labs/5-security-identity-compliance/08-aws-kms-introduction/)** | `🟡 Intermediate`
  > Symmetric key lifecycle, SSE-KMS, and auditing with CloudTrail

</details>
<details>
<summary>👉 <b>🌐 Network and Content Delivery</b> (3 Labs)</summary>
<br>


- **01. [Amazon VPC](./labs/4-network-and-content-delivery/01-vpc-introduction/)** | `🟢 Foundational`
  > Public/private subnets, NAT Gateway, IGW, and AZs


- **02. [Amazon CloudFront](./labs/4-network-and-content-delivery/02-cloudfront-introduction/)** | `🟢 Foundational`
  > CDN with distribution via Edge Locations


- **03. [Amazon API Gateway](./labs/4-network-and-content-delivery/03-api-gateway-introduction/)** | `🟢 Foundational`
  > Serverless microservice with Lambda integration

</details>
<details>
<summary>👉 <b>📦 Storage</b> (4 Labs)</summary>
<br>


- **01. [S3: Introduction and Policies](./labs/2-storage/01-s3-introduction/)** | `🟡 Intermediate`
  > Bucket Policies (JSON), Block Public Access (BPA), and Recovery via Versioning


- **02. [S3: Advanced Management](./labs/2-storage/02-s3-advanced-management/)** | `🟢 Foundational`
  > Versioning, Lifecycle, Pre-signed URLs, and Server Access Logs


- **03. [S3: Basic & Advanced](./labs/2-storage/03-s3-basic-advanced/)** | `🟢 Foundational`
  > Storage class automation and temporary URLs


- **04. [EBS: Volumes and Snapshots](./labs/2-storage/04-ebs-mount-snapshots/)** | `🟡 Intermediate`
  > ext4 mount via CLI and retention policies with DLM

</details>
<details>
<summary>👉 <b>🗄️ Database</b> (3 Labs)</summary>
<br>


- **01. [Introduction to Amazon DynamoDB](./labs/3-database/01-amazon-dynamodb-introduction/)** | `🟢 Foundational`
  > Table creation, item insertion, and Query vs Scan operations


- **02. [DynamoDB Serverless CRUD](./labs/3-database/02-dynamodb-lambda-crud/)** | `🟡 Intermediate`
  > REST API with Lambda + Boto3 on NoSQL table


- **03. [DynamoDB LSI & GSI](./labs/3-database/03-dynamodb-lsi-gsi/)** | `🟡 Intermediate`
  > Query optimization — Scan vs Query and index rotation

</details>
<details>
<summary>👉 <b>🖥️ Compute</b> (4 Labs)</summary>
<br>


- **01. [Introduction to Amazon EC2](./labs/1-compute/01-ec2-introduction/)** | `🟢 Foundational`
  > Lifecycle: Launch, Monitoring, Security, and Vertical Resize


- **02. [EC2 + CloudShell](./labs/1-compute/02-ec2-console-cloudshell/)** | `🟢 Foundational`
  > Web instances with User Data via Console and CLI


- **03. [Elastic Beanstalk](./labs/1-compute/03-elastic-beanstalk/)** | `🟢 Foundational`
  > PaaS deployment with IAM Instance Profile


- **04. [Auto Scaling + ALB](./labs/1-compute/04-auto-scaling-alb/)** | `🟡 Intermediate`
  > High availability with Launch Templates, ASG, and Load Balancer

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
</details>
