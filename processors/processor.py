from crawlers.UrlSearcher import UrlSearcher

base_url = 'http://tieba.baidu.com/f?kw=%C4%E6%D7%AA%BC%E0%B6%BD&fr=ala0&tpl=5'

crawler = UrlSearcher('www.baidu.com', 100, 100, 100)
crawler.search_valid_urls()