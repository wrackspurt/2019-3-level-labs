from bs4 import BeautifulSoup
import json
from datetime import datetime, date


BASE_URL = 'https://habr.com/ru/news/'

creation_date = date(year=2019, month=9, day=24)


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


#def publish_report(title_list, path):
    dictionary = {
        'url': BASE_URL,
        'date': '2019-09-24',
        'articles': title_list
    } 
 #  filename='aricles.json'
   #with open(filename, 'w') as fp:
    # print(json.dump(dictionary, fp)) 
   # rh = dict(title_list)
   # print(json.dumps(rh))


def main():

    print(find_articles(get_html_page(BASE_URL)))


if __name__ == '__main__':
    main()
