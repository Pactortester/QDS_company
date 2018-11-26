# coding=utf-8
import os
import smtplib
import unittest

import time
from email.mime.text import MIMEText

# from config.HTMLTestRunner  import HTMLTestRunner
import logging

from config.HTMLTestReportCN import HTMLTestRunner

# //                            _ooOoo_
# //                           o8888888o
# //                           88" . "88
# //                           (| -_- |)
# //                            O\ = /O
# //                        ____/`---'\____
# //                      .   ' \\| |// `.
# //                       / \\||| : |||// \
# //                     / _||||| -:- |||||- \
# //                       | | \\\ - /// | |
# //                     | \_| ''\---/'' | |
# //                      \ .-\__ `-` ___/-. /
# //                   ___`. .' /--.--\ `. . __
# //                ."" '< `.___\_<|>_/___.' >'"".
# //               | | : `- \`.;`\ _ /`;.`/ - ` : | |
# //                 \ \ `-. \_ __\ /__ _/ .-` / /
# //         ======`-.____`-.___\_____/___.-`____.-'======
# //                            `=---='
# //         .............................................
# //                  佛祖镇楼                  BUG辟易
# //          佛曰:
# //                  写字楼里写字间，写字间里程序员；
# //                  程序人员写程序，又拿程序换酒钱。
# //                  酒醒只在网上坐，酒醉还来网下眠；
# //                  酒醉酒醒日复日，网上网下年复年。
# //                  但愿老死电脑间，不愿鞠躬老板前；
# //                  奔驰宝马贵者趣，公交自行程序员。
# //                  别人笑我忒疯癫，我笑自己命太贱；
# //                  不见满街漂亮妹，哪个归得程序员？

#  观自在菩萨，行深般若波罗蜜，照见五蕴皆空，度一切苦厄……  无一切bug
#
# def send_mail(path):
#     with open(path,'rb') as file:
#         msg = file.read()
#
#     mail_body = MIMEText(msg, _subtype='html', _charset="utf-8")
#     now = time.strftime("%Y-%m-%d_%H-%M-%S")
#     # 多功能，internet，mail，扩展，文本ll
#     mail_body["Subject"] = "权大师测试报告"+ now
#     mail_body["from"] = "lijiawei@quandashi.com"
#     mail_body["to"] = "lijiawei@quandashi.com"
#
#     smtp = smtplib.SMTP()
#     smtp.connect("smtp.quandashi.com")
#     smtp.login('lijiawei@quandashi.com', "!QAZ1qaz")
#     smtp.send_message(mail_body,mail_body["from"], mail_body["to"])
#     smtp.quit()
#     print("mail has been sent!")


# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.globalparam import case_path, report_path
from utils.log import Log
from config import globalparam

# 测试报告的路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人
recvaddress = ['lijiawei@quandashi.com']
# 163的用户名和密码
sendaddr_name = 'm15624992422@163.com'
sendaddr_pswd = '!QAZ1qaz'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver


    @staticmethod
    def __get_report():
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        now = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.msg['Subject'] = '权大师测试报告_'+now
        self.msg['date'] = time.strftime("%Y-%m-%d_%H-%M-%S")

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="QDS_TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.163.com')
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(case_path, "*test.py")
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    path = report_path + "\\" + now + "_report.html"
    with open(path, 'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title="权大师测试报告", description="Environment ：win10 chrome", tester="lijiawei").run(suite)
    # send_mail(path)
    sendMail = SendMail()
    sendMail.send()