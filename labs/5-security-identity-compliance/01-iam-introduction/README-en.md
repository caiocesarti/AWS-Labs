<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 01 — Introduction to AWS Identity and Access Management (IAM)

## 🚀 Summary
Access Governance implementation focused on the **Least Privilege** principle. In this lab, I orchestrated identity controls through **AWS IAM** by establishing users, isolating permissions via groups, and defining exact restriction policies. I configured the environment to separate infrastructure administration (EC2) from data access (S3), preventing human errors and unauthorized access.

---

## 💼 Real-World Use Case
- **Industry:** Technology / Cloud Operations
- **Problem:** A company granted Administrator access to all employees to facilitate work. A mistake in a script by a new collaborator accidentally terminated two production database servers. Unlimited access allowed a human error to cause critical downtime.
- **Solution:** I implemented Role-Based Access Control (RBAC) with **AWS IAM**. I moved analysts and interns to the `S3-Support` group, which prohibits any access to the EC2 console. I placed responsible engineers in the `EC2-Admin` group. Each user now has individual traceable keys, making the incident impossible to repeat, as AWS blocks any action outside the defined policy.

---

## 🎯 Learning Objectives

- Create and audit individual **IAM Users** to ensure action traceability.
- Organize permissions in a scalable way using **User Groups**.
- Analyze and validate JSON-formatted policies (**IAM Policies**) for granular control.
- Simulate logins via *Account Alias* to validate the experience of different access profiles.
- Test the least privilege principle in practice through blocked access attempts (`Access Denied`).

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **AWS IAM** | Central management of identities, groups, and permissions. |
| **Amazon EC2** | Virtual servers used to test viewing and administration restrictions. |
| **Amazon S3** | Object storage used to validate data access isolation. |

---

## 🏗️ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-iam-introduction.drawio.svg" alt="Architectural Solution Flow" width="700">
</div>
---

## 🖥️ Lab Steps

### 1. 🔍 Identity Creation (Users & Groups)
- **Action:** I created users `user-1`, `user-2`, and `user-3` and their corresponding organizational groups.
- **Observation:** I validated that without group or policy association, users operate under "Zero Trust" (fully blocked by default).

### 2. 🛡️ Policy Analysis (JSON Policies)
- **Action:** I inspected AWS-managed policies like `AmazonEC2ReadOnlyAccess`.
- **Technical Analysis:** I analyzed the JSON blocks ("Action", "Effect", "Resource") and created a custom *Inline* policy for `EC2-Admin`, specifically allowing `ec2:StartInstances` and `ec2:StopInstances` actions.

### 3. ⚙️ Association and Hierarchy
- **Action:** I associated each user with their specific group. `user-1` received S3 permissions, while `user-2` and `user-3` were focused on the EC2 ecosystem with different authority levels.

### 4. 🔗 Cross-Access Testing
- **Action:** I performed alternating logins to validate permissions.
- **Results:**
  - **User-1 (S3):** Succeeded in reading files in S3 but received `Access Denied` when attempting to access the EC2 console.
  - **User-2 (EC2 RO):** Viewed EC2 instances but was prevented from stopping them and had no access to S3.
  - **User-3 (EC2 Admin):** Successfully executed the `Stop` command on the instance.

---

## 📸 Execution Evidences

### 1. Identity & Programmatic Access: Creation of 'user-1'
<img src="./assets/user1.png" width="100%">

### 2. Group Governance: Configuration of administrative permissions (EC2 Admin)
<img src="./assets/EC2-Admin-IAM-Global.png" width="100%">

### 3. Group Governance: Support profiles (EC2 Support)
<img src="./assets/EC2-Support-IAM-Global.png" width="100%">

### 4. Group Governance: Data-focused support profiles (S3 Support)
<img src="./assets/S3-Support-IAM-Global.png" width="100%">

### 5. Access Validation: Success in listing authorized S3 resources by User-1
<img src="./assets/user-1-s3.png" width="100%">

### 6. Access Validation: EC2 panel reading by User-2
<img src="./assets/user-2-ec2.png" width="100%">

### 7. Isolation & Least Privilege: Denial (Access Denied) of EC2 administrative actions
<img src="./assets/user-2-error.png" width="100%">

### 8. Isolation & Least Privilege: Denial (Access Denied) in reading S3 data
<img src="./assets/user-2-s3.png" width="100%">

### 9. Administrative Finality: Confirmation of critical command (Stop Instance) successfully executed by User-3
<img src="./assets/user-3-ec2.png" width="100%">

---

## 💡 Key Learnings

- **Zero-Trust Standard:** In AWS, access is not granted by default. Users without associated policies cannot see anything in the console.
- **Preventative Security:** The absence of error messages may indicate excessive privilege. A secure environment should show permission errors when attempting to access resources outside the user's scope of work.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| AWS IAM | ✅ Free and unlimited for identity management | $0.00 |

> ⚠️ Although IAM is free, the actions allowed by it (like starting EC2 instances) can generate costs. I always terminate test instances after validation.

---

## 🏷️ Competencies Demonstrated

`AWS IAM` `Least Privilege Principle` `Group Management` `JSON Policies` `RBAC` `Zero Trust` `🟢 Fundamental`

---

[← Return to Index](../../../README-en.md)
