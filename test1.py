import unittest
import json


def check_out(afile):
    check = 0
    with open(afile, "r") as file:
        data_s = json.load(file)
    if data_s["url"] == "https://habr.com/ru/news/":
        check = 1
    if len(data_s["articles"]) >= 1:
        check = 1
    for i in data_s["articles"]:
        for k in i:
            if i[k] != None:
                check = 1
                break
    return(check)

"""
class TestPage(unittest.TestCase):
    def test_html_page(self):
        result = check_out('articles.json')
        self.assertEqual(result, 1)
        
        if __name__ == '__main__':
    unittest.main()
"""


print(check_out('articles.json'))



