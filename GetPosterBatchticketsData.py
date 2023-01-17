import requests
import json
from config import url_batch

def get_menu_data():
    r = requests.get(url_batch)
    konvert_list = json.loads(r.content)
    f_list = konvert_list['response']
    drink_menu = {}
    for i in f_list:
        drink_menu[i['product_name']] = [i['category_name'], i['menu_category_id'], i['product_id'], i['price']['2']]
    return drink_menu
