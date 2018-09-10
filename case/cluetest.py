# coding=utf-8

import time
from selenium.webdriver import ActionChains
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class ClueTest(MyTestCase):
    """线索源测试集"""

    def test_clue1(self):

        """开放平台线索测试"""
        dl = DengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)
        """新版首页"""

        self.driver.execute_script("window.scrollBy(0,3000)")  # 滑动滚动条

        ActionChains(self.driver).move_to_element("#section-tools > div > ul > li:nth-child(2)").perform()
        time.sleep(4)
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector("#section-tools > div > ul > li.active > dl > dd > a").click()
        print("开放平台咨询_弹框")
        self.driver.find_element_by_id("userName").send_keys(unicode())
        self.driver.find_element_by_id("userTel").send_keys("15624992498")
        self.driver.find_element_by_id("userQue").send_keys(unicode()+unicode())

        name = self.driver.find_element_by_id("userName").get_attribute("value")
        tel = self.driver.find_element_by_id("userTel").get_attribute("value")
        que = self.driver.find_element_by_id("userQue").get_attribute("value")
        print("姓名:" + name)
        print("电话:" + tel)
        print("问题:" + que)

        self.driver.find_element_by_css_selector("#contactModal > form > span").click()

        print("线索录入成功!")

    def test_clue2(self):

        """专利二级页线索测试"""
        dl = DengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)
        """新版首页"""

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector()).perform()

        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])


        self.driver.find_element_by_css_selector("#anchor03 > div > a").click()
        print("专利咨询_弹框")
        self.driver.find_element_by_id("userName").send_keys(unicode())
        self.driver.find_element_by_id("userTel").send_keys("15624992498")
        self.driver.find_element_by_id("userQue").send_keys(unicode()+unicode())

        name = self.driver.find_element_by_id("userName").get_attribute("value")
        tel = self.driver.find_element_by_id("userTel").get_attribute("value")
        que = self.driver.find_element_by_id("userQue").get_attribute("value")

        print("姓名:" + name)
        print("电话:" + tel)
        print("问题:" + que)

        self.driver.find_element_by_css_selector("#sub-qus").click()

        print("线索录入成功!")
