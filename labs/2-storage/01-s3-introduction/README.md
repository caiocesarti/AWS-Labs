<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 01 — Introdução ao Amazon S3: Políticas de Bucket e Versionamento

## 🚀 Resumo
Implementação de regras de segurança granulares em armazenamento de objetos (Amazon S3). O laboratório mapeia a criação de Bucket Policies escritas em JSON, demonstra o controle irrestrito de dados via Block Public Access (BPA) e garante capacidade de Recuperação de Desastres (DR) utilizando Versionamento.

---

## 💼 Caso de Uso Real
- **Indústria:** Setor Financeiro / Banco de Dados Médico
- **Problema:** Um sistema corporativo gera relatórios sigilosos e faz upload para um bucket S3. Vazamentos de dados via "buckets públicos" se tornaram a principal manchete de brechas da nuvem (S3 Leak). Além disso, automações com falhas frequentemente deletam ou sobrescrevem arquivos valiosos por acidente, causando perdas significativas.
- **Solução:** Aplicar uma camada blindada de proteção. Um bloqueio mestre (BPA) veda qualquer acesso da internet. Uma `Bucket Policy` rigorosa é montada para aceitar escritas *estritamente* daquela aplicação original. Finalmente, liga-se o `Object Versioning`; se um script malicioso "deletar" um relatório histórico, a AWS apenas insere um rótulo (*Delete Marker*), permitindo recuperar o arquivo real com facilidade.

---

## 🎯 Objetivos de Aprendizado

- Instanciar a infraestrutura de dados S3 mitigando vazamentos na elaboração (*Security By Design*).
- Dominar o **Block Public Access (BPA)** compreendendo precedências lógicas na hierarquia global AWS.
- Configurar e inspecionar permissões restritas via **Bucket Policies (JSON)** limitando a leitura/escrita S3 estritamente a entidades mapeáveis.
- Ativar proteção através de **Object Versioning**, desarmando os riscos de comandos de remoção.
- Operar conectores via **AWS CLI** disparando testes reais em infraestrutura EC2 para checar segurança perimetral.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon S3** | O alicerce isolando os arquivos, trancado via Políticas nativas. |
| **Amazon EC2** | Representa o consumidor (aplicação real). Acessado diretamente via Systems Manager para testar a fronteira. |
| **AWS IAM** | Governança subjacente blindando credenciais de API através de Service Roles exclusivas. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-s3-introduction.drawio.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 📦 Criação Segura do Repositório (S3)
- **Ação:** Criei o ambiente primário `reportbucket-<id>`.
- **Configuração:** Apliquei provisoriamente a liberação de ACLs com intuito exclusivo de testar a funcionalidade falha de gerência manual. Testei o upload nativo de relatórios para verificar o bloqueio global.

### 2. 🛡️ Controle Restrito de Borda (BPA)
- **Ação:** Configurei a blindagem absoluta global no Bucket. 
- **Verificação:** Desativar o Block Public Access de fato permite que ACLs funcionem, o que evidencia *por que* devemos manter essa barreira ativa. Esse switch global sobrepõe hierarquicamente qualquer ACL configurada nos objetos.

### 3. 📝 Escrita de Bucket Policies
- **Ação:** Fechei acessos externos, abrindo rota exclusiva para o servidor EC2.
- **Configuração:** Utilizando o *AWS Policy Generator*, forgei um escopo JSON exato habilitando `PutObject` e `GetObject` apenas para o ARN do perfil da minha instância EC2.
- **Resultado:** Qualquer outra rede ou sistema computacional externo é bloqueado ativamente pela política.

### 4. 💻 Prova de Conceito CLI (Teste Real)
- **Ação:** Assumi o terminal da instância através do *Systems Manager*.
- **Configuração (AWS CLI):** Listei repositórios pelo comando `aws s3 ls` e submeti arquivos via `aws s3 cp`, validando que minha instância obteve o acesso estabelecido na Bucket Policy.
- **Validação:** Ao solicitar link anônimo direto no navegador, a requisição foi devidamente barrada.

