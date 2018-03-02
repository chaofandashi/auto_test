#-*-coding:utf-8-*- 
from selenium import webdriver
from selenium import webdriver
from page_obj.base_api import Base
from selenium.webdriver.common.by import By
from model.function import *

class Login(Base):
    url='/'
    username_loc=(By.ID,'loginname')
    password_loc=(By.ID,'nloginpwd')
    submit_loc=(By.ID,'loginsubmit')
    login_name=(By.LINK_TEXT,u'账户登录')

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    def type_submit(self):
        self.find_element(*self.submit_loc).click()
    def type_login(self):
        self.find_element(*self.login_name).click()

    def login_action(self,username,password):
        self.open()
        self.type_login()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
    # 断言是否登录成功
    loginPass_loc = (By.LINK_TEXT, u'超烦大师之迷...')
    loginFail_loc = (By.LINK_TEXT, u"账户登录")
    def type_loginPass_hint(self):
        res=self.find_element(*self.loginPass_loc).text
        if u'超烦大师' in res:
            return True
        else:
            return False
    def type_loginFail_hint(self):
        res2 = self.find_element(*self.loginFail_loc).text
        if u"账户登录" in res2 :
            return True
        else :
            return False



