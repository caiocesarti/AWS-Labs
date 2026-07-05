<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 03 â€” IntroduÃ§Ã£o ao Amazon API Gateway

## ðŸš€ Resumo
ImplementaÃ§Ã£o de arquitetura Serverless orientada a eventos. Este laboratÃ³rio guia a estruturaÃ§Ã£o de um backend funcional puro (*Backend-as-a-Service*) conectando a orquestraÃ§Ã£o pÃºblica do **Amazon API Gateway** ao processamento sob demanda do **AWS Lambda** (Node.js). ConstruÃ­ um microsserviÃ§o de "FAQ" escalÃ¡vel resolvendo rotas HTTP e entregando *payloads* em JSON, isolando o cÃ³digo interno e rastreando mÃ©tricas vitais pelo **Amazon CloudWatch**.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Software Corporativo / Aplicativos de Atendimento
- **Problema:** Um aplicativo web mantÃ©m um serviÃ§o de "Perguntas Frequentes (FAQ)". Inicialmente, eles alocaram esse serviÃ§o em servidores EC2 rodando ininterruptamente apenas para atender 200 usuÃ¡rios diÃ¡rios. AlÃ©m do custo de servidores ociosos, a arquitetura demorava dias para implantar atualizaÃ§Ãµes no texto e travava se ocorresse um trÃ¡fego simultÃ¢neo acima do esperado na Black Friday.
- **SoluÃ§Ã£o:** Migrei a lÃ³gica do FAQ estritamente para Arquitetura Serverless (*AWS Lambda*). Agora, o cÃ³digo dorme na nuvem sem gerar custo. Configurei o **Amazon API Gateway** para atuar como o "porteiro pÃºblico". Quando ocorre uma chamada HTTP (`GET /faq`), o Gateway acorda a funÃ§Ã£o Lambda instantaneamente, processando o JSON em ~50ms e devolvendo o objeto antes de dormir novamente. Consegui reduzir a fatura de servidores a zero reais mensais com a vantagem do escalonamento orgÃ¢nico ilimitado.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Instanciar receptores frontais provisionando um **Amazon API Gateway** e gerando rotas padrÃ£o *REST*.
- Escrever cÃ³digo computacional ativando uma funÃ§Ã£o serverless transiente **AWS Lambda** rodando rotinas **Node.js**.
- Interligar o Gateway mapeando gatilhos (*Triggers*) que traduzem comandos HTTP `GET` para invocaÃ§Ã£o de servidor interna.
- Configurar *Endpoints PÃºblicos* formatando os pacotes de requisiÃ§Ã£o e resposta em modelos JSON.
- Avaliar mÃ©tricas operacionais rastreando logs de execuÃ§Ã£o pontuais pelo depurador profundo do **Amazon CloudWatch Logs**.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o                | Papel no Lab                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Amazon API Gateway** | Gateway web encarregado de ingerir conexÃµes pÃºblicas, gerir autorizaÃ§Ãµes e trafegar dados de forma roteada. |
| **AWS Lambda**         | Camada Serverless de computaÃ§Ã£o escalÃ¡vel. Executa processos paralelos com base no trigger de acionamento.  |
| **Amazon CloudWatch**  | Ferramenta holÃ­stica de monitoramento extraindo em texto real os consoles logados (`console.log()`).        |

---

## ðŸ—ï¸ Arquitetura da SoluÃ§Ã£o

<div align="center">
  <img src="./assets/architecture-api-gateway-introduction.drawio.png" alt="Arquitetura da SoluÃ§Ã£o" width="700">
</div>

*(O fluxo demonstra como o API Gateway abstrai o acesso de usuÃ¡rios, blindando o processamento do banco local hospedado na Lambda).*

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ Desenvolvimento do NÃºcleo Backend (AWS Lambda)
- **AÃ§Ã£o:** Programei o array dinÃ¢mico em plataforma gerenciada isolando o hardware logÃ­stico.
- **ConfiguraÃ§Ã£o de ExecuÃ§Ã£o:**
  - Ambiente de Software (Runtime): Utilizei a versÃ£o padrÃ£o isolada *Node.js 22.x*.
  - No cÃ³digo `index.js`, criei um Array mapeado aleatoriamente (`Math.random()`) capaz de cuspir respostas diferentes de uma espÃ©cie de "FAQ" simulada, montando um header HTTP correto de reposta contendo blocos JSON lÃ³gicos formatados.
  - O cÃ³digo operacional repousa explÃ­cito neste laboratÃ³rio dentro da pasta: [/src/index.js](./src/index.js).

### 2. ðŸŒ Provisionamento da RecepÃ§Ã£o PÃºblica (API Gateway)
- **AÃ§Ã£o:** Arquitetei a malha de conexÃ£o recebendo tÃºneis abertos de trÃ¡fego convertidos para a rede fechada Lambda.
- **Acoplamento Integrativo:** ConstruÃ­ a associaÃ§Ã£o declarando nativamente dentro dos atributos de "Trigger" da Lambda o anexo do *Amazon API Gateway* com permissÃµes totais via porta aberta `REST`.
- **ExposiÃ§Ã£o Frontend:** Implantei as instÃ¢ncias no espaÃ§o de palco `myDeployment`, habilitando imediatamente a URL Invoker.

