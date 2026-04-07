<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 01 — Introdução ao Amazon EC2: Ciclo de Vida e Monitoramento

## 🚀 Resumo
Provisionamento core de um servidor web na nuvem com foco em resiliência e elasticidade. O modelo de instâncias virtuais permite:
- **Proteção contra perdas:** Bloqueio ativo contra encerramento acidental por erro humano.
- **Escala elástica:** Redimensionamento vertical em tempo real de CPU, RAM e volume de disco sem recriação do servidor.
- **Bootstrapping automatizado:** Injeção de scripts (User Data) na inicialização para zero toque pós-deploy.

---

## 💼 Caso de Uso Real
- **Indústria:** E-commerce / Sistemas Legados
- **Problema:** Um servidor monolítico tradicional on-premise atinge pico de uso de CPU e Disco durante uma campanha de vendas. A ampliação física exige horas de downtime, compra de hardware e migração de dados arriscada, podendo corromper o sistema.
- **Solução:** Utilizar o Amazon EC2 com volumes EBS desvinculados permite pausar a instância por curtíssimo prazo, dobrar seus recursos vitais via API/Console e voltar ao ar instantaneamente, retendo todos os dados intactos.

---

## 🎯 Objetivos de Aprendizado

*   Lançar uma instância com suporte a **User Data** e **Proteção contra Encerramento**.
*   Utilizar ferramentas de diagnóstico remoto (**Logs do Sistema** e **Screenshot**).
*   Liberar tráfego HTTP configurando o firewall de rede (**Security Groups**).
*   Executar o **Upscaling** vertical e expansão dinâmica de disco (EBS).
*   Validar as travas de segurança antes de forçar o encerramento do recurso.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon EC2** | Provedor de servidores virtuais elásticos e redimensionáveis. |
| **Amazon EBS** | Armazenamento de blocos persistente para o volume raiz do sistema. |
| **Amazon CloudWatch** | Coleta de métricas e telemetria básica de performance. |
| **AWS IAM** | Gerenciamento de permissões de acesso e roles de serviço. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-ec2.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 🚀 Lançamento e Bootstrapping
- **Ação:** Criei o `Web Server` utilizando a *Amazon Linux 2023 AMI*.
- **Configuração:** Ativei de forma explícita a trava `disableApiTermination` em Detalhes Avançados.
- **Automação:** Injetei o script de bootstrap para instalação desacompanhada do Apache (`httpd`).
> 📄 **Ver script:** [src/user-data.sh](./src/user-data.sh).

### 2. 🛡️ Liberação de Firewall (Porta 80)
- **Desafio:** A instância nova rejeita todo o tráfego HTTP por padrão (Timeout).
- **Ação:** Modifiquei o **Security Group** anexado a ela.
- **Resultado:** Inseri a regra de *Inbound* tipo `HTTP` na porta `80` liberando acesso para `0.0.0.0/0`.

### 3. 📈 Redimensionamento Dinâmico (Resize)
- **Ação em Instância:** Executei a transição em tempo real do tipo `t3.micro` para `t3.small` (Dobra da capacidade computacional).
- **Ação em Armazenamento:** Realizei a expansão direta via painel do volume EBS Elastic Block Store de **8 GiB para 10 GiB** sem perda de dados.

### 4. 🔍 Monitoramento Remoto
- **Logs do Sistema:** Validei profundamente o sucesso do *User Data* sem abrir conexão SSH.
- **Diagnóstico OOB:** Capturei a tela do console virtual para analisar a integridade do ciclo de boot do Linux hospedado.

### 5. 🛑 Encerramento e Provas de Segurança
- **Desafio:** A tentativa direta de terminação recebeu erro da API do EC2.
- **Solução:** Removi manualmente a Proteção contra Encerramento, permitindo finalmente a limpeza do ciclo de vida.

---

## 📸 Evidências de Execução

### 1. Instância "Web Server" em execução com verificações de status aprovadas
<img src="./assets/01-ec2-running.png" width="100%">

### 2. Log do sistema confirmando a instalação do pacote httpd via User Data
<img src="./assets/02-system-log.png" width="100%">

### 3. Captura de tela do console de boot validando o carregamento do Linux
<img src="./assets/03-instance-screenshot.png" width="100%">

### 4. Configuração da regra de entrada HTTP no Security Group
<img src="./assets/04-security-group-rule.png" width="100%">

### 5. Navegador exibindo "Hello From Your Web Server!" via IP público
<img src="./assets/05-browser-validation.png" width="100%">

### 6. Detalhes da instância exibindo o novo tipo t3.small e volume de 10GB
<img src="./assets/06-instance-resized.png" width="100%">

### 7. Erro de API bloqueando o encerramento devido à proteção ativada
<img src="./assets/07-termination-protection.png" width="100%">

> [!IMPORTANT]
> Alguns identificadores foram mascarados por boas práticas de segurança.

---

## 💡 Principais Aprendizados

*   **Evitar Erros Fatais:** A Proteção contra Encerramento é obrigatória para instâncias críticas (bancos de dados).
*   **Diagnóstico Remoto:** Logs e capturas de tela eliminam a necessidade de rede ativa (SSH/RDP) para analisar falhas em boot.
*   **Elasticidade Vertical:** O redimensionamento ilustra puramente o modelo "recurso sob demanda" da nuvem.
*   **Segurança Step-by-Step:** Security groups usam `Deny by Default`, forçando a abertura de tráfego explicitamente.

---

## 🔗 Recursos Adicionais

- [Launch Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [Amazon EC2 - User Data and Shell Scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [Amazon EC2 Root Device Volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html)
- [Tagging Your Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
- [Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [Status Checks for Your Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)
- [Getting Console Output and Rebooting Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html)
- [Amazon EC2 Metrics and Dimensions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- [Resizing Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)
- [Stop and Start Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
- [Amazon EC2 Service Quotas e Limites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
- [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)
- [Termination Protection for an Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingTerminationProtection)

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| EC2 (t3.micro) | ✅ 750h/mês (12 meses) | $0,00 |
| EBS (gp3, 10GB) | ✅ 30GB/mês | $0,00 |
| CloudWatch (métricas básicas) | ✅ Gratuito | $0,00 |
| **Total** | | **$0,00** |

> ⚠️ Lembre-se de limpar os recursos após o lab para evitar cobranças.

---

## 🏷️ Competências Demonstradas

`EC2` `EBS` `Security Groups` `CloudWatch` `User Data` `Vertical Scaling` `Termination Protection` `🟢 Fundamental`

---

## 📜 Alinhamento com Certificações

Este lab cobre objetivos de:
- **CLF-C02:** Domínio 3 — Tecnologia e Serviços de Cloud
- **SAA-C03:** Domínio 2 — Arquitetura Resiliente
- **SAA-C03:** Domínio 3 — Arquitetura de Alta Performance

---

[← Voltar ao índice](../../../README.md)
