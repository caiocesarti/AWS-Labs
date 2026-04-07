<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 07 â€” Auditoria BÃ¡sica de Identidade e Ambiente AWS

## ðŸš€ Resumo
Auditoria de Arquitetura e ValidaÃ§Ã£o de Conformidade: Neste laboratÃ³rio, realizei uma imersÃ£o focada na extraÃ§Ã£o de evidÃªncias de seguranÃ§a e controles de rede. Simulei as aÃ§Ãµes de um analista de seguranÃ§a, cobrindo a verificaÃ§Ã£o de identidades via IAM Simulator, avaliaÃ§Ã£o de regras de firewall (Security Groups), checagem de ACLs de rede (VPC NACLs) e anÃ¡lise forense atravÃ©s de logs do CloudTrail armazenados no S3.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** GovernanÃ§a, Risco e Compliance (GRC)
- **Problema:** Um fundo de investimento iniciou uma auditoria tÃ©cnica (Due Diligence) em uma startup antes de comprÃ¡-la. Eles precisavam de provas de que as bases de dados crÃ­ticas nÃ£o estavam expostas Ã  internet e de que os desenvolvedores nÃ£o tinham permissÃ£o para apagar recursos de produÃ§Ã£o por conta prÃ³pria.
- **SoluÃ§Ã£o:** Como arquiteto, conduzi a auditoria provendo evidÃªncias formais. Utilizei o **IAM Policy Simulator** para provar que o usuÃ¡rio `User-1` estÃ¡ impossibilitado de deletar grupos ou bancos de dados. Mapeei os **Security Groups** e as **NACLs** da VPC para atestar que apenas portas especÃ­ficas da administraÃ§Ã£o estÃ£o abertas. Por fim, extraÃ­ os logs brutos do **AWS CloudTrail** direto do S3 para mostrar o histÃ³rico completo de aÃ§Ãµes na conta, garantindo a transparÃªncia e seguranÃ§a exigidas pelos compradores.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Consolidar a extraÃ§Ã£o de evidÃªncias analisando permissÃµes de usuÃ¡rios no **AWS IAM**.
- Validar bloqueios de seguranÃ§a em tempo real usando o **IAM Policy Simulator**.
- Inspecionar firewalls de host atravÃ©s dos **Security Groups** do Amazon EC2.
- Mapear barreiras de sub-rede utilizando as **NACLs (Network Access Control Lists)** da VPC.
- Rastrear e analisar chamadas de API extraindo arquivos JSON brutos do **AWS CloudTrail**.
- Garantir a integridade dos logs de auditoria armazenados no **Amazon S3**.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS IAM** | ValidaÃ§Ã£o de polÃ­ticas e simulaÃ§Ã£o de acessos (Policy Simulator). |
| **Amazon EC2** | Alvo das inspeÃ§Ãµes de firewall e regras de acesso. |
| **Amazon VPC** | AnÃ¡lise de isolamento lÃ³gico de rede e regras de NACL. |
| **AWS CloudTrail** | GravaÃ§Ã£o e rastreio de todos os eventos de gestÃ£o da conta. |
| **Amazon S3** | Armazenamento de longa duraÃ§Ã£o para os arquivos compactados de log. |

---

## ðŸ—ï¸ Arquitetura de ValidaÃ§Ã£o de Auditoria

<div align="center">
  <img src="./assets/architecture-aws-basic-audit.drawio.png" alt="Arquitetura de Auditoria de Redes e Identidade" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ Auditoria de Identidade (IAM)
- **AÃ§Ã£o:** Avaliei as restriÃ§Ãµes do perfil `user-1`. Em vez de ler centenas de linhas de JSON, processei um teste no simulador para confirmar que o usuÃ¡rio recebe um "Denied" ao tentar deletar recursos, provando a eficÃ¡cia das polÃ­ticas.

### 2. ðŸ›¡ï¸ Auditoria de Firewall e Rede (VPC/EC2)
- **AÃ§Ã£o:** Inspecionei os Security Groups para garantir que protocolos sensÃ­veis (como SSH) estavam limitados apenas aos IPs da empresa.
- **ValidaÃ§Ã£o:** Verifiquei as NACLs da VPC para atestar uma segunda camada de bloqueio (stateless) que impede o trÃ¡fego de saÃ­da nÃ£o autorizado, reforÃ§ando o isolamento dos bancos de dados.

### 3. ðŸ” ExtraÃ§Ã£o Forense de Logs (S3/CloudTrail)
- **AÃ§Ã£o:** Resgatei manualmente os arquivos `.json.gz` armazenados no bucket S3 da auditoria. 
- **AnÃ¡lise:** Abri os arquivos brutos para validar a origem (IP, usuÃ¡rio e timestamp) das chamadas de API, gerando o relatÃ³rio final que comprova a rastreabilidade total do ambiente.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Auditoria de Identidade: ValidaÃ§Ã£o de restriÃ§Ãµes via IAM Policy Simulator
<img src="./assets/IAM-Policy-Simulator.png" width="100%">

### 2. Auditoria de Rede: InspeÃ§Ã£o de regras de entrada no Security Group
<img src="./assets/Acls-Inbound.png" width="100%">

### 3. Controle de Acesso: ConfiguraÃ§Ã£o de NACLs atuando na sub-rede
<img src="./assets/acls-VPC-Console.png" width="100%">

### 4. InventÃ¡rio de Recursos: Detalhes do volume EBS associado Ã  instÃ¢ncia
<img src="./assets/Volume-details-EC2.png" width="100%">

### 5. Monitoramento: MÃ©tricas de performance e saÃºde no CloudWatch
<img src="./assets/Metrics-CloudWatch.png" width="100%">
<img src="./assets/Metrics-CloudWatch-instance.png" width="100%">

---

### 6. Rastreabilidade: Detalhes da trilha de auditoria do CloudTrail
<img src="./assets/Trail-details-CloudTrail.png" width="100%">

### 7. Armazenamento Forense: Logs brutos e compactados salvos no S3
<img src="./assets/logs-S3-bucket-S3.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Defesa em Profundidade:** Entendi que um bom Security Group nÃ£o anula a necessidade de uma NACL forte. Se um erro humano abrir o firewall do servidor, a regra da rede (VPC) ainda pode bloquear o ataque.
- **Rastreabilidade Ã© Lei:** Sem logs Ã­ntegros no S3, investigaÃ§Ãµes de "quem apagou o quÃª" sÃ£o baseadas apenas em suposiÃ§Ãµes. O CloudTrail fornece a prova irrefutÃ¡vel necessÃ¡ria para compliance legal.
- **Simulador de PolÃ­ticas:** O IAM Simulator economiza horas de "tentativa e erro". Ele permite prever o comportamento de permissÃµes complexas antes mesmo de liberar o acesso ao usuÃ¡rio final.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| IAM Policy Simulator | âœ… Gratuito | $0,00 |
| AWS CloudTrail | âœ… Primeira trilha gratuita | $0,00 |
| Amazon VPC | âœ… ConfiguraÃ§Ã£o de rede gratuita | $0,00 |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`IAM Policy Simulator` `VPC NACL` `Security Groups` `AWS CloudTrail` `Auditoria de SeguranÃ§a` `S3 Log Analytics` `ðŸŸ¡ IntermediÃ¡rio`

---

## ðŸ“œ Alinhamento com CertificaÃ§Ãµes

- **CLF-C02:** DomÃ­nio 2 â€” SeguranÃ§a e Conformidade
- **SAA-C03:** DomÃ­nio 1 â€” Design de Arquiteturas Seguras

---

[â† Voltar ao Ã­ndice](../../../README.md)