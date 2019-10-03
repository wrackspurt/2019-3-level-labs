import unittest
import requests
from requests_prep_kis_yu import base_url


def check_out_url(url):
     r = requests.head(url)
     return r.status_code
#def check_out_url1(url):


class TestUrl(unittest.TestCase):
    def test_url(self):
        result = check_out_url(base_url)
        self.assertEqual(result, 200)


if __name__ == '__main__':
        unittest.main()

