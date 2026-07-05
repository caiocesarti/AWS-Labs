<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 02 â€” IntroduÃ§Ã£o ao Amazon CloudFront

## ðŸš€ Resumo
ImplementaÃ§Ã£o de Redes de DistribuiÃ§Ã£o de ConteÃºdo (CDN) utilizando o **Amazon CloudFront**. Este laboratÃ³rio detalha a orquestraÃ§Ã£o de *Edge Locations* (Locais de Borda) globais para fragmentar a latÃªncia de entrega, conectando instÃ¢ncias baseadas em **Amazon S3**. Explorei a hospedagem estÃ¡tica otimizada de mÃ­dias globais construindo uma proteÃ§Ã£o unificada que bloqueia o acesso direto ao *Bucket S3* via controles nativos restritos (OAC).

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Portal de NotÃ­cias / E-commerce de MÃ­dia
- **Problema:** Um e-commerce lanÃ§a um evento contendo imagens promocionais pesadas (4K). Todo o conteÃºdo repousa em um Ãºnico bucket S3 alocado em *Norte da VirgÃ­nia (us-east-1)*. Quando os clientes no Brasil, JapÃ£o ou AustrÃ¡lia acessam o site, o trÃ¡fego transoceÃ¢nico atrasa o carregamento em atÃ© 6 segundos, gerando perda de vendas e uma fatura de transferÃªncia (*Data Transfer Out*) massiva ligada Ã  longa distÃ¢ncia fÃ­sica do pacote.
- **SoluÃ§Ã£o:** Integrei o **Amazon CloudFront** como a ponte interceptadora primÃ¡ria das *URLs*. A mÃ­dia do S3 passou a ser armazenada em cache proativamente em centenas de *Edge Locations* prÃ³ximos dos clientes. Quando um usuÃ¡rio no JapÃ£o solicita a mÃ­dia, o CloudFront a entrega localmente em incrÃ­veis 10ms de latÃªncia. Apenas a primeira requisiÃ§Ã£o vai ao S3 em us-east-1; o restante flui pelas bordas descentralizadas. AlÃ©m disso, bloqueei o *Bucket* exigindo que o acesso Ã  URL aconteÃ§a unicamente pelo CloudFront, barrando leituras diretas abertas.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Consolidar recipientes providenciando o **Amazon S3** como Ã¢ncoras inativas de conteÃºdo nativo (Origin).
- Provisionar interfaces associando **DistribuiÃ§Ãµes CloudFront (Global CDN)** isoladas e dinÃ¢micas.
- Orquestrar a proteÃ§Ã£o do *Origin* definindo rotas rigorosas que garantem a indisponibilidade total dos links S3 abertos nativamente.
- Despachar sites DNS automÃ¡ticos focando em domÃ­nios de acesso rÃ¡pidos (`.cloudfront.net`).
- Integrar painÃ©is HTML estÃ¡ticos simulando a leitura do CDN em baixa latÃªncia global.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **Amazon CloudFront** | Operador principal CDN que serve cÃ³pias ativas cacheadas nos domÃ­nios perifÃ©ricos solicitantes. |
| **Amazon S3** | Provedor host passivo raiz (Origem) encarregado da hospedagem dos arquivos sem exposiÃ§Ã£o direta. |
| **AWS Edge Locations** | Mini-datacenters da AWS espalhados globalmente servindo trÃ¡fegos operacionais em baixa latÃªncia. |

---

## ðŸ—ï¸ Arquitetura da SoluÃ§Ã£o

<div align="center">
  <img src="./assets/Diagrama-CloudFront.png" alt="Arquitetura da Solução" width="700">
</div>

*(O design destaca que somente 1 requisiÃ§Ã£o acessa o S3; depois toda a malha Ã© atendida nas bordas).*

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. ðŸ“‹ ConfiguraÃ§Ã£o da Base Original PrimÃ¡ria (S3 Origin)
- **AÃ§Ã£o:** Formatar o bucket host para armazenar o arquivo raiz.
- **ConfiguraÃ§Ã£o de ProteÃ§Ã£o:** Estabeleci as restriÃ§Ãµes bloqueando a visualizaÃ§Ã£o externa. Sublinhei restriÃ§Ãµes nativas mantendo as *ACLs* desativadas e o parÃ¢metro de *Bloqueio Global PÃºblico* totalmente ativo.
- **VerificaÃ§Ã£o Negativa:** Validei a proteÃ§Ã£o rodando um upload (`.jpg`) e tentando abrir no navegador. O erro visual `AccessDenied` provou que o sistema de bloqueios funciona blindando a arquitetura isolada.

