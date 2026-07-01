<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 01 — Create an HR Agent with Amazon Quick

## 🚀 Executive Summary
Building an intelligent HR assistant using **Spaces** and **Custom Chat Agents** features in Amazon Quick. This model demonstrates how Generative AI integrated into Quick can centralize access to corporate documents and automate internal Human Resources support:
- **Spaces as knowledge bases:** Organization of HR documents into searchable, shareable, and reusable collections.
- **Custom agents:** Creation of conversational interfaces with configurable persona, tone, and knowledge sources.
- **Controlled sharing:** Selective distribution of agents with granular permissions (Owner vs Viewer).

---

## 💼 Real-World Use Case
- **Industry:** Human Resources / Corporate Services
- **Problem:** Paulo, HR Director at UmaEmpresa, spends hours weekly searching for information scattered across departmental systems, shared network drives, and emails. When employees ask about policies or benefits, he needs to consult multiple sources for accurate answers. Critical knowledge is trapped in silos and repetitive tasks consume valuable time.
- **Solution:** A custom chat agent in Amazon Quick that automatically queries official HR documents organized in Spaces and returns precise, contextualized answers in natural language, freeing the team for strategic tasks.

---

## 🎯 Learning Objectives

*   Create Amazon Quick **Spaces** and upload documents into them.
*   Test document retrieval with example chat prompts.
*   Create custom chat agents using the **Quick Agent Builder**.
*   Configure the agent's **persona**, **communication style**, and **knowledge sources**.
*   **Share** a custom chat agent with another Quick user.
*   Test an agent and **refine** configuration based on test results.
*   Document how to **maintain and share** a custom chat agent.

---

## 🛠️ AWS Services Used

| Service | Role in the Lab |
|---------|------------|
| **Amazon Quick** | BI platform with unified chat, spaces, and generative AI agents. |
| **Quick Spaces** | Organized collections of searchable documents to feed agents. |
| **Quick Agent Builder** | Interface for creating and customizing chat agents. |
| **Amazon S3** | Storage for workshop materials initial download. |
| **AWS IAM** | User management and access permissions (QuickUser / QuickUser2). |

---

## 🏗️ Solution Architecture

<div align="center">
  <img src="./assets/architecture.png" alt="Solution Architecture" width="700">
</div>

---

## 🖥️ Lab Steps

### 1. 💬 Exploring Quick's Unified Chat
- **Download:** I downloaded the workshop files (`workshop-assets.zip`) from the S3 bucket, containing UmaEmpresa HR documents: employee handbook, leave policy, onboarding checklist, performance review guidelines, holiday calendar, and employee feedback data.
- **Login:** I accessed the Amazon Quick console as `QuickUser`.
- **General knowledge test:** I tested the default system chat (*My Assistant*) in *General knowledge* mode with questions about onboarding best practices.
- **Web search:** I enabled web search to get current trends and validated the cited sources.
- **File upload:** I uploaded `employee_handbook.pdf` directly to the chat session and tested questions about company policies, confirming the agent cited the handbook as its source.

### 2. 📂 Creating and Testing Quick Spaces
- **Space 1 — HR - Company Policies:** I created the space with description `Central repository for company-wide HR policies and procedures` and uploaded: `employee_handbook.pdf`, `leave_policy.pdf`, `performance_review_guidelines.pdf`, `public_holidays.csv`.
- **Space 2 — HR - Operations:** I created the space with description `HR operations data, analytics, and internal procedures` and uploaded: `onboarding_checklist.pdf`, `employee_feedback_full_dataset.pdf`.
- **Testing:** I linked both spaces to the chat and tested with prompts about leave policies, onboarding checklists, and required documentation, confirming the correct sources were referenced.

### 3. 🤖 Creating Custom Chat Agents
- **Agent via Natural Language:** I created the `HR Policy Assistant` agent using a descriptive prompt. Quick automatically generated persona, instructions, and linked the *HR - Company Policies* space. I tested with vacation policy questions and validated that `leave_policy.pdf` was cited as the source.
- **Agent via Builder:** I created the `HR Policy Assistant - Builder` agent manually with detailed persona instructions, a welcome message, and 3 suggested prompts. I linked the space and tested in preview mode.

