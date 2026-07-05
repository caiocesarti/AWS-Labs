<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 02 â€” API Gateway Stages & Lambda Aliases

## ðŸš€ Resumo
DevOps Serverless e Deploy Blue/Green: Neste laboratÃ³rio, implementei estratÃ©gias seguras de atualizaÃ§Ã£o de cÃ³digo utilizando **AWS Lambda** e **Amazon API Gateway**. Configurei o uso de **Versions** imutÃ¡veis e **Aliases** (PROD/DEV) para controlar o ciclo de vida da aplicaÃ§Ã£o. AlÃ©m disso, utilizei **Stage Variables** no API Gateway para rotear o trÃ¡fego dinamicamente, permitindo que uma Ãºnica API aponte para diferentes versÃµes da funÃ§Ã£o Lambda dependendo da URL acessada, garantindo deploys sem downtime e testes seguros em ambiente de desenvolvimento.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Engenharia de Software e MicroserviÃ§os
- **Problema:** Em um projeto de sistema bancÃ¡rio, os desenvolvedores atualizavam a mesma funÃ§Ã£o Lambda que os clientes usavam em produÃ§Ã£o. Uma alteraÃ§Ã£o mal testada derrubou o serviÃ§o de pagamentos por horas, pois nÃ£o havia uma separaÃ§Ã£o entre o cÃ³digo que estava sendo escrito e o cÃ³digo estÃ¡vel que os clientes acessavam.
- **SoluÃ§Ã£o:** Reestruturei o fluxo de deploy. Agora, a Lambda possui uma versÃ£o congelada ("versÃ£o 1") associada ao **Alias PROD**. O API Gateway possui dois "Stages": `/producao` e `/desenvolvimento`. Configurei uma Stage Variable chamada `lambdaAlias`. Quando o cliente acessa `/producao`, a API usa a variÃ¡vel para chamar o Alias `PROD` (estÃ¡vel). Quando o desenvolvedor acessa `/desenvolvimento`, a API chama o Alias `DEV` (que aponta para o cÃ³digo mais recente, `$LATEST`). Isso isola completamente os erros de desenvolvimento do ambiente crÃ­tico de produÃ§Ã£o.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Desenvolver funÃ§Ãµes **AWS Lambda** com lÃ³gica de resposta para integraÃ§Ã£o com API Gateway.
- Criar e gerenciar **Versions** imutÃ¡veis de funÃ§Ãµes Lambda.
- Implementar **Aliases** (como `PROD` e `DEV`) para apontar para versÃµes especÃ­ficas.
- Configurar o **Amazon API Gateway** para expor endpoints REST.
- Utilizar **Stage Variables** no API Gateway (`${stageVariables.lambdaAlias}`) para roteamento dinÃ¢mico.
- Validar o conceito de Blue/Green Deployment testando links paralelos de produÃ§Ã£o e desenvolvimento.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS Lambda** | Processamento backend com suporte a versionamento e aliases. |
| **Amazon API Gateway** | ExposiÃ§Ã£o de endpoints e gerenciamento de estÃ¡gios (Stages). |
| **AWS IAM** | PermissÃ£o para que o API Gateway invoque a funÃ§Ã£o Lambda (Resource-based policy). |

---

## ðŸ—ï¸ Arquitetura de Deploy (Dev/Prod)

<div align="center">
  <img src="./assets/architecture-lambda-api-gateway.drawio.png" alt="Arquitetura de Deploy" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ PreparaÃ§Ã£o do Backend (Lambda)
- **AÃ§Ã£o:** Criei uma funÃ§Ã£o Lambda bÃ¡sica em Python.
- **Versionamento:** Publiquei a "VersÃ£o 1" (imutÃ¡vel) e criei os Aliases `PROD` (apontando para a V1) e `DEV` (apontando para o rascunho `$LATEST`).

### 2. ðŸ›¡ï¸ ConfiguraÃ§Ã£o da API DinÃ¢mica
- **AÃ§Ã£o:** No API Gateway, criei um recurso `/hello` e um mÃ©todo GET.
- **Roteamento:** Em vez de selecionar a funÃ§Ã£o Lambda fixa pelo nome, utilizei a sintaxe de variÃ¡vel: `MinhaFuncao:${stageVariables.lambdaAlias}`. Isso faz com que a API decida qual versÃ£o chamar no momento da requisiÃ§Ã£o.

### 3. ðŸ” CriaÃ§Ã£o dos EstÃ¡gios (Stages)
- **AÃ§Ã£o:** Criei dois Stages: `producao` e `desenvolvimento`.
- **VariÃ¡veis:** No stage `producao`, defini a variÃ¡vel `lambdaAlias` com o valor `PROD`. No stage `desenvolvimento`, defini o valor `DEV`.

