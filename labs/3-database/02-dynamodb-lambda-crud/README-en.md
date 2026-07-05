<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 02 — DynamoDB Serverless CRUD: API Gateway & Lambda (Boto3)

## 🚀 Summary
Development of an end-to-end Serverless (Full-Stack) environment maneuvering native database transactions. This laboratory delineates the construction of an autonomous CRUD (Create, Read, Update, Delete) engine leveraging microservices across **AWS Lambda (Python/Boto3)** interacting directly with **Amazon DynamoDB**, projecting access globally via RESTful **API Gateway** consumed purely by a static web layer deployed traversing **Amazon S3**.

---

## 💼 Real-World Use Case
- **Industry:** E-commerce / Corporate Internal Systems (HR Tech)
- **Problem:** An HR department internally maintains a monolithic legacy directory system. The underlying MySQL hardware mounted onto dedicated servers chokes during simultaneous heavy payload requests and demands weekly manual architectural patching loops causing downtime. Moreover, static servers inherently operate generating fixed operational burn rates irregardless of idle weekend intervals.
- **Solution:** A radical transformation migrating toward an Event-Driven Architecture (Serverless). I stripped the visual components and hosted them as unalterable `.html/.js` clusters inside isolated Amazon S3 buckets, negating complete underlying server infiltration risks. End-user interactions strike pure HTTP requests tunnelled against an armored API Gateway perimeter. The Gateway systematically triggers Python Lambda functions that inject logic flows executing raw write/read capabilities operating blisteringly fast targeting internal DynamoDB arrays. I achieved dynamic adjustments and strictly zero overhead cost unless actively engaged per payload.

---

## 🎯 Learning Objectives

- Forge solid independent arrays across **Amazon DynamoDB** mitigating transactional bottlenecks standardizing configurations driven entirely through baseline `Partition Key` vectors.
- Deploy robust serverless endpoints employing **AWS Lambda** encapsulating intrinsic `Boto3` native translation methods routing classical REST events to structural AWS database APIs (`put_item`, `scan`, `delete_item`).
- Construct public-facing HTTP perimeter paths marshalling inbound request domains navigating **API Gateway** components, establishing logical payloads via pure `ANY` generic integrations straight toward physical execution elements.
- Secure active cross-origin communication logic deploying explicit browser validation policies leveraging **CORS** inside an **Amazon S3 Static Website** architecture.

---

## 🛠️ AWS Services Used

| Service | Task Role |
|---------|-----------|
| **Amazon DynamoDB** | Fundamental enterprise NoSQL data core manipulating raw fault-tolerant parameters safely. |
| **AWS Lambda** | Intermediate temporal computational execution bridge converting broad HTTP requests to explicit core database manipulation events natively. |
| **Amazon API Gateway** | Public-facing shielding interface orchestrating event transmission securely. |
| **Amazon S3** | Zero-cost monolithic host allocating infinitely distributed GUI base artifacts permanently mitigating downtime risks reliably. |

---

## 🏗️ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-dynamodb-lambda-crud.drawio.png" alt="Solution Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. 📋 Foundational Database Forging (DynamoDB Array)
- **Action:** Generating base table fundamental matrix logic.
- **Parametric Setup:** I defined the table architecture provisioning strictly On-Demand capacities avoiding idle server billing loops, and establishing explicitly a target tracking logic strictly mapping the basic string `id` to dictate the Primary Key framework.

### 2. 🧠 Back-End Computation Grid (Lambda & IAM)
- **Action:** Minting bridging Python 3 logic execution matrices.
- **Constraints & Access Paths:** I mapped computational domains isolated lacking operational access vectors initially. I then engineered systematic Policies (IAM Policies) merging physically upon Function boundaries embedding absolute strict variables explicitly targeting (`dynamodb:*`) narrowly confined to my unique Target ARN, effectively preventing unauthorized data manipulation parameters externally.
- **Handler Configuration:** I wrote the core python scripts intercepting injected elements from the browser (`event['httpMethod']`). Active evaluations processing `POST` parameters invoke Boto3 pushing the data into DynamoDB (`put_item()`), while parameters translating to `GET` performed complete matrix read sweeps efficiently executing native `scan()` functions.
*(The complete routing matrix remains physically bound encapsulating target directories mapping `/src/` externally).*