### 2. ðŸ—„ï¸ AtivaÃ§Ã£o Transcontinental de Entrega (CloudFront)
- **AÃ§Ã£o:** Provisionar a DistribuiÃ§Ã£o espelhando ativamente o AWS Edge.
- **IntegraÃ§Ã£o:** Injetei no campo Origin Domain o bucket restritivo matriz gerado no S3.
- **ParametrizaÃ§Ã£o OAI/OAC:** Adicionei controles de "Origin Access Control". Determinei cirurgicamente que a polÃ­tica permitisse puro e simples fluxo que vem exclusivamente da nuvem do CloudFront para acessar minhas pastas raiz do S3 ("Update policy").

### 3. ðŸ” ValidaÃ§Ã£o End-to-End via Endpoint Edge
- **AÃ§Ã£o:** Bater na infraestrutura empÃ­rica injetando componentes simples Web em HTML.
- **RequisiÃ§Ã£o HTML Cruzada:** Forjei um laboratÃ³rio prÃ¡tico editando um index local (`myimage.html`) inserindo no cÃ³digo `<img>` o prefixo DNS AWS: `dXXX.cloudfront.net`.
- **Efeito Visual PrÃ¡tico:** Acessei o teste no browser. O trÃ¡fego realizou eficientemente a primeira carga (*Miss* de cache) indo no S3. Refreshes subsequentes (*Hits*) trouxeram a imagem velozmente da borda local.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. S3 Origin Setup: CriaÃ§Ã£o da base nativa operante no bucket S3 raiz para reter o objeto
<img src="./assets/S3-buckets-S3.png" width="100%">

### 2. Bucket Isolation: Foco no artefato estanque interno alocado sem trÃ¢mites livres e bloqueado em sigilo
<img src="./assets/cfcaiocesar2026-S3-bucket-S3.png" width="100%">

### 3. CDN Global Distribution: CloudFront globalizado despachando URLs formatados para entrega das mÃ­dias ativas isoladamente
<img src="./assets/Distributions-CloudFront-Global.png" width="100%">

### 4. Low Latency Verification: Teste front-end batendo nas rotas DNS sem violar as rotas diretas do S3 original
<img src="./assets/cloudfront-teste-myimage-html.png" width="100%">
> [!IMPORTANT]
> Mascarei visualmente os links de distribuiÃ§Ã£o autÃªntica por sigilo.
> O script em HTML pode ser consultado fisicamente inspecionando o repositÃ³rio em `/src/myimage.html`.

---

## ðŸ’¡ Principais Aprendizados

- **ProteÃ§Ã£o Origem Blindada (OAC):** Ao amarrar o Origin Access Control, converti a CDN num formidÃ¡vel escudo frente ao bucket: qualquer cliente ou ataque mirando no formato padrÃ£o S3 Ã© instantaneamente barrado. Apenas conexÃµes validadas pela DistribuiÃ§Ã£o global encontram o alvo.
- **Estabilidade Escalonada:** Entendi o poder perimetral da nuvem mitigando impactos e picos (*Data Transfer Extortions Costs*). A infraestrutura processa o trÃ¡fego nas redes fÃ­sicas dos nÃ³s em TÃ³quio sem exigir sequer um byte adicional da mÃ¡quina nos Estados Unidos durante o resto da temporada sazonal comercial.
- **Conectividade Edge Integrada:** Vi como uma regiÃ£o `us-east-1` restrita pode alcanÃ§ar clientes Europeus operando e sentindo velocidades operacionais tal qual provedores e data centers locais estivessem presentes instalados dentro do mesmo prÃ©dio fÃ­sico.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| CloudFront Data CDN | âœ… 1TB fixo + 10 MilhÃµes HTTPS requisiÃ§Ãµes | $0,00 |
| S3 Storage | âœ… Base estÃ¡tica operando na cobertura atÃ© 5GB | $0,00 |
| **Total Estimado** | | **$0,00** |

> âš ï¸ Interrompa explÃ­citamente a distribuiÃ§Ã£o em dois passos preventivos. Alterne primeiramente o *Status* aplicando `Disable` confirmando a desativaÃ§Ã£o da malha regional inteira. Sequencialmente execute o `Delete`. Por fim, elimine os arquivos raÃ­zes esquecidos da matriz *S3 Origin*.

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`CloudFront` `Amazon CDN` `Edge Locations` `S3 Origin Validation (OAC)` `Data Transfer Scaling` `Global Architecture` `Website Security Perimeter` `ðŸŸ¢ Fundamental`

---

[â† Voltar ao Ã­ndice](../../../README.md)
