
import time
from utils.random import unicode


from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.screenshort import get_screenshort


class MfSbTest(MyTestCase):
    """商标搜索查询测试集"""

    def test_sbss(self):
        """商标搜索"""

        dl = DengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
        #     "#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > h3 > a")).perform()
        # ActionChains(self.driver).release()
        # self.driver.find_element_by_css_selector("#com-navbar > div > div.drop-nav > div > ul > li:nth-child(1) > div > dl:nth-child(1) > dd > a:nth-child(1)").click()
        # time.sleep(2)
        #
        # # 获取打开的多个窗口句柄
        # windows = self.driver.window_handles
        # # 切换到当前最新打开的窗口
        # self.driver.switch_to.window(windows[-1])
        # self.assertIn("注册商标查询_中国商标查询_权大师官网",self.driver.title)
        # print(self.driver.title)
        #
        # self.driver.add_cookie({'name': 'QDS_COOKIE',
        #                         'value': 'ab63c857c28ff94e241a578ecd1994ac520eece6',  # 一周有效期  2018-7-9_10-46
        #                         'Domain': '.quandashi.com'})
        #
        # self.driver.refresh()

        # self.driver.find_element_by_css_selector("#qds-searchkey").send_keys("测试")
        self.driver.find_element_by_css_selector("#serch-word").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("注册商标查询_中国商标查询_权大师官网", self.driver.title)
        print(self.driver.title)
        dl.refresh()
        ss=unicode()
        print("搜索商标名称："+ss)
        self.driver.find_element_by_css_selector("body > div.brandSearch2-page > div > div.search > div.searchPanel.clearfix > input.input.search-text").send_keys("{}".format(ss))
        self.driver.find_element_by_css_selector("#btnSearchkey").click()

        time.sleep(4)



        print(self.driver.title)

        get_screenshort(self.driver, "test_sbss.png")

        print("商标搜索测试通过")
