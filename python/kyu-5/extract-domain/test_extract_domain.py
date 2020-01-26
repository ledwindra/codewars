from extract_domain import domain_name

class TestExtractDomain:

    def test_google_com(self):
        assert domain_name('http://google.com') == 'google'

    def test_google_jp(self):
        assert domain_name('http://google.co.jp') == 'google'

    def test_xakep_ru(self):
        assert domain_name('www.xakep.ru') == 'xakep'

    def test_youtube_com(self):
        assert domain_name('https://youtube.com') == 'youtube'