#!/bin/bash
# =============================================================================
# Lab 06 — Criação de instância EC2 via AWS CloudShell / CLI
# =============================================================================
# Pré-requisito: execute este script no AWS CloudShell (não requer configuração
# de credenciais — o CloudShell já herda as permissões da sessão logada).
#
# ATENÇÃO: Substitua os valores abaixo pelo seu nome antes de executar.
# Não use espaços nem caracteres especiais nos nomes.
# =============================================================================

# -----------------------------------------------------------------------------
# PASSO 1 — Definir variáveis personalizadas
# Substitua <seunome> pelo seu nome e sobrenome sem espaços (ex: caiocesar)
# -----------------------------------------------------------------------------
GRUPO_SEGURANCA="<seunome>-grupo"    # ex: caiocesar-grupo
NOME_INSTANCIA="instancia-<seunome>" # ex: instancia-caiocesar
PAR_CHAVE="parchave-<seunome>"       # deve corresponder ao par criado no console

# -----------------------------------------------------------------------------
# PASSO 2 — Criar o Security Group com permissão HTTP (porta 80)
# -----------------------------------------------------------------------------
SECURITY_GROUP_ID=$(aws ec2 create-security-group \
  --group-name "$GRUPO_SEGURANCA" \
  --description "Permitir HTTP" \
  --query "GroupId" \
  --output text)

echo "Security Group criado: $SECURITY_GROUP_ID"

# -----------------------------------------------------------------------------
# PASSO 3 — Liberar tráfego HTTP (porta 80) para qualquer origem
# -----------------------------------------------------------------------------
aws ec2 authorize-security-group-ingress \
  --group-id "$SECURITY_GROUP_ID" \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

# -----------------------------------------------------------------------------
# PASSO 4 — Obter o ID da AMI Amazon Linux 2023 mais recente e lançar instância
#
# O User Data (base64) contém o script de inicialização do servidor web:
#   #!/bin/bash
#   yum -y install httpd
#   systemctl enable httpd
#   systemctl start httpd
#   echo '<html><h1>Olá do seu servidor web!</h1></html>' > /var/www/html/index.html
# -----------------------------------------------------------------------------
aws ec2 run-instances \
  --instance-type t2.micro \
  --image-id $(aws ssm get-parameters-by-path \
    --path "/aws/service/ami-amazon-linux-latest" \
    --query "Parameters[?ends_with(Name, 'al2023-ami-kernel-default-x86_64')].Value" \
    --output text) \
  --security-group-ids "$SECURITY_GROUP_ID" \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value='$NOME_INSTANCIA'}]" \
  --key-name "$PAR_CHAVE" \
  --user-data "IyEvYmluL2Jhc2gKeXVtIC15IGluc3RhbGwgaHR0cGQKc3lzdGVtY3RsIGVuYWJsZSBodHRwZApzeXN0ZW1jdGwgc3RhcnQgaHR0cGQKZWNobyAnPGh0bWw+PGgxPk9sw6EgZG8gc2V1IHNlcnZpZG9yIHdlYiE8L2gxPjwvaHRtbD4nID4gL3Zhci93d3cvaHRtbC9pbmRleC5odG1sCg=="

echo "Instância '$NOME_INSTANCIA' solicitada com sucesso!"
echo "Aguarde ~2 minutos e localize o IPv4 público no console EC2."
