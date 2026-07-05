<div align="right">
  <a href="./README-en.md">🇺🇸 English</a> |
  <a href="./README.md">🇧🇷 Português</a>
</div>

# Lab 02 — Gerenciamento Avançado de Amazon S3: Versionamento, Ciclo de Vida e Segurança

## 🚀 Resumo
Implementação de governança de dados (*Data Governance*) e práticas de *FinOps* para o Amazon S3. O laboratório arquiteta políticas automatizadas limitando custos através de Transições de Ciclo de Vida (Standard → Glacier), ativa trilhas de auditoria (Server Access Logging) e estabelece canais de compartilhamento restrito utilizando URLs Pré-assinadas.

---

## 💼 Caso de Uso Real
- **Indústria:** Saúde / Jurídico (Compliance)
- **Problema:** Um escritório de advocacia acumula centenas de terabytes em petições no S3. Pagar a taxa integral do *S3 Standard* para arquivos de 5 anos atrás (que raramente são lidos) custa milhares de dólares. Além disso, quando solicitam compartilhar um lote sensível de documentos temporariamente com um auditor externo, criar recursos IAM na infraestrutura é complexo e inseguro.
- **Solução:** Aplicam-se as **Lifecycle Rules**. O arquivo fica na área rápida (Standard) por 30 dias; depois uma regra migra matematicamente o arquivo para o *Deep Archive*, onde o custo cai significativamente. Para o acesso do auditor externo, forja-se uma **Pre-signed URL** via CLI expirável em 5 minutos, garantindo que o arquivo se torne inacessível sem a necessidade de criar regras complexas ou prover usuários sistêmicos.

---

## 🎯 Objetivos de Aprendizado

- Ativar e gerenciar **Object Versioning** como salvaguarda primária contra remoção.
- Configurar **Regras de Ciclo de Vida (Lifecycle Rules)** aplicando princípios rígidos de *FinOps* para retenção prolongada migrando bytes para o ecossistema Glacier.
- Produzir e distribuir ativamente **URLs Pré-assinadas (Pre-signed URLs)** via AWS CLI, garantindo acesso temporal a objetos sigilosos.
- Atrelar monitoramento ativando **Server Access Logging**, pavimentando a pista para relatórios perimetrais globais (SIEM).

---

## 🛠️ Serviços AWS Utilizados

| Serviço | Papel no Lab |
|---------|-------------|
| **Amazon S3** | Estrutura primária recebendo dados, hospedando logs de acesso e processando o versionamento interno. |
| **S3 Lifecycle** | Regra nativa orquestrando a redução de custos por métricas temporais diárias (Transições/Expirações). |
| **AWS CLI** | Executa parâmetros programáticos gerando instantaneamente tokens criptográficos (Pre-signed URL). |

---

## 🏗️ Arquitetura da Solução

<div align="center">
  <img src="./assets/architecture-s3-advanced-management.png" alt="Arquitetura da Solução" width="700">
</div>

---

## 🖥️ Etapas do Laboratório

### 1. 🛡️ Proteção por Versionamento Estrutural
- **Ação:** Instanciei os repositórios base.
- **Configuração:** Acoplei o *Bucket Versioning* imediatamente. Emulei um ataque forçando exclusões de arquivos via painel; demonstrei validando que as deleções na verdade disparam *Delete Markers*, enclausurando o arquivo puro abaixo em estado recuperável e seguro.

### 2. 📉 Engenharia de FinOps (Ciclo de Vida)
- **Ação:** Criei ativamente Regras de Retenção a longo prazo de ponta a ponta.
- **Configuração de Transições:**
  - `Dia 30`: Rebaixamento dinâmico para *Standard-IA* (Infrequent Access).
  - `Dia 90`: Transferência final para o cofre congelado do *Glacier Flexible Retrieval*, cortando os custos brutos passivos severamente.
  - `Ano 1`: Fim de validade legal. Expiração e exclusão definitiva efetuada pelos motores AWS.

### 3. ⏱️ Compartilhamento Restrito Cronometrado (Pre-signed URL)
- **Ação:** Distribuí um arquivo de forma sigilosa operando via tokens fora do painel gerencial.
- **AWS CLI:** `aws s3 presign s3://nome-do-bucket/log.txt --expires-in 300`
- **Validação:** A *String* gerada me garantiu que o portador do link receba tráfego HTTP sem barreiras pelo limite exato de 5 minutos, perdendo acesso instantaneamente sem necessidade de automações de revogação diretas.

### 4. 🕵️‍♂️ Auditoria Global (Access Logs)
- **Ação:** Estabeleci a trilha rastreável preparando um ambiente integrável (SIEM).
- **Configuração:** Construí um *Target Bucket* desenhado focando absorver registros puros rastreando Put/Gets perenemente, reportando status de sucessos ou quedas mapeando origens de rede ativamente de forma invisível ao repositório cliente primário alvo de produção.

---

## 📸 Evidências de Execução

### 1. Visualização dos buckets criados e de suas responsabilidades segregadas
<img src="./assets/01-s3-buckets-list.png" width="100%">

### 2. Trava essencial apontando proteção permanente de edição como "Enabled"
<img src="./assets/02-s3-versioning-active.png" width="100%">

### 3. Cronogramas operando contra IA e camadas densas do Glacier
<img src="./assets/03-s3-lifecycle-rules.png" width="100%">

### 4. Sistema autônomo Server Access empurrando logs para balde de auditoria separado
<img src="./assets/04-s3-server-logging-config.png" width="100%">

> [!IMPORTANT]
> Alguns identificadores foram mascarados por boas práticas de segurança cibernética corporativa.

---

## 💡 Principais Aprendizados

- **Versionamento Dinâmico:** Compreendi que Versionamento atua blindando os estátus de objetos através de *Delete Markers*. Notei entretanto, que ignorar as regras de *Lifecycle* fará versões antigas acumularem perigosamente os impostos estáticos no final do mês sem limites programáticos lógicos de saneamento.
- **Governança Pós-Ciclo:** Confiar na memória de humanos movendo planilhas pesadas é caro. As *Lifecycle Rules* executam migração cirúrgica para as camadas Archive, gerando escalabilidade saudável sem afetar a arquitetura front-end acessada rotineiramente.
- **Autorização Encriptada Temporária:** As *Pre-signed URLs* resolvem buracos de DevOps fornecendo fendas temporárias via AWS CLI sem que eu precisasse atribuir privilégios perigosos cruzando as contas em redes abertas não monitoradas. O Token desaparece magicamente com excelente confiabilidade após a vigência dos seus pacotes.

---

## 💰 Consciência de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| S3 Standard | ✅ 5GB / 2.000 PUTs / 20.000 GETs | $0,00 |
| S3 Glacier | Cobrado após transição temporal | $0,00 |
| **Total** | | **$0,00** |

---

## 🏷️ Competências Demonstradas

`S3` `Versionamento` `Lifecycle Rules` `Pre-signed URLs` `Server Access Logging` `FinOps` `Glacier` `🟢 Fundamental`

---

[← Voltar ao índice](../../../README.md)
