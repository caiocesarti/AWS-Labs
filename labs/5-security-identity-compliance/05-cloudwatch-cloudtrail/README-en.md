<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 05 — Cloud Observability & Security: CloudWatch + CloudTrail + SNS

## 🚀 Summary
Infrastructure Telemetry and Forensic Governance. In this lab, I established a native observability environment in AWS. I configured structural alarms to monitor CPU usage in EC2 instances undergoing stress load testing. In parallel, I enabled a comprehensive activity tracker using **AWS CloudTrail**, ensuring every API call in the account is logged and exported to an S3 bucket with encryption.

---

## 💼 Real-World Use Case
- **Industry:** Site Reliability Engineering (SRE) and Operational Systems
- **Problem:** An e-commerce platform suffered from silent crashes overnight. Web servers hit 100% CPU lockouts, yet the engineering team only discovered the outages hours later through customer complaints. Additionally, they couldn't identify if a failed script or a specific user performed manual changes to the network.
- **Solution:** I implemented a dual-axis defensive strategy. I configured **Amazon CloudWatch** to track CPU levels. If usage passes 70% for 5 minutes, it triggers an email alert via **Amazon SNS**, notifying me on my phone in real-time. For auditing, I enabled **AWS CloudTrail** to record all management events in S3. Now, I can pinpoint why the server failed and who initiated the changes in seconds.

---

## 🎯 Learning Objectives

- Create telemetry alarms in **CloudWatch** tracking hardware metrics (`CPUUtilization`).
- Orchestrate automatic email notifications using **Amazon SNS** topics.
- Enable and configure **AWS CloudTrail** for continuous auditing of account management events.
- Perform synthetic stress tests on Linux instances to validate alarm activation.
- Store audit logs securely and permanently in an **Amazon S3** bucket.

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **Amazon CloudWatch** | Real-time metric tracking and alarm orchestration. |
| **AWS CloudTrail** | Forensic API tracer archiving account activity metadata. |
| **Amazon SNS** | Messaging service for dispatching email alerts. |
| **Amazon EC2** | Target Linux server for executing load tests. |
| **Amazon S3** | Long-term repository for storing encrypted CloudTrail JSON logs. |

---

## 🏗️ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-cloudwatch-cloudtrail.drawio.png" alt="Solution Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. ⚙️ Deploying EC2 Telemetry
- **Action:** I provisioned a Linux instance and created a CloudWatch alarm.
- **Rules:** If CPU levels exceed 70% for 5 consecutive minutes, the state changes to `In Alarm`. I linked an SNS topic so I receive an email notification immediately upon triggering.

### 2. 🛡️ Synthetic Load Test (CPU Spike)
- **Action:** I accessed the instance via SSH and installed the `stress` utility.
- **Command:** I initiated the command `stress --cpu 8 --timeout 600` to force maximum hardware processing.
- **Validation:** I monitored the CloudWatch graph hit 100% and confirmed receiving the diagnostic email alarm within minutes.

### 3. 🔍 Activating the Governance Trail (CloudTrail)
- **Action:** I enabled CloudTrail globally across the account.
- **Configuration:** I created a management "Trail" to record all API calls or console interactions. I routed the logs to a dedicated S3 bucket, ensuring logs are compressed and immutable for forensic long-term storage.

---

## 📸 Execution Evidences

### 1. Creating the alarm in CloudWatch
<img src="./assets/01-create-alarm-cloudwatch.png" width="100%">

### 2. Selecting CPU metrics for the alarm
<img src="./assets/02-select-metric-alarms-cloudwatch.png" width="100%">

### 3. Graphed metrics visualization
<img src="./assets/03-select-metric-alarms-graphed-metrics.png" width="100%">

### 4. Specifying the target metric (CPUUtilization)
<img src="./assets/04-specify-metric.png" width="100%">

### 5. Defining conditions and threshold (>70%)
<img src="./assets/05-conditions.png" width="100%">

### 6. Configuring notification actions (SNS)
<img src="./assets/06-configure-actions.png" width="100%">

### 7. Alarm name and details
<img src="./assets/07-add-alarm-details.png" width="100%">

### 8. Preview and final alarm creation
<img src="./assets/08-preview-and-create.png" width="100%">

### 9. Creating the audit trail in CloudTrail
<img src="./assets/09-create-trail-cloudtrail.png" width="100%">

### 10. Selecting log event types
<img src="./assets/10-choose-log-events.png" width="100%">

### 11. Review and trail creation
<img src="./assets/11-review-and-create.png" width="100%">

### 12. Active trails panel in CloudTrail
<img src="./assets/12-trails.png" width="100%">

### 13. SNS topic subscription confirmation
<img src="./assets/13-subscription-confirm-sns.png" width="100%">

### 14. "In Alarm" state triggered in CloudWatch
<img src="./assets/14-in-alarm.png" width="100%">

### 15. SNS notification successfully dispatched
<img src="./assets/15-notification-sns.png" width="100%">

### 16. Alert email received confirming the trigger
<img src="./assets/16-alarm-email-received.png" width="100%">

---

## 💡 Key Learnings

- **Host vs. OS Metrics:** CloudWatch monitors what AWS "sees" outside the instance (CPU, Network, Disk Read/Write). To monitor internal metrics like RAM usage, I learned that installing the `CloudWatch Agent` is required.
- **Automated Alarms:** Alarms serve more than humans; they can act as triggers for Lambda functions to automatically stop compromised instances or scale environments as usage peaks.
- **Long-term Compliance:** While CloudTrail retains event history for 90 days by default, exporting logs to S3 allows for years of record-keeping, essential for regulatory compliance and deep investigations.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Amazon CloudWatch | ✅ 10 free alarms included | $0.00 |
| AWS CloudTrail | ✅ First continuous Trail setup is free | $0.00 |

---

## 🏷️ Competencies Demonstrated

`AWS CloudWatch` `AWS CloudTrail` `Amazon SNS` `CPU Metrics` `Log Auditing` `Stress Testing` `🟡 Intermediate`

---

[← Return to Index](../../../README-en.md)
