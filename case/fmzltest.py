# coding=utf-8

import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class FmZlTest(MyTestCase):
    """发明专利测试集"""

    def test_fmzlbz_1(self):
        """标准型-单个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar >  div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(1)").click()

        time.sleep(2)
        self.assertIn("发明专利标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  #单个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_fmzlbz_2(self):
        """标准型-多个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(1)").click()
        time.sleep(2)

        self.assertIn("发明专利标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        #self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  #多个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_fmzlbz_3(self):
        """标准型-不减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(1)").click()
        time.sleep(2)

        self.assertIn("发明专利标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        #self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        #self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click() #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector("body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()


        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_fmzldb_1(self):
        """担保型-单个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar >  div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(2)").click()

        time.sleep(2)
        self.assertIn("发明专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_fmzldb_2(self):
        """担保型-多个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(2)").click()
        time.sleep(2)

        self.assertIn("发明专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_fmzldb_3(self):
        """担保型-不减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(2) > dd > a:nth-child(2)").click()
        time.sleep(2)

        self.assertIn("发明专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2) > input[type=\"checkbox\"]")  #多个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_fmzl_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.width1200 > div > div > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.width1200 > div > div > ul > li.row-step > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()