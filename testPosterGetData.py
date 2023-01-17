import requests
import json
dict_1 = {}

url_leftovers = 'https://athome.joinposter.com/api/storage.getStorageLeftovers' \
                '?category_id=11' \
                '&token=856930:84743117e3fe60f857d5363bde5f750b'

url_kategories = 'https://athome.joinposter.com/api/menu.getCategories' \
                 '?token=856930:84743117e3fe60f857d5363bde5f750b&fiscal=1&type=products'

url_prod = 'https://athome.joinposter.com/api/menu.getProducts' \
                '?token=856930:84743117e3fe60f857d5363bde5f750b' \
                '&type=batchtickets'

url_storeges = 'https://athome.joinposter.com/api/storage.getStorages' \
               '?token=856930:84743117e3fe60f857d5363bde5f750b'

url_get_categories = 'https://athome.joinposter.com/api/menu.getCategories' \
                     '?token=856930:84743117e3fe60f857d5363bde5f750b'


data = {'spot_id': '1',
        'spot_tablet_id': '1',
        'table_id': '1',
        'user_id': '3',
        'guests_count': '1'
        }
url_create_transaction = 'https://athome.joinposter.com/api/transactions.createTransaction' \
                         '?token=856930:84743117e3fe60f857d5363bde5f750b'




url_create_incoming_order = 'https://athome.joinposter.com/api/incomingOrders.createIncomingOrder' \
                            '?token=856930:84743117e3fe60f857d5363bde5f750b' \
                            '&spot_id=1' \
                            'phone=+380680000000' \
                            'products=["product_id" = 169, "count" = 1]'
url_add_prod_in_transaction = 'https://athome.joinposter.com/api/transactions.addTransactionProduct' \
                              '?token=856930:84743117e3fe60f857d5363bde5f750b' \

url_get_Employees = 'https://athome.joinposter.com/api/access.getEmployees' \
                    '?token=856930:84743117e3fe60f857d5363bde5f750b'
#{'user_id': 3, 'name': 'Вика', 'login': 'maidanova25@gmail.com', 'role_name': 'root', 'role_id': 3, 'user_type': 90, 'access_mask': 2147483647, 'last_in': '2022-12-14 19:33:08'}
url_get_spot = 'https://athome.joinposter.com/api/spots.getSpots' \
               '?token=856930:84743117e3fe60f857d5363bde5f750b'
#{'spot_id': 1, 'name': 'Краснопольская ', 'address': 'Краснопольская 2Г', 'lat': None, 'lng': None, 'spot_delete': 0}

url_get_tablets = 'https://athome.joinposter.com/api/access.getTablets' \
                    '?token=856930:84743117e3fe60f857d5363bde5f750b'
#{'tablet_id': '1', 'tablet_name': 'вежа', 'spot_id': '1'}, {'tablet_id': '2', 'tablet_name': 'парк', 'spot_id': '2'}


r = requests.post(url_create_transaction, data)
konvert_list = json.loads(r.content)
print(konvert_list)

r = requests.post(url_add_prod_in_transaction)
konvert_list = json.loads(r.content)
print(konvert_list)








'''r = requests.get(url_get_categories)
konvert_list = json.loads(r.content)
f_list = konvert_list['response']
drink_category = {}
for i in f_list:
    drink_category[i['category_id']] = i['category_name']

for i in drink_category:
    print(i, drink_category[i])
r = requests.get(url_prod)
konvert_list = json.loads(r.content)
f_list = konvert_list['response']
for i in f_list:
    if i['menu_category_id'] == '76':
        print(i)'''





