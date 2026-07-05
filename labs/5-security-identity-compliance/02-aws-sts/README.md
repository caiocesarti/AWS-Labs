<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 02 â€” AWS Security Token Service (STS)

## ðŸš€ Resumo
GestÃ£o de Identidade DinÃ¢mica. Neste laboratÃ³rio, demonstrei a implementaÃ§Ã£o de credenciais temporÃ¡rias utilizando o pacote **AWS STS (Security Token Service)** e **Boto3 (Python)**. SubstituÃ­ o uso de chaves permanentes por um processo onde o cÃ³digo assume uma **IAM Role** de acesso restrito (`AssumeRole`), recebendo chaves vÃ¡lidas por apenas 1 hora para operaÃ§Ãµes seguras no Amazon S3.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** AutomaÃ§Ã£o Cloud e IntegraÃ§Ã£o de Sistemas
- **Problema:** Um script de automaÃ§Ã£o precisava ler dados de um bucket S3 diariamente. O administrador gerou um par de chaves fixas (Access Key / Secret Key), mas o desenvolvedor as deixou expostas em um repositÃ³rio pÃºblico do GitHub. Horas depois, as chaves foram usadas para vazar toda a base de dados da empresa.
- **SoluÃ§Ã£o:** Reformulei a arquitetura para forÃ§ar o uso de Credenciais TemporÃ¡rias. Criei um script Python que utiliza o `AssumeRole` do AWS STS. O usuÃ¡rio que executa o script nÃ£o tem permissÃ£o de leitura no S3, apenas a permissÃ£o para assumir uma Role especÃ­fica. O cÃ³digo solicita acesso ao STS, recebe chaves temporÃ¡rias que autorizam a leitura no S3 por tempo limitado e executa a tarefa. Mesmo se essas chaves vazarem, elas expiram sozinhas em minutos, neutralizando ataques sem necessidade de intervenÃ§Ã£o humana.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Diferenciar na prÃ¡tica entre **IAM Policies** (o que pode ser feito) e **Trust Policies** (quem pode fazer).
- Provisionar **IAM Roles** parametrizadas para delegar permissÃµes a scripts e aplicaÃ§Ãµes.
- Utilizar a API `AssumeRole` via SDK Python (Boto3) para solicitar credenciais efÃªmeras.
- Capturar e gerenciar variÃ¡veis de seguranÃ§a (Access Key, Secret Key e Session Token) no cÃ³digo.
- Validar o acesso temporÃ¡rio ao **Amazon S3** e confirmar o bloqueio automÃ¡tico apÃ³s a expiraÃ§Ã£o.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o       | Papel no Lab                                               |
| ------------- | ---------------------------------------------------------- |
| **AWS STS**   | Emissor (Token Provider) das chaves de curta duraÃ§Ã£o.      |
| **AWS IAM**   | CriaÃ§Ã£o da Role, do usuÃ¡rio e das polÃ­ticas de confianÃ§a.  |
| **Amazon S3** | Recurso de destino para validar as permissÃµes temporÃ¡rias. |

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ ConfiguraÃ§Ã£o de UsuÃ¡rio e Role (IAM)
- **AÃ§Ã£o:** Criei o usuÃ¡rio "Operador" sem permissÃµes diretas.
- **ConfiguraÃ§Ã£o da Role:** Criei a `S3-Access-Role` com permissÃ£o de leitura no S3. Configurei a **Trust Policy** para permitir que apenas o ARN do "Operador" pudesse assumir essa Role.

### 2. ðŸ’» Desenvolvimento do Script (AssumeRole)
- **AÃ§Ã£o:** Desenvolvi uma aplicaÃ§Ã£o em Python para gerenciar a solicitaÃ§Ã£o de tokens.
- **ImplementaÃ§Ã£o:** O script usa `boto3.client('sts')` para executar a funÃ§Ã£o `assume_role`. ExtraÃ­ as strings `AccessKeyId`, `SecretAccessKey` e `SessionToken` do payload retornado.
- **CÃ³digo-Fonte:** O script completo estÃ¡ disponÃ­vel em [src/assume_role.py](./src/assume_role.py).

### 3. ðŸ” ValidaÃ§Ã£o e Teste de ExpiraÃ§Ã£o
- **AÃ§Ã£o:** Injetamos as credenciais temporÃ¡rias em um novo cliente S3 no Boto3.
- **Resultado:** O script listou os arquivos do bucket com sucesso (HTTP 200). Validei que as permissÃµes originais do usuÃ¡rio continuavam bloqueadas, provando que o acesso sÃ³ foi possÃ­vel atravÃ©s do STS.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Programmatic Access Setup: Criando credenciais para o usuÃ¡rio 'Operador' iniciar o processo de STS
<img src="./assets/01-create-access-key.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **SeguranÃ§a Transiente:** Tokens dinÃ¢micos mitigam danos se o cÃ³digo ou a mÃ¡quina local forem comprometidos. Esta Ã© a base de funcionamento das Instance Profiles e Lambda Execution Roles.
- **Trust Policies:** Aprendi que uma Permission Policy diz "Bata no S3", mas a Trust Policy Ã© quem decide "Quem pode bater no S3". Sem uma Trust Policy configurada corretamente, o STS revoga imediatamente qualquer tentativa de assumir a funÃ§Ã£o.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier?                                    | Custo Estimado |
| ------- | --------------------------------------------- | -------------- |
| AWS STS | âœ… OperaÃ§Ãµes de geraÃ§Ã£o de token sÃ£o gratuitas | $0,00          |
| AWS IAM | âœ… Gratuito                                    | $0,00          |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS STS` `AssumeRole` `Credenciais TemporÃ¡rias` `Python Boto3` `Trust Policies` `SeguranÃ§a Automatizada` `ðŸŸ¢ Fundamental`

---

[â† Voltar ao Ã­ndice](../../../README.md)
