import unittest
from requests_prep_kis_yu import find_articles


def count_articles():
    with open('ИТ Новости на Хабре_ главные новости технологий.html', 'r', encoding='utf-8') as file:
        return len(find_articles(file))


class TestArticles(unittest.TestCase):
    def test_articles(self):
        res = count_articles()
        self.assertEqual(res, 20)


if __name__ == '__main__':
    unittest.main()
