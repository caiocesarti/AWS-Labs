<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 02 — Pesquisando e Criando Fluxos com o Amazon Quick

## 🚀 Resumo
Exploração dos recursos de **Pesquisa com IA** e **Fluxos automatizados** do Amazon Quick para automatizar tarefas de RH com múltiplos agentes, integrações de API, lógica condicional e pesquisa aprofundada com citações:
- **Quick Research:** Geração de relatórios de pesquisa abrangentes com fontes da web e dados internos da empresa.
- **Quick Flows:** Criação de fluxos automatizados a partir de conversas em linguagem natural, com etapas condicionais e chamadas de API.
- **Conectores de Ação (OpenAPI):** Integração do Quick com APIs externas para gerenciamento de funcionários, férias, calendário e vagas.
- **Fluxo de Integração de Funcionários:** Automação completa de onboarding — criação de registro, e-mail de boas-vindas e chamado de TI em um único fluxo.

---

## 💼 Caso de Uso Real
- **Indústria:** Recursos Humanos / Serviços Corporativos
- **Problema:** Paulo, diretor de RH da AnyCompany, passa horas semanais pesquisando informações em fontes internas e externas. Funcionários enfrentam dificuldades com ferramentas existentes para tarefas como gestão de férias, criação de eventos e gestão de vagas. A equipe de RH cria manualmente registros de funcionários, envia e-mails de boas-vindas e solicita crachás para novos contratados várias vezes por semana.
- **Solução:** Utilização do Amazon Quick Research para pesquisas guiadas por IA, Quick Flows para automação de processos multi-etapas e conectores OpenAPI para integração com sistemas internos de RH — tudo orquestrado via linguagem natural.

---

## 🎯 Objetivos de Aprendizado

*   Criar **relatórios de pesquisa** abrangentes usando o Amazon Quick Research.
*   Criar um **fluxo simples** a partir de uma conversa de chat.
*   **Integrar** o Amazon Quick a sistemas externos via conectores OpenAPI.
*   Projetar **fluxos de trabalho com várias etapas**, combinando chamadas de API, pesquisas na web e geração de conteúdo.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon Quick** | Plataforma de BI com chat, pesquisa, fluxos e agentes de IA generativa. |
| **Quick Research** | Motor de pesquisa com IA para relatórios abrangentes baseados em citações. |
| **Quick Flows** | Automação de fluxos de trabalho multi-etapas com lógica condicional. |
| **Quick Spaces** | Coleções organizadas de documentos pesquisáveis. |
| **Quick Connectors (OpenAPI)** | Integração com APIs externas via especificação OpenAPI. |
| **Amazon S3** | Armazenamento dos materiais do workshop para download inicial. |
| **Amazon Cognito** | Autenticação OAuth2 para a API de RH integrada. |
| **Amazon API Gateway** | API REST de RH consumida pelo Quick via conector. |
| **AWS IAM** | Gerenciamento de usuários e permissões de acesso. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture.webp" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 📂 Preparação dos Espaços e Materiais
- **Download de materiais:** Baixei os arquivos do workshop — `api-details.txt` e `api-schema.json` do bucket S3 `api-artifacts`, e `hr_files.zip` contendo os documentos de RH via link direto.
- **Criação dos Espaços:**
  - **RH - Políticas da Empresa:** Espaço com descrição `Repositório central para políticas e procedimentos de RH de toda a empresa`, contendo: `employee_handbook.pdf`, `leave_policy.pdf`, `performance_review_guidelines.pdf`, `public_holidays.csv`.
  - **RH - Operações:** Espaço com descrição `Dados operacionais de RH, análises e procedimentos internos`, contendo: `onboarding_checklist.pdf`, `employee_feedback_full_dataset.pdf`.

### 2. 🔍 Pesquisa Guiada por IA com Quick Research
- **Objetivo da pesquisa:** "Quais são as melhores práticas atuais para políticas de trabalho remoto em empresas de tecnologia de médio porte, incluindo medição de produtividade, ferramentas de colaboração e considerações sobre equilíbrio entre vida profissional e pessoal?"
- **Configuração de fontes:** Ativei pesquisa na web com preferência por sites de notícias e periódicos acadêmicos, excluindo mídias sociais e blogs. Conectei o espaço *RH - Políticas da Empresa* como recurso Quick.
- **Refinamento do plano:** Adicionei instruções para incluir seção sobre considerações legais e análise comparativa entre abordagens de diferentes indústrias.
- **Execução:** Iniciei a pesquisa que gerou um relatório estruturado com citações verificáveis, tópicos navegáveis e possibilidade de exportação em PDF/Word.