### 3. ðŸ” ValidaÃ§Ã£o Endpoint E2E (Execution via CloudWatch)
- **AÃ§Ã£o:** Rastreei e testei empiricamente as variabilidades das rotas formatadas geradas no processo final.
- **IntegraÃ§Ã£o Web Browser:** Abri no navegador a HTTPS URL criada pelo Gateway para avaliar o carregamento cruzado confirmando os retornos com o padrÃ£o de status de transaÃ§Ã£o estrita na rede recebendo um cÃ³digo `HTTP 200`.
- **ExecuÃ§Ãµes Mock Locais (Test Events):** Verifiquei em parelelo se instÃ¢ncias da Lambda quebram enviando pacotes json vazios isoladamente `{}`. O resultado ocorreu bem sucedido pelo console subjacente interno.
- **Auditoria AnalÃ­tica (CloudWatch):** Cruzei a auditoria inspecionando nativamente cada timestamp logado validando exatos milissegundos utilizados visualizando o ambiente via *CloudWatch Streams Logs*.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Lambda Dashboard: Monitoria listando recursos e atestando as funÃ§Ãµes criadas operacionais
<img src="./assets/01-lambda-list.png" width="100%">

### 2. Function Settings: ConfiguraÃ§Ã£o das lÃ³gicas restritivas bloqueando processos perimetrais na plataforma
<img src="./assets/02-lambda-settings.png" width="100%">

### 3. Code Snippet: Espelho do editor integrado do Node.js detalhando os Arrays mapeados geradores de dados
<img src="./assets/03-lambda-code.png" width="100%">

### 4. Trigger Logic: ConfiguraÃ§Ã£o injetando parÃ¢metros operantes da borda conectivo publicamente
<img src="./assets/04-api-gateway-trigger.png" width="100%">

### 5. Deployment URL: VisÃ£o das URLs de destino da API validando protocolos HTTPS estÃ¡ticos
<img src="./assets/05-api-info.png" width="100%">

### 6. Execution verification: Bloco verde nativo ilustrando o Test Event de retorno sem timeouts
<img src="./assets/06-execution-test.png" width="100%">

### 7. Log Groups: Tabela agrupada capturando Grupos de Logs cronolÃ³gicos no CloudWatch
<img src="./assets/07-cloudwatch-logs.png" width="100%">

### 8. Trace Detail: ExtraÃ§Ã£o minuciosa validando mÃ©tricas milissegundos e eficiÃªncia
<img src="./assets/08-log-stream.png" width="100%">
> [!IMPORTANT]
> IDs das contas restritivas atreladas nativamente foram ofuscados mitigando vetores superficiais em cumprimento Ã s diretivas de sigilo de identidade originais.

---

## ðŸ’¡ Principais Aprendizados

- **Custo Operacional Linear:** Avaliei que em uma lambda eu rastreio puramente fraÃ§Ãµes logadas (via CloudWatch). Um cÃ³digo durando singelos 7ms resulta em custos fixos efetivos virtualmente nulos em trÃ¡fegos medianos descartando EC2 ligadas permanentemente.
- **AbstraÃ§Ã£o Direta (Proxy Integration):** A associaÃ§Ã£o de API Gateway provou uma flexibilizaÃ§Ã£o absurda na abstraÃ§Ã£o da lÃ³gica nativa HTTP mascarando a Lambda internamente transformando dados em simples formataÃ§Ã£o padronizada em evento.
- **Rastreabilidade Fina (CloudWatch):** Considerando que as mÃ¡quinas sÃ£o invisÃ­veis, deduzi imediatamente que nÃ£o existem acessos `SSH`. Qualquer debug depende completamente da maestria de atrelar impressÃµes logadas explÃ­citas fluindo no painel dinÃ¢mico log central original.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso            | Free Tier?                                                                          | Custo Estimado |
| ------------------ | ----------------------------------------------------------------------------------- | -------------- |
| AWS Lambda         | âœ… 1 MilhÃ£o requisiÃ§Ãµes mensais + limite generoso logado free permanente             | $0,00          |
| Amazon API Gateway | âœ… Chamadas em camada free de retornos escalonÃ¡veis operacionais (12 Meses Iniciais) | $0,00          |
| Amazon CloudWatch  | âœ… 5GB integrados por log formatados e capturados originais                          | $0,00          |
| **Total Mensal**   |                                                                                     | **$0,00**      |

> âš ï¸ As cotas gratuitas perdoam execuÃ§Ãµes marginais geradas durante os testes da API. Desmanche a *Trigger* apÃ³s finalizados os aprendizados apagando explicitamente os Endpoints REST e limpando a lixeira AWS para reprimir bots varredores randÃ´micos globais de gerar logs nÃ£o autorizados.

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`Amazon API Gateway` `AWS Lambda Core` `Serverless Execution` `REST Integrations` `Node.js Web Arrays` `CloudWatch Profiling` `Cloud Tracing` `ðŸŸ¢ Fundamental`

---

[â† Voltar ao Ã­ndice](../../../README.md)
