# coding=utf-8

import time
import random

import logging

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class HomeTest(MyTestCase):

    """个人中心测试集"""

    def test_address(self):

        """发票地址管理"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)

        """添加邮寄地址"""
        self.driver.find_element_by_link_text("邮寄地址管理").click()

        self.assertIn("权大师_邮寄地址管理", self.driver.title)
        print(self.driver.title)
        time.sleep(1)

        # self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li:nth-child(3) > ul > li.selected > a").click()
        self.driver.find_element_by_css_selector("#addAddress").click()
        ss=unicode()
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(1) > td:nth-child(2) > input").send_keys("{}".format(ss))
        print("收件人名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys("15624992422")
        self.driver.find_element_by_css_selector("#address_info").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        qq=unicode()
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(4) > td:nth-child(2) > textarea").send_keys("{}".format(qq))
        print("收件人地址:北京市昌平区{}街道".format(qq))
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(3) > td.td-title").click()
        self.driver.find_element_by_css_selector("#submit-editAddress").click()

        print("添加邮寄地址成功！")

        get_screenshort(self.driver,"test_address.png")

        print("测试通过！")

    def test_invoice(self):

        """发票申请测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)



        self.driver.find_element_by_link_text("发票申请").click()

        self.assertIn("权大师_我的发票申请", self.driver.title)
        print(self.driver.title)
        time.sleep(1)

        self.assertEqual(1, 0 ,"此账号无发票可申请!")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > ul > li.list.selected > a").click()
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > ul > li:nth-child(3) > a").click()
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.search-form > form > ul > li:nth-child(1) > dl:nth-child(1) > dd > input").send_keys("Z80509824620")
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.search-form > form > ul > li:nth-child(2) > div > input").click()
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > div > div.section1 > table > tbody > tr > td:nth-child(8) > div > a").click()
        # # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > div > div.section1 > table > tfoot > tr > td.td-selectSingle > div > a").click()
        # time.sleep(2)
        #
        #
        # # self.driver.find_element_by_css_selector("#invoiceModal > ul > li.tab.active")
        #
        #
        #
        # self.driver.find_element_by_css_selector("#invoiceModal > ul > li.tab.active").click()
        #
        # # self.driver.find_element_by_name("invoiceType").click()
        # self.driver.find_element_by_css_selector("#radio-isgs > label:nth-child(2)").click()
        #
        # self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr:nth-child(3) > td:nth-child(2) > input").clear()
        # self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr:nth-child(3) > td:nth-child(2) > input").send_keys("北京梦知网科技有限公司")
        # self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr.tr-sbh.active > td:nth-child(2) > input").clear()
        # self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr.tr-sbh.active > td:nth-child(2) > input").send_keys("91330784689989022Q")
        # self.driver.find_element_by_css_selector("#invoice-general").click()
        #
        # print("发票申请提交成功")
        # print("测试通过！")

    def test_official(self):

        """官文邮寄测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        """官文管理"""
        self.driver.find_element_by_link_text("官文管理").click()

        self.assertIn("权大师_官文待申请", self.driver.title)
        print(self.driver.title)

        self.assertEqual(1, 0, "此账号无官文可申请!")
        # time.sleep(1)
        #
        #
        # self.driver.find_element_by_name("receiptNo").send_keys("23491381")
        # self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/form/p/input").click()
        #
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.person-postofficial.order-page > div.official-doc-wrap > table > tbody > tr:nth-child(2) > td:nth-child(1) > span").click()
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.cho-wrap-wrap > div > dl > dd.next-btn").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.person-postofficial.order-page > div.confirm-post-addr > p.addr-head > a").click()
        # self.driver.find_element_by_name("receivedName").send_keys("老戏骨")
        #
        # self.driver.find_element_by_name("receivedTel").send_keys("15624992422")
        # self.driver.find_element_by_name("divisionName").click()
        # self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        # self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        # self.driver.find_element_by_name("street").send_keys("TBD云集中心")
        # time.sleep(1)
        #
        # self.driver.find_element_by_xpath("//*[@id=\"address_info\"]/p[5]/a[2]").click()
        #
        # get_screenshort(self.driver,"test_official.png")
        # print("官文邮寄成功！")
        # print("测试通过！")

    def test_batch_payment(self):
        """批量支付测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        self.assertIn("权大师_我的商标", self.driver.title)
        print(self.driver.title)

        """待付款"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > ul > li:nth-child(2) > a").click()
        """全选订单批量支付"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > table > thead > tr > th:nth-child(1) > label").click()
        time.sleep(2)

        info_1 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > div.order-detail-fix > div > div.right > div > span").text
        print(info_1)

        number_1 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > div.order-detail-fix > div > div.right > div > span > i:nth-child(2) > i").text
        """立即付款"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > div.order-detail-fix > div > div.right > div > a").click()
        time.sleep(5)
        info_2 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.section-orderInfo.clearfix > div.order-info-box > div > h2").text
        print(info_2)
        number_2 = self.driver.find_element_by_css_selector("#total").text

        self.assertEqual(number_1,number_2,"批量支付金额异常!")
        print("批量支付测试通过!")

    def test_patent_cancel(self):
        """取消专利订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page-tab > a.p-index").click()
        time.sleep(4)

        while True:

            n = self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > ul > li:nth-child(2) > a").text
            self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > div > a.order-cancel-old").click()

            alert = self.driver.switch_to.alert
            # print("弹框信息:" + alert.text)
            alert.accept()

            time.sleep(2)
            self.driver.find_element_by_css_selector("#alert > div > div.footer > a").click()
            time.sleep(2)

            print(n)
            if str(n) == "待付款 (4889)":
                break

        print("取消未付款专利订单,测试通过!")

    def test_copyright_cancel(self):
        """取消版权订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page-tab > a.c-index").click()
        time.sleep(4)

        while True:

            n = self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > ul > li:nth-child(2) > a").text
            self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(7) > div > a.order-cancel-old").click()

            alert = self.driver.switch_to.alert
            # print("弹框信息:" + alert.text)
            alert.accept()

            time.sleep(2)
            self.driver.find_element_by_css_selector("#alert > div > div.footer > a").click()
            time.sleep(2)

            print(n)
            if str(n) == "待付款 (1)":
                break

        print("取消未付款专利订单,测试通过!")