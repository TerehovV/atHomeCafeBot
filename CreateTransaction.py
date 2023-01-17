import requests
import json
from config import url_create_transaction, url_add_prod_in_transaction


data = {'spot_id': '1',
        'spot_tablet_id': '1',
        'table_id': '1',
        'user_id': '3',
        'guests_count': '1'
        }


def create_check():
    r = requests.post(url_create_transaction, data)
    konvert_list = json.loads(r.content)
    f_list = konvert_list['response']
    transaction = f_list['transaction_id']
    print('create check is run')
    return transaction

data2 = {'spot_id': '1',
         'spot_tablet_id': '1',
         'transaction_id': '126514',
         'product_id': '104',
         }

def add_prod_in_check():
    r = requests.post(url_add_prod_in_transaction, data2)
    konvert_list = json.loads(r.content)

    print(konvert_list)

add_prod_in_check()

