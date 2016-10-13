import urllib2
import math
import re

class ComicImageCrawler:
    def __init__(self, post_urls, bath_path):
        self.__post_urls = post_urls
        self.__bath_path = bath_path
        self.BASE_URL = 'http://tieba.baidu.com'
        self.search_pattern = r'<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/.*.jpg" size='

    def __search_one_post(self, url_suffix):
        url = self.BASE_URL + url_suffix

        image_set = re.findall(pattern, response.read())
