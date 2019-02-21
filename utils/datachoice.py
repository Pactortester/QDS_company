import random
import re
import time

import numpy as np
import requests

from config.globalparam import data_path


def xz(filename):

    data = np.loadtxt(data_path + "\\" + filename)

    return str(random.choice(data))



def credit_code(filename):
    """读取数据"""
    f = open(data_path + "\\" + filename)
    line = f.readline()
    data_list = []
    while line:
        num = list(map(str, line.split()))
        data_list.append(num)
        line = f.readline()
    f.close()
    data_array = np.array(data_list)

    return str(random.choice(data_array)).replace("['", "").replace("']", "")



def spider():
    """爬取数据"""
    for i in range(1, 2):
        url = 'http://www.creditsd.gov.cn/creditsearch.listcreditsd.dhtml?page={}'.format(i)
        r = requests.get(url)
        r.encoding = 'gb2312'
        match = re.findall(r"<td>(.*)</td>", r.text)
        for link in match:
            print(link)


def nice(list_name):
    """尼斯分类去重"""

    # list_name 为获取的text文字

    s_1 = re.findall(r"\d+", list_name)
    s_2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
           '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
           '37', '38', '39', '40', '41', '42', '43', '44', '45']
    # s_2中有而s_1中没有的
    return random.choice(list(set(s_2).difference(set(s_1))))


def check_url(self,url):
    """分享url有效性校验"""
    self.driver.get(url)
    print(self.driver.title)
    time.sleep(2)
    order_number = self.driver.find_element_by_css_selector(
        "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(2) > td.pay-platform-charge").text
    order_charge = self.driver.find_element_by_css_selector(
        "body > div > section.section-applybaseinfo.pay-info.pay-infoall > ul > table > tbody > tr:nth-child(3) > td.pay-platform-charge").text
    if order_charge == '':
        self.assertEqual(1, 2, "h5链接异常请及时查看!")
    else:
        print("订单编号:" + order_number)
