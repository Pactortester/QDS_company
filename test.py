# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 10:29
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
# http://www.creditsd.gov.cn/creditsearch.listcreditsd.dhtml?page=1
# coding:utf-8

import re
import requests
import random
import numpy as np

"""爬取"""
for i in range(1,10):
    url = 'http://www.creditsd.gov.cn/creditsearch.listcreditsd.dhtml?page={}'.format(i)
    r = requests.get(url)
    r.encoding = 'gb2312'
    matchs = re.findall(r"<td>(.*)</td>", r.text)
    for link in matchs:
        print(link)



"""读取"""
f = open(r"G:\QDS_company\data\credit_code.txt")
line = f.readline()
data_list = []
while line:
    num = list(map(str,line.split()))
    data_list.append(num)
    line = f.readline()
f.close()
data_array = np.array(data_list)
print(str(random.choice(data_array)).replace("['","").replace("']",""))
