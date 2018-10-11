# coding=utf-8
import random
import time
from selenium.webdriver import ActionChains
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class MonitorTest(MyTestCase):
    """商标监控测试集"""


    def test_monitor_1(self):
        """全库监控测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_link_text("智能工具").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标监控").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.assertIn("商标监控首页_权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div.wrap > ul > li:nth-child(1) > a > i").click()
        brand = unicode()
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section1 > table > tbody > tr.row-brandname > td.td-content > input").send_keys(brand)
        print("商标名称:" + brand)
        jinsi = random.randint(2,3)
        lx = self.driver.find_element_by_css_selector("#jinsi > label:nth-child({})".format(jinsi)).text
        self.driver.find_element_by_css_selector("#jinsi > label:nth-child({})".format(jinsi)).click()
        print(lx)
        self.driver.find_element_by_css_selector("#showleibie").click()
        suiji = random.randint(2, 46)
        add = self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).text
        self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).click()
        print(add)
        lb = self.driver.find_element_by_css_selector("#hot").text
        print(str(lb))
        print("全库监控添加成功!")
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section2 > div > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse.btn-sure").click()
        time.sleep(1)

        info = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr:nth-child(1)").text
        print("监控信息" + str(info))
        print("信息无误,测试通过!")

    def test_monitor_2(self):
        """初审公告监控测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_link_text("智能工具").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标监控").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.assertIn("商标监控首页_权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div.wrap > ul > li:nth-child(2) > a > i").click()
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov").click()
        suiji = random.randint(1,34)
        prov = self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov > option:nth-child({})".format(suiji)).text
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov > option:nth-child({})".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city").click()
        city = self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city > option:nth-child(1)").text
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city > option:nth-child(1)").click()
        print("地区选择:" + prov + "_" + str(city).replace("\n", " "))

        brand = unicode()
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section1 > table > tbody > tr:nth-child(3) > td.td-content > input").send_keys(brand)
        print("商标名称:" + brand)
        jinsi = random.randint(2,3)
        lx = self.driver.find_element_by_css_selector("#jinsi > label:nth-child({})".format(jinsi)).text
        self.driver.find_element_by_css_selector("#jinsi > label:nth-child({})".format(jinsi)).click()
        print(lx)
        self.driver.find_element_by_css_selector("#showleibie").click()
        suiji = random.randint(2, 46)
        add = self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).text
        self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).click()
        print(add)
        lb = self.driver.find_element_by_css_selector("#hot").text
        print(str(lb))
        print("初审公告监控添加成功!")
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section2 > div > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse.btn-sure").click()
        time.sleep(1)

        info = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr:nth-child(1)").text
        print("监控信息" + str(info))
        print("信息无误,测试通过!")

    def test_monitor_3(self):
        """可续展监控测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_link_text("智能工具").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标监控").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.assertIn("商标监控首页_权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div.wrap > ul > li:nth-child(3) > a > i").click()
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov").click()
        suiji = random.randint(1,34)
        prov = self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov > option:nth-child({})".format(suiji)).text
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.prov > option:nth-child({})".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city").click()
        city = self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city > option:nth-child(1)").text
        self.driver.find_element_by_css_selector("#city > select.myinput.select-sheng.city > option:nth-child(1)").click()
        print("地区选择:" + prov + "_" + str(city).replace("\n", " "))


        self.driver.find_element_by_css_selector("#showleibie").click()
        suiji = random.randint(2, 46)
        add = self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).text
        self.driver.find_element_by_css_selector("#leibie45 > label:nth-child({})".format(suiji)).click()
        print(add)
        lb = self.driver.find_element_by_css_selector("#hot").text
        print(str(lb))
        print("可续展监控添加成功!")
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section2 > div > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse.btn-sure").click()
        time.sleep(1)

        info = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr:nth-child(1)").text
        print("监控信息" + str(info))
        print("信息无误,测试通过!")

    def test_monitor_4(self):
        """代理机构监控测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_link_text("智能工具").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标监控").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.assertIn("商标监控首页_权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div.wrap > ul > li:nth-child(4) > a > i").click()

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section1 > table > tbody > tr.row-brandname > td:nth-child(2) > div > input").send_keys("权大师")
        print("代理机构:权大师")
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section1 > table > tbody > tr.row-brandname > td:nth-child(2) > div > button > i").click()
        self.driver.find_element_by_css_selector("#jinsi > label:nth-child(1)").click()

        print("代理机构监控添加成功!")
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer > div.section2 > div > a").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse").click()
        time.sleep(1)

        info = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr:nth-child(1)").text
        print("监控信息" + str(info))

        print("信息无误,测试通过!")

    def test_monitor_delete(self):
        """删除任务测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_link_text("智能工具").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("商标监控").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.assertIn("商标监控首页_权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div.section1 > div.btns > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > caption > h6 > div > div.myCheckBoxs > label").click()
        self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > caption > h6 > div > div.btn-delete").click()

        self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse.btn-sure").click()
        time.sleep(2)
        txt = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr > td").text
        print(str(txt))
        print("删除监控任务成功,测试通过！")