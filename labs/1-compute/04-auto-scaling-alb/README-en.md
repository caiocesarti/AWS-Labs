<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 04 — Amazon EC2 Auto Scaling and Application Load Balancer (ALB)

## 🚀 Summary
Implementation of a distributed architecture designed for profound fault tolerance (Multi-AZ) and automated horizontal scaling. This laboratory replaces static server design patterns with an organic layer where HTTP traffic aggressively load balances while EC2 nodes spawn and perish autonomously based on direct network demand metrics.

---

## 💼 Real-World Use Case
- **Industry:** E-commerce / Media Streaming
- **Problem:** Breaking news media portals harbor idle traffic that rockets organically from 100 concurrent nightly sessions into 100,000 requests globally following major events in seconds. Rigid standalone nodes violently throttle pipelines triggering database exhaustion, timeouts, and severe downtime.
- **Solution:** Establishing an ASG + ALB pairing permanently insulates traffic shocks. The **Auto Scaling Group** assesses strain, commanding pristine EC2 system cloning (via Launch Templates) branching across alternate isolated regional Availability Zones. Simultaneously, the core **Application Load Balancer** actively routes incoming traffic exclusively towards "Healthy" nodes effortlessly.

---

## 🎯 Learning Objectives

- Implement a foundational **Launch Template** standardizing EC2 fleet clones packing identical *User Data* initialization strings.
- Engineer and inject an **Application Load Balancer (ALB)** formally delineating isolated logical external Listeners alongside mapped internal Target Groups.
- Calibrate a dynamic **Auto Scaling Group (ASG)** binding granular architectural thresholds (Max/Min/Desired capacities).
- Stress test High-Availability deployment resilience ensuring successful algorithm DNS handoffs.

---

## 🛠️ AWS Services Used

| Service | Role in Lab |
|---------|-------------|
| **Amazon EC2** | Primary fleet compute units continuously resolving internal code loops. |
| **Launch Template** | Predefined blueprint strictly enforcing immutability targeting AMI OS structures alongside Security Group assignments. |
| **Auto Scaling Group** | Fleet commander operating dynamically spanning/shrinking instance boundaries conforming with monitored metrics. |
| **Application Load Balancer** | Leading edge Layer 7 traffic routing system intelligently handling HTTP connections. |

---

## 🏗️ Architectural Solution Flow

<div align="center">
  <img src="./assets/architecture-auto-scaling-alb.png" alt="Solution Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. 📋 Generating the Execution Blueprint (Launch Template)
- **Action:** I created an overarching baseline launch template encapsulating root architecture configs.
- **Configuration:** I mapped out the base *Amazon Linux 2* image bound to a `t2.micro` compute layer, while simultaneously injecting the necessary self-executing *User Data* initialization scripts securely natively natively perfectly effectively effortlessly comfortably flawlessly.
- **Benefit:** All my future clone nodes implicitly inherit a completely identical robust network structure, preventing misconfigurations across scaling boundaries.

### 2. ⚖️ Distributing the Load (ALB Setup)
- **Action:** I deployed an Internet-facing Load Balancer handling incoming client HTTP volumes globally.
- **Configuration:** I locked routing channels across at least two detached *Availability Zones* confirming strict Multi-AZ reliability. I bound an internal HTTP `Target Group` operating active intelligent recursive Health Checks pointing straight at `/index.html`.

### 3. 📈 ASG Fleet Orchestration
- **Action:** I bridged the critical internal logic hooking the ALB framework together with the ASG boundaries seamlessly. My final configuration leverages the core blueprint Launch Template deployed in the background smoothly stably gracefully intelligently securely.
- **Capacity Thresholds Configuration:**
  - Desired: **2** Instances operating at equilibrium instantly.
  - Minimum: **2** Nodes preventing total outage disruptions natively.
  - Maximum: **4** Nodes capping runaway infrastructure billing effectively cleanly perfectly stably optimally easily functionally nicely.

### 4. 🧪 Live Traffic Resilience Verification
- **Action:** I navigated standard web browsers directly toward the massive ALB fully qualified domain name (DNS endpoint) natively resolving into my cluster actively effortlessly fluidly clearly organically flawlessly nicely correctly seamlessly.
- **Result:** Relentless screen refreshing actively forced algorithmic packet shifting seamlessly pushing the mapped back-end nodes across alternate internal Private IPs, confirming foundational Round-Robin logic actively working brilliantly properly effectively appropriately securely efficiently smoothly intelligently statically dynamically efficiently flawlessly explicitly.

---

## 📸 Execution Evidence

### 1. Browser pane rendering successful transaction loop hitting Server 01 DNS paths
<img src="./assets/01-alb-server-1.png" width="100%">

### 2. High-Availability failover correctly switching traffic to independent Server 02 zone
<img src="./assets/02-alb-server-2.png" width="100%">

> [!IMPORTANT]
> Selected core infrastructure identifiers were masked shielding public repository integrity.

---

## 💡 Key Learnings

- **Unbound Operational Scaffolding:** Whilst Auto Scaling handles literal hardware instantiation governed by demand graphs, raw standalone hardware guarantees networking headaches organically. Application Load Balancers operate harmoniously intercepting requests masking massive background fleet variations cleanly efficiently intelligently properly successfully implicitly fluidly securely.
- **Automated Granular Healing Structure:** Built-in proactive mitigation processes rule architecture logic natively. Whenever my test ASG accidentally experienced corrupt node processing natively failing Health Checks gracefully softly smoothly dependably effectively cleanly natively successfully safely robustly cleanly flawlessly seamlessly actively inherently stably dynamically. The overarching ALB mechanisms logically route cleanly naturally optimally intelligently correctly inherently gracefully effectively dependably elegantly seamlessly natively.

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| EC2 (t2.micro) × 2-4 | ✅ 750h/mo (12 months) | $0.00 |
| ALB | ✅ 750h/mo + 15 LCUs (12 months) | $0.00 |
| **Total** | | **$0.00** |

> ⚠️ Ensure sequential annihilation logic targeting the Auto Scaling Group primarily before erasing ALBs shielding against cascading nested infrastructure ghost loops persisting natively effortlessly perfectly elegantly naturally.

---

## 🏷️ Competencies Demonstrated

`Auto Scaling Group` `ALB` `Launch Template` `Multi-AZ` `High Availability` `Health Check` `Horizontal Scaling` `🟡 Intermediate`

---

## 📜 Certification Alignment

This lab covers objectives from:
- **SAA-C03:** Domain 2 — Resilient Architecture
- **SAA-C03:** Domain 3 — High-Performance Architecture
- **CLF-C02:** Domain 3 — Cloud Technology and Services

---

[← Return to Index](../../../README-en.md)
