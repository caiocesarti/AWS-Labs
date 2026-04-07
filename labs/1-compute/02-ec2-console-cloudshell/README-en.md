<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 02 — Exploring AWS with Amazon EC2

## 🚀 Summary
Automated infrastructure provisioning (`IaaS`) utilizing graphical (Console) and programmatic (CloudShell/CLI) approaches. The lab demonstrates that a targeted web server launch achieves identical parameter integrity regardless of establishing configurations via iterative interface clicking or directly compiling native Bash arguments (Base64 wrapper).

---

## 💼 Real-World Use Case
- **Industry:** Systems Engineering / DevOps
- **Problem:** Developers must iterate through dozens of disposable test instances per week to experiment with code packages. Conducting this manually through the console consumes 15 minutes each iteration, fueling mortal errors like omitting security rules or boot scripts.
- **Solution:** Embracing the AWS CloudShell as a CLI bastion abstracts away the graphical layers. Issuing a consolidated `aws ec2 run-instances` string containing base64 enclaved User Data ensures exact replication of target environments within raw seconds, locking infrastructure as an auditable codepath.

---

## 🎯 Learning Objectives

- **Provision EC2 instances** natively utilizing the AWS Console.
- Configure HTTP reachability over the web targeting **Security Groups**.
- Instantiate and harness a **Key Pair** ensuring tight remote authentication properties.
- Automate bootstrap initialization routines purely leveraging **User Data** directives.
- Engage the **AWS CloudShell** subsystem provisioning compute power dynamically from CLI APIs.
- Comprehend and navigate the granular instance lifecycle down to safe destruction operations.

---

## 🛠️ AWS Services Used

| Service | Role in Lab |
|---------|-------------|
| **Amazon EC2** | Foundational computational capacities targeting scalable architectures (Virtual Servers). |
| **AWS CloudShell** | Pre-authenticated browser-based secure shell explicitly translating bash inputs dynamically addressing the AWS CLI system. |
| **Amazon VPC** | Logical hosting envelope where isolation rules inherently process all structural traffic behaviors natively. |

---

<div align="center">
  <img src="./assets/architecture-ec2-console-cloudshell.drawio.png" alt="Solution Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. 🖱️ EC2 via Console (Graphical Interface)
- **Action:** I manually provisioned a traditional `t2.micro` server operating an Amazon Linux 2 AMI core.
- **Configuration:** I generated standard `.pem` *Key Pairs* and systematically adjusted the primary Security Group to permit `HTTP` interactions (Port 80 Inbound).
- **Automation:** I injected a customized `User Data` bash script to automatically install and start the `httpd` daemon upon instance launch.
> 💡 *Validation:* After reaching 2/2 status checks, accessing the Public IP in a browser renders the "Hello from your web server!" page.

### 2. 💻 EC2 via AWS CloudShell (Command Line System)
- **Action:** By completely bypassing the visual environment, I opened up the CloudShell container properly utilizing dynamic authentication keys effectively.
- **Configuration:** I issued precise API arguments to establish a custom Security Group, configure port 80 rules, and launch the EC2 instance via the CLI.
- **CLI Automation:** Recognizing that standard script blocks can be complex to pass via CLI parameters, I encoded the User Data script into a `Base64` payload, ensuring a flawless injection into the `run-instances` command.
> 📄 **See exact script and syntax parameters:** [src/cloudshell-commands.sh](./src/cloudshell-commands.sh).

### 3. 🧹 Systematic Resource Eradication (Cleanup)
- **Primary Goal:** I terminated both the `webserver` and `instance-cli` EC2 instances to stop ongoing compute costs.
- **Secondary Goal:** I deleted the matching Security Groups once the instances were fully terminated.

---

## 📸 Execution Evidence

### 1. Successful browser load displaying the web output response
<img src="./assets/01-browser-validation.png" width="100%">

### 2. Two distinct resources generated via Console and CloudShell channels
<img src="./assets/02-instances-running-useu2.png" width="100%">

### 3. In-depth parameters confirming the "Running" status of the instances
<img src="./assets/03-instances-running.png" width="100%">

### 4. Termination process confirming the correct cleanup of resources
<img src="./assets/04-instances-terminated.png" width="100%">

### 5. Active terminal inputs used in CloudShell to generate instances dynamically
<img src="./assets/05-cloudshell-cli.png" width="100%">

### 6. Overview panel showing the coexisting server structures
<img src="./assets/07-instances-overview.png" width="100%">

---

## 💡 Key Learnings

- **Provisioning Flexibility:** I demonstrated that AWS supports both guided manual actions and programmatic terminal-based infrastructure invocation.
- **Bootstrapping Power:** Injecting configuration via _User Data_ removes the need for manual post-deployment setup, ensuring instances are operational upon launch.
- **Network Isolation:** I verified that public access requires explicit security group rules, as AWS defaults to a secure "deny-all" inbound posture.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| EC2 (t2.micro) × 2 | ✅ 750h/mo (12 months) | $0.00 |
| CloudShell | ✅ Free | $0.00 |
| **Total** | | **$0.00** |

---

## 🏷️ Competencies Demonstrated

`EC2` `CloudShell` `AWS CLI` `Security Groups` `User Data` `Key Pairs` `Base64 Encoding` `Bash Scripting` `🟢 Fundamental`

---

## 📜 Certification Alignment

This lab covers objectives from:
- **CLF-C02:** Domain 3 — Cloud Technology and Services
- **DVA-C02:** Domain 1 — Development with AWS Services

---

[← Return to Index](../../../README-en.md)
