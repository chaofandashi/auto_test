#-*-coding:utf-8-*- 
from selenium import webdriver

class Base():

    def __init__(self,driver,test_url):
        self.driver=driver
        self.base_url=test_url
        self.timeout=30

    def _open(self,url):
        _url=self.base_url+url
        print ("test page is %s"%_url)
        self.driver.get(_url)
        assert self.driver.current_url==_url,'Did not land on'

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)