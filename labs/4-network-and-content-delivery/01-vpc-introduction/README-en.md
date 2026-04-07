<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 01 â€” Introduction to Amazon Virtual Private Cloud (VPC)

## ðŸš€ Summary
Asynchronous Messaging and Distributed Resilience: In this lab, I implemented the core foundations of cloud infrastructure: Virtual Private Networks. I provisioned a logically isolated **Amazon VPC**, segmenting the environment into Public (Web/Proxy) and Private Subnets (Database). I configured granular connectivity layers through an **Internet Gateway (IGW)**, **Route Tables**, and a dedicated **NAT Gateway** to ensure secure, unidirectional internet access without exposing the internal backend.

---

## ðŸ’¼ Real-World Use Case
- **Industry:** Banking Sector / Digital Healthcare
- **Problem:** An operational hospital migrated core electronic medical records into standard cloud resources utilizing publicly assigned default subnets. Without isolation, foreign malicious traffic systematically hijacked explicit routing paths subjecting the raw database arrays to brute force scanning, ultimately compromising instance data integrity on open ports.
- **Solution:** A radical transformation deploying isolated *Network Segmentation*. I routed complete internal flow controls through a custom mapped Amazon VPC configuration specifically pushing critical payload data targets deep into *Private Subnets*, functionally blocking public IP assignment capabilities. Since instances required patch update cycles downloading globally, I mandated isolated proxy communication by allocating a decoupled *NAT Gateway* processor natively stationed inside an exterior *Public Subnet*. This fused explicitly with security groups permanently suppressing inbound hostile access.

---

## ðŸŽ¯ Learning Objectives

- Construct solid physical underlying independent infrastructural Amazon VPC perimeters mapping strict origin CIDR Base blocks (e.g., `10.0.0.0/16`).
- Distribute app workloads dividing virtual nodes segmenting structural isolation boundaries addressing **Public** and **Private** subnets.
- Decode static path mappings routing boundary access endpoints configuring standard **Internet Gateway (IGW)** hardware.
- Engineer internal routing patterns bifurcating dynamic pathways via unique mapping **Route Tables**.
- Authorize unidirectional reverse connectivity orchestrating instances unexposed directly pulling backend proxies mapping through **NAT Gateways**.
- Identify logic controls bounding static peripheral evaluations via subnet **Network ACLs** and core stateful bounds spanning **Security Groups**.

---

## ðŸ› ï¸ AWS Services Used

| Service               | Task Role                                                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Amazon VPC**        | Massively scalable highly tailored environment effectively recreating datacenter boundaries cleanly within the AWS cloud.     |
| **VPC Subnets**       | Sub-divisions explicitly restricting overarching CIDR block networks separating Public internet bounds from internal paths.   |
| **Internet Gateways** | Perimeter physical hardware bridging open translation streams directly mapping internal architectures natively externally.    |
| **NAT Gateways**      | Unidirectional shielding endpoints processing outbound traffic and repelling open inbound connection loops correctly.         |
| **Route Tables**      | Algorithmic logic mapping path directives dictating flow routing parameters properly among attached isolated core components. |

---

## ðŸ—ï¸ Architectural Solution Flow

<div align="center">
  <img src="./assets/Diagrama-1.png" alt="Infrastructure Diagram - Part 1" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-2.png" alt="Infrastructure Diagram - Part 2" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-3.png" alt="Infrastructure Diagram - Part 3" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-4.svg" alt="Infrastructure Diagram - Part 4" width="700">
</div>

---

## ðŸ–¥ï¸ Lab Steps

### 1. ðŸ“‹ Controlled Instantiation tracking VPC Wizard Deployments
- **Action:** Guided configuration array orchestrating logical topographies natively.
- **Parametric Setup:**
  - Network Flag (Tag): `Lab-vpc`
  - Overarching Output Root CIDR Payload: `10.0.0.0/16`
  - Core Availability Zone Constraint: `1`
  - Total External Edge Arrays (*Public Subnets*): `1` (CIDR boundaries targeting `10.0.25.0/24`)
  - Target Core Internal Matrices (*Private Subnets*): `1` (CIDR boundaries targeting `10.0.50.0/24`)
- **Action:** I provisioned the architecture using an assisted method to ensure the correct topology. AWS automatically allocated the `Internet Gateway (IGW)` and initialized the `NAT Gateway` instances in a single operation, streamlining the manual configuration process.

