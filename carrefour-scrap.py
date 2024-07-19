from classes.price import Price
from classes.product import Product
import requests
import json

def get_categories():
    session = requests.get('https://www.carrefour.es/cloud-api/categories-api/v1/categories/menu?sale_point=005457&depth=1&current_category=foodRootCategory&limit=3&lang=es&freelink=true')
    jsonResponse = session.json()
    jsonObject = json.loads(json.dumps(jsonResponse))
    menu = jsonObject["menu"][0]['childs'][0]['childs'][1:]
    print(type(menu))
    for category in menu:
        nombre = category['name']
        categoria = category['id']
        print(f'Nombre: {nombre}, id: {categoria}')
    
    
def init_scrap():
    get_categories()
    
init_scrap()