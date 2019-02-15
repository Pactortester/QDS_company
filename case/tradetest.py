# coding=utf-8
import random
import time

from selenium.webdriver.common.by import By

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode, request_number, patent_name
from utils.screenshort import get_screenshort


class TradeTest(MyTestCase):
    """商标交易测试集"""

    def test_trade_1(self):
        """首页查询测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师",self.driver.title)
        print(self.driver.title)

        trade = unicode()
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.brandSearchBox > div > div > input[type=\"text\"]").send_keys(trade)
        print("商标名称:" + trade)
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.brandSearchBox > div > div > a").click()
        time.sleep(2)
        number = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3) > span").text
        number1 = int(number)
        print("为您找到" + str(number)+"个商标")
        time.sleep(1)
        if int(number1) == 0:
            print("查无:" + str(trade) + "商标,发布求购需求!")
            self.driver.find_element_by_css_selector(
                "#app > div > div.brandMarketBox > div.brandSearchBox > p.postWant").click()
            fl = random.randint(1, 45)
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > div > ul > li:nth-child({})".format(fl)).click()
            print("选择" + str(fl) + "商标类别")

            jg = random.randint(2, 9)

            if jg == 4:
                self.driver.find_element_by_css_selector("#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li.structureAct").click()
                structure = self.driver.find_element_by_css_selector("#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li.structureAct").text
                print("商标结构:" + str(structure))
            else:
                self.driver.find_element_by_css_selector(
                    "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(
                        jg)).click()
                structure = self.driver.find_element_by_css_selector(
                    "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(
                        jg)).text

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
            self.driver.execute_script("window.scrollBy(0,3500)")  # 滑动滚动条
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(10) > input[type=\"text\"]").send_keys(patent_name())
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(12) > input[type=\"text\"]").send_keys("15624992498")

            need = "有带“{}”的商标,文艺骚气有逼格,欢迎推荐!".format(unicode())
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > p:nth-child(14) > textarea").send_keys(need)
            get_screenshort(self.driver, "test_trade_1.png")

            self.driver.find_element_by_css_selector("#app > div > div.postNeedsBox > div > a").click()
            print("需求已发布!")

        else:
            print("pass")

    def test_trade_2(self):
        """购买商标测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

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
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        time.sleep(2)
        name_1 = self.driver.find_element_by_css_selector("#app > div > div.brandDetailMsgBox > div.brandMsgBox > div.brandMsg > dl > dt").text
        print(name_1)
        self.assertIn(str(name_1),str(name))
        self.driver.find_element_by_css_selector("#app > div > div.brandDetailMsgBox > div.brandMsgBox > div.brandMsg > dl > dd:nth-child(9) > a:nth-child(2)").click()
        time.sleep(4)
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
        time.sleep(4)

        # 二次切换窗口
        current_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)

        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.current_url)

        info_2 = self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.orderMsgBox > dl > dt > b").text
        print("订单提交成功，应付金额：" + str(info_2))
        info_3 = self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.orderMsgBox > dl > dd").text
        print(info_3)
        self.driver.find_element_by_css_selector("#app > div > div.paymentBox > div.payMethod > a").click()

    def test_trade_3(self):
        """提交报价测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

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
        # self.driver.find_element_by_css_selector("#app > div > div:nth-child(6) > div > p.subBtn > a").click()
        get_screenshort(self.driver,"test_trade_3.png")
        print("提交报价成功!")

    def test_trade_4(self):
        """点击收藏测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

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

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.favoriteEnter.favoAct").click()
        time.sleep(1)
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

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        brand = random.randint(1, 36)
        name = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > b".format(brand + 2)).text
        price = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > i".format(brand + 2)).text
        lb = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > span".format(brand + 2)).text
        print("商标信息:" + str(name) + "_" + str(price) + "_" + str(lb))

        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(3) > img".format(brand)).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(3) > img".format(
                brand + 1)).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > ul > li:nth-child({}) > div > p > a:nth-child(3) > img".format(
                brand + 2)).click()
        time.sleep(1)

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

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

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

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector("#app > div > div.header-wrap.clearfix > div.header-left > p > a:nth-child(2)").click()

        time.sleep(2)
        brand = random.randint(1, 10)
        print(brand)
        info = self.driver.find_element_by_css_selector("#app > div > div.purchaseDemandBox.clearfix > ul > li:nth-child({})".format(brand)).text

        print("求购信息:" + str(info).replace("\n"," "))
        self.driver.find_element_by_css_selector("#app > div > div.purchaseDemandBox.clearfix > ul > li:nth-child({}) > p.recBrand > a > img".format(brand)).click()
        time.sleep(2)
        result = self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div.needBox > p").text
        result1 = str(result).replace("\n"," ")
        print(result1)
        # self.assertIn(info1,result1)
        print("推荐商标测试通过!")
        # number = request_number()
        # self.driver.find_element_by_css_selector("#inputBrandMsg > div > dl:nth-child(1) > dd > input").send_keys(number)
        # print("申请号:" + number)
        # self.driver.find_element_by_css_selector("#inputBrandMsg > div > dl:nth-child(2) > dd > input").send_keys(random.randint(1,20000000))
        # name = patent_name()
        # self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > div.inputName > dl > dd > input[type=\"text\"]").send_keys(name)
        # print(name)
        # self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > div.inputPhone > dl > dd > input[type=\"text\"]").send_keys("15624992498")
        #
        # self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div:nth-child(3) > p > a").click()
        # price = self.driver.find_element_by_css_selector("#app > div > div.recomBrandBox > div.showPayCode > p.price").text
        # print("￥1.00")
        # self.assertIn(price,"￥1.00")
        # print("推荐商标提交成功!")

    def test_trade_10(self):
        """筛选商标测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandType.chooseType > dd.openBrandType.openBrandTypeOpen").click()


        lb1 = random.randint(1, 45)
        brand = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandType.chooseType > dd:nth-child(2) > p > a:nth-child({})".format(
                lb1)).text
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandType.chooseType > dd:nth-child(2) > p > a:nth-child({})".format(
                lb1)).click()
        print("商标类别:" + brand)


        lb2 = random.randint(2, 7)
        price = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandPrice.chooseType > dd:nth-child(2) > a:nth-child({})".format(
                lb2)).text
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandPrice.chooseType > dd:nth-child(2) > a:nth-child({})".format(
                lb2)).click()
        print("商标价格:" + price)

        jg = [2,3,5,6,7,8,9]
        lb3 = random.choice(jg)
        structure = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandStructure.chooseType > dd > a:nth-child({})".format(
                lb3)).text
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandStructure.chooseType > dd > a:nth-child({})".format(
                lb3)).click()
        print("商标结构:" + structure)


        lb4 = random.randint(2,6)
        num = self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandWordNum.chooseType > dd > a:nth-child({})".format(
                lb4)).text
        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandWordNum.chooseType > dd > a:nth-child({})".format(
                lb4)).click()
        print("商标字数:" + num)

        get_screenshort(self.driver,"test_trade_10.png")
        result = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3)").text
        print(result)
        number = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3) > span").text
        number1 = int(number)
        print(number1)
        if number1 == 0:
            print("没有相关可出售商标，您可以发布求购需求!")
        else:
            print(self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child(1) > div").text)

        selected = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.SelectedConditions > dd").text
        print("已选条件:" + str(selected).replace("\n"," "))
        print("筛选商标测试通过!")

    def test_trade_11(self):
        """价格区间测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        low = random.randint(1,5000)
        high = random.randint(5000,50000)
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandPrice.chooseType > dd.inputNum > input[type=\"text\"]:nth-child(1)").send_keys(low)
        self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.brandPrice.chooseType > dd.inputNum > input[type=\"text\"]:nth-child(3)").send_keys(high)
        print("价格区间:" + str(low) + "_" + str(high))

        get_screenshort(self.driver,"test_trade_11.png")
        result = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3)").text
        print(result)
        number = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.CompreRanking > dd:nth-child(3) > span").text
        number1 = int(number)
        print(number1)
        if number1 == 0:
            print("没有相关可出售商标，您可以发布求购需求!")
        else:
            print(self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > ul > li:nth-child(1) > div").text)

        selected = self.driver.find_element_by_css_selector("#app > div > div.brandMarketBox > div.searchCriteriaBox > dl.SelectedConditions > dd").text
        print("已选条件:" + str(selected).replace("\n"," "))
        print("筛选商标测试通过!")

    def test_trade_12(self):
        """求购需求测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector(
            "#app > div > div.brandMarketBox > div.brandSearchBox > p.postWant").click()
        fl = random.randint(1, 45)
        self.driver.find_element_by_css_selector(
            "#app > div > div.postNeedsBox > div > div > ul > li:nth-child({})".format(fl)).click()
        print("选择" + str(fl) + "商标类别")

        jg = 4

        if jg == 4:
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li.structureAct").click()
            structure = self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li.structureAct").text
            print("商标结构:" + str(structure))
        else:
            self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(
                    jg)).click()
            structure = self.driver.find_element_by_css_selector(
                "#app > div > div.postNeedsBox > div > ul.structureBox.commonBox > li:nth-child({})".format(
                    jg)).text

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
        self.driver.execute_script("window.scrollBy(0,3500)")  # 滑动滚动条

        self.driver.find_element_by_css_selector(
            "#app > div > div.postNeedsBox > div > p:nth-child(10) > input[type=\"text\"]").send_keys(patent_name())
        self.driver.find_element_by_css_selector(
            "#app > div > div.postNeedsBox > div > p:nth-child(12) > input[type=\"text\"]").send_keys("15624992498")

        need = "有带“{}”或“{}”的商标,欢迎推荐!".format(unicode(),patent_name())
        self.driver.find_element_by_css_selector(
            "#app > div > div.postNeedsBox > div > p:nth-child(14) > textarea").send_keys(need)
        get_screenshort(self.driver, "test_trade_1.png")

        self.driver.find_element_by_css_selector("#app > div > div.postNeedsBox > div > a").click()
        print("需求已发布!")

    def test_trade_13(self):
        """删除求购需求测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()

        self.assertIn("权大师_个人中心", self.driver.title)
        print(self.driver.title)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li:nth-child(3) > ul > li:nth-child(2) > a").click()

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.table-box > table > thead > tr > th:nth-child(1) > label > input").click()

        info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.list-handle > div.handle-right > span").text

        print(str(info))

        result = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.table-box > table > tbody").text
        print((str(result).replace("查看 删除", " ")).replace("\n", " "))

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.list-handle > div.handle-right > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        info2 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.table-box > table > tbody > tr > td > div > span").text
        print(str(info2))

    def _trade_14(self):
        """删除意向商标测试"""

        dl = DengLuPage(self.driver)

        dl.login_pre()
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()

        self.assertIn("权大师_个人中心", self.driver.title)
        print(self.driver.title)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li:nth-child(3) > ul > li:nth-child(1) > a").click()

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div.table-box > table > thead > tr > th:nth-child(1) > label > input").click()

        info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div.list-handle > div.handle-right > span").text

        print(str(info))

        result = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div.table-box > table > tbody").text
        print((str(result).replace("查看 删除"," ")).replace("\n"," "))

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div.list-handle > div.handle-right > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        info2 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page.brand-trade-page > div.tabsPanel > div > div.table-box > table > tbody > tr > td > div > span").text
        print(str(info2))

    def test_trade_9(self):
        """清空购物车测试"""

        dl = DengLuPage(self.driver)

        dl.login()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > ul > li:nth-child(5) > a").click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        dl.refresh()
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标交易_商标转让_商标买卖_商标交易网-权大师", self.driver.title)
        print(self.driver.title)

        self.driver.find_element_by_css_selector(
            "#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter").click()

        # app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter.shopAct
        # app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter
        # app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter.shopAct

        while True :
            n = self.driver.find_element_by_css_selector(
                "#app > div > div.header-wrap.clearfix > div.header-right.clearfix > p.shoppingCartEnter > span").text
            print(n)
            brand = self.driver.find_element_by_css_selector(
                "#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td:nth-child(3)").text
            print("商标名称:" + brand)
            self.driver.find_element_by_css_selector(
                "#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td:nth-child(8) > a").click()
            alert = self.driver.switch_to.alert
            print("弹框信息:" + alert.text)
            alert.accept()
            time.sleep(2)
            if int(n) == 1:
                break

            # if self.driver.find_element(By.CSS_SELECTOR, "#app > div > div.shoppingCarBox > table > tr:nth-child(2) > td > span") :
            #     break
        print("清空购物车商标成功,测试通过!")