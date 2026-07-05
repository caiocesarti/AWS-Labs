<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 03 — IAM Security Profile: Architecting S3 Read-Only Analysts

## 🚀 Summary
Security implementation emphasizing the **Least Privilege** principle by limiting an IAM identity exclusively to S3 Read-Only capabilities. In this lab, I validated architectural write blockages and total isolation of other services (like EC2) through cross-access testing. I proved that read policies prevent the user from modifying data or interacting with unauthorized APIs within the AWS account.

---

## 💼 Real-World Use Case
- **Industry:** Data Auditing and Compliance
- **Problem:** A financial company hired an external auditor to verify S3 contracts. The IT team created a generic "PowerUser" account. The auditor accidentally deleted critical files and began scanning EC2 servers, creating security risks.
- **Solution:** I implemented an audited account strictly following the Least Privilege principle. I created the `analyst-s3` user associated only with the `AmazonS3ReadOnlyAccess` policy. Now, any attempt to delete files or access the EC2 panel results in an immediate "Access Denied" block directly from the AWS infrastructure, protecting production data integrity.

---

## 🎯 Learning Objectives

- Consolidate **AWS IAM** mechanics by segmenting access through Users, Groups, and Policies.
- Provision users with **AWS Management Console** access under secure credential processes.
- Apply AWS Managed Policies focused on reading capabilities.
- Validate binary write blockages (upload/delete) using incognito browser sessions.
- Test service isolation (S3 vs EC2) to ensure the user does not "leak" into other dashboards.

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **AWS IAM** | Identity provider and permission logic engine. |
| **Amazon S3** | Target resource used to test read permissions and write blocks. |

---

## 🏗️ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-iam-s3-readonly.drawio.png" alt="Architectural Solution Flow" width="700">
</div>
---

## 🖥️ Lab Steps

### 1. ⚙️ Pre-requisite Bucket Configuration
- **Action:** I provisioned a test S3 bucket and uploaded a simulation file (`TesteLab1.txt`) to serve as the auditing target.

### 2. 🛡️ Identity and Group Structuring
- **Action:** I created the `Analistas-S3` group and attached the `AmazonS3ReadOnlyAccess` policy.
- **Implementation:** I configured the `analista-s3-caiocesar` user with console access and added them to the group, ensuring they inherited the read-only permissions without individual policy assignment.

### 3. 🔍 Stress Tests and Security Auditing
- **Action:** I performed a test login in an incognito window to validate permissions.
- **Results:**
  - **Success:** I navigated the S3 buckets and read the test file perfectly.
  - **Denial:** The console immediately blocked upload attempts (Access Denied) and returned permission errors when I tried to access the Amazon EC2 panel.

---

## 📸 Execution Evidences

### 1. Resource Isolation: Visual proof of the "Access Denied" screen when attempting to view EC2 resources
<img src="./assets/01-iam-user-denied-ec2.png" width="100%">

### 2. Managed Integrity: Blocked upload attempt on S3 validating the ReadOnly policy logic
<img src="./assets/02-s3-upload-test.png" width="100%">

---

## 💡 Key Learnings

- **Management via Groups:** I learned that policies should never be linked directly to an IAM User. Using groups makes permission management cleaner and avoids security residue.
- **Implicit Deny:** In AWS, what is not explicitly allowed is denied. The fact that the user cannot even see the names of EC2 instances proves that AWS's original security shield works by default.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| AWS IAM | ✅ Free | $0.00 |
| Amazon S3 | ✅ Covered by Free Tier (small files) | $0.00 |

---

## 🏷️ Competencies Demonstrated

`AWS IAM` `S3 ReadOnly` `Managed Policies` `Least Privilege` `Security Validation` `🟢 Fundamental`

---

[← Return to Index](../../../README-en.md)
