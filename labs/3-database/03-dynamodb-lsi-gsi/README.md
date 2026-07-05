<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 03 — DynamoDB: Índices Secundários Locais (LSI) e Globais (GSI)

## 🚀 Resumo
Dominância em modelagem de dados avançada e otimização de performance (*Performance Tuning*) no Amazon DynamoDB. Confrontei empiricamente o desperdício computacional de varreduras amplas (*Scans*) contra a eficiência de consultas indexadas (*Queries*). Expandi a arquitetura NoSQL criando Índices Secundários Locais (LSI) no nascimento da tabela, e Índices Secundários Globais (GSI) elásticos, operando injeções de arquivos JSON nativamente via AWS CloudShell.

---

## 💼 Caso de Uso Real
- **Indústria:** E-commerce / Logística
- **Problema:** Um sistema de registro de "Pedidos" foi criado no DynamoDB usando `ID do Cliente` (Partition Key) e `Data do Pedido` (Sort Key). Ele funciona perfeitamente para clientes consultando seu histórico de compras. Contudo, a equipe financeira precisa gerar um relatório isolando **todos** os pedidos que estão "Entregues" ordenados por "Valor". Como o filtro foge da *Partition Key* principal, a aplicação força operações de `Scan`. Resultado: a cada requisição, a aplicação varre milhões de pedidos para encontrar a minoria que está entregue, esgotando a capacidade (RCU) e travando a plataforma.
- **Solução:** Reengenharia orientada aos Padrões de Acesso (*Access Patterns*). Em vez de `Scans` ineficientes, injetei um **LSI** para permitir buscar pedidos do mesmo cliente por "Status". Mais importante, construí um **GSI (Global Secondary Index)** em paralelo, que atua como uma "tabela sombra". Esse GSI transforma o `Status` ("Entregue") na Partition Key primária e o `Valor Total` na Sort Key. Agora, a query financeira atinge apenas os pedidos entregues indexados em ordem de valor, operando de forma 100% eficiente e custos baixíssimos, independentemente do volume do banco.

---

## 🎯 Objetivos de Aprendizado

- Consolidar tabelas robustas fixando padrões primários da correlação **Chave de Partição (PK)** e **Chave de Classificação/Ordenação (SK)**.
- Forjar um **LSI (Índice Secundário Local)** limitando filtros de reordenação estruturais restritos à hierarquia original da Partition Key.
- Arquitetar um **GSI (Índice Secundário Global)** transcendendo limites físicos nativos definindo Chaves de Partição inteiramente novas.
- Evidenciar a ineficiência financeira extraindo blocos consumindo *Unidades de Leitura (RCU)* em massa por um **Scan** contra a **Eficiência Máxima (100%)** do comando **Query**.
- Provisionar de forma ágil injetando dados via `aws dynamodb batch-write-item` carregando JSON brutos pela linha de comando CloudShell.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon DynamoDB** | Motor *Serverless* providenciando as frações independentes espelhando dados sincronizados em visões locais e globais LSI/GSI. |
| **AWS CloudShell** | Máquina virtual embarcada na sub-rede console executando scripts de integração em massa nativamente habilitada com IAM ativo. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-dynamodb-lsi-gsi.drawio.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 📋 Criação do Repositório Transacional e LSI
- **Ação:** Criei a tabela base `Pedido-<seunome>`.
- **Eixos Nativos:** Definidas as chaves apontando para `ID do Usuario` (String) e ordenação secundária exigindo `Data do Pedido` (String).
- **LSI Coupling:** Atrelei unicamente no instante da criação o índice Local (`LSI-PedidoseunomeStatus`). Ele acata a PK nativa (ID), mas altera a ordenação de busca visando extrair o campo `Status`.

### 2. 🗄️ Injeção de Dados em Lote (AWS CloudShell)
- **Ação:** Preenchimento de dados simulando volume e dispensando cliques manuais.
- **Integração:** Invoquei o terminal CloudShell criando um arquivo `pedidos_import.json` e atirei carga na AWS rodando o comando: `aws dynamodb batch-write-item`.
- **Validação:** A ferramenta retornou um objeto `UnprocessedItems: {}` nulo, atestando que os 25 itens foram indexados perfeitamente em massa.

### 3. 🔍 A Ferida Aberta: SCAN vs QUERY
- **Ação:** Executei comparativos validando otimização (*Performance Tuning*).
- **A Falha do Scan:** Busquei por registros do "Usuário 001" rodando via interface gráfica uma execução de *Scan*. A base varreu os arquivos matrizes ponta a ponta e me relatou apenas **"Eficiência 11.54%"** — Lemos tráfego inútil para pescar o item alvo isolado.
- **A Retomada via Query:** Passando a identificação estrutural (U001) e forçando uma *Query*, a extração operou direto na partição física gravando expressivos **"Eficiência 100%"**.

