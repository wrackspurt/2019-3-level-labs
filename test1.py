import unittest
import json
import unittest
import json
from requests_prep_kis_yu import base_url


class TestPage(unittest.TestCase):
    def test_url_exists(self):
        with open("articles.json", encoding='utf-8') as file:
            data_s = json.load(file)
        self.assertIsNotNone(data_s["url"])

    def test_url(self):
        with open("articles.json", encoding='utf-8') as file:
            data_s = json.load(file)
        self.assertEqual(data_s["url"], base_url)

    def test_date(self):
        with open("articles.json", encoding='utf-8') as file:
            data_s = json.load(file)
        self.assertIsNotNone(data_s["creationDate"])

    def test_articles(self):
        with open("articles.json", encoding='utf-8') as file:
            data_s = json.load(file)
        self.assertGreaterEqual(len(data_s["articles"]), 1)

    def test_titles(self):
        with open("articles.json", encoding='utf-8') as file:
            data_s = json.load(file)
        for i in data_s["articles"]:
            for k in i:
                self.assertIsNotNone(i[k])


if __name__ == '__main__':
    unittest.main()