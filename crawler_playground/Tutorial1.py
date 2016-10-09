import urllib2

request = urllib2.Request('http://tieba.baidu.com/p/4801141948')
response = urllib2.urlopen(request)
print response.read()