import random
import re
import time


from utils.logincookie import DengLuPage
from utils.mytestcase import MyTestCase
from utils.random import unicode


class SbNumTest(MyTestCase):

    """相似商标个数测试集"""

    def test_number1(self):

        """智能注册_自助商标跳转测试"""

        dl = DengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(1) > a").click()
        time.sleep(1)
        self.assertIn("保姆快速注册-权大师", self.driver.title)
        print("智能商标注册-权大师")
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            #aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        sbmc=unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(sbmc))
        print("商标名称：{}".format(sbmc))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()

        suiji = random.randint(2, 46)

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        zf=self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-left > a:nth-child(2) > span").text
        print(zf)
        number1 = re.sub("\D", "", zf)
        print(number1)
        time.sleep(1)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-left > a:nth-child(2) > span").click()
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

        number2=self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text

        print("权大师为您找到相关结果{}个".format(number2))

        self.assertIn(number2,number1)

        print("检索相似商标数量一致,测试通过！")

    def test_number2(self):
        """智能注册_推荐商标跳转测试"""

        dl = DengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > ul > li:nth-child(1) > a").click()
        time.sleep(1)
        self.assertIn("保姆快速注册-权大师", self.driver.title)
        print("智能商标注册-权大师")
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        sbmc = unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(sbmc))
        print("商标名称：{}".format(sbmc))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a:nth-child(1)").click()

        self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znfirst").click()
        fl = random.randint(2, 12)
        self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znfirst > option:nth-child({})".format(fl)).click()
        fenlei1 = self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znfirst > option:nth-child({})".format(fl)).text

        self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znsecond").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znsecond > option:nth-child(2)").click()
        fenlei2 = self.driver.find_element_by_css_selector("body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-industry1 > div > select.myInput.znsecond > option:nth-child(2)").text

        print("选择所在领域："+fenlei1+"_"+fenlei2)

        zf = self.driver.find_element_by_css_selector(
            "#section-recommend > div.section-bodyer > div:nth-child(1) > h4 > div.header-left > a:nth-child(2) > span").text
        print(zf)
        number1 = re.sub("\D", "", zf)
        print(number1)
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#section-recommend > div.section-bodyer > div:nth-child(1) > h4 > div.header-left > a:nth-child(2) > span").click()
        time.sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        dl.refresh()

        time.sleep(2)
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

        self.assertIn(number2, number1)

        print("检索相似商标数量一致,测试通过！")
