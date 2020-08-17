# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import logging


class SendEmail:
    """发送邮件"""
    global sender
    global my_pass
    sender = '997296384@qq.com'  # 发件人邮箱账号
    my_pass = 'ucrwmxkbvqycbcjd'  # 使用qq邮件作为发送服务器获得的授权码

    def send_mail(self, receiveList, sub, content):
        # 设置邮件基本内容
        msg = MIMEMultipart()  # 创建一个带附件的实例
        msg['Subject'] = sub  # 设置邮件标题
        msg['From'] = formataddr(["licongyi", sender])  # 发件人名称
        msg['To'] = ";".join(receiveList)  # 收件人列表
        msg.attach(MIMEText(content, "plain", "utf-8"))  # 邮件正文内容

        # # 邮件携带附件
        # filename = "../report/" + now + "-report.html"  # 保存的报告路径和名称
        # att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="result.html"'  # 这里的filename可以任意写，是邮件中附件显示的名字
        # msg.attach(att1)  # 添加附件，如果有多个附件，同理添加

        # 发送邮件
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, my_pass)
        server.sendmail(sender, receiveList, msg.as_string())
        print("邮件发送成功"+str(receiveList))
        server.quit()

    def send_main(self):
        receiver = ['licongyi01@163.com', 'licongyi@wecash.net']
        sub = "接口自动化测试报告"
        content = "接口自动化测试结果，详情见附件"
        self.send_mail(receiver, sub, content)

s=SendEmail()
s.send_main()