### 3. 🔄 Criação de Fluxo a partir de um Chat
- **Consulta inicial:** Fiz perguntas sobre o processo de integração na AnyCompany com prompts vinculados aos Espaços de RH.
- **Geração do fluxo:** A partir da conversa, criei um Quick Flow com o prompt: *"Gere um fluxo que receba perguntas específicas de integração e forneça respostas detalhadas sobre os processos de integração de funcionários, utilizando a documentação de RH disponível nos Espaços Rápidos."*
- **Exploração dos elementos:** Identifiquei os componentes: entrada de texto, saída Quick Data (vinculada a Espaços), saída de Conhecimento Geral, e os tipos de etapas disponíveis (Chat Agent, Research, Web Search, UI Agent, Image, Reasoning Group, App Actions, Files).
- **Execução:** Testei o fluxo com a pergunta *"Qual é a responsabilidade dos novos contratados e de seus gerentes no primeiro dia de trabalho?"* e validei as saídas passo a passo.

### 4. 🔌 Integração da API via Conector de Ação
- **Configuração do conector:** Criei a integração `API de RH` usando a especificação OpenAPI (`api-schema.json`) com autenticação OAuth2 (Client ID, Client Secret, Token URL, Authorization URL do `api-details.txt`).
- **Autenticação:** Realizei login via Amazon Cognito com as credenciais do `api-details.txt` e confirmei status "Conectado".
- **Teste da API:** Executei a ação `ListarVagasDeEmprego` e confirmei o retorno com 3 vagas (Sales Manager, Senior Software Engineer, Marketing Manager) com status HTTP 200.
- **Interação por linguagem natural:**
  - *"Quais vagas de emprego estão abertas no momento?"* — listou as vagas via integração.
  - *"Preciso solicitar férias para a próxima semana, de terça a quarta-feira"* — gerou formulário para `CreateTimeOffRequest`.
  - *"Quem é o empresário de John Stiles?"* — consultou a API para buscar o gerente.

### 5. 🏗️ Criação do Fluxo de Integração de Funcionários
- **Entradas do fluxo:** Criei 7 campos de entrada de texto — Nome, Sobrenome, E-mail, Departamento, Cargo, Data de Contratação e E-mail do Gerente.
- **Verificação de duplicidade:** Etapa `Verificar se o funcionário existe` via ação `ListarFuncionários` da API de RH com filtragem por e-mail.
- **Grupo de Raciocínio:** Configurei lógica condicional `Fluxo de Criação de Funcionários` para executar as etapas seguintes apenas se o e-mail não for encontrado.
- **Criação de registro:** Etapa `Criar registro de funcionário` via ação `CriarFuncionário` com os dados dos campos de entrada.
- **E-mail de boas-vindas:** Geração personalizada usando o espaço *RH - Políticas da Empresa* como fonte + envio via ação `EnviarEmail` com cópia para o gerente.
- **Chamado de TI:** Geração de ticket de solicitação de crachá com prioridade condicional (Alta se a data de contratação for até 7 dias) + criação via ação `CriarTicket`.
- **Resumo:** Etapa final de conhecimento geral consolidando todas as ações realizadas.

### 6. ✅ Teste do Fluxo Completo
- **Dados de teste:** Executei o fluxo para Martha Rivera — Engenheira de Software, Departamento de Engenharia, data de contratação 2025-12-01, gerente `akua_mansa@anycompany.com`.
- **Validação:** Confirmei que todas as etapas foram concluídas com sucesso:
  - Verificação de existência no sistema.
  - Criação do registro do funcionário.
  - Geração e envio do e-mail de boas-vindas personalizado.
  - Criação do chamado de TI para configuração de crachá.
  - Resumo completo de integração.

