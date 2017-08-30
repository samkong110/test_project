#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from  HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import os
import time

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("jiangxu@dianbaobao.com","1qaz@WSX")
    smtp.sendmail("jiangxu@dianbaobao.com","shitaoxujiang@163.com",msg.as_string())
    smtp.quit()
    print 'email has send out!'

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print file_new
    return file_new

if __name__ == '__main__':
    test_dir = './test_case'
    test_report = 'D:\\test_project\\report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')

    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

