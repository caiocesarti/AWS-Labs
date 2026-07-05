<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 08 — AWS Serverless Demonstrated — Practical Exam Lab

<p align="center">
  <img src="assets/Serverless.webp" alt="AWS Serverless Demonstrated — Banner" width="100%"/>
</p>

## 🚀 Executive Summary
This lab is a **hands-on Exam Lab** where I troubleshot, configured, and hardened a serverless e-commerce platform, overcoming **7 interdependent challenges** directly in the AWS console. The project ranges from orchestration with Step Functions to security with WAF and CI/CD with CodePipeline.

---

## 💼 Real-World Use Case
- **Industry:** E-commerce / Retail
- **Problem:** A recently launched serverless e-commerce architecture exhibited critical security flaws, incomplete functions in the deployment pipeline, and poorly orchestrated checkout processes, leading to dropped orders and shopping cart persistence failures.
- **Solution:** Implementation and remediation of a microservices-based architecture. Secure API gateways, Cognito authentication protected by WAF, and robust order orchestration with Step Functions and DynamoDB tables were configured, ensuring scalability and resilience.

---

## 🎯 Learning Objectives
*   **Fix and enhance** CI/CD pipelines (CodePipeline) for Lambda functions.
*   **Secure** APIs using Amazon API Gateway, Amazon Cognito, and AWS WAF rules.
*   **Orchestrate** asynchronous processes and fault handling with AWS Step Functions.
*   **Isolate** network resources by configuring VPCs for Lambda functions.

---

## 🛠️ AWS Services Used

| Service                   | Role in the Lab                                             |
| ------------------------- | ----------------------------------------------------------- |
| **AWS Lambda**            | 6 domain functions (products, cart, orders, notifs).        |
| **Amazon API Gateway**    | REST API with proxy integration and CORS.                   |
| **Amazon Cognito**        | User authentication and authorization.                      |
| **AWS WAF**               | Managed rules for API protection against attacks.           |
| **Amazon DynamoDB**       | State persistence for shopping cart and orders.             |
| **AWS Step Functions**    | Asynchronous orchestration with robust error handling.      |
| **Amazon SQS & SNS**      | Decoupling and automated order notifications.               |
| **AWS CodePipeline**      | CI/CD pipeline with manual approval stages.                 |
| **Amazon VPC**            | Network isolation for sensitive Lambda functions.           |

---

## 🖥️ Lab Steps

### Challenge A: CI/CD with CodePipeline
- Fixed an incomplete pipeline to allow continuous and secure updates of a Lambda function, implementing a manual approval stage.

### Challenge B: API Gateway Configuration
- Full implementation and configuration of Amazon API Gateway, ensuring proper routing (proxy integration) and CORS security.

### Challenge C & D: Security with Cognito and WAF
- Configured the Amazon Cognito User Pool.
- Secured the API by linking API Gateway to Cognito for authorization.
- Deployed AWS WAF ACLs to block malicious traffic before reaching logical layers.

### Challenge E: Cart Persistence
- Remedied IAM policies and partition structures in Amazon DynamoDB to efficiently persist shopping cart items.

### Challenge F: Order Orchestration
- Adjusted state machines in AWS Step Functions, orchestrating SQS, SNS, and DynamoDB to process orders asynchronously and handle graceful failures.

### Challenge G: Network Boundaries with VPC
- Isolated sensitive Lambda functions by placing them within an Amazon VPC, configuring the appropriate Subnets, Security Groups, and NAT Gateways.

---

## 📸 Execution Evidence

### Microcredential Earned
<p align="center">
  <img src="assets/serverless-demonstrated.webp" alt="AWS Serverless Demonstrated Badge" width="180"/>
</p>

> [!IMPORTANT]
> This credential certifies the successful completion of the official AWS Skills Builder practical exam.

---

## 💡 Key Learnings
*   **Orchestration beats Choreography in transactions:** Using Step Functions ensured that failures in checkout stages could be structurally rolled back, unlike pure SQS/SNS chaining.
*   **Defense in Depth:** The combination of WAF mitigating Layer 7 attacks and Cognito ensuring identity proved essential for REST API integrity.
*   **VPC in Lambdas requires planning:** Network configuration for Lambdas requires careful attention to Cold Start times and proper ENI (Elastic Network Interface) permissions.

---

## 🔗 Additional Resources
- [AWS Skill Builder — Microcredentials](https://explore.skillbuilder.aws/learn/public/learning_plan/view/2070/microcredentials)
- [Amazon API Gateway Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| AWS Lambda | ✅ 1M requests/mo | $0.00 |
| Amazon API Gateway | ✅ 1M requests/mo | $0.00 |
| Amazon DynamoDB | ✅ 25GB, 25 WCU/RCU | $0.00 |
| AWS Step Functions | ✅ 4,000 transitions/mo | $0.00 |
| **Total** | | **$0.00** |

---

## 🏷️ Competencies Demonstrated

`AWS Lambda` `Amazon API Gateway` `Amazon Cognito` `AWS WAF` `Amazon DynamoDB` `AWS Step Functions` `Amazon SQS` `Amazon SNS` `AWS CodePipeline` `Amazon VPC` `Serverless` `Microservices` `🔴 Advanced`

---

## 📎 Reference

> This lab generated an in-depth technical walkthrough article:
> **👉 [Article: AWS Serverless Demonstrated — Exam Lab na Prática](https://labs.caiocesar.tec.br/2026/06/27/aws-serverless-demonstrated-exam-lab/)**
> 
> *Note: This repository is for study purposes and does not contain proprietary code from the AWS lab.*

---

[← Back to Index](../../../README-en.md)
