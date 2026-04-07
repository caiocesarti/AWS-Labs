<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 03 — Amazon S3 Básico e Avançado: Versionamento e URLs Pré-assinadas

## 🚀 Resumo
Estabelecimento de infraestrutura de Storage com foco em resiliência e delegação de acessos corporativos. Este lab unifica o provisionamento seguro sob diretrizes *BPA*, imunidade a exclusões via *Versionamento* histórico e distribuição temporal de ativos confidenciais utilizando URLs Pré-assinadas com validade de curtíssimo prazo.

---

## 💼 Caso de Uso Real
- **Indústria:** Consultoria / Auditoria Fiscal
- **Problema:** O setor de controladoria armazena recibos fiscais vitais na AWS. Eles precisam frequentemente enviar arquivos específicos ("Recibo-X.pdf") para analistas externos. Modificar as ACLs para permitir IPs não confiáveis enfraquece a borda; anexar arquivos em e-mails quebra políticas de DLP e perde rastreabilidade. Em paralelo, a manipulação constante gera risco altíssimo de exclusão humana do recibo original.
- **Solução:** Arquitetura Híbrida de Segurança. Todo bucket recebe o bloqueio absoluto de acesso público. Ativo o **Object Versioning** garantindo que mesmo deleções acidentais se convertam apenas em marcadores ocultos (*Delete Markers*). Para o envio externo, forjo uma **Pre-signed URL** concedendo acesso de leitura criptografado que fenece matematicamente em 60 segundos exatos, transferindo o arquivo massivo pela banda da própria nuvem.

---

## 🎯 Objetivos de Aprendizado

- Instanciar a infraestrutura primária S3 sob o rigor do **Block Public Access (BPA)** global.
- Configurar integridade histórica utilizando o **Versionamento de Objetos**, testando ativamente a proteção matemática contra remoções destrutivas.
- Mapear a transição de custos ativando regras silenciosas de **Lifecycle Rules**, empurrando arquivos frios para matrizes Glacier.
- Dominar a distribuição de arquivos perimetrais sintetizando **Pre-signed URLs** com cronômetros de autodestruição lógica em T-60s.

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon S3** | Provedor de dados matriz gerenciando a retenção histórica subjacente e transições frias (Lifecycle). |
| **S3 Presigned URLs** | Motor de autorização baseado em assinaturas, gerando vetores de transferência limitados que dispensam usuários IAM estáticos. |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-s3-basic-advanced.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 🛡️ Fechamento Primário da Borda
- **Ação:** Provisionei o bucket `seu-nome-bucket-lab3` na região us-east-1.
- **Configuração:** Apliquei obrigatoriamente o pacote de Bloqueio de Acesso Público. A infraestrutura base nasce impenetrável perante acessos não autenticados na internet.

### 2. 🗄️ Proteção Ativa Anti-Sobrescrita (Versioning)
- **Ação:** Engajei o rastreamento unificado de versão.
- **Teste Destrutivo:** Operei uma edição agressiva subindo o arquivo `Lab3.txt` idêntico com bytes modificados (*Versão 1* vs *Versão 2*).
- **Tratamento:** A infraestrutura S3 ignorou a premissa de deleção computacional real, empilhando IDs nativos absolutos isolados garantindo a ressurreição pontual de dados adulterados.

### 3. 📉 FinOps Automatizado (Lifecycle Rules)
- **Ação:** Configurei a regra `MoverParaGlacierApos30Dias`.
- **Comportamento Lógico:** Todo pacote detectado sem modificação sob o frame de 30 dias é sumariamente despromovido para o *Glacier Instant Retrieval*. No 31º dia, a política encarregada limpa lixo residual.

### 4. 🔗 Compartilhamento com Autodestruição (Pre-signed URL)
- **Ação:** Criei uma assinatura de distribuição temporal focada para clientes alheios usando meu CLI.
- **Geração:** Utilizei o credenciamento temporário nativo do IAM atrelado ao meu perfil montando a string cronometrada `ExpiresIn: 60`.
- **Validação:** Em uma aba limpa anônima, passei o link. A *Versão 1* processou Download em HTTP 200. Decorridos estritos 60 segundos, a mesma janela recarregada apresentou falha retornando o bloqueio terminal `AccessDenied`, atestando a força do mecanismo criptográfico temporal.

---

## 📸 Evidências de Execução

### 1. Interface comprovando o histórico ativado e mantendo as versões seguras
<img src="./assets/01-s3-versioning-active.png" width="100%">

### 2. Navegação externa bem-sucedida atestando captura do payload temporário autorizado
<img src="./assets/02-s3-presigned-url.png" width="100%">

### 3. Fim de janela HTTP 403 provando blindagem e término pela nuvem
<img src="./assets/03-s3-presigned-url-expired.png" width="100%">

> [!IMPORTANT]
> Alguns identificadores críticos sofreram mascaramento aderindo fortemente a *compliance* global de segurança.
> O material bruto usado nos testes (`Lab3.txt`) está persistido em [/src](./src/).

---

## 💡 Principais Aprendizados

- **Preservação Passiva Anti-Wiper:** Demonstrei que frente ao Versionamento enrijecido, a deleção simples falha e oculta a versão real protegendo os dados. Essa mecânica sozinha é a salvaguarda mestre que absorve incidentes severos (*Ransomware/Bugs*).
- **O Fim das Delegações Inseguras:** Entendi que compartilhar URL Pré-assinada elimina a necessidade jurássica de entregar criar usuários IAM soltos para terceiros baixarem dados temporais, mitigando riscos severos. O token expira e a segurança volta ao estado absoluto sem rastros.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| S3 Standard | ✅ 5GB | $0,00 |
| **Total** | | **$0,00** |

> ⚠️ Apaguei o histórico de Versões iterando ID por ID para conseguir destruir o balde no fim do lab com sucesso sem alertas do painel AWS.

---

## 🏷️ Competências Demonstradas

`S3` `Versionamento` `Lifecycle Rules` `Pre-signed URLs` `Block Public Access` `Glacier` `🟢 Fundamental`

---

## 📜 Alinhamento com Certificações

Este lab engole objetivos de engenharia testados em avaliações de segurança:
- **CLF-C02:** Domínio 3 — Tecnologia e Serviços de Cloud
- **SAA-C03:** Domínio 4 — Arquitetura Otimizada em Custo

---

[← Voltar ao índice](../../../README.md)
