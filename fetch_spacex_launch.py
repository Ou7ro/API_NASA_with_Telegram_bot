import requests
import argparse
from environs import env
from pathlib import Path
from supporting_scripts import download_file


def fetch_spacex_last_launch(args, dir_path):
    url_spacex = 'https://api.spacexdata.com/v5/launches/{0}'.format(args)
    response = requests.get(url_spacex)
    response.raise_for_status()
    departure_images = response.json()['links']['flickr']['original']
    for number, picture in enumerate(departure_images):
        path = Path(dir_path) / f'spacex_{number}.jpeg'
        download_file(picture, path)


def main():
    dir_path = env.str('DIRECTORY_PATH', default='images')
    Path(dir_path).mkdir(exist_ok=True)
    parser = argparse.ArgumentParser(description='''Default is latest launch''')
    parser.add_argument('--id', help='ID', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id, dir_path)


if __name__ == '__main__':
    main()
