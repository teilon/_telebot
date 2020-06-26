import requests
from typing import Dict

host = 'http://78.155.206.12:5080'
query_buy = '/status/buy/'
query_sale = '/status/sale/'


def get_stat(currency_name: str) -> Dict:
    answer_buy = _get_buy_stat(currency_name)
    answer_sale = _get_sale_stat(currency_name)
    return {'buy': answer_buy, 'sale': answer_sale}

def _get_buy_stat(currency_name: str) -> str:
    result = 'Покупка {}'.format(currency_name)
    query = host + query_buy + currency_name

    response = requests.get(query)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            result += '\n{} [{}]'.format(item['buy'], item['handler_name'])
    return result

def _get_sale_stat(currency_name: str) -> str:
    result = 'Продажа {}'.format(currency_name)
    query = host + query_sale + currency_name

    response = requests.get(query)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            result += '\n{} [{}]'.format(item['sale'], item['handler_name'])
    return result