<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 04 â€” Criando um OrÃ§amento na AWS com Budgets

## ðŸš€ Resumo
GovernanÃ§a de Custos e FinOps: Neste laboratÃ³rio, configurei um orÃ§amento mensal proativo na minha infraestrutura AWS utilizando o **AWS Budgets**. Defini limites personalizados para monitorar o faturamento e emitir alertas automÃ¡ticos por e-mail, protegendo o ambiente contra gastos inesperados causados por esquecimentos ou erros de configuraÃ§Ã£o.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** FinOps (OperaÃ§Ãµes Financeiras na Nuvem)
- **Problema:** Desenvolvedores de uma startup provisionaram instÃ¢ncias RDS e EC2 potentes para um teste de carga no final de semana e esqueceram de desligÃ¡-las. No final do mÃªs, a empresa recebeu uma conta de US$ 2.400,00 por hardware que ficou ligado ociosamente.
- **SoluÃ§Ã£o:** Implementei uma regra de faturamento usando o AWS Budgets. Fixei um teto de gastos para o ambiente de testes. Se o sistema detectar que o custo real ultrapassou 10% do limite, ou se a previsÃ£o (Forecast) indicar que o orÃ§amento serÃ¡ estourado atÃ© o fim do mÃªs, ele dispara e-mails de alerta para mim. Isso permite que eu interrompa os recursos no momento em que o gasto foge do controle, economizando milhares de dÃ³lares em desperdÃ­cio.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Compreender o modelo de pagamento por uso da AWS e a necessidade de monitoramento.
- Navegar pelo painel de **Billing and Cost Management** e configurar orÃ§amentos.
- Criar **Cost Budgets** (orÃ§amentos de custo) com valores absolutos.
- Diferenciar entre alertas de custos "Reais" (Actual) e "Previstos" (Forecasted).
- Configurar notificaÃ§Ãµes automÃ¡ticas por e-mail integradas ao sistema de billing.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS Budgets** | Ferramenta principal para criaÃ§Ã£o e monitoramento do teto de gastos. |
| **Amazon SNS** | (Back-end) ResponsÃ¡vel por processar e enviar os alertas de e-mail. |

---

## ðŸ—ï¸ Arquitetura da SoluÃ§Ã£o

<div align="center">
  <img src="./assets/architecture-aws-budgets.drawio.png" alt="Arquitetura da SoluÃ§Ã£o" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ ConfiguraÃ§Ã£o do OrÃ§amento
- **AÃ§Ã£o:** Acessei o dashboard de Budgets e criei um novo "Cost Budget".
- **ImplementaÃ§Ã£o:** Defini um perÃ­odo mensal recorrente e estipulei um teto de seguranÃ§a de **US$ 10,00** para proteger minha conta contra surpresas no cartÃ£o de crÃ©dito.

### 2. ðŸ›¡ï¸ DefiniÃ§Ã£o de Alertas (Thresholds)
- **AÃ§Ã£o:** Configurei as regras de notificaÃ§Ã£o para que o orÃ§amento nÃ£o fosse apenas um grÃ¡fico passivo.
- **ConfiguraÃ§Ã£o:** Defini que, assim que o gasto real atingir 10% do total (US$ 1,00), um e-mail deve ser enviado imediatamente para meu endereÃ§o pessoal.

### 3. ðŸ” ValidaÃ§Ã£o Final
- **AÃ§Ã£o:** Revisei o sumÃ¡rio do orÃ§amento. O console confirmou a ativaÃ§Ã£o do rastreador, mostrando o consumo atual em 0%. Agora, qualquer recurso que eu esquecer de desligar serÃ¡ "delatado" pelo sistema antes que o custo se torne um problema.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Budget Overview: Painel geral de Budgets com o meu orÃ§amento ativo e configurado
<img src="./assets/01-overview-aws-budgets.png" width="100%">

### 2. Alert Threshold: Ajuste do limite de 10% para disparo do alerta real
<img src="./assets/02-edit-budget-step1.png" width="100%">

### 3. Notification Setup: ConfiguraÃ§Ã£o das aÃ§Ãµes automÃ¡ticas opcionais
<img src="./assets/03-edit-budget-step2.png" width="100%">

### 4. Final Security Review: RevisÃ£o final dos parÃ¢metros de proteÃ§Ã£o financeira
<img src="./assets/04-edit-budget-revisao.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Nuvem nÃ£o Ã© On-Premise:** Em infraestrutura prÃ³pria, um servidor ligado "nÃ£o custa mais" no fim do mÃªs. Na AWS, cada minuto conta. O Budget educa o arquiteto a ter uma mentalidade de economia (FinOps).
- **SeguranÃ§a para LaboratÃ³rios:** Todo ambiente de estudo precisa de um teto financeiro. Isso evita que um erro tÃ©cnico resulte em uma dÃ­vida financeira real.
- **AutomaÃ§Ã£o de Bloqueio:** Descobri que Ã© possÃ­vel configurar o Budgets para, alÃ©m de enviar e-mail, disparar uma Lambda que desliga as instÃ¢ncias automaticamente quando o custo atinge o teto (Shutdown preventivo).

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Budgets | âœ… Os 2 primeiros orÃ§amentos sÃ£o gratuitos vitaliciamente | $0,00 |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS Budgets` `GestÃ£o de Custos` `FinOps` `Billing & Cost Explorer` `Alertas de E-mail` `ðŸŸ¢ Fundamental`

---

[â† Voltar ao Ã­ndice](../../../README.md)
