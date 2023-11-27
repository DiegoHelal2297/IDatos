import requests

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

CANT_ELEM = 4

# Mercado libre
def find_ML(elem):
    url = f"https://api.mercadolibre.com/sites/MLU/search?q={elem}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        res = {}
        split_elem = elem.lower().split(" ")
        for i, item in enumerate(data['results']):
            if (i >= CANT_ELEM):
                break
            if find_word(item['title'].lower(), split_elem):
                new_element = {"price": item['price'], "currency_id": item['currency_id'], "URL": item['permalink']}
                res[item['title']] = new_element;
        return res
    else:
        return None

# Ebay
def find_ebay(elem, API_KEY_Ebay):
    try:
        api = Finding(siteid='EBAY-US', appid=API_KEY_Ebay, config_file=None)
        request = {
            'keywords': elem,
            'paginationInput': {
                'entriesPerPage': 100,
                'pageNumber': 1
            }
        }
        response = api.execute('findItemsAdvanced', request)

        res = {}
        if response.status_code == 200:
            split_elem = elem.lower().split(" ")
            for i,item in enumerate(response.reply.searchResult.item):
                if i >= CANT_ELEM:
                    break

                # Me fijo si hay que tener en cuenta impuestos aduaneros
                price = float(item.sellingStatus.convertedCurrentPrice.value)
                impuestos_aduana = 0
                if (price) > 200:
                    impuestos_aduana = (price * 0.6)
                if find_word(item.title.lower(), split_elem):
                    new_element = {"price": price, "currency_id": item.sellingStatus.currentPrice._currencyId, "taxes": impuestos_aduana, "URL": item.viewItemURL}
                    res[item.title] = new_element;

        return res
    except ConnectionError as e:
        return None

# Aplicamos la funcion de filtrado para no ingresar resultados que no contengan el elemento a buscar dentro del título
def find_word(phrase, split_elem):
    for word in split_elem:
        if not (word in phrase):
            return False
    return True