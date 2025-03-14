import requests
import os
import telegram
from urllib.parse import urlparse


def displays_image_format(url):
    responce = requests.get(url)
    responce.raise_for_status()
    responce_parse = urlparse(responce.url)
    path_separation = os.path.splitext(responce_parse.path)
    path_image, changed_format = path_separation
    return changed_format


def download_file(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def send_image(tg_token, path, tg_chat_id):
    bot = telegram.Bot(token=tg_token)
    with open(path, 'rb') as save_file:
        bot.send_document(chat_id=tg_chat_id, document=save_file)
