import random
import re
import time

from selenium.webdriver import ActionChains
from utils.random import unicode
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.screenshort import get_screenshort


class IndexTest(MyTestCase):
    """首页跳转测试集"""

    def test_sb2(self):
        """商标二级页测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-hotservice > div > dl:nth-child(2) > dt > a.more").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("商标注册|商标申请|商标免费查询-权大师", self.driver.title)
        print(self.driver.title)
        get_screenshort(self.driver,"test_sb2.png")

    def test_bq2(self):
        """版权二级页测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-hotservice > div > dl:nth-child(4) > dt > a.more").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("版权登记|版权登记流程|版权变更|版权转让-权大师", self.driver.title)
        print(self.driver.title)
        get_screenshort(self.driver,"test_bq2.png")

    def test_zl2(self):
        """专利二级页测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-hotservice > div > dl.body2 > dt > a.more").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("专利查询|国家专利查询|专利申请|实用新型专利-权大师", self.driver.title)
        print(self.driver.title)
        get_screenshort(self.driver,"test_zl2.png")

    def test_classify_1(self):
        """商品分类搜索测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector("#section-tools > div > ul > li:nth-child(3)")).perform()

        time.sleep(2)
        ActionChains(self.driver).release()
        self.driver.find_element_by_link_text("立即使用").click()
        time.sleep(2)
        self.assertIn("商品分类_商标类似商品和服务区分表基于尼斯分类第十版2016", self.driver.title)
        print(self.driver.title)
        dl.refresh()
        brand = unicode()
        self.driver.find_element_by_css_selector("#niceList > div.page-search.w-center > div > input").send_keys(brand)
        print("商品关键词:" + brand)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#search").click()
        get_screenshort(self.driver,"test_classify_1.png")

    def test_classify_2(self):
        """商品分类点击测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector("#section-tools > div > ul > li:nth-child(3)")).perform()

        time.sleep(2)
        ActionChains(self.driver).release()
        self.driver.find_element_by_link_text("立即使用").click()
        time.sleep(2)
        self.assertIn("商品分类_商标类似商品和服务区分表基于尼斯分类第十版2016", self.driver.title)
        print(self.driver.title)

        num = random.randint(1,45)

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_css_selector("#niceList > div.page-content.w-center > ul > li:nth-child({})".format(num))).perform()


        mc = self.driver.find_element_by_css_selector("#niceList > div.page-content.w-center > ul > li:nth-child({}) > div.first-name".format(num)).text

        print("选择了第{}类".format(num) + "_" + mc)

        self.driver.find_element_by_css_selector("#niceList > div.page-content.w-center > ul > li:nth-child({}) > div.first-intro > div > a".format(num)).click()

        time.sleep(2)
        ActionChains(self.driver).release()

        self.assertIn("商品分类详情_商标类似商品和服务区分表基于尼斯分类第十版2016", self.driver.title)
        print(self.driver.title)
        print(self.driver.current_url)

        lb = self.driver.find_element_by_css_selector("#niceDetail > div.page-content.w-center > div > div.nice-right > div.nice-first-info.open > h2").text

        print(lb)

        number = re.sub("\D", "", lb)

        print(number)

        self.assertIn(str(num),str(number))

        print("商标类别一致测试通过！")

    def test_register(self):

        """智能注册系统测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,1500)")  # 滑动滚动条

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector("#section-tools > div > ul > li.active > a")).perform()

        time.sleep(2)
        ActionChains(self.driver).release()
        self.driver.find_element_by_link_text("立即使用").click()
        time.sleep(2)
        self.assertIn("智能商标注册-权大师", self.driver.title)
        print(self.driver.title)
        print(self.driver.current_url)

    def test_know(self):

        """权知道测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,3500)")  # 滑动滚动条
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-news > div > ul > li.col-know > div > a").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("商标注册常识_专业的商标业务知识分享平台_权大师", self.driver.title)
        print(self.driver.title)

    def test_perspective(self):

        """行业透视测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,3500)")  # 滑动滚动条
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-news > div > ul > li:nth-child(1) > div.row2 > a").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("更前沿的商标,专利,版权资讯,更快更准确的把握行业信息_权大师", self.driver.title)
        print(self.driver.title)

    def test_information(self):

        """权资讯测试"""
        dl = DengLuPage(self.driver)

        dl.login()
        time.sleep(1)

        self.driver.execute_script("window.scrollBy(0,3500)")  # 滑动滚动条
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-news > div > ul > li.col-industry.col-information > div.row2 > a").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.assertIn("更前沿的商标,专利,版权资讯,更快更准确的把握行业信息_权大师", self.driver.title)
        print(self.driver.title)

    def test_data(self):
        """数据搜索测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        tip = self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li.col-2 > a > h3").text
        data = self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li.col-2 > a > div.row2 > strong").text
        user = self.driver.find_element_by_css_selector("body > div.section-hotservice > ul > li.col-2 > a > div.row3 > strong").text

        print(str(tip))
        print("数据搜索:" + str(data))
        print("服务用户:" + str(user))
