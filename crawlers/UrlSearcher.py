# coding=utf-8
import urllib2
import math
import re

class UrlSearcher:
        def __init__(self, base_url, begin_number, end_number, max_posts):
            self.base_url = base_url
            self.begin_number = begin_number
            self.end_number = end_number
            self.set = set()
            for x in range(begin_number, end_number + 1, 1):
                self.set.add(x)
            print 'Size: ' + str(self.set.__len__())
            if max_posts < 100:
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
            while pn <= self.max_posts:
                print ('Begin searching from post number: ' + str(pn))

                url = self.base_url + '&pn=' + str(pn)
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
                pattern = self.__build_pattern()

                result = re.findall(pattern, response.read())

                if result:
                    for url in result:
                        title = re.search('逆转监督\s*\d+', url)
                        num = re.search('\d+', title.group()).group()
                        if int(num) in self.set:
                            print url
                            print 'Found number: ' + str(num)
                            self.set.remove(int(num))

                pn += 50
            print ('End search on the basic url...')
            if self.set.__len__() == 0:
                print 'Found all targets'
            else:
                for number in set:
                    print 'Miss number' + str(number)
        def __build_pattern(self):
            pattern = r'<a href="/p/\d+" title=".*贴吧汉化.*逆转监督\s*\d+.*>'
            return pattern
