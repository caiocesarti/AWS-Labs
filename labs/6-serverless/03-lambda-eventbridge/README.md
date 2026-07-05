<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 03 â€” AutomaÃ§Ã£o com Lambda e EventBridge (Terminador de EC2)

## ðŸš€ Resumo
GovernanÃ§a de Custos e AutomaÃ§Ã£o (FinOps): Neste laboratÃ³rio, implementei uma soluÃ§Ã£o de orquestraÃ§Ã£o de infraestrutura totalmente automatizada. Desenvolvi um script em **Python (Boto3)** rodando no **AWS Lambda** para identificar e encerrar instÃ¢ncias EC2 que estejam ligadas. Configurei o **Amazon EventBridge** para atuar como um agendador (Cron-job), disparando essa rotina periodicamente para garantir que ambientes de teste nÃ£o fiquem ligados fora do horÃ¡rio comercial, eliminando custos desnecessÃ¡rios com recursos ociosos.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Cloud Governance e FinOps Corporativo
- **Problema:** Em um departamento de QA, desenvolvedores sobem dezenas de instÃ¢ncias EC2 todos os dias para testes rÃ¡pidos. O problema recorrente era que, ao final do expediente ou antes do fim de semana, muitos esqueciam de desligar os servidores. Isso gerava cobranÃ§as pesadas de servidores rodando 100% ociosos por dias seguidos.
- **SoluÃ§Ã£o:** Criei um "Script Faxineiro". Configurei uma Lambda com permissÃµes especÃ­ficas para listar e encerrar instÃ¢ncias. Utilizei o **Amazon EventBridge** para criar uma regra de agendamento que dispara todas as noites Ã s 20:00 (ou a cada 1 minuto para testes). A automaÃ§Ã£o varre a regiÃ£o, encontra as instÃ¢ncias ligadas e as desliga automaticamente. O resultado foi uma reduÃ§Ã£o drÃ¡stica na conta mensal de AWS da empresa, sem depender da memÃ³ria dos engenheiros.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Aplicar o princÃ­pio de **Least Privilege** criando uma policy IAM que permite apenas `Describe` e `Terminate` em instÃ¢ncias EC2.
- Desenvolver scripts de automaÃ§Ã£o utilizando a biblioteca **Boto3 (SDK AWS para Python)**.
- Manipular listas de recursos retornadas em formato JSON para filtragem de instÃ¢ncias por status.
- Configurar agendamentos automÃ¡ticos utilizando expressÃµes Cron no **Amazon EventBridge**.
- Ajustar configuraÃ§Ãµes de performance da Lambda (como o `Timeout`) para lidar com loops de mÃºltiplos recursos.
- Validar a automaÃ§Ã£o monitorando a transiÃ§Ã£o de estado da EC2 de "Running" para "Shutting-down" sem intervenÃ§Ã£o manual.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS Lambda** | ExecuÃ§Ã£o da lÃ³gica de automaÃ§Ã£o em Python. |
| **Amazon EventBridge** | Gatilho de agendamento (Schedule) para disparar a funÃ§Ã£o. |
| **AWS IAM** | Role de execuÃ§Ã£o com permissÃµes restritas para gerenciar EC2. |
| **Amazon EC2** | Recursos alvo da automaÃ§Ã£o de desligamento. |

---

## ðŸ—ï¸ Arquitetura de AutomaÃ§Ã£o de Custo

<div align="center">
  <img src="./assets/architecture-lambda-eventbridge.drawio.png" alt="Arquitetura de AutomaÃ§Ã£o de Custo" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ CriaÃ§Ã£o da Role de ExecuÃ§Ã£o (IAM)
- **AÃ§Ã£o:** Criei uma Policy personalizada com permissÃµes de `ec2:DescribeInstances` e `ec2:TerminateInstances`.
- **PropÃ³sito:** Garantir que a Lambda tenha poder apenas para desligar mÃ¡quinas, sem permissÃ£o para criar novos recursos ou acessar outros serviÃ§os sensÃ­veis.

### 2. ðŸ›¡ï¸ Desenvolvimento do Script (Lambda)
- **AÃ§Ã£o:** Desenvolvi o cÃ³digo em Python 3.12 usando o handler padrÃ£o da Lambda. 
- **LÃ³gica:** O script filtra todas as instÃ¢ncias que estÃ£o com o `State` igual a `running` e extrai seus `InstanceIds`. Em seguida, envia o comando de finalizaÃ§Ã£o para todos os IDs encontrados de uma sÃ³ vez.
- **Ajuste:** Aumentei o `Timeout` da funÃ§Ã£o para garantir que ela tenha tempo de processar a lista caso existam muitas instÃ¢ncias.
> ðŸ“„ **Ver cÃ³digo fonte:** [src/lambda_function.py](./src/lambda_function.py).

