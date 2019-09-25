import json
import requests
from bs4 import BeautifulSoup
from datetime import date

base_url = 'https://habr.com/ru/news/'
creation_date = date(year=2019, month=9, day=25)
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
        "creationDate": str(creation_date),
        "articles": articles_dict
    }
    #try:
    #    data = json.load(open(path))
    #except:
    #    data = []

    #data.append(titles)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(titles, file, indent=2, ensure_ascii=False)


def main():

    publish_report(jpath, find_articles(get_html_page(base_url)))


if __name__ == '__main__':
    main()
