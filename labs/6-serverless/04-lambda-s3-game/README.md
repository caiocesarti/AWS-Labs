<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 04 â€” Full-Stack Serverless (S3, API Gateway e Lambda)

## ðŸš€ Resumo
Arquitetura Full-Stack Serverless Moderna: Neste laboratÃ³rio, construÃ­ uma aplicaÃ§Ã£o completa de "Jogo de AdivinhaÃ§Ã£o" utilizando apenas serviÃ§os gerenciados. Hospedei o front-end estÃ¡tico (HTML/JS) no **Amazon S3**, utilizei o **Amazon API Gateway** para expor uma interface REST e desenvolvi a lÃ³gica de processamento no backend com **AWS Lambda (Node.js)**. Esta arquitetura demonstra como criar aplicaÃ§Ãµes escalÃ¡veis que custam zero enquanto nÃ£o estÃ£o sendo acessadas, eliminando a necessidade de gerenciar servidores ou mÃ¡quinas virtuais.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Marketing Digital e Hotsites Promocionais
- **Problema:** Uma agÃªncia precisava lanÃ§ar um site para uma campanha de apenas uma semana. Eles esperavam picos imensos de acessos logo apÃ³s os comerciais na TV, mas nos outros horÃ¡rios o site ficaria vazio. Manter servidores ligados 24/7 para aguentar o pico seria extremamente caro e ineficiente.
- **SoluÃ§Ã£o:** Implementei uma soluÃ§Ã£o Full-Stack Serverless. Coloquei o site estÃ¡tico no S3 (Static Website Hosting), que aguenta trÃ¡fego massivo com custo baixÃ­ssimo. Para a parte interativa da promoÃ§Ã£o, usei Lambda + API Gateway. O resultado foi um site que escala instantaneamente para milhares de usuÃ¡rios simultÃ¢neos durante os comerciais e que nÃ£o cobra absolutamente nada pelos perÃ­odos de inatividade, economizando 90% do orÃ§amento original de infraestrutura.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Hospedar sites estÃ¡ticos com alta disponibilidade via **Amazon S3 Static Website Hosting**.
- Desenvolver lÃ³gica de backend em **Node.js** rodando em **AWS Lambda**.
- Criar e publicar endpoints RESTful utilizando o **Amazon API Gateway**.
- Configurar e entender o **CORS (Cross-Origin Resource Sharing)** para permitir que o front-end no S3 se comunique com a API.
- Integrar o front-end com o backend utilizando chamadas `fetch()` em JavaScript nativo.
- Validar a comunicaÃ§Ã£o sÃ­ncrona entre serviÃ§os desacoplados na AWS.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **Amazon S3** | Hospedagem do front-end estÃ¡tico (HTML e JavaScript). |
| **AWS Lambda** | Processamento da lÃ³gica do jogo e geraÃ§Ã£o de respostas. |
| **Amazon API Gateway** | Interface de entrada para as requisiÃ§Ãµes do navegador. |

---

## ðŸ—ï¸ Arquitetura Serverless

<div align="center">
  <img src="./assets/architecture-lambda-s3-game.drawio.png" alt="Arquitetura Serverless" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ Backend e LÃ³gica (Lambda)
- **AÃ§Ã£o:** Criei uma funÃ§Ã£o Lambda em Node.js 20.x.
- **LÃ³gica:** Desenvolvi um handler que recebe um nÃºmero via JSON, compara com um nÃºmero secreto e retorna se o palpite foi alto, baixo ou correto, incluindo os headers necessÃ¡rios para o navegador aceitar a resposta.

### 2. ðŸ›¡ï¸ Interface de ComunicaÃ§Ã£o (API Gateway)
- **AÃ§Ã£o:** Configurei uma API REST com o mÃ©todo POST.
- **CORS:** Ativei o suporte a CORS no API Gateway para permitir que o domÃ­nio do S3 (origem diferente) fizesse requisiÃ§Ãµes para a API sem ser bloqueado pela seguranÃ§a do navegador.

### 3. ðŸ” Hospedagem e ConexÃ£o (S3)
- **AÃ§Ã£o:** Criei um bucket, desativei o bloqueio de acesso pÃºblico e ativei o "Static Website Hosting".
- **IntegraÃ§Ã£o:** No arquivo `index.html`, inseri a URL do endpoint gerado pelo API Gateway. Fiz o upload do arquivo para o bucket e obtive a URL pÃºblica do site.

### 4. ðŸ§° ValidaÃ§Ã£o Final
- **Teste:** Acessei o site pelo navegador, digitei os palpites e recebi as respostas instantÃ¢neas vindas da Lambda atravÃ©s do API Gateway, confirmando que toda a cadeia de serviÃ§os estava comunicando perfeitamente.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. CÃ³digo e ConfiguraÃ§Ã£o da Lambda
<img src="./assets/01-lambda-configuration.png" width="100%">

### 2. Rotas e Mock CORS no API Gateway
<img src="./assets/02-api-gateway-routes.png" width="100%">

### 3. Hospedagem de Website EstÃ¡tico no S3
<img src="./assets/03-s3-website-bucket.png" width="100%">

### 4. Interface do Jogo e ValidaÃ§Ã£o Final
<img src="./assets/04-game-interface-result.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Desacoplamento Total:** Front-end e Backend podem (e devem) viver em lugares diferentes. Isso permite escalar cada parte de forma independente.
- **O desafio do CORS:** Aprendi que o navegador Ã© rigoroso com chamadas entre domÃ­nios diferentes. Configurar os headers `Access-Control-Allow-Origin` corretamente no API Gateway Ã© o que permite essa arquitetura funcionar.
- **Servidores InvisÃ­veis:** A maior vantagem Ã© a paz de espÃ­rito. NÃ£o hÃ¡ sistema operacional para atualizar, nem servidor para monitorar se vai cair. A AWS gerencia toda a infraestrutura embaixo da aplicaÃ§Ã£o.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Lambda | âœ… 1 MilhÃ£o de chamadas/mÃªs | $0,00 |
| Amazon API Gateway | âœ… 1 MilhÃ£o de chamadas/mÃªs | $0,00 |
| Amazon S3 | âœ… Hospedagem gratuita atÃ© 5GB | $0,00 |
| **Total Estimado** | | **$0,00** |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS Lambda` `Amazon API Gateway` `Amazon S3 Static Hosting` `CORS` `Serverless Full-Stack` `Node.js` `ðŸŸ¡ IntermediÃ¡rio`

---

[â† Voltar ao Ã­ndice](../../../README.md)
