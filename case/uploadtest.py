# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 14:35
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: uploadtest.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
import os
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config.globalparam import driver_path
from utils.datachoice import credit_code
from utils.logincookie import DengLuPage
from utils.mytestcase import MyTestCase
from utils.random import unicode
from utils.screenshort import get_screenshort


class UpLoadTest(MyTestCase):

    """文件上传图形注册测试集"""

    def _hhr_order_pic(self):

        """合伙人商标注册_图形"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()
        time.sleep(2)

        """上传商标图片"""
        path = driver_path + "\\" + "Upload_files.exe"
        os.system(path)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-fcontent > div > textarea").send_keys("小鸡图片")

        print("商标图形:小鸡图片")

        time.sleep(5)
        self.driver.find_element_by_css_selector("#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别"""
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类!".format(suiji))
        time.sleep(3)

        for i in self.driver.find_elements_by_css_selector(
                "#personalCenter2-rightContainer > div > div.order-form-page > div > div.smartRegister-section > div.order-categories-calc > div.order-categories-total > span.span-total > strong > i"):
            print("总价:" + i.text)
            ii = i.text


        self.driver.execute_script("window.scrollBy(0,1000)")  # 滑动滚动条
        """申请人信息"""

        self.driver.find_element_by_css_selector("#selectOwnerType > label.label.fownertype.active").click()
        self.driver.find_element_by_css_selector("#overseastype > label.label.checked").click()
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.agentInfo-wrap > div > div > div > div > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "文思海辉技术有限公司{}".format(random.randint(1, 1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        print("申请人信息填写成功!")

        """客户联系人信息"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys(
            "dalao")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys(
            "15624992488")
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys(
            "1456470136@qq.com")

        print("联系人信息填写成功!")

        """订单改价"""

        self.driver.find_element_by_name("customPrice").clear()
        new_total = int(str(ii).replace(".00", "")) + 500
        self.driver.find_element_by_name("customPrice").send_keys(new_total)
        print("改价:增加500服务费!")

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()


        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > div.order-detail-fix > div > div.right.change-price > div.pay-btns > a:nth-child(2)").click()

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = int(str(o.text).replace(".00", ""))
        get_screenshort(self.driver,"test.png")

        time.sleep(2)
        self.assertEqual(oo, new_total)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver, "test_hhr_order_1.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_link_text("复制").click()

        print("订单已发送客户付款!")

        # 订单url校验

        self.driver.get(pay_url)
        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(2)
        order_number = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)").text
        order_time = self.driver.find_element_by_css_selector(
            "#table-contract > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)").text
        if order_time == '':
            self.assertEqual(1, 2, "付款链接异常请及时查看!")
        else:
            print("订单编号:" + order_number)

    def _znzz_pic(self):
        """智能注册_图形"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i


        self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()

        """上传商标图片"""
        path = driver_path + "\\" + "Upload_files.exe"
        os.system(path)

        print("商标图形:小鸡图片")
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()


        print("选择了第{}类商标分类!".format(suiji))

        print(1)
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()
        print(2)

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)


        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(random.randint(1,5))).click()
        time.sleep(2)

        # 添加社会信用代码
        self.driver.find_element_by_name("creditcode").send_keys(credit_code("credit_code.txt"))

        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys("03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_1.png")

        for i in self.driver.find_elements_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def _hwgs_pic(self):
        """海外高速_图形"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("海外商标注册|国际商标注册|商标注册流程|商标注册代理-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:" + a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.recommend-help > i").click()
        # body > div.recommend-help > i

        self.driver.find_element_by_css_selector("#selectBrandType > label:nth-child(2)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.brand-info-wrap.form-wrap.show3 > ul > li.brand-upload > div > div.brand-upload-wrap > div.shoudong-create > ul > li > div > div > div.photo-box.btnuploadtuyang > div").click()

        """上传商标图片"""
        path = driver_path + "\\" + "Upload_files.exe"
        os.system(path)

        print("商标图形:小鸡图片")

        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "#selectCategoryType > label:nth-child(2)").click()
        self.driver.execute_script("window.scrollBy(0,1200)")  # 滑动滚动条
        suiji = random.randint(2, 45)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()

        print("选择了第{}类商标分类!".format(suiji))

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap.brandinfo-wrap > div.register-pay > div > ul > li.row-step > a").click()

        try:
            self.driver.find_element(By.LINK_TEXT, "确认")
            a = True
        except:
            a = False
        if a is True:
            """不足10小项确认提交"""
            self.driver.find_element_by_link_text("确认").click()
        elif a is False:
            pass

        time.sleep(3)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.register-wrap div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_hwgs_1.png")
        for i in self.driver.find_elements_by_css_selector(
                "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.register-wrap > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()