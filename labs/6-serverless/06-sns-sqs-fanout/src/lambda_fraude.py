import json

def lambda_handler(event, context):
    """
    Simula a análise de fraude em pedidos de alto valor (> 500).
    Acionado via SQS (Desacoplado) - Filtrado pelo SNS.
    """
    print("### LAMBDA ANÁLISE DE FRAUDE INICIADA (TRIGGER SQS) ###")
    
    for record in event['Records']:
        # Diferente das Lambdas diretas do SNS, aqui a mensagem está no 'body' do SQS
        sqs_body = json.loads(record['body'])
        
        # O corpo do SQS contém o JSON original do SNS se 'Raw Message Delivery' estiver desmarcado
        sns_message = json.loads(sqs_body['Message'])
        sns_attributes = sqs_body['MessageAttributes']
        
        transaction_val = sns_attributes.get('TransactionValue', {}).get('Value')
        
        print(f"Analisando Risco para Pedido: {sns_message.get('pedido_id')}")
        print(f"Valor da Transação Detectado: ${transaction_val}")
        print(f"Aguardando verificação de score anti-fraude...")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Análise de Fraude Concluída!')
    }
