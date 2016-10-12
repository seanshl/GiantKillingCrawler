# coding=utf-8
import urllib2
import math
import re

class UrlSearcher:
    def __init__(self, base_url, begin_number, end_number, max_posts):
        self.base_url = base_url
        self.begin_number = begin_number
        self.end_number = end_number

        if (max_posts < 100):
            self.max_posts = max_posts
        else:
            self.max_posts = int((math.ceil(max_posts / 100) + 1) * 100)
        try:
            request = urllib2.Request(self.base_url)
            response = urllib2.urlopen(request)
            print ('UrlSearcher initialized, set the max posts to be %s' % self.max_posts)
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"connection error", e.reason
                return None

    def search_valid_urls(self):
        pn = 0
        while (pn <= self.max_posts):
            print ('Begin searching from post number: ' + str(pn))
            url = self.base_url + '&pn=' + str(pn)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pattern = self.__build_pattern()
            result = re.search(pattern, response.read())
            if (result):
                print result.group()

            pn += 50
        print ('End search on the basic url...')

    def __build_pattern(self):
        pattern = '<a href="/p.*>'
        return pattern
