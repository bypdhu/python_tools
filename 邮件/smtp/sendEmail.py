#!/usr/bin/python
# -*- encoding:utf-8 -*-
"""
@Title : BugContrast
@Author : bianbian
@Email : bianyp_os@sari.ac.cn
@Copyright : 2016-2017, autotest
@Date : 20160325
@Functions : send email

"""

import smtplib
from email.mime.text import MIMEText
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SendEmail(object):

    def __init__(self):
        # 通用芯片与基础软件研究中心
        # self.mail_host = '172.29.51.200'
        # self.mail_user = 'bianyp@cpu-os.cn'
        # self.mail_passwd = 'Aa12345'
        # self.mail_postfix = 'cpu-os.cn'
        # self.sub = 'jenkins-autotest'
        # self.content = "<h>for test</h>"
        # self.mail_to_list = ['bianyp@cpu-os.cn', 'xiejx@cpu-os.cn']

        # 易居中国创新研发中心
        self.mail_host = 'mail.ehousechina.com'
        self.mail_user = 'bianyunpeng@ehousechina.com'
        self.mail_passwd = 'Bian123456'
        self.mail_postfix = 'cpu-os.cn'
        self.sub = 'jenkins-autotest'
        self.content = "<h>for test</h>"
        self.mail_to_list = ['bianyunpeng@ehousechina.com']

    def set_content(self, content):
        self.content = content

    def set_mail_to_list(self, mail_to_list):
        if not mail_to_list:
            self.mail_to_list = mail_to_list

    def set_sub(self, sub):
        self.sub = sub

    def send_email(self, to_list=None, sub=None, content=None):
        if not to_list:
            to_list = self.mail_to_list
        if not sub:
            sub = self.sub
        if not content:
            content = self.content
        from_me = 'bianbian'+'<'+self.mail_user+'>'
        msg = MIMEText(content, _subtype='html', _charset='gb2312')
        msg['Subject'] = sub
        msg['From'] = from_me
        msg['To'] = ';'.join(to_list)
        try:
            sl = smtplib.SMTP(self.mail_host, 25, timeout=600)
            for i in range(10):
                try:
                    print i
                    sleep(0.5)
                    sl.login(self.mail_user, self.mail_passwd)
                    break
                except:
                    sl.esmtp_features['auth']='LOGIN PLAIN'
            sl.sendmail(from_me, to_list, msg.as_string())
            sl.close()
            return True
        except Exception,e:
            print e
            return False


if __name__ == '__main__':
    se = SendEmail()
    status = se.send_email()
    if status:
        print "发送成功"
    else:
        print "发送失败"
