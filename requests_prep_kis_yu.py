# Practie 1
doigralis'

import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/news/'

habr_news_request = requests.get(url)

habr_news_content = habr_news_request.text

parsed_page = BeautifulSoup(habr_news_content)

print(parsed_page.find_all('h2'))
