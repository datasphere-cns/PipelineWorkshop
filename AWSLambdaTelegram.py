#------------------------------------------------------------------
#Autor: Nelson Zepeda
#Correo: nelson.zepeda@datasphere.tech
#Fecha Creación: Julio 1, 2022
#Log Cambios:
#
#
#------------------------------------------------------------------

from html.parser import HTMLParser
import http.client
from http.client import HTTPException
import json
import os
from urllib.parse import urljoin

TELEGRAM_API_HOST = "api.telegram.org"


def lambda_handler(_event, _context):

    # Conexion con Telegram API
    conn = http.client.HTTPSConnection(TELEGRAM_API_HOST)

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    # Validar token
    if telegram_token is not None:

        
        endpoint = f"/bot{telegram_token}/sendMessage"

        payload = {
            'chat_id': os.getenv('TELEGRAM_CHATID'), #ChatID obtenido con @RawDataBot
            'text':'Un nuevo archivo ha sido depositado'
        }

        headers = {'content-type': "application/json"}

        # POST request
        conn.request("POST", endpoint, json.dumps(payload), headers)

        # Get the request response
        res = conn.getresponse()

        return {
            'statusCode': res.status,
            'body': json.dumps('Lambda executed.')
        }
    else:
        raise EnvironmentError("Variable token vacia")