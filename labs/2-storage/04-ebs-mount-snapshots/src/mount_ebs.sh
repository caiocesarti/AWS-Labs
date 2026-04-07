#!/bin/bash
# Script de referência contendo os passos executados dentro do MobaXterm na EC2 (Amazon Linux 2)

# 1. Identificar o disco bruto anexado (geralmente /dev/xvdf ou /dev/sdh dependendo do hypervisor)
echo "Listando dispositivos de bloco..."
lsblk

# DEFINA AQUI A VARIÁVEL DO SEU DISCO IDENTIFICADO NO COMANDO ACIMA
DISCO="/dev/xvdf"

# 2. Formatar o volume EBS com o sistema de arquivos ext4
# AVISO: Apenas execute em volumes NOVOS/vazios, caso contrário perderá dados!
echo "Formatando o disco $DISCO em formato ext4..."
sudo mkfs.ext4 $DISCO

# 3. Criar o diretório que servirá como Ponto de Montagem (Mount Point)
MOUNT_DIR="/mnt/dados"
echo "Criando o diretório de montagem em $MOUNT_DIR..."
sudo mkdir -p $MOUNT_DIR

# 4. Montar o disco
echo "Montando $DISCO no diretório $MOUNT_DIR..."
sudo mount $DISCO $MOUNT_DIR

# 5. Validação final
echo "Validando a montagem física no sistema de arquivos:"
lsblk
df -hT | grep $MOUNT_DIR

echo "SUCESSO: Seu diretório $MOUNT_DIR está pronto e amparado por um EBS durável!"
