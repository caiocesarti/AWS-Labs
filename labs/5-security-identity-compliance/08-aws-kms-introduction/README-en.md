<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 08 â€” Introduction to AWS Key Management Service (KMS)

## ðŸš€ Summary
Controlled Encryption and Traceable Compliance. In this lab, I explored the foundations of **AWS KMS** to protect data at rest. I configured the full lifecycle of a symmetric key (Customer Managed Key), from provisioning to usage monitoring via CloudTrail. I implemented SSE-KMS encryption on S3 buckets, ensuring that only authenticated users with specific permissions could decipher the stored files.

---

## ðŸ’¼ Real-World Use Case
- **Industry:** Healthcare (Hospitals and Insurance)
- **Problem:** A medical records system stored confidential exams in S3 using basic AWS encryption. A compliance audit (HIPAA/GDPR) failed the system because the company had no control over who held the keys and no detailed audit record showing who viewed each exam individually.
- **Solution:** I implemented a **Customer Managed Key (CMK)**. Now, all exam uploads use SSE-KMS linked to this key. This means that besides S3 permission, a doctor must have explicit permission in the KMS Key Policy. Every time an exam is downloaded and decrypted, **AWS CloudTrail** records a `Decrypt` event, providing the exact forensic proof of who accessed sensitive patient data, ensuring full regulatory compliance.

---

## ðŸŽ¯ Learning Objectives

- Create and manage **Customer Managed Keys (CMKs)** with symmetric algorithms.
- Configure **Key Policies** to separate the roles of Key Administrator and Key User.
- Apply **SSE-KMS** encryption to Amazon S3 objects.
- Validate protection effectiveness by attempting to access files via public links (Signature V4).
- Analyze **AWS CloudTrail** logs to audit decryption operations (`Decrypt`).
- Understand the scheduled key deletion process to avoid unnecessary costs.

---

## ðŸ› ï¸ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **AWS KMS** | Management of master keys and encryption policies. |
| **Amazon S3** | Secure object storage with encryption at rest. |
| **AWS CloudTrail** | Auditing and tracking of cryptographic key usage in the account. |

---

## ðŸ—ï¸ Encryption Pipeline Architecture

<div align="center">
  <img src="./assets/architecture-aws-kms-introduction.drawio.png" alt="Encryption Pipeline Architecture" width="700">
</div>

---

## ðŸ–¥ï¸ Lab Steps

### 1. âš™ï¸ Symmetric Key Creation (CMK)
- **Action:** I created the `myFirstKey` in the KMS dashboard.
- **Configuration:** I defined my user as an Administrator (can manage the key) and as a User (can use the key to encrypt/decrypt). This separation is vital in real companies to prevent the IT team from "snooping" on protected data.

### 2. ðŸ›¡ï¸ Secure S3 Upload
- **Action:** I uploaded an image to an S3 bucket.
- **Configuration:** During the upload, I changed the default encryption to **SSE-KMS** and selected the `myFirstKey`. The file was saved at rest already encrypted with my custom security layer.

### 3. ðŸ” Failure Testing and Auditing
- **Action:** I attempted to access the file via a public link by adjusting the object's ACL.
- **Result:** The link failed with a signature error ("Signature Version 4 required"). This proves that even with public S3 access, KMS blocks anyone who lacks the decryption key.
- **Auditing:** I accessed CloudTrail and located the `Decrypt` event. The log displayed my user, the exact timestamp, and the key used, closing the audit cycle.

---

## ðŸ“¸ Execution Evidences

### 1. Key Configuration: Custom key (Customer Managed Key) active and configured in the console
<img src="./assets/KMS.png" width="100%">

### 2. Secure Storage: File in S3 using SSE-KMS encryption linked to my custom key
<img src="./assets/mycloudtrailbucket-S3-bucket-S3.png" width="100%">

### 3. S3 Access Control: Adjusting bucket permissions and ACLs to test encryption barriers
<img src="./assets/mycloudtrailbucket-S3-Acl.png" width="100%">

### 4. Access Testing: Public link access denied due to KMS cryptographic protection
<img src="./assets/Make-objects-public-S3-bucket-mycloudtrailbucket-S3.png" width="100%">

### 5. Forensic Auditing: CloudTrail logs tracking key usage and encryption/decryption events
<img src="./assets/Trails-CloudTrail.png" width="100%">

### 6. Key Permissions: Control panel for key permissions (Admins vs. Users)
<img src="./assets/Key-remove.png" width="100%">

## ðŸ’¡ Key Learnings

- **Key Policies vs. IAM Policies:** I learned that having "AdministratorAccess" in IAM doesn't automatically grant access to a KMS key if it has a restrictive policy. KMS has its own "wall" of permissions.
- **Mandatory Signature:** Files protected by KMS require the application to use valid temporary tokens (SigV4). This effectively kills attacks from leaked internet links.
- **Custom Key Costs:** Unlike standard AWS-managed keys (`aws/s3`), custom keys cost $1/month. Therefore, it's essential to delete them after laboratory testing.

---

## ðŸ’° Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| AWS KMS (Custom Key) | âŒ Monthly fee for active keys | ~$1.00/month |
| Amazon S3 (Storage) | âœ… Included in Free Tier | $0.00 |

> âš ï¸ **Important Warning:** I scheduled the KMS key for deletion immediately after the lab. AWS imposes a minimum 7-day waiting period before a key is permanently deleted to prevent accidental data loss.

---

## ðŸ·ï¸ Competencies Demonstrated

`AWS KMS` `Customer Managed Keys` `SSE-KMS` `S3 Encryption` `AWS CloudTrail` `Signature V4` `ðŸŸ¡ Intermediate`

---

[â† Return to Index](../../../README-en.md)
