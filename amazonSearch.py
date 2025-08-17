import requests
from pprint import pprint
import json

def search_amazon():
    product_list = ['laptops', 'smart phones', 'headphones', 'earphones', 'smart watches', 'tablets', 'cameras', 'gaming consoles', 'speakers']
    result=[]

    for product in product_list:
        print(f'Searching for {product}...')
        payload = {
            'source': 'amazon_search',
            'domain': 'in',
            'query': product,
            'parse': True,
            'start_page': '1',
            'pages': '5'
        }

        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=({USERNAME}, {PASSWORD}),
            json=payload,
        )

        data = response.json()['results'][0]['content']['results']['organic']

        r = min(8, len(data))
        for i in range (r):
            if data[i]['rating'] == 0:
                continue
            result.append({
                'title':data[i]['title'],
                'url':'https://www.amazon.in'+data[i]['url'],
                'rating':data[i]['rating'],
                'reviews_count':data[i]['reviews_count'],
                'price':data[i]['currency']+' '+str(data[i]['price'])
            })

    with open('inventory.json', 'w') as f:
        json.dump(result, f, indent=4)

search_amazon()
