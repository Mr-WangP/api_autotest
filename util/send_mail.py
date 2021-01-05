# coding=utf-8
import smtplib
from email.mime.text import MIMEText


class SendMail:
    global sender
    global host
    global pwd
    global receiver
    global port

    pwd = 'xxx'
    host = 'smtp.qq.com'
    sender = 'xxx'
    receiver = "xxx"
    port = 465

    def send_mail(self, path):

        f = open(path, 'rb')
        mail_body = f.read()
        f.close()

        msg = MIMEText(mail_body, 'HTML', 'UTF-8')
        msg['subject'] = "api测试报告发送"
        msg['from'] = sender
        msg['to'] = receiver

        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
