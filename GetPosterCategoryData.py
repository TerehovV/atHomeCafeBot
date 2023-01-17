import requests
import json
from config import url_get_categories


def get_category():
    r = requests.get(url_get_categories)
    konvert_list = json.loads(r.content)
    t_list = konvert_list['response']
    drink_category = {}
    for i in t_list:
        drink_category[i['category_id']] = i['category_name']
    return drink_category

