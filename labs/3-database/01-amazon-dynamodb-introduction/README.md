<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 01 — Introdução ao Amazon DynamoDB: Modelagem NoSQL e Estrutura de Chaves

## 🚀 Resumo
Implantação de banco de dados não-relacional (NoSQL) de altíssima performance. Este laboratório abrange a modelagem arquitetônica baseada em *Composite Primary Keys* (Partition + Sort Keys), submissão de atributos heterogêneos sem esquema definido (*Schema-less*), e analisa diretamente a eficiência computacional confrontando metodologias de extração vetorial entre `Query` vs `Scan`.

---

## 💼 Caso de Uso Real
- **Indústria:** Plataformas de Streaming Musical / EdTechs
- **Problema:** Um aplicativo de streaming emergente usa um banco de dados relacional clássico (SQL) para indexar dezenas de milhões de músicas escutadas diariamente pelos usuários. Em horários de pico, milhões de inserts travam o banco, que exige colunas rígidas (esquema engessado) resultando em perda de dados e quedas no aplicativo.
- **Solução:** Migração do catálogo para o **Amazon DynamoDB**. Ao configurar as Chaves Primárias corretamente (`Artist` + `Song`), dividi o banco em partições para atingir latência paralela abaixo de 10 milissegundos. Como é *schema-less*, novas músicas podem vir com atributos extras (`Features`, `Genre`, `BPM`) organicamente. Adotando consultas estritas via chaves primárias (`Query`), anulei o custo de varreduras globais (`Scan`).

---

## 🎯 Objetivos de Aprendizado

- Instanciar infraestrutura puramente *Serverless* lançando Tabelas NoSQL sem provisionar servidores subjacentes.
- Compreender a matriz de fragmentação gerindo a combinação de uma **Partition Key** atuando com uma **Sort Key** auxiliar.
- Interagir através da API nativa injetando atributos em formato JSON bruto, explorando a natureza heterogênea das colunas omitidas.
- Diferenciar cenários de custo severo mensurando a operação global de **Scan**, versus o caminho indexado exato utilizando **Query**.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon DynamoDB** | Banco de Dados NoSQL Serverless operando com latência contínua na casa de milissegundos de um dígito. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-amazon-dynamodb-introduction.drawio.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 📋 Criação do Repositório (NoSQL Table)
- **Ação:** Instanciei a tabela base.
- **Configurações Fundamentais:** Defini o nome como `Music`. Fixei a Chave de Partição (*Hash Key*) no atributo `Artist`. Modelei a Chave de Classificação (*Range Key*) com o atributo secundário `Song`. 
- **Conceito Arquiteto:** Somadas, ambas formam a identificação única do item impedindo sobreposições da minha base.

### 2. 🗄️ Injeção de Dados Assíncrona (Put Items)
Aproveitei a elasticidade da nativa modelagem inserindo dados heterogêneos:
- **Pink Floyd / Money:** Adicionei dados simples como `Album` e `Year`.
- **John Lennon / Imagine:** Incluí um novo atributo orgânico (`Genre`) inativo globalmente na tabela.
- **Psy / Gangnam Style:** Ingeri um modelo comportando uma estrutura focada em duração (`Duration in seconds`).
- **Efeito:** Sem a necessidade do clássico `ALTER TABLE`. Todo item operou para mim como um micro-documento JSON isolado.

### 3. 🔍 Eficiência Computacional (Query vs Scan)
Prova real das diferenças perimetrais:
- **Query (Consulta Estrutural):** Pedi exatamente pelo Partition e Sort Key. Confirmei que o motor acessa rapidamente o endereço que gerencia aquela música específica.
- **Scan (Verificação Bruta):** Ordenei via console um varrimento total mirando o ano (`Year: 1973`). Validei que, sem o auxílio da chave primária, a base percorre todo o ecossistema consumindo créditos absurdos.

---

## 📸 Evidências de Execução

### 1. Traçado direto de arquitetura no painel fixando a Matriz Composta (Partition + Sort Keys)
<img src="./assets/Table-Music-Amazon-DynamoDB.png" width="100%">

### 2. Interface tabular desvendando a injeção schema-less
<img src="./assets/Items-Amazon-DynamoDB.png" width="100%">

### 3. Formulário de API focado na variação e edição unitária em hot-state do documento associado sem travar o banco
<img src="./assets/Item-Psy-edit-Amazon-DynamoDB.png" width="100%">

### 4. Extração matemática cirúrgica via Query
<img src="./assets/Items-Query-Amazon-DynamoDB.png" width="100%">

### 5. Visualização analítica do comando ineficiente Scan
<img src="./assets/Items-Scan-Amazon-DynamoDB.png" width="100%">

> [!IMPORTANT]
> Em contas produtivas, varreduras `Scan` frequentemente exaurem o limite massivo financeiro da nuvem.

---

## 💡 Principais Aprendizados

- **NoSQL Impõe Modelagem Preventiva:** Aprendi que não questiono o DynamoDB no momento da leitura (com `JOINs` massivos); eu pré-estruturo os dados com a arquitetura `Partition+Sort Key` alinhada visando as Extrações futuras (*Access Patterns*).
- **Sem Servidor, sem Patch, sem Espera:** Percebi que provisionar a Tabela significa iniciar as entregas na mesma hora. Diferente do RDS instanciando motores inteiros, recebo meu EndPoint nativo.
- **Flexibilidade com Schema-less:** Comprovei que novas métricas individualizadas não prejudicam as matrizes com bytes inativos preenchendo colunas vazias de registros antigos.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| DynamoDB (On-Demand) | ✅ 25 WCUs + 25 RCUs gratuitos continuamente (e atrelados a 25GB) | $0,00 |
| **Total** | | **$0,00** |

---

## 🏷️ Competências Demonstradas

`DynamoDB` `NoSQL` `Partition Key` `Sort Key` `Query` `Scan` `Schema-less` `Serverless Storage` `🟢 Fundamental`

---

[← Voltar ao índice](../../../README.md)
