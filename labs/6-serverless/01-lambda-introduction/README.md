<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 01 â€” IntroduÃ§Ã£o ao AWS Lambda: Processamento de Imagens Serverless

## ðŸš€ Resumo
Processamento de Dados Orientado a Eventos: Neste laboratÃ³rio, explorei as capacidades computacionais *Serverless* da AWS com o **AWS Lambda**. Projetei uma arquitetura autÃ´noma onde o upload de uma imagem em um bucket do **Amazon S3** dispara automaticamente uma funÃ§Ã£o em **Python 3.12**. Utilizando a biblioteca **Pillow**, a funÃ§Ã£o redimensiona a imagem para criar uma miniatura (thumbnail) e a armazena em um segundo bucket de destino, sem a necessidade de gerenciar qualquer servidor.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** E-commerce e Portais de ConteÃºdo
- **Problema:** Em um site de vendas, os usuÃ¡rios faziam upload de fotos de produtos que chegavam a 10 MB. O site precisava exibir miniaturas rÃ¡pidas para o catÃ¡logo, mas o servidor principal da aplicaÃ§Ã£o ficava lento ao processar essas imagens de forma sÃ­ncrona, afetando a experiÃªncia de navegaÃ§Ã£o de todos os clientes.
- **SoluÃ§Ã£o:** Desacoplei o processamento de imagens utilizando **AWS Lambda**. Integrei o bucket S3 de origem para atuar como gatilho. Agora, assim que a foto Ã© salva, a Lambda acorda, gera a miniatura em milissegundos e a salva em um bucket de saÃ­da. O servidor principal da aplicaÃ§Ã£o ficou livre para focar apenas nas vendas, enquanto a escalabilidade do processamento de imagens tornou-se infinita e extremamente barata, jÃ¡ que pago apenas pelo tempo exato de execuÃ§Ã£o de cada redimensionamento.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Criar funÃ§Ãµes **AWS Lambda** utilizando o runtime Python 3.12.
- Configurar gatilhos (Triggers) automÃ¡ticos baseados em eventos do **Amazon S3**.
- Manipular arquivos em tempo real utilizando a biblioteca **Pillow** dentro do ambiente Serverless.
- Gerenciar permissÃµes de acesso granulares via **IAM Roles** (Leitura no S3 de origem e Escrita no S3 de destino).
- Utilizar o armazenamento efÃªmero `/tmp/` da Lambda para processamento temporÃ¡rio de arquivos.
- Monitorar execuÃ§Ãµes e depurar erros atravÃ©s do **Amazon CloudWatch Logs**.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o | Papel no Lab |
|---------|-------------|
| **AWS Lambda** | ExecuÃ§Ã£o do cÃ³digo Python para redimensionamento de imagens. |
| **Amazon S3** | Armazenamento dos buckets de origem (fotos brutas) e destino (miniaturas). |
| **Amazon CloudWatch** | Monitoramento de mÃ©tricas e retenÃ§Ã£o de logs de execuÃ§Ã£o. |
| **AWS IAM** | DefiniÃ§Ã£o da role de execuÃ§Ã£o com permissÃµes de privilÃ©gio mÃ­nimo. |

---

## ðŸ“ Arquitetura do Projeto

<div align="center">
  <img src="./assets/architecture-lambda-introduction.drawio.png" alt="Arquitetura do Projeto" width="700">
</div>

---

## âš™ï¸ Fases da ImplementaÃ§Ã£o

### Parte 1 â€” PreparaÃ§Ã£o do Storage (S3)
- **AÃ§Ã£o:** Criei dois buckets: `images-original-66f` e `images-resized-66f`.
- **PropÃ³sito:** Isolar o ambiente de entrada do ambiente de saÃ­da, evitando loops infinitos onde a Lambda redimensionaria a prÃ³pria miniatura.

### Parte 2 â€” Desenvolvimento da FunÃ§Ã£o (Lambda)
- **AÃ§Ã£o:** Criei a funÃ§Ã£o `CreateThumbnail` e configurei a Role do IAM.
- **ImplementaÃ§Ã£o:** Desenvolvi o script em Python utilizando o SDK `boto3`. Como a biblioteca `Pillow` nÃ£o Ã© nativa do Lambda, preparei um pacote de implantaÃ§Ã£o (.zip) contendo as dependÃªncias necessÃ¡rias para o processamento de imagem.

### Parte 3 â€” ConfiguraÃ§Ã£o do Gatilho
- **AÃ§Ã£o:** Adicionei um gatilho de "S3 Event Notification" na Lambda.
- **Filtro:** Configurei para disparar apenas em eventos de `s3:ObjectCreated:*` e opcionalmente para extensÃµes especÃ­ficas, garantindo que a funÃ§Ã£o nÃ£o seja invocada por arquivos desnecessÃ¡rios.

