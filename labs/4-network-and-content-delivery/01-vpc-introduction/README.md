<div align="right">
  <a href="./README-en.md">ðŸ‡ºðŸ‡¸ English</a> |
  <a href="./README.md">ðŸ‡§ðŸ‡· PortuguÃªs</a>
</div>

# Lab 01 â€” IntroduÃ§Ã£o ao Amazon Virtual Private Cloud (VPC)

## ðŸš€ Resumo
Mensageria AssÃ­ncrona e ResiliÃªncia DistribuÃ­da: Neste laboratÃ³rio, implementei os fundamentos da infraestrutura de nuvem: Redes Virtuais Privadas. Provisonei uma **Amazon VPC** isolada logicamente, segmentando o ambiente em Sub-redes PÃºblicas (Web/Proxy) e Privadas (Bancos de Dados). Configurei camadas granulares de conectividade atravÃ©s de um **Internet Gateway (IGW)**, tabelas de roteamento (*Route Tables*) e um **NAT Gateway** dedicado para garantir acesso seguro e unidirecional Ã  internet sem expor o backend interno.

---

## ðŸ’¼ Caso de Uso Real
- **IndÃºstria:** Setor BancÃ¡rio / SaÃºde Digital (HealthTech)
- **Problema:** Um hospital implanta seu sistema de prontuÃ¡rios eletrÃ´nicos na AWS. Contudo, ao subirem os servidores web e de banco de dados na mesma rede pÃºblica padrÃ£o, cibercriminosos interceptam portas expostas e iniciam ataques de *Brute Force*, comprometendo instÃ¢ncias vulnerÃ¡veis.
- **SoluÃ§Ã£o:** Reengenharia orientada por fragmentaÃ§Ã£o de rede (*Network Segmentation*). Roteei o trÃ¡fego via uma Amazon VPC customizada. Empurrei os componentes crÃ­ticos para dentro de *Sub-redes Privadas*, tornando a alocaÃ§Ã£o de IPs pÃºblicos impossÃ­vel. Como instÃ¢ncias privadas precisam baixar pacotes da internet sem serem acessadas de fora, estruturei um *NAT Gateway* ancorado numa *Sub-rede PÃºblica*. Essa infraestrutura consolida camadas de defesa protegendo os dados.

---

## ðŸŽ¯ Objetivos de Aprendizado

- Instanciar a infraestrutura de redes configurando uma Amazon VPC isolada via modelo CIDR Base (Ex: `10.0.0.0/16`).
- Isolar a aplicaÃ§Ã£o distribuindo componentes em sub-redes **PÃºblicas** e **Privadas** estrategicamente.
- Decodificar e operar a entrada e saÃ­da atrelando o **Internet Gateway (IGW)**.
- Mapear caminhos direcionando solicitaÃ§Ãµes atravÃ©s da bifurcaÃ§Ã£o em **Tabelas de Roteamento (Route Tables)**.
- Habilitar conectividade reversa mascarando identidades privadas usando o trÃ¡fego de um **NAT Gateway**.
- Contrastar restriÃ§Ãµes transacionais pontuais cruzando perÃ­metros por **Network ACLs** e **Security Groups**.

---

## ðŸ› ï¸ ServiÃ§os AWS Utilizados

| ServiÃ§o              | Papel no Lab                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| **Amazon VPC**       | A rede inteiramente customizÃ¡vel que emula um *Data Center* privativo.                          |
| **VPC Subnets**      | Matrizes segmentando blocos estruturados de IP por nÃ­vel de acesso (PÃºblico/Privado).           |
| **Internet Gateway** | Ponte garantindo comunicaÃ§Ãµes essenciais conectando a nuvem Ã  grande rede pÃºblica.              |
| **NAT Gateway**      | Dispositivo que providencia exclusivamente saÃ­da de requisiÃ§Ãµes originadas nas redes fechadas.  |
| **Route Tables**     | Roteadores virtuais que ditam o escoamento direcionando qual trÃ¡fego escaparÃ¡ por quais pontes. |

---

## ðŸ—ï¸ Arquitetura da SoluÃ§Ã£o

<div align="center">
  <img src="./assets/Diagrama-1.png" alt="Diagrama de Infraestrutura - Parte 1" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-2.png" alt="Diagrama de Infraestrutura - Parte 2" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-3.png" alt="Diagrama de Infraestrutura - Parte 3" width="700">
</div>

<div align="center">
  <img src="./assets/Diagrama-4.svg" alt="Diagrama de Infraestrutura - Parte 4" width="700">
</div>

---

## ðŸ–¥ï¸ Etapas do LaboratÃ³rio

### 1. ðŸ“‹ LanÃ§amento Controlado via VPC Wizard
- **AÃ§Ã£o:** CriaÃ§Ã£o assistida da topologia base.
- **ConfiguraÃ§Ãµes Vitais:**
  - IdentificaÃ§Ã£o (Tag): `Lab-vpc`
  - Bloco CIDR Mestre IPv4: `10.0.0.0/16`
  - NÃºmero de Zonas de Disponibilidade (AZs): `1`
  - Quantidade de *Subnets PÃºblicas*: `1` (CIDR: `10.0.25.0/24`)
  - Quantidade de *Subnets Privadas*: `1` (CIDR: `10.0.50.0/24`)
