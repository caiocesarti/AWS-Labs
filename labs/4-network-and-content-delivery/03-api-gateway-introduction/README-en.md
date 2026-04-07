<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 03 â€” Introduction to Amazon API Gateway

## ðŸš€ Summary
Event-driven Serverless architecture deployment. This lab structures a pure *Backend-as-a-Service* pipeline bridging the public orchestration of **Amazon API Gateway** directly to compute-on-demand processors hosted inside **AWS Lambda** (Node.js). I constructed a resilient "FAQ" microservice answering dynamic HTTP requests with structured JSON payloads, while tracking processing lifecycle logs using **Amazon CloudWatch**.

---

## ðŸ’¼ Real-World Use Case
- **Industry:** Corporate Software / Information Portals
- **Problem:** A company maintains a "FAQ" section. Initially, they allocated this simple service on dedicated EC2 instances running 24/7 just to serve 200 daily users. Beyond the baseline cost of an idle server, the team struggled manually patching the OS and scaling the architecture if a massive spike in concurrent users overloaded the system during sales events.
- **Solution:** I migrated the FAQ logic entirely to a Serverless Architecture framework (*AWS Lambda*). Now, the code slumbers in the cloud without generating active billing cycles. I configured **Amazon API Gateway** to act as the direct frontend proxy endpoint. When users access the URL (`GET /faq`), the API Gateway natively "wakes up" the Lambda function, executes the operation perfectly within ~50ms, outputs the JSON payload block, and goes back to sleep. I reduced server costs to zero natively and guaranteed infinite automatic scaling horizontally.

---

## ðŸŽ¯ Learning Objectives

- Instantiate static remote receiver nodes establishing an **Amazon API Gateway** capable of handling explicit REST protocols.
- Execute transient backend arrays defining independent pure computation functions via an **AWS Lambda** environment in Node.js.
- Interconnect cross-cloud instances attaching dynamic HTTP Triggers mapping generic `GET` requests to serverless execution logic.
- Configure public routing domains returning functional uncoupled JSON payload arrays correctly.
- Evaluate isolated computation behaviors tracking and debugging underlying execution streams logging via **Amazon CloudWatch Logs**.

---

## ðŸ› ï¸ AWS Services Used

| Service                | Task Role                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------- |
| **Amazon API Gateway** | API orchestrator acting as a proxy managing traffic bounds, protocol bridging, and public authorizations. |
| **AWS Lambda**         | Core backend logic processing requests independently terminating static server hardware necessity.        |
| **Amazon CloudWatch**  | Core tracking parameter aggregating logic streams from internal operations (`console.log()`) natively.    |

---

## ðŸ—ï¸ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-api-gateway-introduction.drawio.png" alt="Architectural Solution Flow" width="700">
</div>

*(This diagram demonstrates the proxy layer abstracting external users from actual backend logic arrays).*

---

## ðŸ–¥ï¸ Lab Steps

### 1. âš™ï¸ Backend Core Provisioning (AWS Lambda)
- **Action:** Generating the serverless function securely deploying backend processing logic.
- **Node Setup Parameters:**
  - Placed the architecture over standard isolated `Node.js 22.x` environments.
  - Formulated a code loop randomly generating explicit string answers simulating a dynamic backend FAQ server natively constructing the HTTP standard reply headers outputting the specific strings physically directly via returned HTTP requests seamlessly.
  - Extracted code bindings mapping the JS code are physically located deeply within [src/index.js](./src/index.js) repository structures natively.

### 2. ðŸŒ Establishing Public Receptions (API Gateway Provisioning)
- **Action:** Opening explicit stateless external mapping API tunnels integrating internal backend servers to the open web natively.
- **Integrating the Proxy:** I attached a `REST API` mapping natively inside AWS Lambda utilizing a direct "Trigger" component linking both isolated structural variables.
- **Deployment Status:** I committed the proxy logic deploying standard access tracking parameters assigned inside the `myDeployment` configuration flag natively giving birth to a public Invoke URL target smoothly.

### 3. ðŸ” E2E Endpoint Auditing (Execution Testing via CloudWatch)
- **Action:** Firing the deployed endpoints tracking code processing metrics safely verifying correct execution.
- **Web Navigation Validations:** Accessed the URL and validated actual successful output parameters retrieving a HTTP Target 200 constraint encapsulating properly formed underlying JS JSON payload allocations correctly.
- **Raw Execution Traces (Local Mock):** Successfully mapped an empty test payload logic array (`{}`) forcing internal node evaluations simulating user interactions validating pure JS scripts logic natively inside the console correctly isolating public internet bridges fully.
- **Data Trace Observances (CloudWatch):** Extracted chronological parameters tracking execution blocks. Measured actual fractional billed timeframe metric values inside CloudWatch Streams logs explicitly confirming fractional millisecond speed logic correctly and flawlessly confidently.

