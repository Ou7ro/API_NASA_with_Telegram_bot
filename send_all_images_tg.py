from dotenv import load_dotenv
import os
from pathlib import Path
import argparse
from random import shuffle
from time import sleep
from environs import env
from supporting_scripts import send_image


def send_all_images(tg_token, tg_chat_id, seconds, file_names, dir_path):
    while True:
        for file_name in file_names:
            file_path = Path(dir_path) / file_name
            send_image(tg_token, file_path, tg_chat_id)
            sleep(seconds)


def send_only_one_images(tg_token, tg_chat_id, args, seconds, dir_path):
    while True:
        file_path = Path(dir_path) / args.name
        send_image(tg_token, file_path, tg_chat_id)
        sleep(seconds)


def shuffle_file_names(path):
    for dirpath, dirnames, filenames in os.walk(path):
        shuffle(filenames)
        return filenames


def main():
    load_dotenv()
    tg_token = env.str('TG_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    seconds = env.int('TIME', default=14400)
    dir_path = env.str('DIRECTORY_PATH', default='images')
    Path(dir_path).mkdir(exist_ok=True)
    parse = argparse.ArgumentParser(description='''Отправляет все имеющиеся фото, по умолчанию, каждые 4 часа.
                                    Чтобы отправлять определенное фото, укажите в аргументе название файла''')
    parse.add_argument('-n', '--name', help='image name')
    args = parse.parse_args()
    file_names = shuffle_file_names(dir_path)
    if args.name is None:
        send_all_images(tg_token, tg_chat_id, seconds, file_names, dir_path)
    else:
        send_only_one_images(tg_token, tg_chat_id, args, seconds, dir_path)


if __name__ == '__main__':
    main()
