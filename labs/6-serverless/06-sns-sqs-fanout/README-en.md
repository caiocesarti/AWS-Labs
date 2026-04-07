<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 06 — Fan-Out Architecture with SNS, SQS, and Lambda

## 🚀 Summary
Advanced Routing for Event-Driven Architectures (EDA): In this lab, I implemented the **Fan-Out** pattern, one of the most powerful architectures for distributed systems. I configured an **Amazon SNS Topic** as a central hub that receives a single event and distributes it simultaneously to multiple subscribers. I used **Subscription Filter Policies** to ensure each service receives only relevant messages, optimizing processing and reducing costs by avoiding unnecessary **AWS Lambda** function and **Amazon SQS** queue invocations.

---

## 💼 Real-World Use Case
- **Industry:** Scalable E-commerce and Logistics Systems
- **Problem:** In a monolithic system, when a customer completes a purchase, the code sequentially triggers invoicing, inventory updates, logistics notifications, and fraud checks. If the logistics API is slow or offline, the entire checkout process stalls for the customer. This system is fragile and impossible to scale individually.
- **Solution:** I implemented a Fan-Out architecture. Now, the checkout process only publishes an "Order Created" event to the SNS. Four different microservices "subscribe" to this topic: the Inventory service (Lambda) updates stock immediately; the Payment service processes the charge; and the Fraud service (which is slower) receives the message through an SQS queue to process at its own pace. If the fraud service fails, the message goes to a DLQ, but the customer already received their purchase confirmation without delay.

---

## 🎯 Learning Objectives

- Design a **Fan-Out** topology for parallel message replication.
- Apply **Subscription Filter Policies** (string and numeric filters) for selective message routing in SNS.
- Integrate SNS with **Amazon SQS** queues to ensure message persistence in long-running processes.
- Utilize **AWS Lambda** for reactive event processing from SNS and SQS.
- Configure **Dead-Letter Queues (DLQ)** within a service chain to increase resilience.
- Monitor the execution of multiple simultaneous services via **Amazon CloudWatch Logs**.

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **Amazon SNS** | Central hub distributing messages to multiple subscribers simultaneously. |
| **Amazon SQS** | Message queuing to ensure slower processes (like fraud analysis) don't lose data. |
| **AWS Lambda** | Workers executing independent business logic. |
| **Amazon CloudWatch** | Monitoring and centralized logging for all microservices. |

---

## 🏗️ Decoupled Fan-Out Architecture

<div align="center">
  <img src="./assets/architecture-sns-sqs-fanout.drawio.png" alt="Fan-Out Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. ⚙️ Resilience Layer (SQS + DLQ)
- **Action:** I created the fraud analysis queue and its respective DLQ.
- **Configuration:** I set the Redrive Policy to 3 attempts before moving the message to the DLQ, ensuring load spikes or temporary failures don't result in lost orders.

### 2. 🛡️ Distribution Hub (SNS)
- **Action:** I created the SNS topic and configured "Subscriptions" for the Lambdas and the SQS queue.
- **Filters:** I configured Filter Policies in the subscription JSON. For example, the fraud queue only receives messages where the `amount` attribute is greater than 500.

### 3. 🔍 Worker Implementation (Lambda)
- **Action:** I developed 4 Lambda functions in Python (Inventory, Payment, Notification, Fraud).
- **Integration:** I configured triggers so the functions would be automatically invoked as soon as the SNS fired the event.
> *Codes available in the [/src](./src/) folder.*

### 4. 🧰 Load and Filter Testing
- **Test:** I published messages to SNS with diverse attributes.
- **Validation:** I verified in CloudWatch that low-value orders did not trigger the fraud Lambda, while expensive orders followed the entire flow, proving the effectiveness of the subscription filters.

---

## 📸 Execution Evidences

### 1. SNS Topic Overview
<img src="./assets/01-sns-topic-overview.png" width="100%">

### 2. SQS Queue Overview (Fraud)
<img src="./assets/02-sqs-queue-overview.png" width="100%">

### 3. DLQ Overview
<img src="./assets/03-sqs-dlq-overview.png" width="100%">

### 4. Subscription Filters
<img src="./assets/04-sns-subscription-filters.png" width="100%">

---

## 💡 Key Learnings

- **Cost-Efficiency with Filters:** Sending all messages to all subscribers is expensive and creates useless processing. Using Filter Policies directly in SNS saves significant compute and billing.
- **Parallel Scalability:** Fan-out allows me to add new services (like a Log Analytics service) just by creating a new subscription, without changing a single line of checkout code.
- **Safety and Isolation:** By placing an SQS queue in front of slow or unstable services (like third-party APIs), I protect the overall application health.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Amazon SNS | ✅ 1 Million publications/month | $0.00 |
| Amazon SQS | ✅ 1 Million requests/month | $0.00 |
| AWS Lambda | ✅ 1 Million invocations/month | $0.00 |
| **Estimated Total** | | **$0.00** |

---

## 🏷️ Competencies Demonstrated

`Amazon SNS` `Amazon SQS` `AWS Lambda` `Fan-Out Pattern` `EDA` `Filter Policies` `Parallel Processing` `🔴 Advanced`

---

## 📜 Certification Alignment

- **DVA-C02:** Domain 1 — Development with AWS Services (Serverless Integration)
- **SAA-C03:** Domain 2 — Design Resilient and Decoupled Architectures

---

[← Return to Index](../../../README-en.md)
