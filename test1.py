import unittest
import json
from requests_prep_kis_yu import base_url


def check1(filename):
    check = 0
    with open(filename, encoding='utf-8') as file:
        data_s = json.load(file)
    for j in data_s["url"]:
        if j is not None:
            check = 1
    return check


def check2(filename):
    check = 0
    with open(filename, encoding='utf-8') as file:
        data_s = json.load(file)
    if data_s["url"] == base_url:
        check = 1
    return check


def check3(filename):
    check = 0
    with open(filename, encoding='utf-8') as file:
        data_s = json.load(file)
    if data_s["creationDate"] is not None:
        check = 1
    return check


def check4(filename):
    check = 0
    with open(filename, encoding='utf-8') as file:
        data_s = json.load(file)
    if len(data_s["articles"]) >= 1:
        check = 1
    return check


def check5(filename):
    check = 0
    with open(filename, encoding='utf-8') as file:
        data_s = json.load(file)
    for i in data_s["articles"]:
        for k in i:
            if i[k] is not None:
                check = 1
                break
    return check


class TestPage(unittest.TestCase):
    def test_url_exists(self):
        result = check1('articles.json')
        self.assertEqual(result, 1)

    def test_url(self):
        result = check2('articles.json')
        self.assertEqual(result, 1)

    def test_date(self):
        result = check3('articles.json')
        self.assertEqual(result, 1)

    def test_articles(self):
        result = check4('articles.json')
        self.assertEqual(result, 1)

    def test_titles(self):
        result = check5('articles.json')
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()









