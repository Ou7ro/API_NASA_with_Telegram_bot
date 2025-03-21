import os
import argparse
from pathlib import Path
from random import choice
from environs import env
from supporting_scripts import send_image


def main():
    env.read_env()
    tg_token = env.str('TG_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    dir_path = env.str('DIRECTORY_PATH', default='images')
    parse = argparse.ArgumentParser(description='''Отправляет случайное фото.
                                                Чтобы отправить определенное фото, укажите в аргументе название файла''')
    parse.add_argument('-n', '--name', help='image name')
    args = parse.parse_args()
    if args.name is None:
        path = Path(dir_path)
        files = os.listdir(path)
        random_files = choice(files)
        file_path = Path(path) / random_files
    else:
        file_path = Path(dir_path) / args.name
    send_image(tg_token, file_path, tg_chat_id)


if __name__ == '__main__':
    main()
