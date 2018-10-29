import random
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
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
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

    def test_sbrs_1(self):
        """商标热搜测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        rs1 = self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item").text
        print("热搜商标_1:" + str(rs1).replace("\n", " "))
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dd").click()
        time.sleep(2)
        rs2 = self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item").text
        print("热搜商标_2:" + str(rs2).replace("\n", " "))
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dd").click()
        time.sleep(2)
        rs3 = self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item").text
        print("热搜商标_3:" + str(rs3).replace("\n", " "))
        get_screenshort(self.driver,"test_sbrs.png")
        print("热搜正常,测试通过!")

    def test_sbrs_2(self):
        """热搜跳转测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        rs = self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item").text
        print("热搜商标:" + str(rs).replace("\n", " "))
        hot = random.randint(1,6)
        name = self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item > span:nth-child({})".format(hot)).text
        print("商标名称:" + name)
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-search > div > dl > dt > span.hot-search-item > span:nth-child({})".format(hot)).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.title)
        dl.refresh()
        number = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
        print(str(number))
        brand = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href > div.brand-info > a > h2").text
        print("商标名称:" + brand)
        info = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href > div.brand-info > div > ul").text
        print(str(info))

        get_screenshort(self.driver,"test_sbrs_2.png")
        print("热搜跳转正常,测试通过!")

    def test_csgg(self):
        """初审公告测试"""

        dl = DengLuPage(self.driver)
        time.sleep(2)
        self.driver.get("https://so.quandashi.com/search/notice/index")
        dl.refresh()
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
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
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        time.sleep(5)
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

    def test_jcjs(self):
        """交叉检索测试"""
        dl = DengLuPage(self.driver)
        self.driver.get("https://pre-so.quandashi.com/")
        dl.refresh_pre()
        time.sleep(2)
        brand = unicode()
        self.driver.find_element_by_name("key").send_keys(brand)
        self.driver.find_element_by_id("btnSearchkey").click()
        time.sleep(3)

        # html = self.driver.execute_script("return document.documentElement.outerHTML")
        # print(str(html))


        """交叉检索"""
        self.driver.find_element_by_class_name("cross-search").click()
        classify = random.randint(1,45)
        time.sleep(2)

        dl = self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({})".format(classify)).text
        print(str(dl))
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({})".format(classify)).click()
        time.sleep(2)

        zl = self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").text
        print(str(zl))
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        time.sleep(2)

        xl = self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").text
        print(str(xl))
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        time.sleep(2)

        # ol = self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").text
        # print(str(ol))
        # self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()


        info = self.driver.find_element_by_class_name("cross-range-list").text
        print(str(info).replace("\n"," "))

        self.driver.find_element_by_css_selector("#searchList > div.page-form.w-center > div.w_category_modal > div > div.btns > a").click()

        """已选条件"""

        select = self.driver.find_element_by_class_name("selected-category").text
        print(str(select).replace("\n"," "))


        result = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text
        print(result)
        time.sleep(2)
        if int(result) == 0:
            print("亲，未检测到您关注的商标，请换个词试试~ 不过您可以就~{}~提起商标申请哦".format(brand))
        else:
            # 搜索结果
            jg = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
            print(jg)
            # 第一个商标信息
            jg1 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href > div.brand-info > div > ul").text
            print(str(jg1).replace("\n", " "))

    def test_hot_trade(self):
        """热门商标出售测试"""
        dl = DengLuPage(self.driver)
        self.driver.get("https://so.quandashi.com/")
        dl.refresh()
        time.sleep(2)
        self.driver.find_element_by_name("key").send_keys(unicode())
        self.driver.find_element_by_id("btnSearchkey").click()
        time.sleep(5)

        trade = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-right > div > ul > li:nth-child(1) > div.hot-brand-detail").text
        print("热门商标信息:" + str(trade).replace("\n"," "))

        self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-right > div > ul > li:nth-child(1) > div.hot-brand-detail > a").click()
        get_screenshort(self.driver,"test_hot_trade.png")
        print("热门商标信息正常测试通过!")

    def test_try(self):
        """尝试注册测试"""
        dl = DengLuPage(self.driver)
        self.driver.get("https://so.quandashi.com/")
        dl.refresh()
        time.sleep(2)
        brand = unicode()
        self.driver.find_element_by_name("key").send_keys(brand)
        self.driver.find_element_by_id("btnSearchkey").click()
        time.sleep(3)

        result = self.driver.find_element_by_css_selector(
            "#searchList > div.page-content.w-center > div.page-content-left > div.search-top > i").text
        print(result)
        time.sleep(2)

        if int(result) == 0:
            print("亲，未检测到您关注的商标，请换个词试试~ 不过您可以就~{}~提起商标申请哦".format(brand))

            wsq = self.driver.find_element_by_css_selector(
                "#searchList > div.page-form.w-center > div.no-result-category > div.no-result-category-box > a:nth-child(1)").text
            print(str(wsq))
            self.driver.find_element_by_css_selector(
                "#searchList > div.page-form.w-center > div.no-result-category > div.no-result-category-box > a:nth-child(1)").click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            time.sleep(2)
            self.driver.set_window_size(1920, 1080)
            print(self.driver.current_url)
            get_screenshort(self.driver, "test_try.png")

        else:
            # 搜索结果
            jg = self.driver.find_element_by_css_selector(
                "#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
            print(jg)

            # 第一个商标信息
            jg1 = self.driver.find_element_by_css_selector(
                "#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href > div.brand-info > div > ul").text
            print(str(jg1).replace("\n", " "))
