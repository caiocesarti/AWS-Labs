<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 09 — AWS Incident Response Demonstrated — Exam Lab na Prática

<p align="center">
  <img src="assets/post-incident-response-demonstrated.webp" alt="AWS Incident Response Demonstrated — Banner" width="100%"/>
</p>

## 🚀 Resumo
Este laboratório é um **Exam Lab prático** focado em resposta a incidentes. Atuei investigando, contendo e erradicando uma ameaça real em um ambiente AWS previamente comprometido. A missão envolveu a conclusão de **6 desafios interdependentes** de análise forense, contenção de danos e endurecimento da infraestrutura diretamente no console AWS.

---

## 💼 Caso de Uso Real
- **Indústria:** Segurança da Informação / SecOps
- **Problema:** Um alerta do AWS GuardDuty apontou comunicação com IPs maliciosos. Uma investigação revelou que credenciais da AWS foram vazadas, instâncias EC2 estavam minerando criptomoedas, e bancos de dados confidenciais foram expostos e possivelmente exfiltrados.
- **Solução:** Isolamento imediato do ambiente através de Security Groups e NACLs. Realização de análise forense consultando logs do CloudTrail via Amazon Athena. Erradicação de backdoors no IAM e EC2, transição para o AWS Systems Manager (SSM) no lugar do SSH, e ativação do AWS Config para garantir conformidade contínua.

---

## 🎯 Objetivos de Aprendizado
*   **Investigar** incidentes de segurança usando o Amazon Athena para consultar logs estruturados do AWS CloudTrail.
*   **Conter** ameaças ativas manipulando rotas, Security Groups e Network ACLs.
*   **Preservar evidências forenses** de forma segura, garantindo a integridade dos dados no S3 e RDS.
*   **Erradicar backdoors** revogando acessos indevidos no IAM e remediando instâncias EC2 comprometidas (ex: forçando IMDSv2).
*   **Prevenir** recorrências utilizando o AWS Config para auditoria contínua.

---

## 🛠️ Serviços AWS Utilizados

| Serviço                       | Papel no Lab                                                      |
| ----------------------------- | ----------------------------------------------------------------- |
| **Amazon EC2**                | Servidores web comprometidos e instâncias de mineração.           |
| **Amazon RDS (MySQL)**        | Banco de dados alvo na subnet privada.                            |
| **AWS IAM**                   | Vetor de persistência: usuários, roles e políticas de acesso.     |
| **AWS CloudTrail**            | Trilha de auditoria e fonte primária de evidências forenses.      |
| **Amazon Athena**             | Consultas SQL complexas nos logs do CloudTrail armazenados no S3. |
| **Amazon S3**                 | Repositório central de logs, evidências e dados exfiltrados.      |
| **AWS Config**                | Monitoramento de conformidade e detecção de desvios na conta.     |
| **Amazon VPC**                | Subnets, Security Groups e Network ACLs para isolamento de rede.  |
| **Application Load Balancer** | Ponto de entrada de tráfego web protegido.                        |
| **AWS Systems Manager**       | Acesso seguro via Session Manager, substituindo instâncias Bastion. |

---

## 🖥️ Etapas do Laboratório

### Desafio A: Segurança de DB e Preservação de Evidências
- Modificação de políticas de acesso para bloquear exfiltração em andamento do Amazon RDS.
- Preservação segura de evidências forenses coletadas no Amazon S3, utilizando bloqueios de imutabilidade.

### Desafio B: Identificação e Erradicação de Recursos
- Descoberta e encerramento de instâncias EC2 clandestinas (mineração de criptomoedas).
- Reforço de segurança nos metadados do EC2, exigindo a versão 2 do Instance Metadata Service (IMDSv2) para mitigar ataques de SSRF.

### Desafio C: Controles de Auditoria e Conformidade
- Restauração das trilhas de auditoria do AWS CloudTrail que haviam sido desabilitadas pelo atacante.
- Implementação de regras no AWS Config para monitorar continuamente o estado de conformidade dos recursos.

### Desafio D: Erradicação de Backdoors e Privilégio Mínimo
- Investigação de logs com o Amazon Athena para mapear a movimentação lateral do atacante.
- Exclusão de chaves de acesso comprometidas e políticas permissivas (backdoors) no AWS IAM.

### Desafio E: Endurecimento de Rede e SSM
- Refatoração dos Security Groups para aderir ao privilégio mínimo.
- Remoção da necessidade de SSH público, implementando o AWS Systems Manager (SSM) Session Manager.

### Desafio F: Bloqueio do Atacante (NACLs)
- Identificação dos endereços IP de comando e controle (C2) do atacante via Athena.
- Criação de Network ACLs explícitas (NACLs) para bloquear o tráfego nos níveis de sub-rede.

---

## 📸 Evidências de Execução

### Microcredencial Conquistada
<p align="center">
  <img src="assets/incident-response-demonstrated.webp" alt="AWS Incident Response Demonstrated Badge" width="180"/>
</p>

> [!IMPORTANT]
> A credencial certifica a aprovação no exame prático oficial da AWS Skills Builder.

---

## 💡 Principais Aprendizados
*   **CloudTrail + Athena = Visibilidade Total:** Analisar arquivos JSON soltos do CloudTrail é inviável em um incidente. Mapear o S3 como uma tabela no Athena usando partições permite responder perguntas como *"quem assumiu essa role ontem?"* em segundos.
*   **IMDSv2 é crítico:** Muitos comprometimentos de EC2 ocorrem via Server-Side Request Forgery (SSRF) acessando o endpoint `169.254.169.254`. Exigir tokens IMDSv2 impede a esmagadora maioria desses ataques.
*   **Session Manager substitui o Bastion:** O uso do SSM Session Manager elimina a necessidade de abrir a porta 22 (SSH) para a internet e ainda mantém um log auditável de todas as sessões.

---

## 🔗 Recursos Adicionais
- [AWS Skill Builder — Microcredentials](https://explore.skillbuilder.aws/learn/public/learning_plan/view/2070/microcredentials)
- [Querying AWS CloudTrail Logs with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html)
- [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS CloudTrail | ✅ 1ª trilha grátis | $0,00 |
| Amazon Athena | ❌ $5.00 por TB escaneado | ~$0,05 |
| Amazon EC2 / RDS | ✅ Depende do tipo de instância | Variável |
| AWS Config | ❌ $0.003 por item registrado | ~$1,00/mês |
| AWS Systems Manager | ✅ Uso padrão gratuito | $0,00 |
| **Total Estimado** | | **~$1,05** |

---

## 🏷️ Competências Demonstradas

`Amazon EC2` `Amazon RDS` `AWS IAM` `AWS CloudTrail` `Amazon Athena` `Amazon S3` `AWS Config` `Amazon VPC` `NACLs` `AWS Systems Manager` `Incident Response` `Forensics` `🔴 Avançado`

---

## 📎 Referência

> Este laboratório gerou um artigo aprofundado com o passo a passo técnico:
> **👉 [Artigo: AWS Incident Response Demonstrated — Exam Lab na Prática](https://labs.caiocesar.tec.br/2026/06/28/aws-incident-response-demonstrated-exam-lab/)**
> 
> *Nota: Este repositório tem fins de estudo e não contém o código proprietário do laboratório da AWS.*

---

[← Voltar ao índice](../../../README.md)
