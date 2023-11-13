import keyboard
import requests
from pprint import pprint
from os import close


def get_info_from_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        global data
        data = {
            'Страна': response.get('country'),
            'Регион': response.get('regionName'),
            'Город': response.get('city'),
            'Широта': response.get('lat'),
            'Долгота': response.get('lon')
        }
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    ip = input("Введите IP цели:")
    get_info_from_ip(ip=ip)
    pprint(data, width=5)
    print('Нажмите Enter,чтобы закончить...')
    keyboard.wait('enter')
    close(1)


if __name__ == '__main__':
    main()
