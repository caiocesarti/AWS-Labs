<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 07 — S3 Event Notifications with Amazon SNS and SQS

## 🚀 Summary
Event-Driven Auditing and Storage Notifications: In this lab, I implemented a reactive architecture to monitor and audit changes in an **Amazon S3** bucket. I configured S3 to trigger **Event Notifications** whenever an object was created or deleted, sending these signals to an **Amazon SNS Topic**. The notification hub simultaneously distributed the data to an email alert and an **Amazon SQS** queue, which served as a persistent buffer for future auditing. I focused on configuring **Resource-Based Policies** for secure communication and formatting data using **Raw Message Delivery** between services.

---

## 💼 Real-World Use Case
- **Industry:** Data Governance and Information Security
- **Problem:** An entertainment company stores valuable assets (videos, audios) in S3 buckets. Recently, files were accidentally deleted, and no one knew by whom or when. The security team needed immediate alerts for critical cases and a persistent log of all operations for forensic analysis, without paying for expensive third-party monitoring or manual API polling.
- **Solution:** I implemented native S3 triggers. Now, the instant a file is uploaded or deleted, the infrastructure reacts. The CISO receives an automatic email alert via SNS, and all operation metadata is injected into an "immutable" SQS queue, where an auditing system can process logs at its own pace, ensuring no file modification goes unnoticed.

---

## 🎯 Learning Objectives

- Configure **S3 Event Notifications** to react to `s3:ObjectCreated` and `s3:ObjectRemoved` triggers.
- Provision and integrate an **Amazon SNS Topic** for parallel event distribution (Fan-out).
- Implement an **Amazon SQS queue** as a durable destination for event auditing.
- Master writing **Resource-Based Policies (JSON)** to authorize services (S3 and SNS) to interact.
- Enable **Raw Message Delivery** in SNS to ensure the payload reaches the SQS queue without unnecessary metadata headers.
- Validate full file traceability from upload to final email alert and queue log.

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **Amazon S3** | Event source monitoring object creation and deletion. |
| **Amazon SNS** | Messaging bus notifying multiple destinations (Email and SQS). |
| **Amazon SQS** | Durable, asynchronous repository for audit log retention. |
| **AWS IAM** | Access policies to ensure secure integration. |

---

## 🏗️ Event-Driven Architecture Flow

<div align="center">
  <img src="./assets/architecture-s3-sns-sqs-events.drawio.png" alt="S3 + SNS + SQS Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. ⚙️ Messaging Infrastructure
- **Action:** I provisioned the `notificacoes-s3` SNS topic and the `fila-eventos-s3` SQS queue.
- **Configuration:** I subscribed both my email and the SQS queue to the SNS topic to receive events simultaneously.

### 2. 🛡️ Security and Permissions (JSON Policies)
- **Action:** I updated the SNS and SQS Access Policies.
- **JSON:** I inserted statements explicitly allowing the S3 bucket to publish messages to the SNS topic and the SNS topic to send messages to the SQS queue, following the least privilege principle using ARNs.

### 3. 🔍 S3 Trigger Configuration
- **Action:** I accessed the bucket properties and enabled "Event Notifications".
- **Filter:** I chose the `All object create events` and `All object removal events` event types, pointing the destination to the SNS topic created earlier.

### 4. 🧰 Operational Validation
- **Simulation:** I uploaded a test image to the bucket.
- **Result:** I received the email alert within seconds and used the "Send and receive messages" feature in SQS to see the JSON payload containing the filename, size, and source IP.

---

## 📸 Execution Evidences

### 1. Alert Received via Email (SNS)
<img src="./assets/01-s3-email-notification.png" width="100%">

### 2. Payload Received in Queue (SQS)
<img src="./assets/02-sqs-message-received.png" width="100%">

---

## 💡 Key Learnings

- **Active S3 Participation:** I learned that storage doesn't have to be passive; it can drive complex automations without servers running polling scripts.
- **Raw Message Delivery Importance:** I understood that formatting payloads as "Raw" when sending to SQS makes it much easier for downstream systems to process, as they don't have to strip the SNS XML envelope.
- **Resource-Based Policies Security:** I reinforced the practice that in AWS, access isn't guaranteed by connection alone, but by explicit policies authorizing Service A to "write" to Service B using their ARNs.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Amazon S3 | ✅ Standard bucket actions (5GB) | $0.00 |
| Amazon SNS | ✅ 1 Million free notifications/month | $0.00 |
| Amazon SQS | ✅ 1 Million free requests/month | $0.00 |
| **Estimated Total** | | **$0.00** |

---

## 🏷️ Competencies Demonstrated

`S3 Events` `Amazon SNS` `Amazon SQS` `JSON Policies` `Data Auditing` `🔴 Advanced`

---

## 📜 Certification Alignment

- **DVA-C02:** Domain 1 — Development with AWS Services (Event Triggers)
- **SAA-C03:** Domain 2 — Design Resilient Architectures (Decoupling and Notification)

---

[← Return to Index](../../../README-en.md)