### 5. ⏱️ Prevenção de Desastres e Retenção (Versioning)
- **Ação:** Habilitei o registro histórico contínuo (Versioning).
- **Validação:** Invoquei o comando `delete` ativamente via CLI. O arquivo sumiu do painel primário, porém ao ativar a visualização de versões demonstrei a criação do `Delete Marker`.
- **Restauro:** Demonstrei que excluir o `Delete Marker` refaz a versão original e a remoção absoluta se dá apenas deletando o seu respectivo `Version ID`.

---

## 📸 Evidências de Execução

### 1. Conectividade garantida sem chaves utilizando infra Session Manager
<img src="./assets/Systems-Manager-Access.png" width="100%">

### 2. Visualização do objeto de teste inicial carregado no bucket S3
<img src="./assets/reportbucket-sample-file-txt.png" width="100%">

### 3. Interface lógica construindo blocos essenciais JSON para permissões S3
<img src="./assets/AWS-Policy-Generator-s3.png" width="100%">

### 4. Compilação exata da sintaxe de ARN restringindo IAM Roles
<img src="./assets/AWS-Policy-Generator-s3-json.png" width="100%">

### 5. Processo de atualização da política diretamente no console S3
<img src="./assets/S3-bucket-S3-policy-update.png" width="100%">

### 6. Confirmação da política de bucket aplicada com sucesso
<img src="./assets/policy-edit-bucket-S3.png" width="100%">

### 7. Ativação do versionamento de objetos para proteção contra exclusão
<img src="./assets/S3-bucket-S3-versioning.png" width="100%">

### 8. Detalhes de um objeto com versionamento ativo e metadados
<img src="./assets/S3-bucket-S3-version-sample-file.png" width="100%">

### 9. Lista completa de versões históricas vinculadas a um único objeto
<img src="./assets/sample-file-txt-Object-in-S3-bucket-versions.png" width="100%">

### 10. Processo de exclusão de objetos para teste de Delete Marker
<img src="./assets/Delete-objects-S3-bucket.png" width="100%">

### 11. Evidência de como o S3 previne exclusões através de Delete Markers isolados
<img src="./assets/-S3-bucket-S3-Delete-Marker.png" width="100%">

### 12. Estancamento cirúrgico removendo o arquivo pela versão física
<img src="./assets/S3-bucket-permanently-delete.png" width="100%">

> [!IMPORTANT]
> Alguns identificadores foram mascarados por boas práticas de segurança.

---

## 💡 Principais Aprendizados

- **Precedência da Camada BPA:** Observei que a configuração `BPA` apoia-se acima do resto. Não adianta ACLs ou Políticas Abertas se o BPA está ativado, marcando isolamento efetivo e completo.
- **Deleção Lógica Integrada:** Compreendi que o Versionamento atua como anti-desastre. Processos nunca apagam os dados ativamente sem apontar pontualmente para IDs de versão, servindo como uma barreira impecável.
- **Integração de Identidades Sólidas:** Atrelar permissões de uma `Service Role` diretamente a uma `Bucket Policy (JSON)` exime configurações dependentes de chaves secretas (Access Keys) evitando exposição estática e vulnerabilidades sistêmicas transversais.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| S3 Standard | ✅ 5GB / 2.000 PUTs / 20.000 GETs | $0,00 |
| EC2 (t2.micro) | ✅ 750h/mês (12 meses) | $0,00 |
| **Total** | | **$0,00** |

---

## 🏷️ Competências Demonstradas

`S3` `Bucket Policies` `Block Public Access` `Versionamento` `IAM Roles` `AWS CLI` `Session Manager` `🟡 Intermediário`

---

## 📜 Alinhamento com Certificações

Este lab engloba conceitos primordiais do:
- **CLF-C02:** Domínio 3 — Tecnologia e Serviços de Cloud
- **SAA-C03:** Domínio 1 — Arquitetura Segura
- **DVA-C02:** Domínio 2 — Segurança

---

[← Voltar ao índice](../../../README.md)
