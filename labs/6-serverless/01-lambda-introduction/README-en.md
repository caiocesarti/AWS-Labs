<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 01 â€” Introduction to AWS Lambda: Serverless Image Processing

## ðŸš€ Summary
Event-Driven Data Processing: In this lab, I explored the *Serverless* compute capabilities of AWS using **AWS Lambda**. I designed an autonomous architecture where uploading an image to an **Amazon S3** bucket automatically triggers a **Python 3.12** function. Using the **Pillow** library, the function resizes the image to create a thumbnail and stores it in a second destination bucket, all without the need to manage any servers.

---

## ðŸ’¼ Real-World Use Case
- **Industry:** E-commerce and Media Portals
- **Problem:** On a shopping site, users uploaded product photos that reached up to 10 MB. The site needed to display small thumbnails for the catalog, but the main application server slowed down when processing these images synchronously, affecting the browsing experience for all customers.
- **Solution:** I decoupled image processing using **AWS Lambda** by integrating an S3 bucket to act as an event trigger. Now, as soon as a photo is saved, the Lambda wakes up, generates the thumbnail in milliseconds, and saves it in an output bucket. The main application server is free to focus only on sales, while image processing scalability becomes infinite and extremely cheap, as I pay only for the exact execution time of each resize.

---

## ðŸŽ¯ Learning Objectives

- Create **AWS Lambda** functions using the Python 3.12 runtime.
- Configure automatic triggers based on **Amazon S3** events.
- Handle files in real-time using the **Pillow** library within the Serverless environment.
- Manage granular access permissions via **IAM Roles** (Read from source S3 and Write to destination S3).
- Utilize Lambda's ephemeral `/tmp/` storage for temporary file processing.
- Monitor executions and debug errors via **Amazon CloudWatch Logs**.

---

## ðŸ› ï¸ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **AWS Lambda** | Python code execution for image resizing. |
| **Amazon S3** | Storage for source buckets (raw photos) and destination (thumbnails). |
| **Amazon CloudWatch** | Metric monitoring and execution log retention. |
| **AWS IAM** | Execution role definition with least privilege permissions. |

---

## ðŸ“ Project Architecture

<div align="center">
  <img src="./assets/architecture-lambda-introduction.drawio.png" alt="Project Architecture" width="700">
</div>

---

## âš™ï¸ Implementation Phases

### Phase 1 â€” Storage Preparation (S3)
- **Action:** I created two buckets: `images-original-66f` and `images-resized-66f`.
- **Purpose:** To isolate the input environment from the output, preventing an infinite loop where the Lambda would resize its own thumbnail.

### Phase 2 â€” Function Development (Lambda)
- **Action:** I created the `CreateThumbnail` function and configured the IAM Role.
- **Implementation:** I developed the script in Python using the `boto3` SDK. Since the `Pillow` library is not native to Lambda, I prepared a deployment package (.zip) containing the necessary dependencies for image processing.

### Phase 3 â€” Trigger Configuration
- **Action:** I added an "S3 Event Notification" trigger to the Lambda.
- **Filter:** I configured it to fire only on `s3:ObjectCreated:*` events and optionally for specific extensions, ensuring the function is not invoked by unnecessary files.

### Phase 4 â€” Testing and Validation
- **Action:** I uploaded a high-resolution image and monitored the CloudWatch Logs.
- **Result:** I validated that the destination bucket received the reduced version of the image instantly, with the log confirming the successful processing.

---

## ðŸ“¸ Execution Evidences

### 1. Preparation (S3): Creation of source and destination buckets
<img src="./assets/S3-buckets.png" width="100%">

### 2. Function Creation: Initialization of the `CreateThumbnail` Lambda
<img src="./assets/Create-Thumbnail-Functions-Lambda.png" width="100%">

### 3. Creation Success: Confirmation of Lambda creation and dashboard visibility
<img src="./assets/Create-Thumbnail-Functions-Lambda-sucess.png" width="100%">

### 4. Basic Settings Edit: Configuration of execution timeout and memory limits
<img src="./assets/Edit-basic-settings-Create-Thumbnail-Functions-Lambda.png" width="100%">

### 5. Runtime and Role: Defining S3-compatible IAM execution permissions
<img src="./assets/Edit-runtime-settings-Create-Thumbnail-Functions-Lambda.png" width="100%">

### 6. Package Deployment: Uploading the code .zip hosted on S3 with external libraries (Pillow)
<img src="./assets/Functions-Lambda-Upload-from-s3.png" width="100%">

### 7. Trigger Configuration: Event associated with image PUT on the source bucket
<img src="./assets/Add-triggers-Lambda.png" width="100%">

### 8. Test Execution: JSON Event Payload simulating an S3 PUT
<img src="./assets/Test-Thumbnail-Functions-Lambda.png" width="100%">

### 9. Invocation Monitoring: Real-time graphs covering Lambda invocations and errors
<img src="./assets/Monitor-Thumbnail-Functions-Lambda.png" width="100%">

### 10. Success/Output: Thumbnail successfully generated and saved by the code
<img src="./assets/images-28032026-resized-S3-bucket-S3.png" width="100%">

### 11. Visual Comparison: Original Image vs. Generated Thumbnail

**Original Image:**
<img src="./assets/HappyFace.jpg" width="100%">

**Processed Upload (Thumbnail):**
<img src="./assets/HappyFace%20(1).jpg" width="100%">

---

### 12. Log Traceability: Stream history of environments triggered by the Lambda
<img src="./assets/CloudWatch-log.png" width="100%">

### 13. Performance Analysis: Confirmation of execution time and billed memory duration
<img src="./assets/CloudWatch-log-events.png" width="100%">

## ðŸ’¡ Key Learnings

- **Event-Driven vs. Polling:** Instead of having a server checking for new files (polling), the Event-Driven architecture reacts only when the event occurs. This eliminates wasted resources and costs for idle servers.
- **Using /tmp/:** I learned that Lambda offers a temporary file system. It is essential to download the image to this directory, process it, and then send it to the destination, as we cannot manipulate the image "in the air" directly in memory in some file processing cases.
- **JSON Event Structure:** Lambda receives the file coordinates (bucket and key), not the file itself. Understanding how to navigate the JSON object sent by S3 is fundamental to the function's success.

---

## ðŸ’° Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| AWS Lambda | âœ… 1 Million free requests/month | $0.00 |
| Amazon S3 | âœ… Up to 5GB in Standard storage | $0.00 |
| **Estimated Total** | | **$0.00** |

---

## ðŸ·ï¸ Competencies Demonstrated

`AWS Lambda` `Amazon S3` `Event-Driven Automation` `Serverless Computing` `Python Boto3` `CloudWatch` `ðŸ”´ Advanced`

---

## ðŸ“œ Certification Alignment

- **CLF-C02:** Domain 3 â€” Technology (Serverless Cloud Computing)
- **DVA-C02:** Domain 1 â€” Development with AWS Services

---

[â† Return to Index](../../../README-en.md)