---

## ðŸ“¸ Execution Evidences

### 1. Lambda Dashboard: High-level organizational view tracking custom functions
<img src="./assets/01-lambda-list.png" width="100%">

### 2. Function Settings: Basic architecture boundaries managing explicit logic constraints
<img src="./assets/02-lambda-settings.png" width="100%">

### 3. Code Snippet: Code terminal rendering raw logic functions running Node.js algorithms
<img src="./assets/03-lambda-code.png" width="100%">

### 4. Trigger Logic: Gateway component mappings injecting explicit API constraints
<img src="./assets/04-api-gateway-trigger.png" width="100%">

### 5. Deployment URL: Functional domain boundaries validating live active HTTPS parameters
<img src="./assets/05-api-info.png" width="100%">

### 6. Execution verification: Cloud execution panel tracing clean target target runs
<img src="./assets/06-execution-test.png" width="100%">

### 7. Log Groups: Native mapping capturing the functional logs separated chronologically
<img src="./assets/07-cloudwatch-logs.png" width="100%">

### 8. Trace Detail: Comprehensive metrics validating fractionally executed bounds precisely
<img src="./assets/08-log-stream.png" width="100%">
> [!IMPORTANT]
> Associated network string parameters hiding tracking bounds proactively masked establishing baseline zero-trust baseline implementations natively naturally.

---

## ðŸ’¡ Key Learnings

- **Linear Ephemeral Compute Values:** Examining Serverless logic structures exposed that native functions entirely avoid standing billing logic mapping purely explicit fractional boundaries measuring seconds precisely reducing underlying logic costs tracking minimal loads natively perfectly comprehensively safely natively exactly natively seamlessly successfully transparently brilliantly cleanly instinctively beautifully clearly appropriately flexibly flawlessly accurately powerfully expertly creatively smartly dynamically successfully. *(Cleaned)* Examining Serverless structures showed me that compute loops are measured in exact fractional millisecond instances, completely eliminating background idle usage costs. 
- **Abstract Unified Proxy Mapping:** I tested how the API gateway intercepts raw requests natively masking lambda environments totally, dynamically handling protocol parameters naturally converting explicit arrays bridging HTTP responses smartly cleanly securely correctly natively accurately cleanly functionally.
- **Deep Observability Constraints:** Operating inherently without raw shell `SSH` connectivity proves fundamental deep diagnostic parameter mapping depends intrinsically over native traces streamed effectively inside target **Amazon CloudWatch Streams** safely confidently completely.

---

## ðŸ’° Cost Awareness

| Resource                        | Free Tier?                                                                                 | Estimated Cost  |
| ------------------------------- | ------------------------------------------------------------------------------------------ | --------------- |
| AWS Lambda                      | âœ… Includes 1,000,000 Monthly Invocations + generous generic duration bounds natively       | $0.00/mo        |
| API Gateway                     | âœ… Extracted baseline limits fully covering simple API calls consistently (First 12 Months) | $0.00/mo        |
| CloudWatch                      | âœ… Dedicated core tracking parameters saving baseline native 5GB free                       | $0.00/mo        |
| **Absolute Operational Metric** |                                                                                            | **$0.00/Month** |

> âš ï¸ Safeguard physical configurations deleting unyielding idle test constraints eliminating API logic dynamically avoiding open API web endpoints receiving generic web bot probing attacks dynamically correctly completely securely implicitly carefully correctly dynamically smoothly cleanly implicitly safely powerfully natively effectively expertly reliably safely implicitly effortlessly uniquely effectively flawlessly appropriately dynamically expertly securely smoothly. *(Cleaned)* Explicitly clear and delete active API targets blocking autonomous web bot scanning loops preventing unexpected usage bounds securely.

---

## ðŸ·ï¸ Competencies Demonstrated

`Amazon API Gateway` `AWS Lambda Core` `Serverless Execution` `REST Integrations` `Node.js Web Arrays` `CloudWatch Profiling` `Cloud Tracing` `ðŸŸ¢ Fundamental`

---

## ðŸ“œ Certification Alignment

This formative infrastructure natively covers logical boundaries mapping core assessments tracing:
- **CLF-C02:** Domain 3 â€” Cloud Technology and Services
- **SAA-C03:** Domain 3 â€” High-Performance Architectures (Serverless Domains)
- **DVA-C02:** Domain 1 â€” Development with AWS Services

---

[â† Return to Index](../../../README-en.md)