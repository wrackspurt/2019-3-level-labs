import unittest
import requests
from requests_prep_kis_yu import base_url
urlw = "http://jdkfvdlk.com"


def check_out_url(url):
    r = requests.head(url)
    return r.status_code


class TestUrl(unittest.TestCase):
    def test_url(self):
        result = check_out_url(base_url)
        self.assertEqual(result, 200)


if __name__ == '__main__':
    unittest.main()

