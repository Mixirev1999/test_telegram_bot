import requests
import time
import random


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6205359567:AAG3fGWI5-tSkkceRU6BgO4MZWncdesrBAk'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
API_WOOFS_URL: str ='https://random.dog/woof.json'
API_FOX_URL: str ='https://randomfox.ca/floof/'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
TEXT: str = 'Смотри!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int


offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str
numbers = [1, 2,3]

while counter < MAX_COUNTER:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            a=random.choice(numbers)
            if a==1:
                cat_response = requests.get(API_CATS_URL)
                cat_link = cat_response.json()[0]['url']
            elif a==2:
                cat_response = requests.get(API_WOOFS_URL)
                cat_link = cat_response.json()['url']
            else:
                cat_response = requests.get(API_FOX_URL)
                cat_link = cat_response.json()['image']
            if cat_response.status_code == 200:

                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1