# coding=utf-8
import random
import time
from selenium.webdriver.common.by import By
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class HhrTest(MyTestCase):

    """合伙中心测试集"""

    def test_partner_modify(self):
        """商标订单修改"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)

        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()

        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > p:nth-child(1)").text)
        # 查看详情
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(9) > div.td-handle > a.info").click()
        time.sleep(3)
        """修改商标名字"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("1")
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功!")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条

        suiji = random.randint(2, 46)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        time.sleep(2)

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()
        print("尼斯分类修改为第{}类!".format(suiji-1))
        time.sleep(1)

        """申请人信息"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a:nth-child(2)").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("田伟")
        self.driver.find_element_by_css_selector("#geren-idCard").clear()
        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906311532")
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功!")
        time.sleep(4)

        """订单联系人"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(7) > div > h2 > a").click()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys("大西瓜")
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys("m15624992422@163.com")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()

        print("订单联系人修改成功!")
        time.sleep(1)
        get_screenshort(self.driver,"test_partner_modify.png")
        print("订单修改测试通过!")

    def test_hhr_order(self):

        """合伙人商标注册"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()

        print("商标名称填写成功!")

        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别"""
        suiji = random.randint(1,46)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类".format(suiji))

        for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
            print("总价:"+i.text)
            ii = i.text

        """申请人信息"""
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/table/thead/tr[1]/td[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"overseastype\"]/label[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/div/div/div/table[1]/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys("文思海辉技术有限公司{}".format(random.randint(1,1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        print("申请人信息填写成功!")


        """客户联系人信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys("15624992488")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys("1456470136@qq.com")

        print("联系人信息填写成功!")


        """订单备注"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S")+"测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()


        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a:nth-child(2)").click()

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        time.sleep(2)
        self.assertIn(oo,ii)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver,"test_hhr_order.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap > div.paying-sk-ewm > div.link > ul > li:nth-child(2) > a").click()

        print("订单已发送客户付款!")

    def test_hhr_historical_1(self):

        """合伙人历史订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()

        print("商标名称填写成功!")

        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > h3 > div > div > a").click()
        time.sleep(2)
        history_number = random.randint(2,10)
        info = self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)



        for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
            print("总价:"+i.text)
            ii = i.text

        """申请人信息"""
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/table/thead/tr[1]/td[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"overseastype\"]/label[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/div/div/div/table[1]/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys("文思海辉技术有限公司{}".format(random.randint(1,1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        print("申请人信息填写成功!")


        """客户联系人信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys("15624992488")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys("1456470136@qq.com")

        print("联系人信息填写成功!")


        """订单备注"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S")+"测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()


        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a:nth-child(2)").click()

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        time.sleep(2)
        self.assertIn(oo,ii)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver,"test_hhr_historical_1.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap > div.paying-sk-ewm > div.link > ul > li:nth-child(2) > a").click()

        print("订单已发送客户付款!")

    def test_hhr_historical_2(self):

        """合伙人历史订单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("商标注册").click()

        """填写商标信息"""

        self.driver.find_element_by_css_selector("#selectBrandType > label.label.checked").click()
        ss = unicode()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-name > td.td-content > input").send_keys("{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(1) > div.brandInfo-wrap > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()

        print("商标名称填写成功!")

        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > h3 > div > div > a").click()
        time.sleep(2)
        info = self.driver.find_element_by_css_selector("#history_order > li.active > h2").text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)



        for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
            print("总价:"+i.text)
            ii = i.text

        """申请人信息"""
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/table/thead/tr[1]/td[2]/a[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"overseastype\"]/label[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div/div[3]/div/div/div/div/table[1]/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys("文思海辉技术有限公司{}".format(random.randint(1,1000)))
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"companylistrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        time.sleep(1)

        print("申请人信息填写成功!")


        """客户联系人信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(1) > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(2) > input").send_keys("15624992488")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.contact-box > ul > li:nth-child(3) > input").send_keys("1456470136@qq.com")

        print("联系人信息填写成功!")


        """订单备注"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.message-box > ul > li > textarea").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S")+"测试订单")

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a.mybtn.mybtn-inverse.mybtn-lg.saveAll").click()


        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div:nth-child(7) > div > a:nth-child(2)").click()

        time.sleep(2)

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        time.sleep(2)
        self.assertIn(oo,ii)

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()

        print("价格一致")

        print("合伙人订单下单成功!")

        get_screenshort(self.driver,"test_hhr_historical_2.png")

        pay_url = self.driver.find_element_by_class_name("pay_url").get_attribute("value")
        print("订单链接:" + pay_url)

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap > div.paying-sk-ewm > div.link > ul > li:nth-child(2) > a").click()

        print("订单已发送客户付款!")

    def test_channel(self):

        """渠道下单单个商标注册"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("渠道下单").click()

        """填写渠道账号"""
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[2]/div[1]/dl/dt/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[2]/div[1]/dl/dt/input").send_keys("15122311450")
        self.driver.find_element_by_xpath("//*[@id=\"inquirer\"]").clear()
        self.driver.find_element_by_xpath("//*[@id=\"inquirer\"]").send_keys("15624992422")



        """填写商标信息"""

        self.driver.find_element_by_xpath("//*[@id=\"selectBrandType\"]/label[1]").click()
        ss = unicode()
        self.driver.find_element_by_name("brandName").send_keys("{}".format(ss))
        self.driver.find_element_by_xpath("//*[@id=\"create-tuyang\"]/label[2]").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[2]/div[3]/ul/li/div[2]/a").click()
        time.sleep(2)
        print("商标名称:{}".format(ss))
        print("商标名称填写成功!")

        self.driver.execute_script("window.scrollBy(0,500)")  # 滑动滚动条

        """商标类别"""
        suiji = random.randint(1,46)
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[5]/td[2]/a[2]").click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类".format(suiji))

        # for i in self.driver.find_elements_by_css_selector("#personalCenter2-rightContainer > div > div.order-form-page > div > div.order-detail-box.order-categories > div.order-categories-total > span.span-total > strong > i"):
        #     print("总价:"+i.text)
        #     ii=i.text

        """申请人信息"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.smartRegister-page.smartRegister-page-source2.smartRegister-page-personal > div:nth-child(5) > div.agentInfo-wrap.agentInfo-wrap-in > div > table > thead > tr > td.td-content > a.btn-choice.fownertype.active").click()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[4]/div[1]/div/table/tbody[1]/tr[1]/td[2]/dl/dt/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[4]/div[1]/div/table/tbody[1]/tr[1]/td[2]/dl/dt/input").send_keys(unicode())
        self.driver.find_element_by_xpath("//*[@id=\"ssq\"]").click()
        self.driver.find_element_by_xpath("//*[@id=\"myadministrative\"]/div/div[2]/div[1]/dl[1]/dd/span[1]").click()
        self.driver.find_element_by_xpath("//*[@id=\"myadministrative\"]/div/div[2]/div[2]/dl[2]/dd/span[1]").click()
        self.driver.find_element_by_name("fcontactName").clear()
        self.driver.find_element_by_name("fcontactName").send_keys("蔡妍妍")
        self.driver.find_element_by_name("fcontactTel").clear()
        self.driver.find_element_by_name("fcontactTel").send_keys("17801188215")
        self.driver.find_element_by_name("ftelephone").send_keys("4001005678")
        self.driver.find_element_by_name("fcontactMail").send_keys("m15624992422@qq.com")
        print("申请人信息填写成功!")

        get_screenshort(self.driver, "test_channel.png")
        for o in self.driver.find_elements_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div/div[1]/div[5]/div/ul/li[3]/em/i"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        # self.assertIn(oo,ii)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.section8 > div > a").click()

    def test_full_business_1(self):

        """合伙人全业务测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("其他业务").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(1) > input[type=\"text\"]").send_keys(unicode())
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(2) > input[type=\"text\"]").send_keys("15624992498")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(3) > input[type=\"text\"]").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > input").click()
        time.sleep(2)
        lx = random.randint(2,4)
        # lx = 2
        yw = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > dl > dd:nth-child({})".format(lx)).text
        print(yw)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > input").click()
        time.sleep(2)
        xm = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > dl > dd:nth-child(1)").text
        print(xm)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > dl > dd:nth-child(1)").click()
        time.sleep(2)

        print("业务需求:"+yw + "_" + xm)
        price = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(7) > div > input[type=\"text\"]").get_attribute("value")
        print("订单价格:" + price)

        income = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(8) > strong > span").text
        print("收益预估:" + str(income))

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(9) > div > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver,"test_full_business_1.png")
        self.driver.find_element_by_css_selector("#saveOrder").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        total = self.driver.find_element_by_css_selector("#total-price").text
        print("订单提交成功，应付金额:" + total)
        self.assertIn(price,total)
        print("价格一致！")

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()
        order_url = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute("value")

        print("订单链接:"+order_url)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()

        print("订单已发送客户付款!")

    def test_full_business_2(self):

        """收益预估测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_link_text("其他业务").click()
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(1) > input[type=\"text\"]").send_keys(unicode())
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(2) > input[type=\"text\"]").send_keys("15624992498")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(3) > input[type=\"text\"]").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > input").click()
        time.sleep(2)
        lx = random.randint(2,4)
        # lx = 2
        yw = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > dl > dd:nth-child({})".format(lx)).text
        print(yw)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(4) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > input").click()
        time.sleep(2)
        xm = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > dl > dd:nth-child(1)").text
        print(xm)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(5) > div > dl > dd:nth-child(1)").click()
        time.sleep(2)
        print("业务需求:"+yw + "_" + xm)

        """3次点击"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > a.input-add").click()
        count_1 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > input[type=\"text\"]").get_attribute("value")
        print("订单数量:" + count_1)
        price_1 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(7) > div > input[type=\"text\"]").get_attribute("value")
        print("订单价格:" + price_1)

        income_1 = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(8) > strong > span").text
        print("收益预估:" + str(income_1))
        time.sleep(3)


        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > a.input-add").click()
        time.sleep(2)
        count_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > input[type=\"text\"]").get_attribute(
            "value")
        print("订单数量:" + count_2)
        price_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(7) > div > input[type=\"text\"]").get_attribute(
            "value")
        print("订单价格:" + price_2)
        income_2 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(8) > strong > span").text
        print("收益预估:" + str(income_2))
        time.sleep(3)


        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > a.input-add").click()
        time.sleep(2)
        count_3 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(6) > div > input[type=\"text\"]").get_attribute(
            "value")
        print("订单数量:" + count_3)
        price_3 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(7) > div > input[type=\"text\"]").get_attribute(
            "value")
        print("订单价格:" + price_3)

        income_3 = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(8) > strong > span").text
        print("收益预估:" + str(income_3))
        get_screenshort(self.driver,"test_full_business_2.png")

    def test_calc_1(self):

        """全业务计算器测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.home-page.userInfo > div.article1.home-page-top.clearfix > div.article-bottom-link > ul > li.income_calc > a > img").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > input").click()
        lx = random.randint(1, 3)
        yw = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(lx)).text
        print("业务类型:" + str(yw))
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").text

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").click()
        print("服务项目:" + str(xm))

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.calculate").click()
        time.sleep(2)
        income = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(6) > strong").text

        print("您的收益:" + str(income))

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.button-white.income_detail_btn").click()
        time.sleep(2)


        num = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(4) > td.td-content.incomeNum").text
        print("案件数量:" + str(num))
        price = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(3) > td.td-content.serviceCharge").text
        print("案件服务费:" + str(price))
        official = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(5) > td.td-content.officialCharge").text
        print("案件官费:" + str(official))


        lastincome = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-detail-box > div.income-detail-bottom > span > strong").text
        print("最后收益:" + str(lastincome))

        get_screenshort(self.driver,"test_calc_1.png")

        self.assertIn(str(income),str(lastincome))

        print("收益一致,测试通过!")

    def test_calc_2(self):

        """右侧计算器测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.public-fixrightbar > ul > li.list.fixright-calc.income_calc").click()

        time.sleep(2)
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > input").click()
        lx = random.randint(1, 3)
        yw = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(lx)).text
        print("业务类型:" + str(yw))
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(1) > div > dl > dd:nth-child({})".format(lx)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > input").click()
        xm = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").text

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(2) > div > dl > dd:nth-child(2)").click()
        print("服务项目:" + str(xm))

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.calculate").click()
        time.sleep(2)
        income = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-body > form > ul > li:nth-child(6) > strong").text

        print("您的收益:" + str(income))

        self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-calc-box > div.modal-button > a.button.button-white.income_detail_btn").click()
        time.sleep(2)


        num = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(4) > td.td-content.incomeNum").text
        print("案件数量:" + str(num))
        price = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(3) > td.td-content.serviceCharge").text
        print("案件服务费:" + str(price))
        official = self.driver.find_element_by_css_selector(
            "#calculateModal > div > div.step.income-detail-box > div.modal-body > table > tbody > tr:nth-child(5) > td.td-content.officialCharge").text
        print("案件官费:" + str(official))


        lastincome = self.driver.find_element_by_css_selector("#calculateModal > div > div.step.income-detail-box > div.income-detail-bottom > span > strong").text
        print("最后收益:" + str(lastincome))

        get_screenshort(self.driver,"test_calc_2.png")

        self.assertIn(str(income),str(lastincome))

        print("收益一致,测试通过!")

    def test_partner_clue_1(self):

        """合伙人认领线索"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()


        try:
            self.driver.find_element(By.CSS_SELECTOR,"#personalCenter2-rightContainer > div.nav > a")
            a = True
        except:
            a = False
        if a is True:
            print("当前无线索,点击申请!")
            self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.nav > a").click()
            time.sleep(2)
            clue = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2)").text
            print(str(clue).replace("\n", " "))
            self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()  # tr-a claim_clue
        elif a is False:
            print("线索存在!")
            time.sleep(2)
            clue = self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2)").text
            print(str(clue).replace("\n"," "))
            self.driver.find_element_by_css_selector(
                "#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()
        get_screenshort(self.driver,"test_partner_clue_1.png")

    def test_partner_clue_2(self):

        """合伙人线索下单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()

        """已认领 第一条线索信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.partner > a.not_select").click()
        info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2)").text
        print("线索详情:" + (str(info).replace("\n" ," ")).replace("查看详情",""))

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()

        """切换窗口打开详情"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)

        # """关掉时间提示"""
        # self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()
        get_screenshort(self.driver,"test_partner_clue_2.png")

        """点击下单"""
        self.driver.find_element_by_css_selector("#bt-a > a.a-two.a-colour").click()
        time.sleep(2)

        """判断客户邮箱是否为空"""
        email = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > form > ul > li:nth-child(3) > input[type=\"text\"]").get_attribute("value")
        if email == "无":
            self.driver.find_element_by_name("email").clear()
            self.driver.find_element_by_name("email").send_keys("test@quandashi.com")
        else:
            print("客户邮箱:" + self.driver.find_element_by_name("email").get_attribute("value"))
            pass
        price = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(7) > div > input[type=\"text\"]").get_attribute(
            "value")
        print("订单价格:" + price)

        income = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(8) > strong > span").text
        print("收益预估:" + str(income))

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > form > ul > li:nth-child(9) > div > textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_hhrqyw_2.png")
        self.driver.find_element_by_css_selector("#saveOrder").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()

        total = self.driver.find_element_by_css_selector("#total-price").text
        print("订单提交成功，应付金额:" + total)
        self.assertIn(price, total)
        print("价格一致！")

        self.driver.find_element_by_css_selector("#payways > ul:nth-child(1) > li > span").click()
        self.driver.find_element_by_css_selector("#alisubmit").click()
        order_url = self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > input").get_attribute(
            "value")

        print("订单链接:" + order_url)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.paying-wrap.paying-sk-wrap.paying-sk-hhr > div.paying-sk-ewm > div.link > a").click()

        print("订单已发送客户付款!")

    def test_partner_clue_3(self):

        """合伙人线索换单"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.distribute > a").click()
        time.sleep(2)
        lb = (100001,100004,100007,100020,100021)
        xm = random.choice(lb)
        print("换单标签:" + self.driver.find_element_by_css_selector("#product_{}".format(xm)).text)
        self.driver.find_element_by_css_selector("#product_{}".format(xm)).click()
        self.driver.find_element_by_css_selector("#close > a").click()
        time.sleep(1)
        info = self.driver.find_element_by_css_selector("#delivery > div.test.test-1 > ul").text
        print("当前线索:" + str(info).replace("\n"," "))
        self.driver.find_element_by_css_selector("#delivery > div.bt-a > a.bt-a-two.a-colour").click()
        get_screenshort(self.driver,"test_partner_clue_4.png")
        time.sleep(3)
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()

    def test_partner_clue_4(self):

        """合伙人线索退回"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)
        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()
        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(2) > a").click()


        """已认领 第一条线索信息"""
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > div.partner > a.not_select").click()
        info = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2)").text
        clue_number = self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(1)").text
        print("线索详情:" + (str(info).replace("\n" ," ")).replace("查看详情",""))

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > a").click()

        """切换窗口打开详情"""
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)


        """关掉时间提示"""
        self.driver.find_element_by_css_selector("#layui-layer1 > span.layui-layer-setwin > a").click()

        get_screenshort(self.driver,"test_partner_clue_4.png")

        """点击退回线索"""
        self.driver.find_element_by_css_selector("#bt-a > a.a-one").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("#close > div > a.other_key").click()
        self.driver.find_element_by_css_selector("#close > div > textarea").send_keys("不做了!")
        self.driver.find_element_by_css_selector("#close > a.a-tow").click()
        print("{}线索已退回!".format(clue_number))

    def test_CancelState(self):
        """取消订单测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)

        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(2) > a").click()
        time.sleep(1)

        # 新版提示
        self.driver.find_element_by_xpath("//*[@id=\"personalCenter2-rightContainer\"]/div[1]/div/a").click()

        self.driver.find_element_by_css_selector(
            "#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > p:nth-child(1)").text)
        # 查看详情
        self.driver.find_element_by_class_name("order-cancel").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("modal-body-textarea").send_keys("下错单了!")
        time.sleep(2)
        self.driver.find_element_by_link_text("提   交").click()
        print("订单取消成功!")
