import re
import time

import requests

from utils.logincookie import DengLuPage
from utils.mytestcase import MyTestCase



class WebSiTest(MyTestCase):
    """网站地图测试集"""
    def test_site(self):

        """网站地图测试"""

        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(2)

        """点击关闭商标广告"""
        # self.driver.find_element_by_css_selector("body > div.festival-modal-bg > a.close").click()

        self.driver.find_element_by_css_selector("body > div.footer-wrap > div > ul.items-2 > li:nth-child(7) > a").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print("获取本页所有链接:")
        # url = 'https://pre-www.quandashi.com/site-map/index'
        # r = requests.get(url)
        # r.encoding = 'gb2312'
        #
        # # 利用 re （太黄太暴力！）
        # matchs = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", r.text)
        # for link in matchs:
        #     print(link)
        time.sleep(2)
        for link in self.driver.find_elements_by_tag_name("a"):
            print(str(link.get_attribute("href")).replace("javascript:;","").replace("javascript:void(0)","").replace("None",""))