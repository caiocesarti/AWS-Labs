import boto3
import argparse
import sys

def assume_role(role_arn, session_name, duration_seconds):
    """
    Assume a role and get temporary credentials.
    """
    sts_client = boto3.client('sts')
    try:
        assumed_role_object = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name,
            DurationSeconds=duration_seconds,
        )
        credentials = assumed_role_object['Credentials']
        return credentials
    except Exception as e:
        print(f"Error assuming role: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='AWS Security Token Service (STS) - Gera credenciais temporárias.')
    parser.add_argument('--role-arn', required=True, help='O ARN da role a ser assumida.')
    parser.add_argument('--session-name', default='SessaoTemporaria', help='Nome da sessão (default: SessaoTemporaria)')
    parser.add_argument('--duration', type=int, default=3600, help='Duração em segundos (default: 3600 | Max: configurado na role)')

    args = parser.parse_args()

    creds = assume_role(args.role_arn, args.session_name, args.duration)

    print("\n" + "="*50)
    print("      CREDENCIAIS TEMPORÁRIAS GERADAS (STS)")
    print("="*50)
    print(f"AWS Access Key ID:     {creds['AccessKeyId']}")
    print(f"AWS Secret Access Key: {creds['SecretAccessKey']}")
    print(f"AWS Session Token:     {creds['SessionToken']}")
    print(f"Data de Expiração:     {creds['Expiration']}")
    print("="*50 + "\n")
    print("### Dica: No CloudShell, para testar estas credenciais, use:")
    print("aws configure")
    print("E adicione manualmente o Session Token no arquivo ~/.aws/credentials\n")

if __name__ == "__main__":
    main()
