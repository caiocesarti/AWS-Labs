<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 05 — Tópico SNS, Filas SQS e Dead-Letter Queue (DLQ)

## 🚀 Resumo
Mensageria Assíncrona e Resiliência Distribuída: Neste laboratório, implementei uma arquitetura de mensageria altamente resiliente utilizando **Amazon SNS** e **Amazon SQS**. Configurei um modelo Pub/Sub para desacoplar a comunicação entre serviços e implementei uma **Dead-Letter Queue (DLQ)** para gerenciar falhas. Garanti a tolerância a erros através de uma **Redrive Policy**, permitindo que mensagens que falham no processamento sejam isoladas para análise sem interromper o fluxo principal do sistema.

---

## 💼 Caso de Uso Real
- **Indústria:** Processamento Financeiro e Microserviços
- **Problema:** Um sistema monolítico de cobrança tentava processar milhares de boletos em lote. Se um único boleto estivesse com dados corrompidos, o script de PDF travava e toda a fila de processamento parava, atrasando a entrega de todos os outros boletos válidos e gerando prejuízo operacional.
- **Solução:** Desacoplei o sistema utilizando SQS e SNS. Agora, cada pedido de boleto é uma mensagem individual. Se um boleto falha (por exemplo, 3 vezes seguidas), a Fila Principal o remove e o envia automaticamente para uma **Fila de Mensagens Mortas (DLQ)**. Isso permite que o sistema continue processando os próximos boletos normalmente, enquanto eu posso analisar calmamente apenas as mensagens que falharam na DLQ para corrigir o erro de dados específico.

---

## 🎯 Objetivos de Aprendizado

- Criar e configurar **Tópicos SNS** para distribuição de mensagens (Fan-out).
- Provisionar **Filas SQS** padrão para armazenamento assíncrono de tarefas.
- Implementar **Dead-Letter Queues (DLQ)** para isolamento de mensagens problemáticas (Poison Messages).
- Configurar **Redrive Policies** com o parâmetro `maxReceiveCount` para controle de tentativas de reprocessamento.
- Aplicar **Resource-Based Policies** no SQS para permitir que o SNS envie mensagens para a fila com segurança.
- Simular falhas de processamento e validar a migração automática de mensagens para a DLQ.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon SNS** | Barramento de notificações que distribui mensagens para os assinantes. |
| **Amazon SQS** | Filas de processamento (Principal) e de contingência (DLQ). |
| **AWS IAM** | Políticas de acesso para permitir a integração segura entre SNS e SQS. |

---

## 🏗️ Arquitetura Pub/Sub + DLQ

<div align="center">
  <img src="./assets/architecture-sns-sqs-dlq.drawio.png" alt="Arquitetura SNS + SQS DLQ" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. ⚙️ Estrutura de Filas (SQS)
- **Ação:** Criei duas filas: `Orders_Queue` e `Orders_DLQ`.
- **Configuração:** Na fila principal (`Orders_Queue`), ativei a Dead-Letter Queue selecionando a `Orders_DLQ` e defini o `Maximum receives` como 3.

### 2. 🛡️ Canal de Distribuição (SNS)
- **Ação:** Criei um tópico SNS chamado `Order_Events`.
- **Assinatura:** Adicionei a `Orders_Queue` como assinante deste tópico.
- **Permissão:** Atualizei a Access Policy da fila SQS para permitir que o ARN do meu tópico SNS execute a ação `sqs:SendMessage`.

### 3. 🔍 Simulação de "Mensagem Venenosa"
- **Ação:** Enviei uma mensagem de teste pelo console do SNS.
- **Falha Controlada:** No console do SQS, visualizei a mensagem, mas não a apaguei (simulando um erro no worker que não consegue completar o processamento). Repeti o processo de "leitura" 3 vezes.

### 4. 🧰 Verificação da DLQ
- **Resultado:** Após a terceira tentativa frustrada, a mensagem desapareceu da fila principal e apareceu instantaneamente na `Orders_DLQ`, provando que o mecanismo de Redrive funcionou e a mensagem foi isolada com sucesso.

---

## 📸 Evidências de Execução

### 1. Criação das Filas SQS
<img src="./assets/01-create-queues.png" width="100%">

### 2. Configuração da DLQ
<img src="./assets/02-create-queue-dlq.png" width="100%">

### 3. Configuração da Fila Principal e Redrive Policy
<img src="./assets/03-create-queue-principal.png" width="100%">

### 4. Criação do Tópico SNS
<img src="./assets/04-create-topic.png" width="100%">

### 5. Inscrição (Subscription) da Fila no Tópico
<img src="./assets/05-create-subscription.png" width="100%">

### 6. Edição da Access Policy da Fila
<img src="./assets/06-edit-queue-policy.png" width="100%">

### 7. Teste de Publicação de Mensagem no SNS
<img src="./assets/07-publish-message.png" width="100%">

### 8. Mensagem Enviada e Disponível na Fila
<img src="./assets/08-send-and-receive-messages.png" width="100%">

### 9. Mensagem Isolada na DLQ Após Falhas
<img src="./assets/09-overview-sqs-dlq.png" width="100%">

### 10. Visão Geral da Fila Principal
<img src="./assets/10-overview-sqs-principal.png" width="100%">

### 11. Visão Geral do Tópico SNS
<img src="./assets/11-overview-sns-topic.png" width="100%">

---

## 💡 Principais Aprendizados

- **Resiliência Sistemática:** O uso de DLQ evita o travamento de workers. Se uma mensagem é "perversa" e quebra o código, ela não deve ficar bloqueando outras mensagens saudáveis para sempre.
- **O Princípio do Desacoplamento:** O SNS não precisa saber se a fila está cheia ou offline. Ele entrega a mensagem e o SQS garante a retenção até que o processamento seja possível.
- **Políticas de Acesso (IAM):** Entendi que para o SNS falar com o SQS, não basta apenas "assinar", é preciso que a Fila dê autorização explícita para o Tópico escrever nela.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| Amazon SNS | ✅ 1 Milhão de publicações gratuitas/mês | $0.00 |
| Amazon SQS | ✅ 1 Milhão de requisições gratuitas/mês | $0.00 |
| **Total Estimado** | | **$0.00** |

---

## 🏷️ Competências Demonstradas

`Amazon SNS` `Amazon SQS` `Dead-Letter Queue (DLQ)` `Assíncronismo` `Microserviços` `Resiliência de Dados` `🟡 Intermediário`

---

## 📜 Alinhamento com Certificações

- **DVA-C02:** Domínio 1 — Desenvolvimento com Serviços AWS (Mensageria)
- **SAA-C03:** Domínio 2 — Design de Arquiteturas Resilientes

---

[← Voltar ao índice](../../../README.md)