### Parte 4 â€” Testes e ValidaÃ§Ã£o
- **AÃ§Ã£o:** Realizei o upload de uma imagem de alta resoluÃ§Ã£o e monitorei o CloudWatch Logs.
- **Resultado:** Validei que o bucket de destino recebeu a versÃ£o reduzida da imagem instantaneamente, com o log confirmando o sucesso do processamento.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. PreparaÃ§Ã£o (S3): CriaÃ§Ã£o dos buckets originais e destino
<img src="./assets/S3-buckets.png" width="100%">

### 2. CriaÃ§Ã£o da FunÃ§Ã£o: InicializaÃ§Ã£o da Lambda `CreateThumbnail`
<img src="./assets/Create-Thumbnail-Functions-Lambda.png" width="100%">

### 3. CriaÃ§Ã£o Bem-sucedida: ConfirmaÃ§Ã£o de criaÃ§Ã£o da Lambda e visibilidade de painel
<img src="./assets/Create-Thumbnail-Functions-Lambda-sucess.png" width="100%">

### 4. EdiÃ§Ã£o BÃ¡sica: ConfiguraÃ§Ã£o de tempo limite e tamanho de memÃ³ria
<img src="./assets/Edit-basic-settings-Create-Thumbnail-Functions-Lambda.png" width="100%">

### 5. Runtime e Role: DefiniÃ§Ã£o de permissÃµes de execuÃ§Ã£o compatÃ­veis com S3
<img src="./assets/Edit-runtime-settings-Create-Thumbnail-Functions-Lambda.png" width="100%">

### 6. Deploy do Pacote: Upload do cÃ³digo .zip hospedado pelo S3 com dependÃªncias (Pillow)
<img src="./assets/Functions-Lambda-Upload-from-s3.png" width="100%">

### 7. ConfiguraÃ§Ã£o de Gatilho: Evento associado a PUT de imagens no bucket fonte
<img src="./assets/Add-triggers-Lambda.png" width="100%">

### 8. Disparo de Teste: Payload do Evento JSON simulando um PUT no S3
<img src="./assets/Test-Thumbnail-Functions-Lambda.png" width="100%">

### 9. Monitoramento de InvocaÃ§Ã£o: GrÃ¡ficos em tempo real das invocaÃ§Ãµes e erros da Lambda
<img src="./assets/Monitor-Thumbnail-Functions-Lambda.png" width="100%">

### 10. Sucesso/Output: Miniatura gerada com sucesso e arquivada via cÃ³digo
<img src="./assets/images-28032026-resized-S3-bucket-S3.png" width="100%">

### 11. ComparaÃ§Ã£o Visual: Imagem Original vs. Miniatura Gerada (Thumbnail)

**Imagem Original:**
<img src="./assets/HappyFace.jpg" width="100%">

**Upload Processado (Miniatura):**
<img src="./assets/HappyFace%20(1).jpg" width="100%">

---

### 12. Rastreabilidade de Logs: HistÃ³rico de instÃ¢ncias acionadas pela Lambda
<img src="./assets/CloudWatch-log.png" width="100%">

### 13. AnÃ¡lise de Performance: ConfirmaÃ§Ã£o de tempo de execuÃ§Ã£o e memÃ³ria faturÃ¡vel
<img src="./assets/CloudWatch-log-events.png" width="100%">

## ðŸ’¡ Principais Aprendizados

- **Event-Driven vs Polling:** Em vez de ter um servidor procurando por arquivos novos (polling), a arquitetura Event-Driven reage apenas quando o evento ocorre. Isso elimina o desperdÃ­cio de recursos e custos com servidores ociosos.
- **O uso do /tmp/:** Aprendi que a Lambda oferece um sistema de arquivos temporÃ¡rio. Ã‰ essencial baixar a imagem para este diretÃ³rio, processÃ¡-la e depois enviÃ¡-la ao destino, jÃ¡ que nÃ£o podemos manipular a imagem "no ar" diretamente na memÃ³ria em alguns casos de processamento de arquivos.
- **Estrutura de Eventos JSON:** A Lambda recebe as coordenadas do arquivo (bucket e chave), e nÃ£o o arquivo em si. Entender como navegar no objeto JSON enviado pelo S3 Ã© fundamental para o sucesso da funÃ§Ã£o.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso | Free Tier? | Custo Estimado |
|---------|-----------|----------------|
| AWS Lambda | âœ… 1 MilhÃ£o de solicitaÃ§Ãµes gratuitas/mÃªs | $0,00 |
| Amazon S3 | âœ… AtÃ© 5GB no padrÃ£o Standard | $0,00 |
| **Total Estimado** | | **$0,00** |

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`AWS Lambda` `Amazon S3` `Event-Driven Automation` `Serverless Computing` `Python Boto3` `CloudWatch` `ðŸ”´ AvanÃ§ado`

---

## ðŸ“œ Alinhamento com CertificaÃ§Ãµes

- **CLF-C02:** DomÃ­nio 3 â€” Tecnologia (Cloud Computing Serverless)
- **DVA-C02:** DomÃ­nio 1 â€” Desenvolvimento com ServiÃ§os AWS

---

[â† Voltar ao Ã­ndice](../../../README.md)