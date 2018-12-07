import random
import re

import numpy as np
import requests

from config.globalparam import data_path


def xz(filename):

    data = np.loadtxt(data_path + "\\" + filename)

    return str(random.choice(data))



def credit_code():
    """读取数据"""
    f = open(data_path + "\\" + "credit_code.txt")
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