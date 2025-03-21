import requests
from environs import env
from pathlib import Path
from supporting_scripts import displays_image_format, download_file


def fetch_nasa_apod(nasa_api_key, dir_path):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_key,
        'count': 30,
        'thumbs': False,
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    url_contents = response.json()
    image_addresses = []
    for url_content in url_contents:
        if 'video' in url_content['media_type']:
            continue
        img_url = url_content['url']
        image_addresses.append(img_url)
    for number, image in enumerate(image_addresses):
        path = Path(dir_path) / f'nasa_apod_{number}{displays_image_format(image)}'
        download_file(image, path)


def main():
    env.read_env()
    dir_path = env.str('DIRECTORY_PATH', default='images')
    Path(dir_path).mkdir(exist_ok=True)
    nasa_api_key = env.str('NASA_TOKEN')
    fetch_nasa_apod(nasa_api_key, dir_path)


if __name__ == '__main__':
    main()
