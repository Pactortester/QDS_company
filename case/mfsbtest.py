import re
import time


from utils.random import patent_name, unicode

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.screenshort import get_screenshort


class MfSbTest(MyTestCase):
    """搜索查询测试集"""

    def test_sbss(self):
        """商标搜索测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#serch-word").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("注册商标查询_中国商标查询_权大师官网", self.driver.title)
        print(self.driver.title)
        dl.refresh()
        ss = unicode()
        print("搜索商标名称："+ss)
        self.driver.find_element_by_css_selector("body > div.brandSearch2-page > div > div.search > div.searchPanel.clearfix > input.input.search-text").send_keys("{}".format(ss))
        self.driver.find_element_by_css_selector("#btnSearchkey").click()
        time.sleep(4)
        print(self.driver.title)
        get_screenshort(self.driver, "test_sbss.png")
        print("商标搜索测试通过")

    def test_csgg(self):
        """初审公告测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li:nth-child(3) > a > img").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("初审公告搜索", self.driver.title)
        print(self.driver.title)
        dl.refresh()
        brand1 = unicode()
        self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(1) > input[type=\"text\"]").send_keys(brand1)
        print("商标名称:" + brand1)
        self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(1) > span").click()
        lx1 = self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(1) > span").text
        print("搜索类型:" + str(lx1))
        time.sleep(2)
        self.driver.set_window_size(1920,1080)
        time.sleep(2)
        get_screenshort(self.driver,"test.png")
        self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > div > a").click()
        time.sleep(5)
        js = "return document.getElementsByClassName(\"search-num\")[0].innerText;"
        ss = self.driver.execute_script(js)
        print(str(ss))

        time.sleep(2)
        get_screenshort(self.driver,"test_csgg_1.png")
        self.driver.refresh()


        brand2 = unicode()
        self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(1) > input[type=\"text\"]").send_keys(
            brand2)
        print("商标名称:" + brand2)
        self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(2)").click()
        lx2 = self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(2)").text
        print("搜索类型:" + lx2)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > div > a").click()
        time.sleep(5)
        js = "return document.getElementsByClassName(\"search-num\")[0].innerText;"
        ss = self.driver.execute_script(js)
        print(str(ss))
        time.sleep(2)
        get_screenshort(self.driver, "test_csgg_2.png")
        self.driver.refresh()

        brand3 = unicode()
        self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(1) > input[type=\"text\"]").send_keys(
            brand3)
        print("商标名称:" + brand3)
        self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(3) > span").click()
        lx3 = self.driver.find_element_by_css_selector(
            "#noticeList > div > div.page-form > ul:nth-child(1) > li:nth-child(2) > label:nth-child(3) > span").text
        print("搜索类型:" + lx3)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#noticeList > div > div.page-form > div > a").click()
        time.sleep(5)
        js = "return document.getElementsByClassName(\"search-num\")[0].innerText;"
        ss = self.driver.execute_script(js)
        print(str(ss))
        time.sleep(2)
        get_screenshort(self.driver, "test_csgg_3.png")

    def test_zlss(self):
        """专利搜索测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#qds-search-common > li:nth-child(2)").click()
        zl = patent_name()
        self.driver.find_element_by_css_selector("#qds-searchkey").send_keys(zl)
        print("专利名称:" + str(zl))
        self.driver.find_element_by_css_selector("#serch-word").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(10)
        self.assertIn("注册专利查询_中国专利查询系统_让知识产生财富_权大师",self.driver.title)
        print(self.driver.title)
        num = self.driver.find_element_by_css_selector("body > div.patentSearchList-wrap.searchList-wrap > div.sort-condition.songti > div > div.s-left > dl > dt").text
        print(str(num))
        number = re.sub("\D", "", num)
        print(number)

        get_screenshort(self.driver,"test_zlss.png")
        print("专利搜索测试通过!")

    def test_qyss(self):
        """企业搜索测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#qds-search-common > li:nth-child(3)").click()
        company = unicode()
        self.driver.find_element_by_css_selector("#qds-searchkey").send_keys(company)
        print(str(company))
        self.driver.find_element_by_css_selector("#serch-word").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        # self.assertIn("注册专利查询_中国专利查询系统_让知识产生财富_权大师", self.driver.title)
        print(self.driver.title)
        print(self.driver.current_url)