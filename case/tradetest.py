# coding=utf-8
import random
import time
from selenium.webdriver import ActionChains
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode, request_number, patent_name
from utils.screenshort import get_screenshort


class TradeTest(MyTestCase):
    """商标交易测试集"""

    def test_trade_1(self):
        """求购需求测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        trade = unicode()
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.brandSearchBox > div > div > input[type=\"text\"]").send_keys(trade)
        print(trade)
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.brandSearchBox > div > div > a").click()
        time.sleep(2)
        number = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3) > span").text
        print("为您找到" + str(number)+"个商标")
        time.sleep(1)
        if int(number) == 0:
            print("查无:" + str(trade) + "商标,发布求购需求!")
            self.driver.find_element_by_css_selector(
                "#app > div > div.brandMarketBox > div.brandSearchBox > p.postWant").click()
            fl = random.randint(1, 45)
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > div > ul > li:nth-child({})".format(fl)).click()
            print("选择" + str(fl) + "商标类别")

            jg = random.randint(2, 9)
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(jg)).click()
            structure = self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(jg)).text

            print("商标结构:" + str(structure))

            zs = random.randint(2, 6)

            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.wordNumBox.commonBox > li:nth-child({})".format(zs)).click()
            words = self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.wordNumBox.commonBox > li:nth-child({})".format(zs)).text

            print("商标字数:" + str(words))

            ys = random.randint(2, 7)

            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.priceBox.commonBox > li:nth-child({})".format(ys)).click()
            budget = self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.priceBox.commonBox > li:nth-child({})".format(ys)).text

            print("商标预算:" + str(budget))

            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(10) > input[type=\"text\"]").send_keys(unicode())
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(12) > input[type=\"text\"]").send_keys("15624992498")
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(14) > textarea").send_keys(
                time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
            get_screenshort(self.driver, "test_trade_1.png")

            self.driver.find_element_by_css_selector("#app > div > div.postNeedsBox > div > a").click()
            print("需求已发布!")

        else:
            print("pass")

    def test_trade_2(self):
        """购买商标测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        brand = random.randint(1,36)
        name = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > b".format(brand)).text
        price = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > i".format(brand)).text
        lb = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > span".format(brand)).text
        print("商标信息:" + str(name) + "_" + str(price) + "_" + str(lb))
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({})".format(brand)).click()
        print("选择购买第" + str(brand) + "个商标.")
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(5)
        name_1 = self.driver.find_element_by_css_selector("#app > div > div.brandDetailMsgBox > div.brandMsgBox > div.brandMsg > dl > dt").text
        print(name_1)
        self.assertIn(str(name_1),str(name))
        self.driver.find_element_by_css_selector("#app > div > div.brandDetailMsgBox > div.brandMsgBox > div.brandMsg > dl > dd:nth-child(9) > a:nth-child(2)").click()
        time.sleep(2)
        price_1 = self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.totalMoney > div > p > span").text

        print(price_1)
        # self.assertIn(price_1,price)
        info_1 = self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.totalMoney > div > p").text
        print(str(info_1))
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.userMsg > div > dl:nth-child(1) > dd > input[type=\"text\"]").send_keys(patent_name())
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.userMsg > div > dl:nth-child(2) > dd > input[type=\"text\"]").send_keys("15624992498")
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.userMsg > div > dl:nth-child(3) > dd > input[type=\"text\"]").clear()
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.userMsg > div > dl:nth-child(3) > dd > input[type=\"text\"]").send_keys("1456470138@qq.com")
        get_screenshort(self.driver,"test_trade_2.png")
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > div.totalMoney > div > a").click()
        time.sleep(2)

        # 二次切换窗口
        current_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)

        time.sleep(2)
        print(self.driver.current_url)

        info_2 = self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.orderMsgBox > dl > dt > b").text
        print("订单提交成功，应付金额：" + str(info_2))
        info_3 = self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.orderMsgBox > dl > dd").text
        print(info_3)
        self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.payMethod > a").click()

    def test_trade_3(self):
        """提交报价测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        brand = random.randint(1, 36)
        name = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > b".format(brand)).text
        price = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > i".format(brand)).text
        lb = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > span".format(brand)).text
        print("商标信息:" + str(name) + "_" + str(price) + "_" + str(lb))

        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(1)".format(brand)).click()

        self.driver.find_element_by_css_selector("#app > div > div:nth-child(6) > div > div > p:nth-child(1) > input[type=\"text\"]").send_keys(unicode())
        self.driver.find_element_by_css_selector(
            "#app > div > div:nth-child(6) > div > div > p:nth-child(2) > input[type=\"text\"]").send_keys("15624992422")
        price = random.randint(1,20000000)
        self.driver.find_element_by_css_selector(
            "#app > div > div:nth-child(6) > div > div > p:nth-child(3) > input[type=\"text\"]").send_keys(price)
        print("报价:" + str(price) + "元!")
        self.driver.find_element_by_css_selector("#app > div > div:nth-child(6) > div > p.subBtn > a").click()
        get_screenshort(self.driver,"test_trade_3.png")
        print("提交报价成功!")

    def test_trade_4(self):
        """点击收藏测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        brand = random.randint(1, 36)
        name = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > b".format(brand)).text
        price = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > i".format(brand)).text
        lb = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > span".format(brand)).text
        print("商标信息:" + str(name) + "_" + str(price) + "_" + str(lb))

        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(2)".format(brand)).click()

        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.favoriteEnter.favoAct").click()

        # 搜索已经收藏的商标
        self.driver.find_element_by_css_selector("#app > div > div > div.collectionFolderSwiper > div > div.searchCondition.clearfix > div.inputConditionBox.clearfix > div.brandName > input[type=\"text\"]").send_keys(name)

        self.driver.find_element_by_css_selector("#app > div > div > div.collectionFolderSwiper > div > div.operationBox > div > a:nth-child(4)").click()

        name_1 = self.driver.find_element_by_css_selector("#app > div > div > div.collectionFolderSwiper > ul > li > div.itemInner > div > b").text

        self.assertIn(name_1,name)

        print("商标收藏成功,测试通过!")

    def test_trade_5(self):
        """删除收藏测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.favoriteEnter.favoAct").click()
        brand = self.driver.find_element_by_css_selector("#app > div > div > div.collectionFolderSwiper > ul > li > div.itemInner > div > b").text
        print("商标名称:" + brand)
        self.driver.find_element_by_css_selector("#app > div > div > div.collectionFolderSwiper > ul > li > div.itemInner > div > p > a:nth-child(2)").click()
        alert = self.driver.switch_to.alert
        print("弹框信息:" + alert.text)
        alert.accept()

        print("收藏商标删除成功,测试通过!")

    def test_trade_6(self):
        """添加购物车测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        brand = random.randint(1, 36)
        name = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > b".format(brand)).text
        price = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > i".format(brand)).text
        lb = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > span".format(brand)).text
        print("商标信息:" + str(name) + "_" + str(price) + "_" + str(lb))

        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(3) > img".format(brand)).click()

        self.driver.find_element_by_css_selector(
            "#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter").click()
        time.sleep(3)

        # 商标
        name_1 = self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td:nth-child(3)").text
        print(name_1)

        self.assertIn(str(name_1), str(name))

        print("商标收藏成功,测试通过!")

    def test_trade_7(self):
        """删除购物车测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter").click()

        brand = self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td:nth-child(3)").text
        print("商标名称:" + brand)
        self.driver.find_element_by_css_selector("#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td:nth-child(8) > a").click()
        alert = self.driver.switch_to.alert
        print("弹框信息:" + alert.text)
        alert.accept()

        print("购物车商标删除成功,测试通过!")

    def test_trade_8(self):
        """推荐商标测试"""

        dl = DengLuPage(self.driver)
        self.driver.get("http://pre-brand-trade.quandashi.com/#/")
        time.sleep(1)
        dl.refresh_pre()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-left > p > a:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#app > div > div.purchaseDemandBox.clearfix > ul > li:nth-child(1) > p.recBrand > a > img").click()
        number = request_number()
        self.driver.find_element_by_css_selector("#inputBrandMsg > div > dl:nth-child(1) > dd > input").send_keys(number)
        print("申请号:" + number)
        self.driver.find_element_by_css_selector("#inputBrandMsg > div > dl:nth-child(2) > dd > input").send_keys(random.randint(1,20000000))
        name = patent_name()
        self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > div.inputName > dl > dd > input[type=\"text\"]").send_keys(name)
        print(name)
        self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > div.inputPhone > dl > dd > input[type=\"text\"]").send_keys("15624992498")

        self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > p > a").click()
        price = self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div.showPayCode > p.price").text
        print("￥1.00")
        self.assertIn(price,"￥1.00")
        print("推荐商标提交成功!")