### 3. ðŸ” ConfiguraÃ§Ã£o do Agendamento (EventBridge)
- **AÃ§Ã£o:** Criei uma regra no EventBridge do tipo "Schedule".
- **ExpressÃ£o:** Utilizei uma expressÃ£o cron para desligamento diÃ¡rio ou uma taxa de "1 minute" para validar o funcionamento do laboratÃ³rio em tempo real.

### 4. ðŸ§° ValidaÃ§Ã£o PrÃ¡tica
- **Teste:** Liguei manualmente uma instÃ¢ncia EC2 "t2.micro". 
- **Resultado:** Esperei o gatilho do EventBridge e observei via console do EC2 a instÃ¢ncia mudando automaticamente para o estado de encerramento, validando o sucesso da automaÃ§Ã£o.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Lista de PolÃ­ticas do IAM
<img src="./assets/01-iam-policies-list.png" width="100%">

### 2. Editor de JSON da Policy
<img src="./assets/02-policy-json-editor.png" width="100%">

### 3. PolÃ­tica Criada com Sucesso
<img src="./assets/03-policy-created-success.png" width="100%">

### 4. Detalhes da PolÃ­tica IAM
<img src="./assets/04-policy-details.png" width="100%">

### 5. Lista de Roles do IAM
<img src="./assets/05-iam-roles-list.png" width="100%">

### 6. CriaÃ§Ã£o de Role: Entidade ConfiÃ¡vel
<img src="./assets/06-create-role-trusted-entity.png" width="100%">

### 7. CriaÃ§Ã£o de Role: Adicionando PermissÃµes
<img src="./assets/07-create-role-add-permissions.png" width="100%">

### 8. CriaÃ§Ã£o de Role: RevisÃ£o
<img src="./assets/08-create-role-review.png" width="100%">

### 9. Detalhes da Role Criada
<img src="./assets/09-role-created-details.png" width="100%">

### 10. CriaÃ§Ã£o da FunÃ§Ã£o Lambda
<img src="./assets/10-lambda-create-function.png" width="100%">

### 11. ConfiguraÃ§Ãµes da FunÃ§Ã£o Lambda
<img src="./assets/11-lambda-function-config.png" width="100%">

### 12. FunÃ§Ã£o Lambda Criada
<img src="./assets/12-lambda-function-created.png" width="100%">

### 13. EdiÃ§Ã£o do Timeout da Lambda
<img src="./assets/13-lambda-edit-timeout.png" width="100%">

### 14. EdiÃ§Ã£o do Handler da Lambda
<img src="./assets/14-lambda-edit-handler.png" width="100%">

### 15. EventBridge: Adicionando Gatilho (Trigger)
<img src="./assets/15-eventbridge-add-trigger.png" width="100%">

### 16. ConfiguraÃ§Ã£o da Regra do EventBridge
<img src="./assets/16-eventbridge-rule-config.png" width="100%">

### 17. VisÃ£o Geral da Lambda: Gatilho Ativo
<img src="./assets/17-lambda-overview-trigger-active.png" width="100%">

### 18. Detalhes do Gatilho da Lambda
<img src="./assets/18-lambda-trigger-details.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Granularidade IAM:** Entendi que dar `AdministratorAccess` para uma Lambda Ã© um risco de seguranÃ§a enorme. AtravÃ©s de permissÃµes pontuais, limitei o "raio de explosÃ£o" de qualquer erro no cÃ³digo.
- **AutomaÃ§Ã£o vs ManutenÃ§Ã£o Manual:** O EventBridge elimina a necessidade de manter servidores dedicados de scripts (como um servidor Jenkins ou Bastion com Crontab). Ã‰ uma soluÃ§Ã£o nativa, barata e sem servidor.
- **Tratamento de ColeÃ§Ãµes com Boto3:** Aprendi a iterar sobre listas complexas de dicionÃ¡rios JSON retornadas pela API da AWS, extraindo apenas os dados necessÃ¡rios para a aÃ§Ã£o final.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Lambda | âœ… 1 MilhÃ£o de invocaÃ§Ãµes gratuitas/mÃªs | $0,00 |
| Amazon EventBridge | âœ… 1 MilhÃ£o de eventos de agendamento/mÃªs | $0,00 |
| **Total Estimado** | | **$0,00** |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS Lambda` `Amazon EventBridge` `Cron Jobs` `FinOps (Custos)` `Boto3 Scripting` `EC2 Automation` `ðŸ”´ AvanÃ§ado`

---

[â† Voltar ao Ã­ndice](../../../README.md)
