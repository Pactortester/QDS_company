import random
import time
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage


class SubjectTest(MyTestCase):
    """合伙专题测试集"""


    def test_hhrzt(self):
        """合伙人计划测试"""

        dl = DengLuPage(self.driver)

        self.driver.get("https://www.quandashi.com/zhuanti/hhr")
        dl.refresh()
        time.sleep(2)
        # self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li:nth-child(1) > a > img").click()
        # # 获取打开的多个窗口句柄
        # windows = self.driver.window_handles
        # # 切换到当前最新打开的窗口
        # self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("合伙人|合伙人计划|权大师", self.driver.title)
        print(self.driver.title)

        charge = random.randint(323, 10000)

        self.driver.find_element_by_css_selector("body > div.hhrzhuanti-wrap > div.section-6 > div.s-right > ul > li:nth-child(1) > dl > dd > input").send_keys(charge)
        print("客户收费:" + str(charge) + "元")

        income = self.driver.find_element_by_css_selector("body > div.hhrzhuanti-wrap > div.section-6 > div.s-right > ul > li.row2 > dl > dd > input").get_attribute("value")

        print("合伙人收益:" + str(income) + "元")
        print("合伙人专题页pass!")


    def test_navigation(self):
        """悬浮导航测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.public-fixrightbar > ul > li.list.list-ad").click()
        txt = self.driver.find_element_by_css_selector("body > div.public-fixrightbar > ul > li.list.list-ad").text
        print(txt)
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("首页", self.driver.title)
        print(self.driver.title)
        print(self.driver.current_url)

    def test_left_banner(self):
        """首页左侧banner"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li:nth-child(1) > a > img").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("智能商标注册-权大师", self.driver.title)
        print(self.driver.title)
        print(self.driver.current_url)
        print("首页左侧banner.url测试通过!")
