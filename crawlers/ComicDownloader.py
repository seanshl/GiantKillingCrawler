# coding=utf-8
import urllib2
import os

class ComicDownloader:
    def __init__(self, img_list, comic_nbr, basic_path):
        self.__img_list = img_list
        self.__comic_nbr = comic_nbr
        self.__basic_path = basic_path

    def download(self):
        print os.path.exists(self.__basic_path + '/' + str(self.__comic_nbr) + '话')
