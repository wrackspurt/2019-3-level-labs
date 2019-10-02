import unittest
import json
from requests_prep_kis_yu import base_url


def check_out(filename):
    check = 0
    with open(filename,  encoding='utf-8') as file:
        data_s = json.load(file)
    if data_s["url"] == base_url:
        check = 1

    if len(data_s["articles"]) >= 1:
        check = 1
    for i in data_s["articles"]:
        for k in i:
            if i[k]!= None:
                check = 1
                break
    return check


class TestPage(unittest.TestCase):
    def test_html_page(self):
        result = check_out('articles.json')
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()






