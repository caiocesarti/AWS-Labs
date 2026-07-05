<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 08 â€” IntroduÃ§Ã£o ao AWS Key Management Service (KMS)

## ðŸš€ Resumo
Criptografia Controlada e Compliance RastreÃ¡vel: Neste laboratÃ³rio, explorei as fundaÃ§Ãµes do **AWS KMS** para proteger dados em descanso. Configurei o ciclo de vida completo de uma chave simÃ©trica (Customer Managed Key), desde o provisionamento atÃ© o monitoramento de uso atravÃ©s do CloudTrail. Implementei a criptografia SSE-KMS em buckets S3, garantindo que apenas usuÃ¡rios autenticados e com permissÃµes especÃ­ficas pudessem decifrar os arquivos armazenados.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** SaÃºde (Hospitais e Seguradoras)
- **Problema:** Um sistema de prontuÃ¡rios mÃ©dicos armazenava exames confidenciais no S3 usando a criptografia bÃ¡sica da AWS. A auditoria de conformidade (HIPAA/LGPD) reprovou o sistema porque a empresa nÃ£o tinha controle sobre quem possuÃ­a as chaves e nem um registro de auditoria detalhado sobre quem visualizou cada exame individualmente.
- **SoluÃ§Ã£o:** Implementei uma chave personalizada gerenciada pelo cliente (**CMK**). Agora, todos os uploads de exames usam SSE-KMS vinculado a essa chave. Isso significa que, alÃ©m de ter permissÃ£o no S3, o mÃ©dico precisa ter permissÃ£o explÃ­cita na polÃ­tica da chave KMS. Cada vez que um exame Ã© baixado e decifrado, o **AWS CloudTrail** registra o evento `Decrypt`, fornecendo a prova forense exata de quem acessou os dados sensÃ­veis dos pacientes, garantindo conformidade total com as leis de privacidade.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Criar e gerenciar **Customer Managed Keys (CMKs)** com algoritmos simÃ©tricos.
- Configurar **Key Policies** para separar as funÃ§Ãµes de Administrador e UsuÃ¡rio da chave.
- Aplicar criptografia **SSE-KMS** em objetos do Amazon S3.
- Validar a eficÃ¡cia da proteÃ§Ã£o tentando acessar arquivos via links pÃºblicos (assinatura Signature V4).
- Analisar logs do **AWS CloudTrail** para auditar operaÃ§Ãµes de descriptografia (`Decrypt`).
- Compreender o processo de exclusÃ£o programada de chaves para evitar custos desnecessÃ¡rios.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS KMS** | Gerenciamento de chaves mestras e polÃ­ticas de criptografia. |
| **Amazon S3** | Armazenamento seguro de objetos com criptografia em repouso. |
| **AWS CloudTrail** | Auditoria e rastreio de uso das chaves criptogrÃ¡ficas na conta. |

---

## ðŸ—ï¸ Arquitetura do Fluxo CriptogrÃ¡fico

<div align="center">
  <img src="./assets/architecture-aws-kms-introduction.drawio.png" alt="Arquitetura do Fluxo CriptogrÃ¡fico" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. âš™ï¸ CriaÃ§Ã£o da Chave SimÃ©trica (CMK)
- **AÃ§Ã£o:** Criei a chave `myFirstKey` no painel do KMS.
- **ConfiguraÃ§Ã£o:** Defini meu usuÃ¡rio como Administrador (pode gerenciar a chave) e tambÃ©m como UsuÃ¡rio (pode usar a chave para criptografar/descriptografar). Esta separaÃ§Ã£o Ã© vital em empresas reais para evitar que o time de TI "bisbilhote" dados protegidos.

### 2. ðŸ›¡ï¸ Upload Seguro no S3
- **AÃ§Ã£o:** Realizei o upload de uma imagem para um bucket S3.
- **ConfiguraÃ§Ã£o:** Durante o upload, alterei a criptografia padrÃ£o para **SSE-KMS** e selecionei a chave `myFirstKey`. O arquivo foi salvo em repouso jÃ¡ criptografado com o meu crivo de seguranÃ§a personalizado.

### 3. ðŸ” Teste de Falha e Auditoria
- **AÃ§Ã£o:** Tentei acessar o arquivo atravÃ©s de um link pÃºblico ajustando a ACL do objeto.
- **Resultado:** O link falhou com erro de assinatura ("Signature Version 4 required"). Isso prova que, mesmo com acesso pÃºblico no S3, o KMS barra o acesso de qualquer um que nÃ£o tenha a chave de descriptografia.
- **Auditoria:** Acessei o CloudTrail e localizei o evento `Decrypt`. O log mostrava meu usuÃ¡rio, o horÃ¡rio exato e a chave utilizada, fechando o ciclo de auditoria.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. ConfiguraÃ§Ã£o de Chave: Chave customizada (Customer Managed Key) ativa e configurada no console
<img src="./assets/KMS.png" width="100%">

### 2. Armazenamento Seguro: Arquivo no S3 utilizando a criptografia SSE-KMS vinculada Ã  minha chave
<img src="./assets/mycloudtrailbucket-S3-bucket-S3.png" width="100%">

### 3. Controle de Acesso S3: Ajuste de permissÃµes e ACL do bucket para testar bloqueios
<img src="./assets/mycloudtrailbucket-S3-Acl.png" width="100%">

### 4. Teste de Acesso: NegaÃ§Ã£o de acesso via link pÃºblico devido Ã  proteÃ§Ã£o criptogrÃ¡fica do KMS
<img src="./assets/Make-objects-public-S3-bucket-mycloudtrailbucket-S3.png" width="100%">

### 5. Auditoria Forense: Logs do CloudTrail registrando o uso da chave e eventos de criptografia/descriptografia
<img src="./assets/Trails-CloudTrail.png" width="100%">

### 6. PermissÃµes de Chave: Painel de controle de permissÃµes (Users/Admins) da chave KMS
<img src="./assets/Key-remove.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Key Policies vs IAM Policies:** Aprendi que ter permissÃ£o "AdministratorAccess" no IAM nÃ£o garante acesso automÃ¡tico Ã  chave KMS se ela tiver uma polÃ­tica restritiva. O KMS tem seu prÃ³prio "muro" de permissÃµes.
- **Obrigatoriedade de Assinatura:** Arquivos protegidos por KMS exigem que a aplicaÃ§Ã£o use tokens temporÃ¡rios vÃ¡lidos (SigV4). Isso mata ataques de links vazados na internet.
- **Custo de Chaves Customizadas:** Diferente da chave padrÃ£o da AWS (`aws/s3`), as chaves customizadas custam $1/mÃªs. Por isso, Ã© fundamental deletÃ¡-las apÃ³s o uso em testes de laboratÃ³rio.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS KMS (Chave Customizada) | âŒ Taxa mensal por chave ativa | ~$1,00/mÃªs |
| Amazon S3 (Armazenamento) | âœ… IncluÃ­do no Free Tier | $0,00 |

> âš ï¸ **Aviso Importante:** Agendei a exclusÃ£o da chave KMS imediatamente apÃ³s o tÃ©rmino do lab. A AWS impÃµe um perÃ­odo de espera mÃ­nimo de 7 dias antes de deletar a chave permanentemente para evitar perdas acidentais de dados.

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS KMS` `Customer Managed Keys` `SSE-KMS` `S3 Encryption` `AWS CloudTrail` `Cloud Compliance` `Signature V4` `ðŸŸ¡ IntermediÃ¡rio`

---

[â† Voltar ao Ã­ndice](../../../README.md)
