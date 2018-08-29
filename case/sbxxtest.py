#


# coding=utf-8

import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import dengLuPage
from utils.screenshort import get_screenshort


class SbXxTest(MyTestCase):
    """商标信息测试集"""

    def test_sbzr(self):
        """商标转让测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(6) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标转让-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_sbzr.png")

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

    def test_sbxz(self):
        """商标续展让测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(6) > dd > a:nth-child(2)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标续展-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_sbxz.png")

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

    def test_sbkz(self):
        """商标宽展测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(6) > dd > a:nth-child(3)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标宽展-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_sbkz.png")

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

    def test_sbxk(self):
        """商标许可备案测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(6) > dd > a:nth-child(4)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标许可备案-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_sbxk.png")

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

    def test_sbbg(self):
        """商标变更测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(6) > dd > a:nth-child(5)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("商标变更-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("全大师")
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_sbbg.png")

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