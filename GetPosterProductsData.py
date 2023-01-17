import requests
import json
from config import url_prod_kat, url_leftovers1
def get_products_data():
    dict_products_data = {}
    r = requests.get(url_prod_kat)
    r2 = requests.get(url_leftovers1)
    konvert_list = json.loads(r.content)
    konvert_list2 = json.loads(r2.content)
    f_list = konvert_list['response']
    f_list2 = konvert_list2['response']
    for i in f_list:
        if 'modifications' in i:
            name = i['product_name'] + ' '
            leftovers = '0'
            category_id = i['menu_category_id']
            mod = (i['modifications'][:])
            for q in mod:
                ingredient_id = (q['ingredient_id'])
                price = (q['spots'][0]['price'])
                dict_products_data[ingredient_id] = [str(int(int(price)/100)), category_id,
                                                     name + q['modificator_name'], leftovers]
        elif 'modifications' not in i:
            name = i['product_name']
            leftovers = '0'
            category_id = i['menu_category_id']
            ingredient_id = i['ingredient_id']
            price = i['price']['1']
            dict_products_data[ingredient_id] = [str(int(int(price)/100)), category_id, name, leftovers]
        else:
            pass
    for i in f_list2:
        if i['ingredient_id'] in dict_products_data:
            dict_products_data[i['ingredient_id']][3] = i['storage_ingredient_left']

    return dict_products_data
