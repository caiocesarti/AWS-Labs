import json
import os


def lambda_handler(event, context):
    """
    Função Lambda - Ambiente de Produção (Versão 2)
    Retorna mensagem fixa de produção, a versão publicada e o alias invocado.
    Compatível com integração Proxy do API Gateway.
    """
    try:
        stage = event['requestContext']['stage']
    except KeyError:
        stage = 'desconhecido'

    response_body = {
        'message': 'Ola do ambiente de Producao!',
        'functionVersion': context.function_version,
        'functionAlias': (
            context.invoked_function_arn.split(':')[-1]
            if ':' in context.invoked_function_arn else '$LATEST'
        )
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response_body, ensure_ascii=False)
    }
