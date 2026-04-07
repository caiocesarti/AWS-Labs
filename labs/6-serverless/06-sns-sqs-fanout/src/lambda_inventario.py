import json

def lambda_handler(event, context):
    """
    Simula a atualização do estoque/inventário de produtos do e-commerce.
    Acionado pelo SNS quando EventType == 'OrderPlaced'
    """
    print("### LAMBDA INVENTÁRIO INICIADA ###")
    
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        attributes = record['Sns']['MessageAttributes']
        
        print(f"Processando Pedido ID: {message.get('pedido_id')}")
        print(f"Itens do Pedido: {message.get('itens')}")
        print(f"Atributo SNS EventType: {attributes.get('EventType', {}).get('Value')}")
        
        # Simulação de lógica de negócio
        for item in message.get('itens', []):
            print(f"-> Verificando estoque para Produto: {item['produto_id']} | Qtd: {item['quantidade']}")
            
    return {
        'statusCode': 200,
        'body': json.dumps('Inventário Processado com Sucesso!')
    }
