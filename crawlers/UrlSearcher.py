import urllib
import urllib2

class UrlSearcher:
    def __init__(self, base_url, begin_number, end_number, max_posts):
        self.base_url = base_url
        self.begin_number = begin_number
        self.end_number = end_number
        self.max_posts = max_posts

    def search_valid_urls(self):
        print ('Begin searching on the basic url...')



