import requests
import time
import random

TOKEN = '7551266931:AAGP690gjKTf7jQlIz3n5MLfnQUMAu3p58Y'
URL = f'https://api.telegram.org/bot{TOKEN}/'


def get_random_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return response.json()[0]['url']


def get_random_dog():
    response = requests.get('https://random.dog/woof.json')
    return response.json()['url']


def get_random_fox():
    response = requests.get('https://randomfox.ca/floof/')
    return response.json()['image']


def send_photo(chat_id, photo_url):
    requests.post(URL + 'sendPhoto', data={'chat_id': chat_id, 'photo': photo_url})


def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(URL + 'getUpdates', params=params)
    return response.json()


def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates['result']:
            chat_id = update['message']['chat']['id']

            # Выбор случайного животного
            animal_choice = random.choice(['cat', 'dog', 'fox'])
            if animal_choice == 'cat':
                photo_url = get_random_cat()
            elif animal_choice == 'dog':
                photo_url = get_random_dog()
            else:
                photo_url = get_random_fox()

            send_photo(chat_id, photo_url)
            offset = update['update_id'] + 1  # Обновляем offset для следующего запроса

        time.sleep(1)  # Пауза перед следующим запросом


if __name__ == '__main__':
    main()