### 4. 🔗 O Poder das Sombras (Índices GSI)
- **Ação:** Resolução para relatórios fora do padrão da Partition Key (ex: compras com `Status = Entregue` somadas a `ValorTotal >= 60`, descartando o ID do cliente).
- **O GSI:** Construí um novo índice (GSI Global) mudando absolutamente a base primária e definindo como chave principal o atributo genérico `Status`, sub-ordenado pelo número de `ValorTotal`.
- **Query Estrita no GSI:** Apontei a console para o novo índice GSI, inseri `Entregue` e cruzei `> 60`. O resultado fluiu de primeira registrando os faturamentos sem qualquer varredura vazia pelos demais itens ("Cancelado", etc).

---

## 📸 Evidências de Execução

### 1. Provisionamento Base: Configuração da tabela com Partition (UserID) e Sort Key (OrderDate)
<img src="./assets/01-create-table-principal.png" width="100%">

### 2. Definição do LSI: Índice Secundário Local para ordenação por Status
<img src="./assets/02-create-lsi-index.png" width="100%">

### 3. Estrutura de Item: Validação manual dos atributos antes da carga massiva
<img src="./assets/03-create-manual-item.png" width="100%">

### 4. Acesso ao CloudShell: Preparação do ambiente CLI para ingestão via JSON
<img src="./assets/04-open-cloudshell.png" width="100%">

### 5. Ingestão em Lote: Execução do `batch-write-item` para popular a tabela
<img src="./assets/05-batch-write-item-cli.png" width="100%">

### 6. Carga Finalizada: Itens indexados e prontos para consulta
<img src="./assets/06-items-returned-gui.png" width="100%">

### 7. Ineficiência Operacional (Scan): Alto consumo de RCU ao varrer toda a tabela
<img src="./assets/07-scan-operation-inefficient.png" width="100%">

### 8. Alta Performance (Query): Extração cirúrgica com 100% de eficiência
<img src="./assets/08-query-operation-efficient.png" width="100%">

### 9. Consulta via LSI: Filtragem por Status de forma otimizada
<img src="./assets/09-query-lsi-index.png" width="100%">

### 10. Expansão para GSI: Índice global para consultas transversais
<img src="./assets/10-create-gsi-index.png" width="100%">

### 11. Consulta Global GSI: Resgate independente da partição primária
<img src="./assets/11-query-gsi-index.png" width="100%">

### 12. Resumo: Painel com a estrutura completa de índices ativos
<img src="./assets/12-table-summary-dynamodb.png" width="100%">

> [!IMPORTANT]
> IDs absolutos e informações sensíveis de conta foram preservados através de tarjas pretas (redaction) aplicadas às capturas de tela.
> O *payload* utilizado na carga (`pedidos_import.json`) encontra-se no mapeamento de [/src](./src/).

---

## 💡 Principais Aprendizados

- **O Pecado do Scan:** Comprovei que o DynamoDB penaliza o descaso computacional cobrando fisicamente pelo RCU inteiro da varredura bloco-a-bloco num Scan. Em bases imensas, você pode zerar seus orçamentos. Somente extrações utilizando modelo *Query* provovem viabilidade na arquitetura nativa NoSQL Serverless.
- **Limitações do LSI:** Diferente do paradigma maleável das Clouds, constatei que Índices Secundários Locais (LSI) exigem previsão minuciosa imutável — devem fisicamente ser gerados junto à criação principal *obrigatória* da tabela sem chance para adicionar e editar *Labels* futuros independentes após o deploy primário da mesma.
- **Ressurreição Global:** Testei que Índices Secundários Globais (GSIs) transcendem hierarquias. Eles geram fluxos magnéticos em tabelas sombras com consumos individuais (RCU próprio) que não afetam a matriz e podem ser criados/apagados futuramente durante todo o ciclo de vida da produção dinamicamente.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| DynamoDB (On-Demand) | ✅ LSI é atrelado à tabela pai; GSI consome fluxos paralelos absorvidos perfeitamente dentro da malha das primeiras 25 RCUs/WCUs vitalícias nativas | $0,00 |
| CloudShell | ✅ Totalmente Gratuito | $0,00 |
| **Total** | | **$0,00** |

> ⚠️ Modelos GSI não desmancham na exclusão automática de dependências AWS primárias, você deve selecionar o GSI internamente desmanchá-lo pontualmente para prevenir faturamentos.

---

## 🏷️ Competências Demonstradas

`DynamoDB` `LSI` `GSI` `Query vs Scan` `Performance Tuning` `CloudShell` `AWS CLI` `Data Modeling` `🟡 Intermediário`

---

[← Voltar ao índice](../../../README.md)