### 2. ðŸ” Forensic Architectural Inspection (Isolated Arrays)
- **Defining Critical Routing Flow Pathways (Route Tables):**
  - Extracting core active dashboard validation parameters, I verified precise explicit routing targeting my *Public Route Table* constraints. Outgoing generic requests (`0.0.0.0/0`) linked cleanly routing traffic inherently bounding out toward the mapped `igw-*` hardware.
  - Investigating the separated *Private Route Tables*, I identified explicit override pathways directly redirecting `0.0.0.0/0` proxy arrays pushing blind target loops reliably mapping the static endpoint node `nat-*`.
- **Fortified Perimeter Matrices (Network ACLs):** I mapped generic stateful boundary components isolating underlying endpoints comprehensively enforcing security correctly.

---

## ðŸ“¸ Execution Evidences

### 1. Lab-VPC Topology: Active monitoring loop visualizing the generated topographies mapping target boundaries actively
<img src="./assets/vpcs-VPC-Console.png" width="100%">

### 2. Master CIDR: Deep core inspection array executing distinct parametric base CIDR allocations dynamically
<img src="./assets/VPC-us-west-2.png" width="100%">

### 3. Subnet Segmentation: Identify core operational isolation boundaries mapping precise variables crossing public and private arrays securely
<img src="./assets/subnets-VPC-Console.png" width="100%">

### 4. Routing Tables: Path execution mapping traffic targets isolating outbound logic outputs optimally
<img src="./assets/VPC-us-west-2-route-table.png" width="100%">

### 5. NAT Gateway: Passive hardware securely mitigating structural reverse inbound attack schemas smoothly
<img src="./assets/NatGateways-VPC-Console.png" width="100%">

### 6. Regional Matrix: Regional geographic view configuring subnet logic efficiently securely cleanly
<img src="./assets/VPC-us-west-2-03-25.png" width="100%">
> [!IMPORTANT]
> Associated network string parameters masking critical identifiers were intentionally omitted reinforcing baseline zero-trust baseline safety.

---

## ðŸ’¡ Key Learnings

- **Subnet Definition Matrix Architecture:** I learned that a "Public Network" natively avoids merely adopting nominal tags. Operationally, subnets derive strict parameters intrinsically by binding associations driven directly mapping explicit `Internet Gateway (IGW)` path constraints to the respective Route Tables exclusively.
- **NAT Bridge Execution Logic:** Engineered physical NAT frameworks securely locking down external exposure. I validated that isolated private Database instances traverse external updates completely securely. They receive massive payloads safely fetching proxy external nodes yet bypassing inherently open external incoming traffic limits completely protecting backend states effectively.

---

## ðŸ’° Cost Awareness

| Resource                            | Free Tier?                                                                                                                                                | Estimated Cost                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Amazon VPC Core Matrices            | âœ… Core network blocks processing passive tables natively cost zero                                                                                        | $0.00/mo                                     |
| Internet Gateway Bridges            | âœ… Static arrays crossing IGW mapping processes incur zero base charges                                                                                    | $0.00/mo                                     |
| **NAT Gateway Processors**          | âŒ Continuous billing framework actively running regardless of bandwidth data processed ($0.045/h passive bound + Data mapping limits routing dynamically) | **~$1.08/Daily Fixed**                       |
| **Absolute Fixed Logic Projection** |                                                                                                                                                           | **$32.40/Monthly Fixed Projection Baseline** |

> [!CAUTION]  
> I consistently delete target components explicitly purging `NAT Gateway` endpoints because they inherently drain core billing quotas universally regardless of active network operation bounds. Floating "Elastic IPs" mapped implicitly during setup demand explicit manual teardowns safely circumventing runaway passive structural costs rapidly.

---

## ðŸ·ï¸ Competencies Demonstrated

`VPC` `Subnets` `NAT Gateway` `Internet Gateway` `Route Tables` `Multi-AZ` `Network ACLs` `Security Groups` `Network Segmentation` `ðŸŸ¢ Fundamental`

---

## ðŸ“œ Certification Alignment

This path dictates baseline network logic mirroring native assessments evaluating:
- **CLF-C02:** Domain 3 â€” Cloud Technology and Services
- **SAA-C03:** Domain 2 â€” Resilient Dependable Architecture Constraints
- **SAA-C03:** Domain 1 â€” Secure Network Architectures

---

[â† Return to Index](../../../README-en.md)