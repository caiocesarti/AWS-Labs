<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 03 — Exploring Amazon Bedrock Playgrounds

## 🚀 Executive Summary
In this hands-on lab, the focus was on evaluating Artificial Intelligence models using **Amazon Bedrock Playgrounds**. The practice involved testing, comparing responses across multiple foundation models, adjusting inference parameters (hyperparameters), and utilizing prompt management to create reusable templates with variables, simulating a secure and controlled environment.

---

## 💼 Real-World Use Case
- **Industry:** Customer Service / Generative AI
- **Problem:** A company's business team wants to find the best AI model to enhance their chat-based customer service experience. However, they lack a clear evaluation method and need to thoroughly compare different foundation models (supporting both text and images) to provide optimal interactions with customers.
- **Solution:** Using Amazon Bedrock as the central orchestrator. Through the *Compare Mode* in the Playgrounds, the team can test and evaluate models in parallel, tweak creativity hyperparameters (such as Temperature and Top P), and manage reusable *Prompts*, ensuring the selection of the most suitable and cost-effective model.

---

## 🎯 Learning Objectives
*   **Evaluate** AI models using the Amazon Bedrock Playgrounds.
*   **Tweak and apply** inference hyperparameters through the AWS visual interface.
*   **Compare** the responses of different text models side-by-side by enabling the compare mode.
*   **Create and manage** reusable *prompts* containing systemic variables and tests.
*   **Publish** immutable versions using Prompt Management.

---

## 🛠️ AWS Services Used

| Service                       | Role in the Lab                                                           |
| ----------------------------- | ------------------------------------------------------------------------- |
| **Amazon Bedrock**            | Central orchestrator and environment to explore, test, and compare LLMs.  |

---

## 🏗️ Solution Architecture

<p align="center">
  <img src="assets/01-architecture.png" alt="Bedrock Lab Architecture" width="800">
</p>

As illustrated, the flow involves **Amazon Bedrock** acting as the orchestration platform:
1. **Explore and Assess:** Users test multiple AI models simultaneously.
2. **Prompts and Tests:** Centralized management of *Prompts*, connecting them to the invoked models.

---

## 🖥️ Lab Steps

### 1. Playground and Hyperparameter Tuning
- Initial navigation through the Chat-based Playgrounds.
- Generating detailed responses with the model (e.g., requesting explanations about AI and hyperparameters).
- Tuning and understanding inference parameters:
  - **Temperature:** Adjusted to control the level of randomness/creativity of the response.
  - **Top P and Top K:** Used to refine probabilities when choosing the next words.
  - **Maximum output tokens:** Configured to allow extensive responses (e.g., 65535).

<p align="center">
  <img src="assets/02-playground.png" width="600">
</p>
<p align="center">
  <img src="assets/03-hyperparameters.png" width="600">
</p>

### 2. Compare Mode
- Enabled the Bedrock compare environment, which splits the interface to support side-by-side testing.
- Sent identical *prompts* to two different models (e.g., Nova 2 Lite and Llama 3) to observe differences in accuracy, formatting, and cohesion during customer service simulations.

<p align="center">
  <img src="assets/04-compare-mode.png" width="600">
</p>

### 3. Prompt Builder and Management
- Built a systemic prompt in the Bedrock *Prompt builder* to act as an assistant (e.g., `CustomerServiceDemo`).
- Defined strict behavioral instructions (*"Create a 5-turn conversation between a friendly customer service agent..."*).
- Introduced **variables** (e.g., `{{product}}`) for dynamic and flexible testing.

<p align="center">
  <img src="assets/05-prompt-management.png" width="600">
</p>
<p align="center">
  <img src="assets/06-prompt-variables.png" width="600">
</p>
<p align="center">
  <img src="assets/07-prompt-test.png" width="600">
</p>

### 4. Version Publishing
- Tested the behavior practically by passing values to the variable (e.g., replacing `{{product}}` with `laptop`).
- Saved the *draft* and successfully published an immutable version (*Version 1*), ready to be used programmatically by applications.

<p align="center">
  <img src="assets/08-prompt-version.png" width="600">
</p>
<p align="center">
  <img src="assets/09-final-result.png" width="600">
</p>

---

## 💡 Key Learnings
*   **Hyperparameters are game-changers:** The simple adjustment of *Temperature* and *Top-P* can turn a focused, analytical model into a highly creative and flexible one, proving that testing is essential before production deployment.
*   **Compare Mode is vital for ROI:** Bedrock makes it easy to compare not just the quality, but the technical feasibility between a high-cost model and a lightweight/open model for solving simpler tasks.
*   **Prompt Management as infrastructure:** Managing prompt versions independently of application code allows you to update AI behavior without requiring complex backend deployments.

---

## 💰 Cost Awareness

| Resource | Base Price | Estimation |
|----------|------------|------------|
| Amazon Bedrock (Playgrounds) | Pay per millions of tokens (e.g., Claude, Nova, Llama) | Very low ($0.05 - $0.50 for exploratory testing). |
| Prompt Management | Free to manage (you pay for model inference) | $0.00 |
| **Estimated Total** | | **<$1.00** |

> *Note: Foundation model pricing on Bedrock varies widely depending on the chosen model (Nova, Claude 3, Llama, Titan, etc).*

---

## 🏷️ Competencies Demonstrated

`Amazon Bedrock` `Generative AI` `LLM Evaluation` `Prompt Engineering` `Prompt Management` `Hyperparameters Tuning` `🟢 Foundational`

---

## 🔗 References

- [AWS Skill Builder](https://explore.skillbuilder.aws/)

---

[← Back to Index](../../../README-en.md)
