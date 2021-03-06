import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def get_netloc_and_path(user_url):
    parse_url = urlparse(user_url)
    finished_parse_url = f'{parse_url.netloc}{parse_url.path}'
    return finished_parse_url

def shorten_link(user_url, http_headers):
    http_body = {'long_url': user_url}
    request_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(request_url, json=http_body, headers=http_headers)
    response.raise_for_status()
    return response.json()['link']


def sum_of_click(bitlink, http_headers):
    finished_parse_url = get_netloc_and_path(bitlink)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{finished_parse_url}/clicks/summary'
    response = requests.get(url, headers=http_headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(user_url, http_headers):
    finished_parse_url = get_netloc_and_path(user_url)
    reqst_url = f'https://api-ssl.bitly.com/v4/bitlinks/{finished_parse_url}'
    response = requests.get(reqst_url, headers=http_headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Данная программа делает из длинной ссылки короткую.'
    )
    parser.add_argument('url', help='Ссылка')
    args = parser.parse_args()
    user_url = args.url

    bitly_token = os.getenv('BITLY_TOKEN')

    http_headers = {'Authorization': f'Bearer {bitly_token}'}

    if is_bitlink(user_url, http_headers):
        print(sum_of_click(user_url, http_headers))
    else:
        print(shorten_link(user_url, http_headers))
