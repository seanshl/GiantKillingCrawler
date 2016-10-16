# coding=utf-8
import urllib2
import urllib
import os

class ComicDownloader:
    def __init__(self, img_list, comic_nbr, basic_path):
        self.__img_list = img_list
        self.__comic_nbr = comic_nbr
        self.__basic_path = basic_path
        if not os.path.exists(self.__basic_path):
            os.mkdir(self.__basic_path)

    def download(self):
        path = self.__basic_path + '/' + str(self.__comic_nbr) + '话/'
        if not os.path.exists(path):
            os.mkdir(path)
        count = 1

        for img_url in self.__img_list:
            filename = path + str(count) + '.jpg'
            print 'downloading ' + filename + '...'
            self.__save_img(filename, img_url)
            count += 1


    def __save_img(self, filename, img_url):
        response = urllib2.urlopen(img_url)
        data = response.read()
        f = open(filename, 'wb')
        f.write(data)
        f.close()


