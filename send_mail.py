#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver = 'smtp.exmail.qq.com'

user = 'jiangxu@dianbaobao.com'
password = '!QAZ2wsx'

receiver = 'shitaoxujiang@163.com'
sender = 'jiangxu@dianbaobao.com'

subject = 'Python send email test'

sendfile = open('D:\\test_project\\report\\log.txt', "rb").read()
att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = "application/octet-stream"
att['Content-Disposition'] = 'attachment;filename="log.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()