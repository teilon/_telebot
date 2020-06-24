import requests

host = 'http://78.155.206.12:5080'
query_buy = '/status/buy/'
query_sale = '/status/sale/'


def get_stat(currency_name):
    answer = 'Покупка {}'.format(currency_name)
    query = host + query_buy + currency_name
    response = requests.get(query)
    data = response.json()
    if response.status_code == 200:
        for item in data:
            answer += '\n{} [{}]'.format(item['buy'], item['handler_name'])

    answer += '\nПродажа {}'.format(currency_name)
    query = host + query_sale + currency_name
    response = requests.get(query)
    data = response.json()
    if response.status_code == 200:
        for item in data:
            answer += '\n{} [{}]'.format(item['sale'], item['handler_name'])

    return answer