### 4. ðŸ§° Teste de ValidaÃ§Ã£o
- **Resultado DEV:** Ao acessar o link de desenvolvimento, vi as mensagens de rascunho que eu estava editando em tempo real.
- **Resultado PROD:** Ao acessar o link de produÃ§Ã£o, o sistema retornou apenas a mensagem congelada da VersÃ£o 1, provando que as minhas ediÃ§Ãµes recentes nÃ£o afetaram o ambiente estÃ¡vel.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. CriaÃ§Ã£o da FunÃ§Ã£o Lambda
<img src="./assets/01-create-lambda-function.png" width="100%">

### 2. FunÃ§Ã£o Criada
<img src="./assets/02-lambda-function-created.png" width="100%">

### 3. ConfiguraÃ§Ã£o de Evento de Teste
<img src="./assets/03-configure-test-event.png" width="100%">

### 4. Resultado do Teste na Lambda
<img src="./assets/04-test-execution-result.png" width="100%">

### 5. CriaÃ§Ã£o do Alias DEV
<img src="./assets/05-create-alias-dev.png" width="100%">

### 6. VisÃ£o Geral da FunÃ§Ã£o Lambda
<img src="./assets/06-lambda-function-overview.png" width="100%">

### 7. VersÃµes Publicadas (Imutabilidade)
<img src="./assets/07-published-versions.png" width="100%">

### 8. CriaÃ§Ã£o do Alias PROD
<img src="./assets/08-create-alias-prod.png" width="100%">

### 9. Lista de Aliases (PROD e DEV)
<img src="./assets/09-aliases-dev-prod.png" width="100%">

### 10. CriaÃ§Ã£o do API Gateway
<img src="./assets/10-create-api-gateway.png" width="100%">

### 11. SeleÃ§Ã£o do Tipo de API (REST)
<img src="./assets/11-select-rest-api.png" width="100%">

### 12. CriaÃ§Ã£o do Recurso /hello
<img src="./assets/12-create-resource-hello.png" width="100%">

### 13. ConfiguraÃ§Ã£o do MÃ©todo GET Integrado com Lambda (Stage Variable)
<img src="./assets/13-create-method-get-proxy.png" width="100%">

### 14. Deploy no Stage de Desenvolvimento
<img src="./assets/14-deploy-stage-desenvolvimento.png" width="100%">

### 15. EdiÃ§Ã£o de IntegraÃ§Ã£o (Adicionando PermissÃµes)
<img src="./assets/15-edit-integration-prod.png" width="100%">

### 16. Deploy no Stage de ProduÃ§Ã£o
<img src="./assets/16-deploy-stage-producao.png" width="100%">

### 17. VisÃ£o Geral dos EstÃ¡gios (Stages)
<img src="./assets/17-stages-overview.png" width="100%">

### 18. Rotas Expandidas nos EstÃ¡gios
<img src="./assets/18-stages-expanded-routes.png" width="100%">

### 19. Teste de Roteamento DinÃ¢mico: Endpoint Desenvolvimento
<img src="./assets/19-test-result-desenvolvimento.png" width="100%">

### 20. Teste de Roteamento DinÃ¢mico: Endpoint ProduÃ§Ã£o
<img src="./assets/20-test-result-producao.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Versioning = SeguranÃ§a:** Uma versÃ£o publicada nunca muda. Isso dÃ¡ a seguranÃ§a de que, se algo quebrar no cÃ³digo novo, eu posso sempre reverter o Alias PROD para uma versÃ£o anterior conhecida em segundos.
- **Poder das Stage Variables:** Elas evitam que eu precise duplicar toda a minha API para ter ambientes de teste. O roteamento Ã© feito de forma limpa e programÃ¡tica.
- **Blue/Green Deployment:** Este lab Ã© a base do deploy seguro. Eu posso subir a VersÃ£o 2, testÃ¡-la no stage de dev e, quando estiver pronto, apenas trocar o Alias PROD da versÃ£o 1 para a 2.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Lambda | âœ… 1 MilhÃ£o req/mÃªs gratuitos | $0,00 |
| Amazon API Gateway | âœ… 1 MilhÃ£o chamadas/mÃªs (12 meses) | $0,00 |
| **Total Estimado** | | **$0,00** |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS Lambda Aliases` `API Gateway Stages` `Stage Variables` `CI/CD Concepts` `Blue-Green Deployment` `Serverless` `ðŸŸ¡ IntermediÃ¡rio`

---

[â† Voltar ao Ã­ndice](../../../README.md)
