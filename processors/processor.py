from crawlers.UrlSearcher import UrlSearcher
from crawlers.ComicImageCrawler import ComicImageCrawler

begin_number = 400
end_number = 406
max_post = 50

base_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E9%80%86%E8%BD%AC%E7%9B%91%E7%9D%A3&fr=search'

url_searcher = UrlSearcher(base_url, begin_number, end_number, max_post)
post_urls = url_searcher.search_valid_urls()

post_crawler = ComicImageCrawler(post_urls, '/Users/liushiyao/Downloads/GiantKilling')
post_crawler.search_all()
