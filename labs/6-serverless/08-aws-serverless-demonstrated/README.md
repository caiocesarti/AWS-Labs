<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 08 — AWS Serverless Demonstrated — Exam Lab na Prática

<p align="center">
  <img src="assets/Serverless.webp" alt="AWS Serverless Demonstrated — Banner" width="100%"/>
</p>

## 🚀 Resumo
Este laboratório é um **Exam Lab prático** onde atuei na correção, configuração e fortalecimento de uma plataforma de e-commerce serverless, enfrentando **7 desafios interdependentes** diretamente no console da AWS. O projeto abrange desde orquestração com Step Functions até segurança com WAF e CI/CD com CodePipeline.

---

## 💼 Caso de Uso Real
- **Indústria:** E-commerce / Varejo
- **Problema:** A arquitetura serverless de um e-commerce recém-lançado apresentou falhas críticas de segurança, funções incompletas no pipeline de deploy, e processos de pagamento não orquestrados adequadamente, causando perda de pedidos e falhas de persistência de carrinho.
- **Solução:** Implementação e correção de uma arquitetura baseada em microsserviços. Foram configurados gateways de API seguros, autenticação via Cognito protegida por WAF, orquestração robusta de pedidos com Step Functions e tabelas DynamoDB, garantindo escalabilidade e resiliência.

---

## 🎯 Objetivos de Aprendizado
*   **Corrigir e aprimorar** pipelines de CI/CD (CodePipeline) para funções Lambda.
*   **Proteger** APIs usando Amazon API Gateway, Amazon Cognito e regras do AWS WAF.
*   **Orquestrar** processos assíncronos e tratamento de falhas com AWS Step Functions.
*   **Isolar** recursos de rede configurando VPCs para funções Lambda.

---

## 🛠️ Serviços AWS Utilizados

| Serviço                   | Papel no Lab                                                |
| ------------------------- | ----------------------------------------------------------- |
| **AWS Lambda**            | 6 funções de domínio (produtos, carrinho, pedidos, notif.). |
| **Amazon API Gateway**    | API REST com integração de proxy e CORS.                    |
| **Amazon Cognito**        | Autenticação e autorização de usuários.                     |
| **AWS WAF**               | Regras gerenciadas de proteção da API contra ataques.       |
| **Amazon DynamoDB**       | Persistência de estado de carrinho e pedidos.               |
| **AWS Step Functions**    | Orquestração assíncrona com tratamento robusto de erros.    |
| **Amazon SQS & SNS**      | Desacoplamento e notificações automáticas de pedidos.       |
| **AWS CodePipeline**      | CI/CD com etapa de aprovação manual.                        |
| **Amazon VPC**            | Isolamento de rede para funções Lambda.                     |

---

## 🖥️ Etapas do Laboratório

### Desafio A: CI/CD com CodePipeline
- Correção de um pipeline incompleto para permitir a atualização contínua e segura de uma função Lambda, utilizando aprovação manual.

### Desafio B: Configuração do API Gateway
- Implementação e configuração completa do Amazon API Gateway, garantindo o roteamento correto (proxy integration) e segurança com CORS.

### Desafio C & D: Segurança com Cognito e WAF
- Configuração do pool de usuários do Amazon Cognito.
- Proteção da API associando o API Gateway ao Cognito para autorização.
- Implementação de ACLs do AWS WAF para bloquear tráfego malicioso antes de atingir as camadas lógicas.

### Desafio E: Persistência de Carrinho
- Correção das políticas IAM e estrutura de partições do Amazon DynamoDB para persistir os itens do carrinho de compras de forma eficiente.

### Desafio F: Orquestração de Pedidos
- Ajuste das máquinas de estado no AWS Step Functions, orquestrando SQS, SNS e DynamoDB para processar os pedidos assincronamente e lidar com falhas.

### Desafio G: Limites de Rede com VPC
- Isolamento de funções Lambda sensíveis colocando-as em uma Amazon VPC, configurando Subnets, Security Groups e NAT Gateways apropriados.

---

## 📸 Evidências de Execução

### Microcredencial Conquistada
<p align="center">
  <img src="assets/serverless-demonstrated.webp" alt="AWS Serverless Demonstrated Badge" width="180"/>
</p>

> [!IMPORTANT]
> A credencial certifica a aprovação no exame prático oficial da AWS Skills Builder.

---

## 💡 Principais Aprendizados
*   **Orquestração supera Coreografia em transações:** O uso do Step Functions garantiu que falhas em etapas do pagamento pudessem ser revertidas de forma estruturada, ao contrário de encadeamentos puros de SQS/SNS.
*   **Segurança em Camadas (Defense in Depth):** A união do WAF mitigando ataques de camada 7 com o Cognito garantindo a identidade mostrou-se essencial para a integridade da API REST.
*   **VPC em Lambdas exige planejamento:** A configuração de rede para Lambdas requer cuidado com tempos de inicialização (Cold Starts) e permissões de ENI corretas.

---

## 🔗 Recursos Adicionais
- [AWS Skill Builder — Microcredentials](https://explore.skillbuilder.aws/learn/public/learning_plan/view/2070/microcredentials)
- [Amazon API Gateway Security](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Lambda | ✅ 1M invocações/mês | $0,00 |
| Amazon API Gateway | ✅ 1M req/mês | $0,00 |
| Amazon DynamoDB | ✅ 25GB, 25 WCU/RCU | $0,00 |
| AWS Step Functions | ✅ 4.000 transições/mês | $0,00 |
| **Total** | | **$0,00** |

---

## 🏷️ Competências Demonstradas

`AWS Lambda` `Amazon API Gateway` `Amazon Cognito` `AWS WAF` `Amazon DynamoDB` `AWS Step Functions` `Amazon SQS` `Amazon SNS` `AWS CodePipeline` `Amazon VPC` `Serverless` `Microservices` `🔴 Avançado`

---

## 📎 Referência

> Este laboratório gerou um artigo aprofundado com o passo a passo técnico:
> **👉 [Artigo: AWS Serverless Demonstrated — Exam Lab na Prática](https://labs.caiocesar.tec.br/2026/06/27/aws-serverless-demonstrated-exam-lab/)**
> 
> *Nota: Este repositório tem fins de estudo e não contém o código proprietário do laboratório da AWS.*

---

[← Voltar ao índice](../../../README.md)
