#-*-coding:utf-8-*- 
from selenium import webdriver
from page_obj.login_api import Login
from model.myunit import *

class LoginTest(Start_end):
    u'''登录测试'''
    url='https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    def test_login1_normal(self):
        u'''正确登陆'''
        po = Login(self.driver,self.url)
        po.login_action('13076220975', '13076282110..')
        print(po.type_loginPass_hint())
        self.assertTrue(po.type_loginPass_hint())
    def test_login1_error(self):
        u'''错误登陆'''
        po2=Login(self.driver,self.url)
        po2.login_action('130','130')
        print(po2.type_loginFail_hint())
        self.assertTrue(po2.type_loginFail_hint())