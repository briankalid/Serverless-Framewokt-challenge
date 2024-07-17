import json
from src import flujo_retorno, retorno_inversion

def profitability_flow(event, context):
    body = json.loads(event["body"])

    result = {"data": flujo_retorno(body,body["Ciclos"])}

    response = {"statusCode": 200, "body": json.dumps(result)}

    return response

def profitability_time(event, context):

    body = json.loads(event["body"])
    
    result = {"data": retorno_inversion(body)}

    response = {"statusCode": 200, "body": json.dumps(result)}

    return response
    