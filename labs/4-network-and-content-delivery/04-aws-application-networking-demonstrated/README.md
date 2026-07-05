<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 04 — AWS Application Networking Demonstrated — Exam Lab na Prática

<p align="center">
  <img src="assets/AWS Application Networking.webp" alt="AWS Application Networking Demonstrated — Banner" width="100%"/>
</p>

## 🚀 Resumo
Este laboratório é um **Exam Lab prático** onde diagnostiquei, corrigi e configurei uma infraestrutura de aplicação de múltiplas camadas em um ambiente real da AWS. Enfrentei **7 desafios interdependentes** envolvendo a criação de uma arquitetura de *service mesh* moderna utilizando o Amazon VPC Lattice, CloudFront, ALB, ECS e API Gateway.

---

## 💼 Caso de Uso Real
- **Indústria:** Tecnologia / Serviços Web
- **Problema:** Uma aplicação web legada de suporte (Service Desk) estava sofrendo com problemas de comunicação entre microsserviços, falhas de segurança na borda, interrupções no tráfego do frontend e monitoramento inadequado. A comunicação entre o frontend e a API de backend não estava roteando corretamente devido a regras de segurança e integração complexa.
- **Solução:** Implementação de uma rede de *service mesh* robusta com Amazon VPC Lattice para facilitar a descoberta de serviços. Proteção da borda com CloudFront e WAF. Correção da comunicação do ALB e ECS, garantindo a resiliência e a visibilidade do tráfego com logs de acesso e alarmes do CloudWatch.

---

## 🎯 Objetivos de Aprendizado
*   **Proteger** a infraestrutura web utilizando Amazon CloudFront e regras do AWS WAF.
*   **Corrigir e escalar** serviços containerizados executando no Amazon ECS por trás de um Application Load Balancer.
*   **Configurar** redes de serviços (*service mesh*) com o Amazon VPC Lattice para descoberta nativa e comunicação segura entre subnets.
*   **Monitorar** e gerar alarmes pró-ativos utilizando o Amazon CloudWatch e Amazon SNS.

---

## 🛠️ Serviços AWS Utilizados

| Serviço                        | Papel no Lab                                                              |
| ------------------------------ | ------------------------------------------------------------------------- |
| **Amazon CloudFront**          | CDN e camada de entrada pública, protegendo a origem (ALB).               |
| **AWS WAF**                    | Regras de proteção web associadas à distribuição CloudFront.              |
| **Application Load Balancer**  | Direcionamento do tráfego de entrada para os clusters ECS.                |
| **Amazon ECS**                 | Execução de microsserviços: `servicedesk-frontend` e `servicedesk-api`.   |
| **Amazon VPC Lattice**         | *Service mesh* gerenciado, conectando as VPCs de frontend e backend.      |
| **Amazon API Gateway**         | Exposição pública de APIs com integração via *proxy*.                     |
| **AWS Lambda**                 | Função de proxy que intermedeia o API Gateway e o VPC Lattice.            |
| **Amazon DynamoDB**            | Banco de dados NoSQL de backend, acessado de forma privada.               |
| **Amazon VPC**                 | Isolamento de rede multi-camadas (subnets públicas e privadas) e SGs.     |
| **Amazon CloudWatch & SNS**    | Coleta de métricas e disparo de alarmes para falhas no serviço.           |
| **Amazon S3**                  | Armazenamento seguro para logs de acesso do balanceador de carga.         |

---

## 🖥️ Etapas do Laboratório

### Desafio A: Configuração de CloudFront para Produção
- Configuração de uma distribuição CloudFront apontando para o Application Load Balancer como origem.
- Associação de regras do AWS WAF para bloquear tráfego malicioso na borda.

### Desafio B: Saúde do ALB e Escalonamento no ECS
- Correção das verificações de saúde (*health checks*) no Target Group do ALB.
- Atualização e escalonamento dos serviços do Amazon ECS para garantir alta disponibilidade.

### Desafio C: Segurança em Múltiplas Camadas
- Refatoração dos *Security Groups* para permitir tráfego estrito entre CloudFront, ALB, VPC Lattice e as tarefas do ECS.

### Desafio D: Service Mesh com VPC Lattice
- Criação e configuração de uma rede de serviços do Amazon VPC Lattice.
- Registro dos serviços frontend e backend, simplificando a descoberta sem regras complexas de roteamento ou peering.

### Desafio E: Integração API Gateway e Lattice
- Resolução de problemas na integração do Amazon API Gateway com a rede interna do VPC Lattice, utilizando o AWS Lambda como proxy.

### Desafio F: Monitoramento e Alarmes
- Criação de alarmes no Amazon CloudWatch baseados em anomalias e erros 5XX.
- Configuração de tópicos no Amazon SNS para notificar a equipe em caso de falhas.

### Desafio G: Logs de Acesso
- Habilitação da retenção e envio de *Access Logs* do ALB para um *bucket* centralizado no Amazon S3, permitindo futuras auditorias.

---

## 📸 Evidências de Execução

### Microcredencial Conquistada
<p align="center">
  <img src="assets/AWS Application Networking Demonstrated.webp" alt="AWS Application Networking Demonstrated Badge" width="180"/>
</p>

> [!IMPORTANT]
> A credencial certifica a aprovação no exame prático oficial da AWS Skills Builder.

---

## 💡 Principais Aprendizados
*   **VPC Lattice simplifica redes complexas:** Ao invés de lidar com dezenas de tabelas de roteamento e regras de VPC Peering, o VPC Lattice forneceu conectividade consistente na camada 7, tornando o *service mesh* mais natural.
*   **Alinhamento estrito de Security Groups:** O fluxo de requisição desde o CloudFront -> ALB -> ECS requer que os *Security Groups* das instâncias alvo referenciem explicitamente o Security Group de origem para garantir a política de privilégio mínimo.
*   **Visibilidade de ponta a ponta:** Ligar os logs de acesso no ALB para o S3 é um passo não apenas de auditoria, mas essencial para diagnosticar *timeouts* entre microsserviços.

---

## 🔗 Recursos Adicionais
- [AWS Skill Builder — Microcredentials](https://explore.skillbuilder.aws/learn/public/learning_plan/view/2070/microcredentials)
- [Amazon VPC Lattice Documentation](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html)
- [Application Load Balancer Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| Amazon CloudFront | ✅ 1TB out/mês | $0,00 |
| Amazon API Gateway | ✅ 1M req/mês | $0,00 |
| AWS Lambda | ✅ 1M invocações/mês | $0,00 |
| Amazon VPC Lattice | ❌ Pago por req. e tempo | ~$1,50/mês |
| Application Load Balancer | ❌ Pago por LCU e tempo | ~$16,00/mês |
| **Total Estimado** | | **~$17,50** |

---

## 🏷️ Competências Demonstradas

`Amazon CloudFront` `AWS WAF` `ALB` `Amazon ECS` `Amazon VPC Lattice` `AWS Lambda` `Amazon API Gateway` `Amazon DynamoDB` `Amazon VPC` `Amazon CloudWatch` `Amazon SNS` `Amazon S3` `🔴 Avançado`

---

## 📎 Referência

> Este laboratório gerou um artigo aprofundado com o passo a passo técnico:
> **👉 [Artigo: AWS Application Networking Demonstrated — Exam Lab na Prática](https://labs.caiocesar.tec.br/2026/06/28/aws-application-networking-demonstrated-exam-lab/)**
> 
> *Nota: Este repositório tem fins de estudo e não contém o código proprietário do laboratório da AWS.*

---

[← Voltar ao índice](../../../README.md)
