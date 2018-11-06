# coding=utf-8
import time
import logging
from selenium.webdriver import ActionChains
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.screenshort import get_screenshort
from utils.random import unicode, patent_number


class ZlYwTest(MyTestCase):
    """专利业务测试集"""

    def test_zljs(self):
        """专利查新检索（报告）测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(1) > dd > a").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("专利查新检索|专利查新检索报告|专利查新检索流程及费用-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_zljs.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

        # com-navbar > div > div.drop-nav > div > ul > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)

    def test_cpwgbz_1(self):
        """产品外观标准_单个申请人减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准

        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgbz_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_cpwgbz_2(self):
        """产品外观标准_多个申请人减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgbz_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_cpwgbz_3(self):
        """产品外观标准_不减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgbz_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_cpwgdb_1(self):
        """产品外观担保_单个申请人减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(2)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓

        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgdb_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_cpwgdb_2(self):
        """产品外观担保_多个申请人减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(2)
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓

        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgdb_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_cpwgdb_3(self):
        """产品外观担保_不减缓测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("外观设计专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(3)
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓
        time.sleep(3)
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_cpwgdb_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guibz_1(self):
        """GUI标准_单个申请人减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guibz_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guibz_2(self):
        """GUI标准_多个申请人减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guibz_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guibz_3(self):
        """GUI标准_不减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()  # 标准
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guibz_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guidb_1(self):
        """GUI担保_单个申请人减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(2)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓

        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guidb_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guidb_2(self):
        """GUI担保_多个申请人减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(2)
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guidb_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_guidb_3(self):
        """GUI担保_不减缓"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(3) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("GUI及系列产品标准申请|专利申请|专利查询|权大师",self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#serviceName > li:nth-child(2)").click()  # 担保
        time.sleep(2)

        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li:nth-child(2)").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_guidb_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzlbz_1(self):
        """标准型-单个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar >  div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(1)").click()

        time.sleep(2)
        self.assertIn("实用新型专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzlbz_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzlbz_2(self):
        """标准型-多个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(1)").click()
        time.sleep(2)

        self.assertIn("实用新型专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzlbz_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzlbz_3(self):
        """标准型-不减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(1)").click()
        time.sleep(2)

        self.assertIn("实用新型专利标准申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #多个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzlbz_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzldb_1(self):
        """担保型-单个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar >  div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(2)").click()

        time.sleep(2)
        self.assertIn("实用新型专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector("#slowItems > label.label.active").click()  # 单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label.label.active").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzldb_1.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzldb_2(self):
        """担保型-多个申请人减缓"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(2)").click()
        time.sleep(2)

        self.assertIn("实用新型专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(2)").click()  # 多个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(2)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzldb_2.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_syzldb_3(self):
        """担保型-不减缓"""
        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(2)").click()
        time.sleep(2)

        self.assertIn("实用新型专利担保申请|专利申请|专利查询|权大师", self.driver.title)
        print(self.driver.title)
        # self.driver.find_element_by_css_selector("#slowItems > label.label.active > input[type=\"checkbox\"]")  #单个申请人减缓
        # self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3) > input[type=\"checkbox\"]")  #多个申请人减缓
        self.driver.find_element_by_css_selector("#slowItems > label:nth-child(3)").click()  # 不减缓

        self.driver.find_element_by_css_selector("#serviceName > li.list.active").click()
        print("服务类别:" + self.driver.find_element_by_css_selector(
            "#serviceName > li.list.active").text + "_" + self.driver.find_element_by_css_selector(
            "#slowItems > label:nth-child(3)").text)
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()

        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_syzldb_3.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()
    """旧版专利商品"""
    # def test_syxxjc(self):
    #     """实用新型专利基础版"""
    #
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(2)
    #     ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
    #     time.sleep(2)
    #     ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
    #     ActionChains(self.driver).release()
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(1)").click()
    #
    #     time.sleep(3)
    #
    #     # 获取打开的多个窗口句柄
    #     windows = self.driver.window_handles
    #     # 切换到当前最新打开的窗口
    #     self.driver.switch_to.window(windows[-1])
    #     self.assertIn("实用新型专利基础版_权大师",self.driver.title)
    #     print(self.driver.title)
    #
    #     for a in self.driver.find_elements_by_css_selector("#total-price"):
    #         print("费用总计:"+a.text)
    #         aa=a.text
    #
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
    #     self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
    #     self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
    #     self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
    #     self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
    #
    #     get_screenshort(self.driver, "test_syxxjc.png")
    #
    #     for i in self.driver.find_elements_by_css_selector(
    #             "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
    #         print("总价:" + i.text)
    #         ii = i.text
    #
    #     self.assertIn(aa, ii)
    #     print("价格一致")
    #
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()
    #
    #     for o in self.driver.find_elements_by_class_name("payable"):
    #         print("订单提交成功，应付金额:" + o.text)
    #         oo = o.text
    #
    #     self.assertIn(oo, ii)
    #
    #     print("测试通过")
    #
    #     self.driver.find_element_by_css_selector("#alisubmit").click()
    #
    # def test_syxxzl(self):
    #     """实用新型专利卓越版"""
    #
    #     dl = DengLuPage(self.driver)
    #     dl.login()
    #     time.sleep(2)
    #     ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
    #     time.sleep(2)
    #     ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
    #     ActionChains(self.driver).release()
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(4) > dd > a:nth-child(2)").click()
    #
    #     time.sleep(3)
    #
    #     # 获取打开的多个窗口句柄
    #     windows = self.driver.window_handles
    #     # 切换到当前最新打开的窗口
    #     self.driver.switch_to.window(windows[-1])
    #     self.assertIn("实用新型专利卓越版_权大师", self.driver.title)
    #     print(self.driver.title)
    #
    #     for a in self.driver.find_elements_by_css_selector("#total-price"):
    #         print("费用总计:" + a.text)
    #         aa = a.text
    #
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
    #     self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
    #     self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
    #     self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
    #     self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
    #
    #     get_screenshort(self.driver, "test_syxxzl.png")
    #
    #     for i in self.driver.find_elements_by_css_selector(
    #             "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
    #         print("总价:" + i.text)
    #         ii = i.text
    #
    #     self.assertIn(aa, ii)
    #     print("价格一致")
    #
    #     self.driver.find_element_by_css_selector(
    #         "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()
    #
    #     for o in self.driver.find_elements_by_class_name("payable"):
    #         print("订单提交成功，应付金额:" + o.text)
    #         oo = o.text
    #
    #     self.assertIn(oo, ii)
    #
    #     print("测试通过")
    #
    #     self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_zlbh(self):
        """专利驳回复审测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(5) > dd > a:nth-child(1)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("发明专利驳回复审_权大师", self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_zlbh.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_zlxg(self):
        """ 专利无效宣告测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(5) > dd > a:nth-child(2)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("专利无效宣告_权大师", self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_zlxg.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_zldb(self):
        """发明专利无效答辩测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(5) > dd > a:nth-child(3)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("发明专利无效答辩_权大师", self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_zldb.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_nfjn(self):
        """年费缴纳测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(6) > dd > a:nth-child(1)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("发明专利年费缴纳-权大师", self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        patent_no = patent_number()
        self.driver.find_element_by_name("patent_no").send_keys("ZL{}".format(patent_no))
        print("专利号:ZL{}".format(patent_no))
        patent_name = unicode()
        self.driver.find_element_by_name("patent_name").send_keys("{}".format(patent_name))
        print("专利名称:{}".format(patent_name))
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_nfjn.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(8) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(8) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_zlbg(self):
        """专利著录项变更测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(2) > div > dl:nth-child(6) > dd > a:nth-child(2)").click()

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("专利著录项变更-权大师", self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_zlbg.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()
