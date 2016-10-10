from crawlers.UrlSearcher import UrlSearcher

base_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E9%80%86%E8%BD%AC%E7%9B%91%E7%9D%A3&fr=search'

crawler = UrlSearcher(base_url, 100, 100, 740)
crawler.search_valid_urls()