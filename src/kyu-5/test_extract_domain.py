import unittest
from extract_domain import domain_name

class ExtractDomain(unittest.TestCase):

    def test_google_com(self):
        self.assertEqual(domain_name('http://google.com'), 'google')

    def test_google_com(self):
        self.assertEqual(domain_name('http://google.co.jp'), 'google')

    def test_google_com(self):
        self.assertEqual(domain_name('www.xakep.ru'), 'xakep')

    def test_google_com(self):
        self.assertEqual(domain_name('https://youtube.com'), 'youtubeß')
    
if __name__ == '__main__':
    unittest.main()