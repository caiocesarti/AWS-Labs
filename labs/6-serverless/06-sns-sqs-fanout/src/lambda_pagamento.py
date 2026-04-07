import json

def lambda_handler(event, context):
    """
    Simula o processamento de pagamentos do e-commerce.
    Acionado pelo SNS quando EventType == 'OrderPlaced' E PaymentType IN ['CreditCard', 'Boleto']
    """
    print("### LAMBDA PAGAMENTO INICIADA ###")
    
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        attributes = record['Sns']['MessageAttributes']
        
        payment_type = attributes.get('PaymentType', {}).get('Value', 'N/A')
        
        print(f"Processando Pagamento para Pedido: {message.get('pedido_id')}")
        print(f"Forma de Pagamento Detectada: {payment_type}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Pagamento Processado!')
    }
