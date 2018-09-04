# !/usr/bin/env python3
# *coding:utf-8*
__author__ = 'loaderlin'

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def send_Email():
    sender = 'rockyfire@126.com'
    receivers = ['loaderlin@163.com','13316025469@163.com']
    message = MIMEText('用Python发送邮件的栗子', 'plain', 'utf-8')
    message['from'] = Header('伍六七', 'utf-8')
    message['to'] = Header('伍六', 'utf-8')
    message['Subject'] = Header('栗子代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender, '你的客户端授权密码')
    smtper.sendmail(sender, receivers, message.as_string())
    print ('邮件发送完成')

if __name__ == "__main__":
    send_Email()

