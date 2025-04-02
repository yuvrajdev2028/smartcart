import requests
import os

def search_amazon(query_string):

    payload = {
    'source': 'amazon_search',
    'domain': 'in',
    'query': query_string,
    'parse': True,
    'start_page': '1',
    'pages': '1'
    }

    response = requests.request(
        'POST',
        'https://realtime.oxylabs.io/v1/queries',
        auth=(os.environ['OXYLABS_USERNAME'], os.environ['OXYLABS_PASSWORD']),
        json=payload,
    )

    data = response.json()['results'][0]['content']['results']['organic']

    result=[]
    for i in range(len(data)):
        if data[i]['rating'] == 0:
            continue
        result.append({
            'title':data[i]['title'],
            'url':'https://www.amazon.in'+data[i]['url'],
            'rating':data[i]['rating'],
            'reviews_count':data[i]['reviews_count'],
            'price':data[i]['currency']+' '+str(data[i]['price'])
        })

        if(len(result)==5):
            break

    if len(result) == 0:
        return 'Unable to fetch query results at the moment. Would you like to buy something else!'

    res_text = 'Here is the list of suitable items.\n'

    for item in result:
        res_text=res_text+f'\n{item['title']}\n{item['url']}\n{item['price']}\nRating: {item['rating']}({item['reviews_count']} Reviews)\n'

    print('\n')

    print(res_text)

    return res_text