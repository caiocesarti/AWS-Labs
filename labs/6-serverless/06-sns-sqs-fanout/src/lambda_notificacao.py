import json

def lambda_handler(event, context):
    """
    Simula o envio de notificações de confirmação para o cliente.
    Acionado pelo SNS quando EventType IN ['OrderConfirmed', 'OrderShipped']
    """
    print("### LAMBDA NOTIFICAÇÃO CLIENTE INICIADA ###")
    
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        attributes = record['Sns']['MessageAttributes']
        
        event_type = attributes.get('EventType', {}).get('Value')
        
        print(f"Enviando e-mail para Cliente ID: {message.get('cliente_id')}")
        print(f"Assunto: O seu pedido {message.get('pedido_id')} mudou para: {event_type}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Notificação Enviada!')
    }
