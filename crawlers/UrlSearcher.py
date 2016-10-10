import urllib
import urllib2
import math

class UrlSearcher:
    def __init__(self, base_url, begin_number, end_number, max_posts):
        self.base_url = base_url
        self.begin_number = begin_number
        self.end_number = end_number

        if (max_posts < 100):
            self.max_posts = max_posts
        else:
            self.max_posts = int((math.ceil(max_posts / 100) + 1) * 100)
        print ('UrlSearcher initialized, set the max posts to be %s' % self.max_posts)



    def search_valid_urls(self):
        print ('Begin searching on the basic url on first 100 pages')
        try:
            request = urllib2.Request(self.base_url)
            response = urllib2.urlopen(request)

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"connection error", e.reason
                return None
        print ('End search on the basic url...')


