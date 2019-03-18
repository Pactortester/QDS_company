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

# coding:utf8
import   requests
import  json
from collections import Counter
from pyecharts import Pie
import hashlib
# 微信Url数据获取连接
Wxurl="https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r=1551517351463&seq=0&skey=@crypt_80cc7620_ac3680d314a5860438086e5d54cf177d"
headers = {
         'Cookie': 'cookie',
        'Host': 'wx.qq.com',
        'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
        }
#TODO  Province_City 使用到的数组集合
Province = []
Countcity=[]
#TODO  存储性别
sexs=[]
#TODO  存储图片
HeadImgUrls=[]
def SexFun(Sexrests):
    # 性别方法
    print("男%s" % Sexrests[1])
    print("女%s" % Sexrests[2])
    print("公众号%s" % Sexrests[0])
    pie = Pie("微信好友性别统计" , title_pos='center', width=1400, height=600)
    pie.add(
        "",
        ['男','女','未知'],
        [Sexrests[1],Sexrests[2],Sexrests[0]],
        radius=[40, 75],
        title='sex',
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
    pie.render('sex.html')
    print(Sexrests)
#TODO  Wechar_data  方法
def Wechar_data(Wxurl,headers):
    global  Province   # 转换为全局变量,假如不转换的话，会报错的
    global  Countcity
    global sexs
    global HeadImgUrls
    list_data = requests.get(Wxurl,headers=headers)
    list_data.encoding = "utf-8"
    print(list_data.text)
    dict1 = json.loads(list_data.text)
    print("%s: %s" % ("好友数" ,dict1["MemberCount"]))  #字典
    listdata=dict1["MemberList"]  # 集合
    #print(listdata)
    for  lists  in  range(0,dict1["MemberCount"]):  # 把全部用户的地址存储
        HeadImgUrls.append(listdata[lists]["HeadImgUrl"])
        sexs.append(listdata[lists]["Sex"])
        Province.append(listdata[lists]["Province"]+""+listdata[lists]["City"])
    rest=Counter(Province)   #这里是分组
    #print(rest)
    """
    Counter({'': 29, '湖南郴州': 21, '湖南长沙': 16, '广东深圳': 14, '广东中山': 9, '广东广州': 8, '北京朝阳': 7, '湖南娄底': 4, '湖南怀化': 4, '北京海淀': 3, '湖南益阳': 3, '上海浦东新区': 3, '安徽合肥': 2, '北京西城': 2, '广东佛山': 2, '广东湛江': 2, '湖南株洲': 2, '浙江杭州': 1, '北京东城': 1, '广东': 1, '四川德阳': 1, '辽宁丹东': 1, '河南三门峡': 1, '湖南张家界': 1, '广东肇庆': 1, '上海长宁': 1, '澳门路环岛': 1, '江苏': 1, '上海': 1, '湖南衡阳': 1, '河南南阳': 1, '湖南永州': 1, '北京': 1, 'North Shore': 1, '湖北恩施': 1, '湖南湘潭': 1, '湖南岳阳': 1, '湖南': 1, 'EnglandSheffield': 1, '湖南邵阳': 1, '湖北武汉': 1, '广东珠海': 1, 'Eastern': 1, '江西南昌': 1, 'SabahSemporna': 1, '四川成都': 1, '北京昌平': 1, '福建宁德': 1})
    """
    sets = set(Province)
    countProvin = list(sets)
    #print(countProvin)  #city
    '''    ['', '河南三门峡', '河南南阳', '北京', '广东肇庆', '广东中山', '上海长宁', '湖南长沙', '广东佛山', '福建宁德', '广东深圳', '湖南娄底', '辽宁丹东', '浙江杭州', '湖北恩施', 'North Shore', '湖南', '北京昌平', '上海浦东新区', '澳门路环岛', '湖南株洲', '湖南邵阳', 'SabahSemporna', '广东广州', '湖南张家界', '湖南衡阳', '湖南永州', '湖北武汉', '北京朝阳', '安徽合肥', '北京西城', '湖南岳阳', '广东', '北京东城', '江西南昌', '广东珠海', '四川德阳', '湖南郴州', '湖南益阳', 'EnglandSheffield', '四川成都', '广东湛江', '江苏', '湖南怀化', 'Eastern', '湖南湘潭', '上海', '北京海淀']'''
    #print(en(countProvin))48
    for  iii  in   range(0,len(countProvin)):
        #print(countProvin[iii])
        Countcity.append(rest[countProvin[iii]])
    #print(Countcity)  # num  list
    try:
        countProvin[0]="暂未填写地区"
    except   Exception:
        print("登录授权已过期")

    pie = Pie("微信好友用户统计：好友%s" %( +dict1["MemberCount"]), title_pos='center',width=1400,height=600)
    pie.add(
        "",
        countProvin,
        Countcity,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
    pie.render()

    #性别判断
    Sexrests = Counter(sexs)  # 这里是分组
    #让代码看上去简单一点使用方法封装
    SexFun(Sexrests)
    HeadimgFun(HeadImgUrls,headers)
def HeadimgFun(imgdata,headers):
    #print(imgdata[0])
    md = hashlib.md5()  # 构造一个md5
    for i in range(0,len(imgdata)):
        utllist="https://wx.qq.com"+imgdata[i]
        reqs = requests.get(utllist,headers=headers)
        reqs.encoding = "utf-8"
        md.update(imgdata[i].encode())
        imgname=md.hexdigest()+".jpg"
        with  open('./images/'+imgname, 'wb') as  f:
            f.write(reqs.content)


Wechar_data(Wxurl,headers)

demo