### 7. 📊 Revisão da Pesquisa
- **Revisão do relatório:** Analisei o relatório completo gerado pelo Quick Research com tópicos navegáveis no painel lateral e citações numeradas com links para as fontes.
- **Exportação:** Validei as opções de compartilhamento (PDF, Word, compartilhamento com outros usuários).
- **Resumo executivo:** Gerei um resumo executivo automatizado a partir do relatório.
- **Iteração:** Testei o recurso de comentários em texto para solicitar aprimoramentos em iterações subsequentes.

---

## 📸 Evidências de Execução

### 1. Quick Research — configuração de objetivo e fontes de pesquisa
<img src="./assets/01-research-config.webp" width="100%">

### 2. Quick Research — relatório completo com tópicos e citações
<img src="./assets/02-research-report.webp" width="100%">

### 3. Fluxo gerado a partir do chat — componentes e etapas
<img src="./assets/03-flow-from-chat.webp" width="100%">

### 4. Execução do fluxo de chat — saída com fontes referenciadas
<img src="./assets/04-flow-run-output.webp" width="100%">

### 5. Conector de Ação — configuração da integração OpenAPI
<img src="./assets/05-connector-config.webp" width="100%">

### 6. Teste da API — ListarVagasDeEmprego com resposta HTTP 200
<img src="./assets/06-api-test-jobs.webp" width="100%">

### 7. Chat com integração — consulta de vagas via linguagem natural
<img src="./assets/07-chat-api-jobs.webp" width="100%">

### 8. Fluxo de Integração — visão completa com todas as etapas
<img src="./assets/08-onboarding-flow-full.webp" width="100%">

### 9. Grupo de Raciocínio — lógica condicional para criação de funcionário
<img src="./assets/09-reasoning-group.webp" width="100%">

### 10. Execução do fluxo de integração — resumo final
<img src="./assets/10-onboarding-run-summary.webp" width="100%">

> [!IMPORTANT]
> Alguns identificadores foram mascarados por boas práticas de segurança.

---

## 💡 Principais Aprendizados

*   **Quick Research automatiza pesquisas complexas:** O motor de pesquisa com IA gera relatórios estruturados com citações verificáveis, combinando fontes da web com dados internos organizados em Espaços.
*   **Fluxos a partir de linguagem natural:** Conversas de chat podem ser transformadas em fluxos automatizados, decompostos em etapas individuais com tipos especializados (Dados, Conhecimento Geral, Ações, Raciocínio).
*   **Conectores OpenAPI ampliam o alcance:** A integração via especificação OpenAPI permite que o Quick interaja com qualquer API REST autenticada, executando operações CRUD por linguagem natural.
*   **Grupos de Raciocínio adicionam lógica:** Permitem ramificação condicional dentro dos fluxos, evitando duplicações e garantindo fluxos idempotentes.
*   **Orquestração end-to-end:** Um único fluxo pode combinar verificações, criação de registros, geração de conteúdo com IA, envio de e-mails e criação de chamados — substituindo processos manuais que levariam dias.

---

## 🔗 Recursos Adicionais

- [Amazon Quick User Guide](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
- [Amazon Quick Flows](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-flows.html)
- [Amazon Quick Research](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-research.html)
- [Amazon Quick Connectors](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-q-connectors.html)
- [OpenAPI Specification](https://swagger.io/specification/)
- [AWS Training and Certification](https://aws.amazon.com/training/)

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| Amazon Quick (Enterprise) | ⚠️ Trial 30 dias | Sob demanda |
| API Gateway (API de RH) | ✅ 1M req/mês | $0,00 |
| Amazon Cognito (autenticação) | ✅ 50K MAUs | $0,00 |
| S3 (materiais do workshop) | ✅ 5GB/mês | $0,00 |
| IAM (usuários) | ✅ Gratuito | $0,00 |
| **Total** | | **Variável** |

> ⚠️ Lembre-se de limpar os recursos após o lab para evitar cobranças.

---

## 🏷️ Competências Demonstradas

`Amazon Quick` `Quick Research` `Quick Flows` `Quick Connectors` `OpenAPI` `Generative AI` `RAG` `Multi-Agent Workflows` `API Integration` `Amazon Cognito` `API Gateway` `IAM` `S3` `🟡 Intermediário`

---

## 📎 Referência

> Este laboratório foi realizado na plataforma [AWS Skill Builder](https://skillbuilder.aws/learn).
> **Código:** SPL-TF-100-MLFLQU-1 — Versão 1.0.3

---

[← Voltar ao índice](../../../README.md)
