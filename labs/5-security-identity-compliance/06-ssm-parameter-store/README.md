<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 06 â€” AWS SSM Parameter Store e KMS: GestÃ£o Segura de Segredos

## ðŸš€ Resumo
GestÃ£o e Blindagem de Segredos SensÃ­veis: Neste laboratÃ³rio, isolei configuraÃ§Ãµes crÃ­ticas de aplicaÃ§Ã£o utilizando o **AWS SSM Parameter Store** em conjunto com o **AWS Key Management Service (KMS)**. Centralizei a gestÃ£o de variÃ¡veis simples (como URLs) e estabeleci parÃ¢metros criptografados do tipo `SecureString` para dados sensÃ­veis (como senhas), garantindo que nenhum segredo fique exposto no cÃ³digo-fonte das aplicaÃ§Ãµes.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Desenvolvimento de Software e Engenharia de Dados
- **Problema:** Em um projeto anterior, desenvolvedores deixaram as credenciais de acesso ao Banco de Dados fixas no cÃ³digo (Hardcoded). Durante um push para o GitHub, essas chaves foram vazadas para um repositÃ³rio pÃºblico, resultando em um incidente de seguranÃ§a onde o banco de dados foi invadido.
- **SoluÃ§Ã£o:** Removi todas as senhas do cÃ³digo. Agora, utilizo o **SSM Parameter Store** como um cofre central. A senha do banco Ã© armazenada como uma `SecureString`, protegida pela criptografia AES-256 do **AWS KMS**. Quando a aplicaÃ§Ã£o sobe (seja no EC2 ou Lambda), ela faz uma chamada Ã  API do SSM para resgatar o segredo. Se o cÃ³digo for vazado no GitHub, o invasor verÃ¡ apenas um caminho (ex: `/app/prod/db_password`), mas nÃ£o terÃ¡ acesso ao valor real, que fica protegido pela camada de identidade da AWS.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Criar hierarquias organizadas de parÃ¢metros (ex: `/app/dev` vs `/app/prod`).
- Armazenar variÃ¡veis sensÃ­veis utilizando o tipo **SecureString** com criptografia KMS.
- Diferenciar o uso de Strings simples (nÃ£o taxadas) de SecureStrings (seguras).
- Gerenciar versÃµes de parÃ¢metros e utilizar Labels para controle de mudanÃ§as.
- Administrar **Key Policies** no KMS para controlar quem pode descriptografar os dados.
- Validar o resgate de segredos via **AWS CLI (CloudShell)** testando as flags de descriptografia.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS SSM Parameter Store** | RepositÃ³rio central de configuraÃ§Ãµes e segredos. |
| **AWS KMS** | Motor de criptografia responsÃ¡vel por proteger as SecureStrings. |
| **AWS CloudShell** | Interface de linha de comando usada para validar o acesso aos parÃ¢metros. |

---

## ðŸ—ï¸ Arquitetura da SoluÃ§Ã£o

<div align="center">
  <img src="./assets/architecture-ssm-parameter-store.drawio.png" alt="Arquitetura da SoluÃ§Ã£o" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ ConfiguraÃ§Ãµes de Ambiente (Strings Simples)
- **AÃ§Ã£o:** Criei parÃ¢metros para endereÃ§os de banco de dados em ambientes diferentes: `/minha-app/dev/db_url` e `/minha-app/prod/db_url`.
- **Resultado:** Estes dados sÃ£o strings abertas no console, ideais para URLs e metadados que nÃ£o sÃ£o sigilosos, mas precisam de centralizaÃ§Ã£o.

### 2. ðŸ›¡ï¸ O Cofre de Senhas (KMS + SecureString)
- **AÃ§Ã£o:** Armazenei a senha real no parÃ¢metro `/minha-app/prod/db_password`.
- **ImplementaÃ§Ã£o:** Selecionei o tipo `SecureString` e a chave KMS padrÃ£o (`aws/ssm`). O valor da senha tornou-se visualmente ilegÃ­vel no console da AWS, aparecendo apenas como asteriscos ou chaves encriptadas.

### 3. ðŸ” ValidaÃ§Ã£o via CLI (AWS CloudShell)
- **AÃ§Ã£o:** Executei comandos no terminal para simular o comportamento de uma aplicaÃ§Ã£o.
- **Teste 1:** Tentei ler o parÃ¢metro sem a flag de descriptografia. O resultado foi um hash encriptado, provando que o dado estÃ¡ protegido em repouso.
- **Teste 2:** Usei o comando `aws ssm get-parameter --name ... --with-decryption`. Como meu usuÃ¡rio tem permissÃ£o no KMS, o sistema revelou a senha em texto claro, validando o fluxo de integraÃ§Ã£o seguro.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. ConfiguraÃ§Ã£o de ParÃ¢metros: DefiniÃ§Ã£o de variÃ¡veis de ambiente para Dev e Prod
<img src="./assets/01-create-parameter-dev.png" width="100%">
<img src="./assets/02-create-parameter-prod.png" width="100%">
<img src="./assets/09-my-parameters.png" width="100%">

---

### 2. SeguranÃ§a e OrganizaÃ§Ã£o: ConfiguraÃ§Ã£o de KMS e Labels para os parÃ¢metros
<img src="./assets/03-configure-key.png" width="100%">
<img src="./assets/04-add-labels.png" width="100%">
<img src="./assets/05-key-policy.png" width="100%">
<img src="./assets/06-key-summary.png" width="100%">

---

### 3. Gerenciamento de Segredos: Armazenamento de senhas como SecureString
<img src="./assets/07-create-parameter-password-dev.png" width="100%">
<img src="./assets/08-create-parameter-password-prod.png" width="100%">

---

### 4. ValidaÃ§Ã£o via CLI: Teste de resgate de parÃ¢metros no AWS CloudShell
<img src="./assets/10-cloudshell-without-decryption.png" width="100%">
<img src="./assets/11-cloudshell-with-decryption.png" width="100%">

---

## ðŸ’¡ Principais Aprendizados

- **Custo-BenefÃ­cio:** O SSM Parameter Store (nÃ­vel Standard) Ã© gratuito para atÃ© 10.000 variÃ¡veis. Ã‰ uma alternativa extremamente econÃ´mica ao AWS Secrets Manager para casos onde nÃ£o preciso de rotaÃ§Ã£o automÃ¡tica de senhas.
- **SeguranÃ§a em Camadas:** Aprendi que, mesmo se alguÃ©m tiver acesso ao console do SSM, se nÃ£o tiver permissÃ£o na "Key Policy" do KMS, nÃ£o conseguirÃ¡ ver o valor real da senha. Isso cria uma barreira dupla de proteÃ§Ã£o.
- **Adeus ao Hardcoded:** Centralizar configuraÃ§Ãµes permite que eu altere uma senha ou URL em um Ãºnico lugar e todas as minhas instÃ¢ncias EC2 ou funÃ§Ãµes Lambda recebam a atualizaÃ§Ã£o na prÃ³xima execuÃ§Ã£o, sem precisar redeployar cÃ³digo.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| SSM Parameter Store | âœ… GrÃ¡tis para parÃ¢metros Standard | $0,00 |
| AWS KMS | âœ… Chaves gerenciadas pela AWS para SSM sÃ£o gratuitas | $0,00 |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS SSM Parameter Store` `KMS` `SecureString` `GestÃ£o de Segredos` `SeguranÃ§a de AplicaÃ§Ã£o` `AWS CLI` `ðŸŸ¡ IntermediÃ¡rio`

---

[â† Voltar ao Ã­ndice](../../../README.md)
