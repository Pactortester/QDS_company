# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 13:59
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: bidatatest.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
import random
import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class BITest(MyTestCase):
    """商标大数据测试集"""


    def test_data_1(self):

        """数据量"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标大数据").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(4)
        self.driver.set_window_size(1920, 1080)

        info_1 = self.driver.find_element_by_css_selector("body > div.main_wrap > ul").text
        print(info_1)

        # print("商标大数据已经下线!")



    def test_data_2(self):

        """BIReportName"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标大数据").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)

        self.driver.find_element_by_class_name("md").click()

        self.driver.find_element_by_css_selector("#BIShow > div.tabBtn.clearfix > a:nth-child(1)").click()

        report = ["最新报告","代理机构排行","商标申请人排行","申请类别排行","申请地区排行","地理标志"]
        suiji = random.choice(report)

        name = self.driver.find_element_by_link_text("{}".format(suiji)).text
        self.driver.find_element_by_link_text("{}".format(suiji)).click()
        print(name)
        time.sleep(2)

        if suiji == "地理标志":
            suiji_2 = random.randint(1,2)
        else:
            suiji_2 = random.randint(1,10)

        info_2 = self.driver.find_element_by_css_selector(
            "#BIShow > div.infoListBox > ul > li:nth-child({})".format(suiji_2)).text
        self.driver.find_element_by_css_selector(
            "#BIShow > div.infoListBox > ul > li:nth-child({})".format(suiji_2)).click()
        print(info_2)


        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)

        print("PDF文档链接:     " + self.driver.current_url)
        get_screenshort(self.driver,"test_data_2.png")

        # print("商标大数据已经下线!")