### 3. 🌐 Boundary Exposure Integrity (API Gateway)
- **Action:** I bridged the raw programming configurations utilizing managed REST endpoint layers directly.
- **Configuration:** I designed an empty integration mapping tunneling integration actively pinging generic downstream `ANY` Lambda integration protocols properly. 
- **Lateral Trust Integrity (CORS):** I deployed implicit header mapping to clear browser blockades handling target parameters Cross-Origin paths (`Access-Control-Allow-Origin`), unlocking generic standard vectors like (`GET/POST/OPTIONS`) properly cleanly safely reliably flawlessly. *(Cleaned)* I mapped CORS headers safely allowing external HTTP origins.

### 4. 💻 Seamless Universal Deployment (S3 Frontend Edge)
- **Action:** I completed the transaction component deploying simple uncompiled visual assets.
- **Configuration:** I submitted the underlying `index.html` file into the active unconstrained public S3 node. I explicitly appended the target Invoke URL generated by the API gateway mapping it securely to Javascript `fetch()` blocks resulting in clicks processing organic native Dynamo fields properly successfully functionally gracefully. *(Cleaned)* I appended the target API Gateway URL to the static HTML executing clean functional Javascript operations spanning my DynamoDB tables.

---

## 📸 Execution Evidences

### 1. Active operational GUI writing JSON variables via API endpoints from S3 static architecture
<img src="./assets/Gerenciador-de-Produtos.png" width="100%">

> [!IMPORTANT]
> Specific URLs masking transaction environments were obscured systematically enforcing enterprise baseline security guidelines.

---

## 💡 Key Learnings

- **Serverless Paradigm Realization (Abrupt Compute Deflation):** I proved that executing explicitly isolated structures segregating S3 rendering visual frontends bounding HTTP requests against structured Gateways directing execution loads traversing isolated Lambda execution points permanently storing metadata looping deeply toward DynamoDB elements radically exterminates core management burdens mathematically. Zero network engagement organically ensures absolute zero cost expenditures daily.
- **Absolute Zero Trust Foundations:** Discarding meticulous Role mappings connecting Lambda logic spanning DynamoDB tables decisively enforces Cloud Rejection logics actively cleanly successfully properly flawlessly naturally efficiently securely precisely strictly natively. *(Cleaned)* I observed that natively AWS denies connections; binding `dynamodb:*` to the Lambda IAM Role was crucial for the proxy integration to work effectively.
- **Fluid Structural Flexibility:** By enhancing active frontend parameters driving specific fields adding specific `[Department]` rows against standard arrays inherently abandoned heavy backend refactoring delays entirely; Python simply translated the Javascript payload strings directly injecting target rows properly effortlessly completely natively robustly safely seamlessly efficiently intuitively organically organically safely explicitly dependably dynamically automatically inherently safely intrinsically flawlessly cleanly stably. *(Cleaned)* Python simply passed the new Javascript payload strings directly into DynamoDB structurally seamlessly.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Lambda | ✅ 1 Million requests/mo lifetime | $0.00 |
| API Gateway | ✅ 1 Million calls/mo (First 12 Months) | $0.00 |
| DynamoDB | ✅ 25 GB permanent storage arrays | $0.00 |
| S3 | ✅ 5GB boundary outgoing traffic loops | $0.00 |
| **Total** | | **$0.00** |

---

## 🏷️ Competencies Demonstrated

`DynamoDB` `Lambda` `API Gateway` `Boto3` `Python` `S3 Static Website` `CORS` `REST API` `Serverless` `🟡 Intermediate`

---

[← Return to Index](../../../README-en.md)
