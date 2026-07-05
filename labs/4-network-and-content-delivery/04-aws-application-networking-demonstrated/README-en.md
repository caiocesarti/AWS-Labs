<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 04 — AWS Application Networking Demonstrated — Practical Exam Lab

<p align="center">
  <img src="assets/AWS Application Networking.webp" alt="AWS Application Networking Demonstrated — Banner" width="100%"/>
</p>

## 🚀 Executive Summary
This lab is a **hands-on Exam Lab** where I troubleshot, configured, and hardened a multi-tier application infrastructure in a real AWS environment. I successfully completed **7 interdependent challenges** involving the creation of a modern service mesh architecture using Amazon VPC Lattice, CloudFront, ALB, ECS, and API Gateway.

---

## 💼 Real-World Use Case
- **Industry:** Technology / Web Services
- **Problem:** A legacy Service Desk web application was suffering from communication issues between microservices, security vulnerabilities at the edge, frontend traffic interruptions, and inadequate monitoring. The communication between the frontend and the backend API was not routing correctly due to complex integration and security rules.
- **Solution:** Implementation of a robust service mesh network with Amazon VPC Lattice to facilitate service discovery. Edge protection using CloudFront and WAF. Remediation of ALB and ECS communications, ensuring resilience and traffic visibility with access logs and CloudWatch alarms.

---

## 🎯 Learning Objectives
*   **Secure** web infrastructure using Amazon CloudFront and AWS WAF rules.
*   **Fix and scale** containerized services running on Amazon ECS behind an Application Load Balancer.
*   **Configure** service networks (service mesh) with Amazon VPC Lattice for native discovery and secure cross-subnet communication.
*   **Monitor** and generate proactive alarms using Amazon CloudWatch and Amazon SNS.

---

## 🛠️ AWS Services Used

| Service                        | Role in the Lab                                                           |
| ------------------------------ | ------------------------------------------------------------------------- |
| **Amazon CloudFront**          | CDN and public entry layer, protecting the origin (ALB).                  |
| **AWS WAF**                    | Web application firewall rules attached to the CloudFront distribution.   |
| **Application Load Balancer**  | Routing incoming traffic to ECS clusters.                                 |
| **Amazon ECS**                 | Running microservices: `servicedesk-frontend` and `servicedesk-api`.      |
| **Amazon VPC Lattice**         | Managed service mesh connecting the frontend and backend VPCs.            |
| **Amazon API Gateway**         | Public API exposure with proxy integration.                               |
| **AWS Lambda**                 | Proxy function mediating between API Gateway and VPC Lattice.             |
| **Amazon DynamoDB**            | Backend NoSQL database accessed privately.                                |
| **Amazon VPC**                 | Multi-tier network isolation (public and private subnets) and SGs.        |
| **Amazon CloudWatch & SNS**    | Metrics collection and alarm triggering for service failures.             |
| **Amazon S3**                  | Secure storage for Load Balancer access logs.                             |

---

## 🖥️ Lab Steps

### Challenge A: CloudFront Configuration for Production
- Configured a CloudFront distribution pointing to the Application Load Balancer as its origin.
- Attached AWS WAF rules to block malicious traffic at the edge.

### Challenge B: ALB Health and ECS Scaling
- Fixed health check endpoints in the ALB Target Group.
- Updated and scaled Amazon ECS services to ensure high availability.

### Challenge C: Multi-Tier Security
- Refactored Security Groups to allow strict, least-privilege traffic between CloudFront, ALB, VPC Lattice, and ECS tasks.

### Challenge D: Service Mesh with VPC Lattice
- Created and configured an Amazon VPC Lattice service network.
- Registered the frontend and backend services, simplifying discovery without complex routing or peering rules.

### Challenge E: API Gateway and Lattice Integration
- Resolved issues in integrating Amazon API Gateway with the internal VPC Lattice network, utilizing AWS Lambda as a proxy layer.

### Challenge F: Monitoring and Alarms
- Created alarms in Amazon CloudWatch based on anomalies and 5XX errors.
- Configured Amazon SNS topics to notify the engineering team in case of failures.

### Challenge G: Access Logs
- Enabled the retention and delivery of ALB Access Logs to a centralized Amazon S3 bucket, allowing for future traffic audits.

---

## 📸 Execution Evidence

### Microcredential Earned
<p align="center">
  <img src="assets/AWS Application Networking Demonstrated.webp" alt="AWS Application Networking Demonstrated Badge" width="180"/>
</p>

> [!IMPORTANT]
> This credential certifies the successful completion of the official AWS Skills Builder practical exam.

---

## 💡 Key Learnings
*   **VPC Lattice simplifies complex networking:** Instead of managing dozens of route tables and VPC Peering rules, VPC Lattice provided consistent Layer 7 connectivity, making the service mesh feel natural.
*   **Strict Security Group alignment:** The request flow from CloudFront -> ALB -> ECS requires the target instances' Security Groups to explicitly reference the origin Security Group to enforce the principle of least privilege.
*   **End-to-End Visibility:** Sending ALB access logs to S3 isn't just for auditing—it's essential for diagnosing inter-service timeouts.

---

## 🔗 Additional Resources
- [AWS Skill Builder — Microcredentials](https://explore.skillbuilder.aws/learn/public/learning_plan/view/2070/microcredentials)
- [Amazon VPC Lattice Documentation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
- [Application Load Balancer Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Amazon CloudFront | ✅ 1TB out/mo | $0.00 |
| Amazon API Gateway | ✅ 1M requests/mo | $0.00 |
| AWS Lambda | ✅ 1M requests/mo | $0.00 |
| Amazon VPC Lattice | ❌ Pay per request & time | ~$1.50/mo |
| Application Load Balancer | ❌ Pay per LCU & time | ~$16.00/mo |
| **Estimated Total** | | **~$17.50** |

---

## 🏷️ Competencies Demonstrated

`Amazon CloudFront` `AWS WAF` `ALB` `Amazon ECS` `Amazon VPC Lattice` `AWS Lambda` `Amazon API Gateway` `Amazon DynamoDB` `Amazon VPC` `Amazon CloudWatch` `Amazon SNS` `Amazon S3` `🔴 Advanced`

---

## 📎 Reference

> This lab generated an in-depth technical walkthrough article:
> **👉 [Article: AWS Application Networking Demonstrated — Exam Lab na Prática](https://labs.caiocesar.tec.br/2026/06/28/aws-application-networking-demonstrated-exam-lab/)**
> 
> *Note: This repository is for study purposes and does not contain proprietary code from the AWS lab.*

---

[← Back to Index](../../../README-en.md)
