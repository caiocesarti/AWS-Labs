<div align="center">
  <img src="./assets/banner.png" alt="AWS Cloud Labs" width="100%"/>

  <br/>

  ![Labs](https://img.shields.io/badge/labs-29-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
  ![Domains](https://img.shields.io/badge/domains-6-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
  ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
  ![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
  ![CI](https://img.shields.io/github/actions/workflow/status/caiocesarti/AWS-Labs/validate.yml?style=flat-square&logo=github&label=CI)

  <p>
    <a href="./README-en.md">🇺🇸 English</a> &nbsp;|&nbsp;
    <a href="./README.md">🇧🇷 Português</a>
  </p>
</div>

---

## Sobre

Repositório com laboratórios práticos de AWS organizados por domínio de produto. Cada lab documenta o provisionamento, os scripts utilizados e evidências de validação. Em expansão contínua.

---

## Domínios cobertos

| Domínio                  | Labs | Tecnologias                                     |
| ------------------------ | ---- | ----------------------------------------------- |
| ⚡ Serverless             | 7    | Lambda, API Gateway, SNS, SQS, DLQ, EventBridge |
| 🔒 Segurança & Compliance | 8    | IAM, STS, KMS, CloudWatch, CloudTrail, SSM      |
| 🌐 Rede & Entrega         | 3    | VPC, CloudFront, API Gateway                    |
| 📦 Storage                | 4    | S3, EBS, Bucket Policy, Lifecycle, DLM          |
| 🗄️ Database               | 3    | DynamoDB, LSI, GSI, Boto3                       |
| 🖥️ Compute                | 4    | EC2, Elastic Beanstalk, Auto Scaling, ALB       |

---

## Labs

### ⚡ Serverless

| #   | Lab                                                                        | Descrição                                                     | Nível           |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------- |
| 01  | [Introdução ao AWS Lambda](./labs/6-serverless/01-lambda-introduction/)    | Redimensionamento automático de imagens com Triggers S3       | 🔴 Avançado      |
| 02  | [Lambda Aliases + API Gateway](./labs/6-serverless/02-lambda-api-gateway/) | Isolamento de estágios dev/prod com aliases e `$LATEST`       | 🟡 Intermediário |
| 03  | [Lambda + EventBridge](./labs/6-serverless/03-lambda-eventbridge/)         | Scheduler cron para desligamento automático de instâncias EC2 | 🔴 Avançado      |
| 04  | [Lambda + S3 + API Gateway](./labs/6-serverless/04-lambda-s3-game/)        | Web app full-stack serverless — jogo de adivinhação           | 🟡 Intermediário |
| 05  | [SNS + SQS + DLQ](./labs/6-serverless/05-sns-sqs-dlq/)                     | Pub/Sub com isolamento de falhas via Dead-Letter Queue        | 🟡 Intermediário |
| 06  | [Fan-Out SNS → SQS](./labs/6-serverless/06-sns-sqs-fanout/)                | Topologia fan-out com filtros de mensagem por atributo        | 🔴 Avançado      |
| 07  | [S3 Event Notifications](./labs/6-serverless/07-s3-sns-sqs-events/)        | Auditoria disparada por eventos nativos de bucket             | 🔴 Avançado      |

### 🔒 Segurança, Identidade e Compliance

| #   | Lab                                                                                         | Descrição                                                              | Nível           |
| --- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------- |
| 01  | [Introdução ao AWS IAM](./labs/5-security-identity-compliance/01-iam-introduction/)         | Gestão de usuários, grupos e políticas de acesso (least privilege)     | 🟢 Fundamental   |
| 02  | [AWS STS: Credenciais Temporárias](./labs/5-security-identity-compliance/02-aws-sts/)       | `AssumeRole` programático para acesso sem credenciais permanentes      | 🟢 Fundamental   |
| 03  | [IAM: S3 ReadOnly](./labs/5-security-identity-compliance/03-iam-s3-readonly/)               | Least privilege com Managed Groups para acesso restrito                | 🟢 Fundamental   |
| 04  | [AWS Budgets](./labs/5-security-identity-compliance/04-aws-budgets/)                        | Controle de gastos com alertas por threshold via e-mail                | 🟢 Fundamental   |
| 05  | [CloudWatch + CloudTrail](./labs/5-security-identity-compliance/05-cloudwatch-cloudtrail/)  | Monitoramento de EC2 em carga + auditoria de API calls                 | 🟡 Intermediário |
| 06  | [SSM Parameter Store + KMS](./labs/5-security-identity-compliance/06-ssm-parameter-store/)  | Gestão de segredos com criptografia AES-256 via KMS                    | 🟡 Intermediário |
| 07  | [Auditoria Básica de Ambiente](./labs/5-security-identity-compliance/07-aws-basic-audit/)   | Análise de IAM, VPC Security e auditoria de logs no CloudTrail/S3      | 🟡 Intermediário |
| 08  | [AWS KMS: Gestão de Chaves](./labs/5-security-identity-compliance/08-aws-kms-introduction/) | Ciclo de vida de chaves simétricas, SSE-KMS e auditoria com CloudTrail | 🟡 Intermediário |

### 🌐 Rede e Entrega de Conteúdo

| #   | Lab                                                                                      | Descrição                                         | Nível         |
| --- | ---------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------- |
| 01  | [Amazon VPC](./labs/4-network-and-content-delivery/01-vpc-introduction/)                 | Subnets públicas/privadas, NAT Gateway, IGW e AZs | 🟢 Fundamental |
| 02  | [Amazon CloudFront](./labs/4-network-and-content-delivery/02-cloudfront-introduction/)   | CDN com distribuição via Edge Locations           | 🟢 Fundamental |
| 03  | [Amazon API Gateway](./labs/4-network-and-content-delivery/03-api-gateway-introduction/) | Microsserviço serverless com integração Lambda    | 🟢 Fundamental |

### 📦 Storage

| #   | Lab                                                                    | Descrição                                                                             | Nível           |
| --- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------- |
| 01  | [S3: Introdução e Políticas](./labs/2-storage/01-s3-introduction/)     | Bucket Policies (JSON), Controle de Acesso Público (BPA) e Recovery via Versionamento | 🟡 Intermediário |
| 02  | [S3: Advanced Management](./labs/2-storage/02-s3-advanced-management/) | Versionamento, Lifecycle, Pre-signed URLs e Server Access Logs                        | 🟢 Fundamental   |
| 03  | [S3: Basic & Advanced](./labs/2-storage/03-s3-basic-advanced/)         | Automação de storage class e URLs temporárias                                         | 🟢 Fundamental   |
| 04  | [EBS: Volumes e Snapshots](./labs/2-storage/04-ebs-mount-snapshots/)   | Mount ext4 via CLI e políticas de retenção com DLM                                    | 🟡 Intermediário |

### 🗄️ Database

| #   | Lab                                                                                   | Descrição                                                          | Nível           |
| --- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------- |
| 01  | [Introduction to Amazon DynamoDB](./labs/3-database/01-amazon-dynamodb-introduction/) | Criação de tabelas, inserção de itens e operações de Query vs Scan | 🟢 Fundamental   |
| 02  | [DynamoDB Serverless CRUD](./labs/3-database/02-dynamodb-lambda-crud/)                | API REST com Lambda + Boto3 em tabela NoSQL                        | 🟡 Intermediário |
| 03  | [DynamoDB LSI & GSI](./labs/3-database/03-dynamodb-lsi-gsi/)                          | Otimização de queries — Scan vs Query e rotação de índices         | 🟡 Intermediário |

### 🖥️ Compute

| #   | Lab                                                                 | Descrição                                                      | Nível           |
| --- | ------------------------------------------------------------------- | -------------------------------------------------------------- | --------------- |
| 01  | [Introduction to Amazon EC2](./labs/1-compute/01-ec2-introduction/) | Ciclo de vida: Launch, Monitoring, Security e Vertical Resize  | 🟢 Fundamental   |
| 02  | [EC2 + CloudShell](./labs/1-compute/02-ec2-console-cloudshell/)     | Instâncias web com User Data via Console e CLI                 | 🟢 Fundamental   |
| 03  | [Elastic Beanstalk](./labs/1-compute/03-elastic-beanstalk/)         | Deploy PaaS com IAM Instance Profile                           | 🟢 Fundamental   |
| 04  | [Auto Scaling + ALB](./labs/1-compute/04-auto-scaling-alb/)         | Alta disponibilidade com Launch Templates, ASG e Load Balancer | 🟡 Intermediário |

---

## Estrutura de cada lab
```text
<lab-name>/
├── README.md      # Contexto da arquitetura e decisões técnicas
├── README-en.md   # Versão em inglês
├── src/           # Scripts (Python / Bash / Boto3)
└── assets/        # Diagramas e evidências de validação
```

> **Nota:** Os códigos de provisionamento (Terraform/CDK) estão centralizados no diretório `/iac` na raiz do projeto, organizados por laboratório.

---

## Autor

**Caio Cesar**
Graduado em TI, AWS re/Start Graduate. Certificações: CLF-C02 · DVA-C02 · SAA-C03 · AIF-C01.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-caiocesardev-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/caiocesardev/)
[![GitHub](https://img.shields.io/badge/GitHub-caiocesarti-181717?style=flat-square&logo=github)](https://github.com/caiocesarti)