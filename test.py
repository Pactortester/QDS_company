# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 10:29
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
# http://www.creditsd.gov.cn/creditsearch.listcreditsd.dhtml?page=1
# coding:utf-8

# import re
# import requests
# import random
# import numpy as np
#
# """爬取"""
# for i in range(1,10):
#     url = 'http://www.creditsd.gov.cn/creditsearch.listcreditsd.dhtml?page={}'.format(i)
#     r = requests.get(url)
#     r.encoding = 'gb2312'
#     matchs = re.findall(r"<td>(.*)</td>", r.text)
#     for link in matchs:
#         print(link)
#
#
#
# """读取"""
# f = open(r"G:\QDS_company\data\credit_code.txt")
# line = f.readline()
# data_list = []
# while line:
#     num = list(map(str,line.split()))
#     data_list.append(num)
#     line = f.readline()
# f.close()
# data_array = np.array(data_list)
# print(str(random.choice(data_array)).replace("['","").replace("']",""))
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from time import sleep
#
# option = webdriver.ChromeOptions()
#
# option.add_argument('disable-infobars')
#
#
#
# driver = webdriver.Chrome(chrome_options=option)
# # driver.get("https://www.helloweba.com/demo/2017/unlock/")
# driver.get("https://login.zhipin.com/?ka=header-login")
# # 定位第一个滑块
# time.sleep(3)
# dragger = driver.find_element_by_class_name("nc_iconfont btn_slide")[0]
#
# action = ActionChains(driver)
# # 通过click_and_hold()方法对滑块按下鼠标左键
# action.click_and_hold(dragger).perform()  # 鼠标左键按下不放
#
# for index in range(200):
#     try:
#         # 接下来就是通过for循环动滑块的位置，
#         # move_by_offset()方法:第一个参数是X轴，
#         # 第二个参数是Y轴，单位为像素。因为是平行移动，
#         # 所以Y设置为0，X每次移动两2个像素。
#         action.move_by_offset(2, 0).perform() # 平行移动鼠标
#     except UnexpectedAlertPresentException:
#         break   # 当解锁成功后会抛UnexpectedAlertPresentException异常，捕捉后跳出循环。
#     action.reset_actions()  # 清除之前的action
#     sleep(0.1)  # 等待停顿时间
#
# # 打印警告框提示
# success_text = driver.switch_to.alert.text
# print(success_text)
# sleep(3)
# driver.quit()


print("hello world!")