#-*-coding:utf-8-*- 
from selenium import webdriver
import os,time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
def insert_img(driver,filename):
    base_path=os.path.dirname(__file__)
    base_path=str(base_path)
    base_path=base_path.replace("\\","/")
    base_path=base_path.split("test_case")[0]
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    path = base_path+r"/test_report/screenshot/"+now+filename+".jpg"
    driver.get_screenshot_as_file(path)

def find_report(dir):
    lists=os.listdir(dir)
    lists.sort(key=lambda fn:os.path.getctime(dir+"//"+fn))
    report=os.path.join(dir,lists[-1])
    print (u"最近报告为 %s"%report)
    return report

def send_email(report):
    f=open(report,'rb')
    email_body=f.read()
    f.close()

    msg=MIMEText(email_body,'html','utf-8')
    msg["Subject"] = Header(u'自动化测试报告','utf-8')
    msg["Form"] = 'hjunping@126.com'
    msg["To"] = '275769643@qq.com'

    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('hjunping@126.com','275769643aa')
    smtp.sendmail('hjunping@126.com','275769643@qq.com',msg=msg.as_string())
    smtp.quit()
    print ("email has send out")

if __name__ == '__main__':
    driver=webdriver.PhantomJS()
    driver.get("http://www.baidu.com")
    insert_img(driver,'baidu')