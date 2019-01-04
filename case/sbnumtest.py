import random
import re
import time
from _cffi_backend import string

from selenium.webdriver import ActionChains

from utils.logincookie import DengLuPage
from utils.mytestcase import MyTestCase
from utils.random import unicode


class SbNumTest(MyTestCase):

    """智能推荐测试集"""

    def test_number1(self):

        """智能注册_自助商标跳转测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = "小米"
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        # self.driver.find_element_by_css_selector(
        #     "#section-selfchoice > div > div.group-left.scroll > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        zf = self.driver.find_element_by_css_selector("#section-selfchoice > div > div.group-right > div > div > h4 > div.header-left > a > span").text
        print(zf)
        number1 = re.sub("\D", "", zf)
        print(number1)
        time.sleep(1)
        self.driver.find_element_by_css_selector("#section-selfchoice > div > div.group-right > div > div > h4 > div.header-left > a > span").click()
        time.sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        dl.refresh()

        time.sleep(1)

        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips1 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips2 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips3 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips4 > a").click()
        # time.sleep(1)

        number2 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text

        print("权大师为您找到相关结果{}个".format(number2))

        self.assertIn(number2,number1)

        print("检索相似商标数量一致,测试通过！")

    def test_number2(self):
        """智能注册_推荐商标跳转测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = "华为"
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label.label.checked").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        """智能推荐"""
        self.driver.find_element_by_css_selector("#selectBusiness > div").click()
        industry = 1
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry))).perform()
        ly = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-left.scroll > span:nth-child({})".format(industry)).text
        time.sleep(2)
        sz = 5
        hy = self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).text
        self.driver.find_element_by_css_selector(
            "#selectBusiness > div > div > div.i-right.scroll > span:nth-child({})".format(sz)).click()
        ActionChains(self.driver).release()

        print("选择所在领域:" + ly + "_" + hy + "_" + "行业精准推荐")


        xt = self.driver.find_element_by_css_selector("#first09 > div.category-recommend-first > span.tips > a:nth-child(1)").text
        js = self.driver.find_element_by_css_selector("#first09 > div.category-recommend-first > span.tips > a:nth-child(2)").text

        print(xt+js)
        number1 = re.sub("\D", "", xt)
        number2 = re.sub("\D", "", js)

        sl = int(number1) + int(number2)
        print(sl)
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#first09 > div.category-recommend-first > span.tips").click()
        time.sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        dl.refresh()

        time.sleep(3)
        #
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips1 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips2 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips3 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips4 > a").click()
        time.sleep(1)

        number3 = self.driver.find_element_by_css_selector(
            "#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text

        print("权大师为您找到相关结果{}个".format(number3))

        self.assertEqual(sl, number3,"相似商标数量不一致请及时查看!")

        print("检索相似商标数量一致,测试通过！")

    def test_number3(self):
        """智能注册_全类商标跳转测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i
        ss = "vivo"
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        print("商标名称:{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.show1.form-wrap > ul > li.brand-upload > div > div.brand-upload-wrap > div.zidongdong-create > ul > li > a").click()
        time.sleep(5)

        """全类保护"""
        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(3)").click()
        time.sleep(20)


        zf = self.driver.find_element_by_css_selector("#first01 > div.category-recommend-first > span.tips > a:nth-child(2)").text
        print(str(zf).replace("，",""))
        number1 = re.sub("\D", "", zf)
        s2 = int(number1) + 0
        print(s2)
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#first01 > div.category-recommend-first > span.tips").click()
        time.sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        dl.refresh()

        time.sleep(3)
        #
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips1 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips2 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips3 > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("body > div.page > div.search-help > div.tips.tips4 > a").click()
        time.sleep(1)

        number2 = self.driver.find_element_by_css_selector(
            "#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text

        print("权大师为您找到相关结果{}个".format(number2))

        self.assertEqual(s2, number2,"相似商标数量不一致请及时查看!")

        print("检索相似商标数量一致,测试通过！")
