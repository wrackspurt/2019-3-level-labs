import json
import requests
from bs4 import BeautifulSoup
import datetime


base_url = 'https://habr.com/ru/news/'
another_url = 'https://arstechnica.com/gadgets/'
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


def find_another_articles(html_page):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    headings = parsed_page.find_all('h2')
    quantity = len(headings)
    title_list = list()
    for i in range(quantity):
        title_list.append(headings[i].text)
    return title_list


def publish_report(path, articles, another_articles):
    articles_dict = []
    another_articles_dict = []
    for i in range(len(articles)):
        articles_dict.append({"title": articles[i]})
    for j in range(len(another_articles)):
        another_articles_dict.append({"title": another_articles[j]})
    titles = {
        "creationDate": creation_date,
        "habrUrl": base_url,
        "habrArticles": articles_dict,
        "arsUrl": another_url,
        "arsArticles": another_articles_dict
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(titles, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    publish_report(jpath, find_articles(get_html_page(base_url)), find_another_articles(get_html_page(another_url)))

