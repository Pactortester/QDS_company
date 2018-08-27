# coding=utf-8
import os
import smtplib
import unittest

import time
from email.mime.text import MIMEText

#from config.HTMLTestRunner  import HTMLTestRunner
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

def send_mail(path):
    with open(path,'rb') as file:
        msg = file.read()

    mail_body = MIMEText(msg, _subtype='html', _charset="utf-8")
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    # 多功能，internet，mail，扩展，文本ll
    mail_body["Subject"] = "权大师测试报告"+ now
    mail_body["from"] = "lijiawei@quandashi.com"
    mail_body["to"] = "lijiawei@quandashi.com"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.quandashi.com")
    smtp.login('lijiawei@quandashi.com', "!QAZ1qaz")
    smtp.send_message(mail_body,mail_body["from"], mail_body["to"])
    smtp.quit()
    print("mail has been sent!")


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("G:\\quandashitest_company\\quandashitest_company\\case\\","*test.py")
    # unittest.TextTestRunner().run(suite)
    path = os.path.dirname(__file__)
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    path = path + "/report/" + now + "_report.html"
    with open(path, 'wb') as file:
        HTMLTestRunner(stream=file, verbosity=1, title="权大师测试报告", description="Environment:  OS:win10  Browser:chrome").run(suite)
    send_mail(path)