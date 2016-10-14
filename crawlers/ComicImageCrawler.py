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
        self.__search_one_post(url_suffix, 405)

    def __search_one_post(self, url_suffix, comic_number):
        url = self.BASE_URL + url_suffix
        print 'Begin crawling on 405'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        raw_set = re.findall(self.__search_pattern, response.read())

        if (raw_set):
            img_list = self.__flat_set(raw_set)
            print 'Analyze comic number: ' + str(comic_number) + '...'
            for img_url in img_list:
                print img_url
                
    def __flat_set(self, raw_set):
        img_list = list()
        for raw_url in raw_set:
            img_list += re.findall('http://imgsrc.baidu.com/forum/\S+.jpg', raw_url)
        return img_list
