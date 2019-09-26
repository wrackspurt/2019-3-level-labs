import unittest
from requests_prep_kis_yu import get_html_page


class Test1(unittest.TestCase):
    def test_1(self):
        url = 'http://122123'
        with self.assertRaises(TypeError):
            get_html_page(url)


if __name__ == '__main__':
    unittest.main()
