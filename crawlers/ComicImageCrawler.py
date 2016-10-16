import urllib2
import re
from ComicDownloader import ComicDownloader

class ComicImageCrawler:
    def __init__(self, post_urls, basic_path):
        self.__post_urls = dict(post_urls)
        self.BASE_URL = 'http://tieba.baidu.com'
        self.__search_pattern = r'<img class="BDE_Image".*width="\d+".*height="\d+".*src="http://imgsrc.baidu.com/forum/.*.jpg"\s*>'
        self.__basic_path = basic_path

    def search_all(self):
        for nbr in self.__post_urls.keys():
            url_suffix = self.__post_urls[str(nbr)]
            self.__search_one_post(url_suffix, nbr)

    def __search_one_post(self, url_suffix, comic_nbr):
        url = self.BASE_URL + url_suffix
        print 'Begin crawling on ' + comic_nbr
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        raw_set = re.findall(self.__search_pattern, response.read())

        if (raw_set):
            print 'Analyze comic number: ' + str(comic_nbr) + '...'
            img_list = self.__flat_set(raw_set)
            print str(img_list.__len__()) + ' images found, begin downloading...'
            self.__download(img_list, comic_nbr)

    def __download(self, img_list, comic_nbr):
        downloader = ComicDownloader(img_list, comic_nbr, self.__basic_path)
        downloader.download()

    def __flat_set(self, raw_set):
        img_list = list()
        for raw_url in raw_set:
            img_list += re.findall('http://imgsrc.baidu.com/forum/\S+.jpg', raw_url)
        return img_list
