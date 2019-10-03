import json
import requests
from bs4 import BeautifulSoup
import datetime


base_url = 'https://habr.com/ru/news/'
current = datetime.datetime.now()
creation_date = current.strftime("%d-%m-%y")
jpath = 'articles.json'


def get_html_page(url):
    news_request = requests.get(url)
    news_content = news_request.text
    return news_content


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    headings = parsed_page.find_all('a', class_='post__title_link')
    quantity = len(headings)
    title_list = list()
    for i in range(quantity):
        title_list.append(headings[i].text)
    return title_list


def publish_report(path, articles):
    articles_dict = []
    for i in range(len(articles)):
        articles_dict.append({"title": articles[i]})
    titles = {
        "url": base_url,
        "creationDate": creation_date,
        "articles": articles_dict
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(titles, file, indent=2, ensure_ascii=False)