### 4. 🔗 Sharing and Access Testing
- **Sharing:** I shared the `HR Policy Assistant` agent with user `QuickUser2` with *Viewer* permission.
- **Testing as QuickUser2:** I logged in as `QuickUser2` and tested the agent with the same questions.
- **Troubleshooting:** I identified and resolved the access issue where `QuickUser2` didn't have access to the space linked to the agent — it was necessary to also share the *HR - Company Policies* space with the user.

### 5. 🔧 Refinement and Documentation
- **Refinement:** I added a supplementary instruction to the agent's persona requiring that responses about leave and benefits mention that government laws and regulations supersede company policies.
- **Validation:** I retested and confirmed that all responses now consistently included the legal mention.
- **Documentation:** I used the agent itself to generate maintenance documentation, including: how to add documents to the space, link to official documentation, sharing policy, and testing and update process.

---

## 📸 Execution Evidence

### 1. Amazon Quick Console — home screen with unified chat
<img src="./assets/01-quick-console-home.png" width="100%">

### 2. Chat with employee_handbook.pdf upload — sources correctly cited
<img src="./assets/02-chat-sources-handbook.png" width="100%">

### 3. "HR - Company Policies" Space with 4 documents in Ready status
<img src="./assets/03-space-company-policies.png" width="100%">

### 4. "HR - Operations" Space with 2 documents in Ready status
<img src="./assets/04-space-operations.png" width="100%">

### 5. Agent creation via natural language prompt in Agent Builder
<img src="./assets/05-agent-natural-language-prompt.png" width="100%">

### 6. HR Policy Assistant configuration — persona, knowledge sources and preview
<img src="./assets/06-agent-config-persona.png" width="100%">

### 7. Agent test with sources — leave_policy.pdf referenced via Space
<img src="./assets/07-chat-leave-policy-sources.png" width="100%">

### 8. HR Policy Assistant - Builder with detailed instructions and response preview
<img src="./assets/08-agent-builder-preview.png" width="100%">

### 9. Agent sharing with QuickUser2 (Viewer) — linked resources warning
<img src="./assets/09-share-agent-quickuser2.png" width="100%">

### 10. Access issue resolution — sharing Space with QuickUser2
<img src="./assets/10-share-space-access-fix.png" width="100%">

> [!IMPORTANT]
> Some identifiers have been masked following security best practices.

---

## 💡 Key Learnings

*   **Spaces persist knowledge:** Unlike chat session uploads, Spaces keep documents organized and permanently accessible for multiple agents.
*   **Two ways to create agents:** Natural language prompts generate configurations automatically as a starting point; the Builder offers granular control for manual refinement.
*   **Sharing requires full access:** Sharing an agent isn't enough — linked Spaces also need to be shared with target users.
*   **Iterative refinement:** Persona instructions can be updated at any time to adjust agent behavior based on user feedback.
*   **AI-generated documentation:** The agent itself can generate maintenance documentation, accelerating knowledge transfer.

---

## 🔗 Additional Resources

- [Amazon Quick User Guide](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
- [Amazon Quick FAQs](https://aws.amazon.com/quicksight/resources/faqs/)
- [Amazon Quick Spaces](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-spaces.html)
- [Amazon Quick Chat Agents](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-chat-agents.html)
- [AWS Training and Certification](https://aws.amazon.com/training/)

---

## 💰 Cost Awareness

| Resource | Free Tier? | Estimated Cost |
|----------|-----------|----------------|
| Amazon Quick (Enterprise) | ⚠️ 30-day trial | On-demand |
| S3 (workshop materials) | ✅ 5GB/mo | $0.00 |
| IAM (users) | ✅ Free | $0.00 |
| **Total** | | **Variable** |

> ⚠️ Remember to clean up resources after the lab to avoid charges.

---

## 🏷️ Competencies Demonstrated

`Amazon Quick` `Quick Spaces` `Chat Agents` `Agent Builder` `Generative AI` `RAG` `IAM` `S3` `Sharing & Permissions` `🟢 Fundamental`

---

## 📜 Certification Alignment

This lab covers objectives from:
- **AIF-C01:** Domain 2 — Generative AI Fundamentals
- **AIF-C01:** Domain 3 — Applications of Foundation Models
- **CLF-C02:** Domain 3 — Cloud Technology and Services

---

[← Back to Index](../../../README-en.md)
