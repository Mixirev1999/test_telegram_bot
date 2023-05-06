import math
import requests
import pprint
import os
import dotenv


if __name__ == '__main__':
    api_url = 'https://api.telegram.org/bot6205359567:AAG3fGWI5-tSkkceRU6BgO4MZWncdesrBAk/sendMessage?chat_id=731057670&text=Ну ты и Миша!'

    dotenv.load_dotenv()

    print(os.getenv('BOT_TOKEN'))
    print(os.getenv('ADMIN_ID'))
    response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        pprint.pprint(response.text)
    else:
        pprint.pprint(response.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
