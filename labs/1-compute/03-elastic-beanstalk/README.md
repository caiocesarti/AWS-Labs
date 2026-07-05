<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 03 — AWS Elastic Beanstalk: Implantação de Aplicação PaaS

## 🚀 Resumo
Deploy corporativo de aplicação web utilizando o modelo PaaS (Platform as a Service) gerenciado pela AWS. Elimina-se o gerenciamento de SO e infraestrutura, delegando ao orquestrador do Elastic Beanstalk o provisionamento simultâneo e automatizado do Auto Scaling, EC2, CloudWatch e Load Balancing.

---

## 💼 Caso de Uso Real
- **Indústria:** Agências de Software / Startups Seed
- **Problema:** Uma startup validando seu MVP não possui recursos para manter operações complexas de Cloud/DevOps. Fazer deploy manual em EC2, instalar Python/Node, configurar Nginx e acoplar certificados SSL toma dias de desenvolvimento e apresenta alto risco por má configuração.
- **Solução:** Empacotar o código da aplicação em um `.zip` e enviá-lo para o Elastic Beanstalk. O serviço lê a linguagem, cria grupos de Auto Escala, define políticas de Load Balancer e coloca a URL da aplicação no ar em 5 minutos, permitindo focar 100% no código.

---

## 🎯 Objetivos de Aprendizado

- Implantar ambientes web estruturados desviando de configurações manuais complexas no EC2.
- Atribuir parâmetros operacionais cruciais (`Instance profiles` & `Service Roles`) cumprindo normativas rígidas do IAM.
- Gerenciar atualizações de pacote de código de forma abstrata.
- Monitorar a saúde subjacente da infraestrutura através do console consolidado do Beanstalk.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Elastic Beanstalk** | Plataforma de orquestração primária que gera instâncias EC2 e gerencia a rede logicamente. |
| **AWS IAM** | Governa as `Service Roles` que o Beanstalk assume para conversar via API com o EC2/S3 em background. |
| **Amazon S3** | Armazena de forma nativa — e criptografada — os artefatos de código (.zip) empurrados ao PaaS. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-elastic-beanstalk.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 🌐 Inicialização do Ambiente
- **Ação:** Criei um `Web server environment` no painel do Beanstalk.
- **Configuração:** Selecionei declarativamente a plataforma correspondente ao código fonte (ex: *Python, Node.js, PHP*), eliminando configuração de dependências cruzadas em máquinas limpas.

### 2. 📦 Upload do Artefato
- **Ação:** Em vez de clonar via Git da instância, exportei a branch em formato zip.
- **Configuração:** Acoplei o arquivo fonte `.zip` diretamente via interface gráfica do assistente, que por trás das cortinas é espelhado no S3 para alta durabilidade.

### 3. 🔐 Vinculação de Roles IAM
- **Desafio:** Por segurança (Mínimo Privilégio), a AWS impede que serviços rodem instâncias sem delegação explícita.
- **Ação:** Criei e atrelei as `Service Roles` necessárias (`AWSElasticBeanstalkWebTier`). O Beanstalk ganha os privilégios legais de fabricar perfis EC2 e subir painéis CloudWatch atrelados.

### 4. ⚙️ Orquestração e Lançamento
- **Ação:** Submeti os parâmetros e lancei o *Wizard*.
- **Conclusão:** O motor executa a diagramação completa gerando instâncias, balanceadores e grupos de segurança automáticos. O endpoint de acesso `*.elasticbeanstalk.com` é ativado com status *Healthy*.

### 5. 🧹 Cleanup em Cascata
- **Ação:** Solicitei explicitamente um `Terminate Environment` na raiz do serviço.
- **Resultado:** A mecânica avançada da AWS destrói implacavelmente todas as instâncias filhas, Load Balancers atrelados e Security Groups paralelos sem gerar recursos órfãos.

---

## 📸 Evidências de Execução

### 1. Criação da Service Role no console IAM para permissões subjacentes
<img src="./assets/01-create-role-iam.png" width="100%">

### 2. Atribuição de permissões AWSElasticBeanstalkWebTier e dependências
<img src="./assets/02-add-permissions.png" width="100%">

### 3. Revisão final dos detalhes do ambiente web antes de solicitar a criação
<img src="./assets/03-name-review-create.png" width="100%">

### 4. Confirmação da Role IAM vinculada ao serviço final
<img src="./assets/04-role-iam.png" width="100%">

### 5. Configuração mandatória do Web Tier e seleção da stack de plataforma
<img src="./assets/05-configure-environment.png" width="100%">

### 6. Vinculação estrita de perfis de instâncias autorizando a API AWS EC2
<img src="./assets/06-configure-service-access.png" width="100%">

### 7. Painel Beanstalk concluído exibindo status "Ok" com URL ativada ao público
<img src="./assets/08-environments-elastic-beanstalk.png" width="100%">

> [!IMPORTANT]
> Alguns identificadores foram mascarados por boas práticas de segurança.

---

## 💡 Principais Aprendizados

- **Produtividade PaaS Absoluta:** O Elastic Beanstalk aterra decisões de infraestrutura e sobrecarga de gerenciamento, provando ser o caminho mais curto entre um pacote funcional local e um backend ativamente produtivo.
- **Limpeza Determinística Incorruptível:** A orquestração hierárquica gera proteção orçamentária; ao erradicar apenas o ambiente matriz global, a nuvem efetua a varredura e morte sistemática dos hardwares aninhados no ecossistema sem deixar resíduos orçamentários.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| Elastic Beanstalk | ✅ Gratuito (cobra-se a infra subjacente) | $0,00 |
| EC2 (t2.micro) | ✅ 750h/mês (12 meses) | $0,00 |
| S3 (artefatos) | ✅ 5GB | $0,00 |
| **Total** | | **$0,00** |

> ⚠️ Lembre-se de limpar os recursos após o lab para evitar cobranças.

---

## 🏷️ Competências Demonstradas

`Elastic Beanstalk` `PaaS` `IAM Roles` `Instance Profile` `Managed Platform` `Deploy Automatizado` `🟢 Fundamental`

---

[← Voltar ao índice](../../../README.md)