- **AÃ§Ã£o:** Provisionei a arquitetura de forma assistida para garantir a correta topologia. A AWS alocou o `Internet Gateway (IGW)` e injetou as instÃ¢ncias de `NAT Gateway` em uma Ãºnica operaÃ§Ã£o, otimizando a configuraÃ§Ã£o manual.

### 2. ðŸ” InspeÃ§Ã£o Arquitetural (Componentes Isolados)
- **Tabelas CrÃ­ticas de Rotas (Route Tables):**
  - Chequei o ambiente logado e validei que a *Tabela Route PÃºblica* aponta rigorosamente as saÃ­das (`0.0.0.0/0`) batendo no destino `igw-*`.
  - Inspecionei a *Tabela Route Privada*, confirmando que os registros genÃ©ricos alteram a saÃ­da redirecionando pacotes cegamente para atravessar o dispositivo fÃ­sico `nat-*`.
- **Muros de Fogo (Network ACLs):** Confirmei os bloqueios padronizados aplicados rigidamente nas subdivisÃµes.

---

## ðŸ“¸ EvidÃªncias de ExecuÃ§Ã£o

### 1. Topologia Lab-VPC: Trajeto consolidado alocando e estabilizando a topologia estruturada
<img src="./assets/vpcs-VPC-Console.png" width="100%">

### 2. CIDR Mestre: Espelhamento dinÃ¢mico visualizando as configuraÃ§Ãµes do CIDR operante
<img src="./assets/VPC-us-west-2.png" width="100%">

### 3. SegmentaÃ§Ã£o de Subnets: Listagem evidenciando a criaÃ§Ã£o das Sub-redes PÃºblicas e Privadas garantindo os perÃ­metros
<img src="./assets/subnets-VPC-Console.png" width="100%">

### 4. Tabelas de Roteamento: O mapeamento matemÃ¡tico isolando trÃ¡fegos com sucesso
<img src="./assets/VPC-us-west-2-route-table.png" width="100%">

### 5. NAT Gateway: Dispositivo criado com sucesso sob o domÃ­nio da Sub-rede PÃºblica
<img src="./assets/NatGateways-VPC-Console.png" width="100%">

### 6. Regional Matrix: Topologia em mapa comprovando a existÃªncia fluida das tabelas e blocos
<img src="./assets/VPC-us-west-2-03-25.png" width="100%">
> [!IMPORTANT]
> IDs das sub-redes e IPs sofreram omissÃ£o visual por diretrizes de seguranÃ§a AWS.

---

## ðŸ’¡ Principais Aprendizados

- **EstruturaÃ§Ã£o de Roteamento:** Entendi que uma "Rede PÃºblica" nÃ£o Ã© "PÃºblica" sÃ³ pelo nome; na AWS, a natureza de uma Sub-rede depende puramente da *AssociaÃ§Ã£o de Rota* (Route Table) enviando o trÃ¡fego `0.0.0.0/0` para um Internet Gateway (IGW).
- **Escudo NAT:** Confirmei na prÃ¡tica o design de redes fechadas: Meus *Bancos de Dados* privados conseguem atualizar softwares conectando-se Ã  internet passando dentro do NAT Gateway, entretanto jamais podem ser encontrados ou atacados diretamente da internet por IPs externos.

---

## ðŸ’° ConsciÃªncia de Custos

| Recurso                   | Free Tier?                                                                                             | Custo Estimado |
| ------------------------- | ------------------------------------------------------------------------------------------------------ | -------------- |
| Amazon VPC Master         | âœ… VPCs em si e Route Tables padrÃ£o sÃ£o isentas de custos                                               | $0,00/mÃªs      |
| Internet Gateway          | âœ… Rotas passivas estÃ¡ticas IGW sÃ£o gratuitas pela AWS                                                  | $0,00/mÃªs      |
| **NAT Gateway**           | âŒ Processadores fÃ­sicos englobados faturam taxa global horÃ¡ria ($0,045/h fixos + $0,045/GB processado) | **~$1,08/Dia** |
| **Total Estimativo Fixo** |                                                                                                        | **$32,40/MÃªs** |

> [!CAUTION]  
> O **NAT Gateway** queima bilhetagem AWS incessantemente por hora, mesmo que vocÃª nÃ£o esteja operando nada. Criei o hÃ¡bito mecÃ¢nico de excluÃ­-los apÃ³s cada laboratÃ³rio de rede, junto aos Elastic IPs "Ã³rfÃ£os" deixados pelo aparelho, pois nÃ£o sÃ£o cobertos pela camada gratuita estendida.

---

## ðŸ·ï¸ CompetÃªncias Demonstradas

`VPC` `Subnets` `NAT Gateway` `Internet Gateway` `Route Tables` `Multi-AZ` `Network ACLs` `Security Groups` `Network Segmentation` `ðŸŸ¢ Fundamental`

---

## ðŸ“œ Alinhamento com CertificaÃ§Ãµes

Este escopo constrÃ³i vetores de nuvem voltados para:
- **CLF-C02:** DomÃ­nio 3 â€” Tecnologia e ServiÃ§os de Cloud
- **SAA-C03:** DomÃ­nio 2 â€” Arquitetura Resiliente de Alta Confiabilidade
- **SAA-C03:** DomÃ­nio 1 â€” Arquiteturas Seguras

---

[â† Voltar ao Ã­ndice](../../../README.md)