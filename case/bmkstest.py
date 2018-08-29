# coding=utf-8

import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.screenshort import get_screenshort


class BmKsTest(MyTestCase):
    """保姆注册测试集"""

    def test_bmks(self):

        """保姆快速注册"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')

        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.dengLu()
        time.sleep(1)
        # self.driver.find_element_by_css_selector("#com-navbar > div > ul > li:nth-child(1) > a").click()
        """新版首页"""
        # self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(1) > a").click()


        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 "
            "> a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div"
            " > dl:nth-child(3) > dd > a:nth-child(1)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(3)


        self.assertIn("保姆快速注册-权大师",self.driver.title)
        print(self.driver.title)

        # 保姆快速注册
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont >"
            " ul > li.list.active").click()

        # #total-price

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_bmks.png")

        for i in self.driver.find_elements_by_css_selector("body > div.myOrder-wrap > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.myOrder-wrap > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()
