import urllib2
import math
import re

class ComicImageCrawler:
    def __init__(self, post_urls):
        self.__post_urls = dict(post_urls)
        self.BASE_URL = 'http://tieba.baidu.com'
        self.__search_pattern = r'<img class="BDE_Image".*width="\d+".*height="\d+".*src="http://imgsrc.baidu.com/forum/.*.jpg"\s*>'

    def search_all(self):
        url_suffix = self.__post_urls['405']
        self.__search_one_post(url_suffix)

    def __search_one_post(self, url_suffix):
        url = self.BASE_URL + url_suffix
        print 'Begin crawling on 405'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        image_set = re.findall(self.__search_pattern, response.read())

        if (image_set):
            for image_url in image_set:
                print image_url
