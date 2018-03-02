#-*-coding:utf-8-*- 
from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from model.function import *

if __name__ == '__main__':
    path=os.path.dirname(__file__)
    test_dir=path+"/test_case"
    report_dir =path+"/test_report"
    print(report_dir)
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login*.py')

    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    report_name = report_dir + '\\' + now + 'report.html'

    fp = open(report_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description='test run')
    runner.run(discover)
    fp.close()

    report = find_report(report_dir)
    send_email(report)