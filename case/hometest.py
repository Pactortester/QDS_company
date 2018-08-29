# coding=utf-8

import time
import random

import logging

from utils.mytestcase import MyTestCase
from utils.logincookie import dengLuPage
from utils.random import Unicode
from utils.screenshort import get_screenshort


class HomeTest(MyTestCase):

    """个人中心测试集"""

    def test_ddzx(self):
        """订单中心"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        """搜索订单"""

        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()

        self.assertIn("权大师_我的商标", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(1) > input").send_keys("Z80510326116")
        self.driver.find_element_by_css_selector("#s-form > ul > li:nth-child(7) > input").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr > td:nth-child(8) > div > a").click()
        time.sleep(1)

        """修改商标名字"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()

        self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功")

        time.sleep(1)

        """修改尼斯分类"""

        suiji=random.randint(2, 46)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()
        time.sleep(2)
        print("尼斯分类修改为第{}类".format(suiji-1))
        time.sleep(2)

        """申请人信息"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()

        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a.btn-choice.fownertype.active").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("田伟")
        self.driver.find_element_by_css_selector("#geren-idCard").clear()
        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("130184198908191520")
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功")
        time.sleep(4)

        """订单联系人"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(8) > div > h2 > a").click()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys("大西瓜")
        self.driver.find_element_by_name("ftelephone").clear()
        self.driver.find_element_by_name("ftelephone").send_keys("0351-5925212")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()
        print("订单联系人修改成功")
        time.sleep(1)


        get_screenshort(self.driver,"ddzxtest.png")

        print("测试通过!")

    def test_dzgl(self):

        """发票地址管理"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        """添加邮寄地址"""
        self.driver.find_element_by_link_text("邮寄地址管理").click()

        self.assertIn("权大师_邮寄地址管理", self.driver.title)
        print(self.driver.title)
        time.sleep(1)

        #self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li:nth-child(3) > ul > li.selected > a").click()
        self.driver.find_element_by_css_selector("#addAddress").click()
        ss=Unicode()
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(1) > td:nth-child(2) > input").send_keys("{}".format(ss))
        print("收件人名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(2) > td:nth-child(2) > input").send_keys("15624992422")
        self.driver.find_element_by_css_selector("#address_info").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        qq=Unicode()
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(4) > td:nth-child(2) > textarea").send_keys("{}".format(qq))
        print("收件人地址:北京市昌平区{}街道".format(qq))
        self.driver.find_element_by_css_selector("#add_Address > table > tbody > tr:nth-child(3) > td.td-title").click()
        self.driver.find_element_by_css_selector("#submit-editAddress").click()

        print("添加邮寄地址成功！")


        get_screenshort(self.driver,"dzgltest.png")

        print("测试通过！")

    def test_fpsq(self):

        """发票申请"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)



        self.driver.find_element_by_link_text("发票申请").click()

        self.assertIn("权大师_我的发票申请", self.driver.title)
        print(self.driver.title)
        time.sleep(1)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > ul > li.list.selected > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > ul > li:nth-child(3) > a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.search-form > form > ul > li:nth-child(1) > dl:nth-child(1) > dd > input").send_keys("Z80509824620")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.search-form > form > ul > li:nth-child(2) > div > input").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > div > div.section1 > table > tbody > tr > td:nth-child(8) > div > a").click()
        #self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.p-invoice-content > div.tabsPanel > div > div.section1 > table > tfoot > tr > td.td-selectSingle > div > a").click()
        time.sleep(2)


        #self.driver.find_element_by_css_selector("#invoiceModal > ul > li.tab.active")



        self.driver.find_element_by_css_selector("#invoiceModal > ul > li.tab.active").click()

        #self.driver.find_element_by_name("invoiceType").click()
        self.driver.find_element_by_css_selector("#radio-isgs > label:nth-child(2)").click()

        self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr:nth-child(3) > td:nth-child(2) > input").clear()
        self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr:nth-child(3) > td:nth-child(2) > input").send_keys("北京梦知网科技有限公司")
        self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr.tr-sbh.active > td:nth-child(2) > input").clear()
        self.driver.find_element_by_css_selector("#invoiceModal > div.tabs-boder > div.tabs-content.active > table > tbody > tr.tr-sbh.active > td:nth-child(2) > input").send_keys("91330784689989022Q")
        self.driver.find_element_by_css_selector("#invoice-general").click()

        print("发票申请提交成功")
        print("测试通过！")

    def test_gwyj(self):

        """官文邮寄"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)

        dl.dengLu()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(1)


        """官文管理"""
        self.driver.find_element_by_link_text("官文管理").click()

        self.assertIn("权大师_官文待申请", self.driver.title)
        print(self.driver.title)
        time.sleep(1)


        self.driver.find_element_by_name("receiptNo").send_keys("23491381")
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/form/p/input").click()

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.person-postofficial.order-page > div.official-doc-wrap > table > tbody > tr:nth-child(2) > td:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.cho-wrap-wrap > div > dl > dd.next-btn").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.person-postofficial.order-page > div.confirm-post-addr > p.addr-head > a").click()
        self.driver.find_element_by_name("receivedName").send_keys("老戏骨")

        self.driver.find_element_by_name("receivedTel").send_keys("15624992422")
        self.driver.find_element_by_name("divisionName").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#administrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_name("street").send_keys("TBD云集中心")
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id=\"address_info\"]/p[5]/a[2]").click()

        get_screenshort(self.driver,"test_gwyj.png")
        print("官文邮寄成功！")
        print("测试通过！")


