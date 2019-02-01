# coding=utf-8
import os
import unittest
import time

from selenium.webdriver.common.by import By

from config.globalparam import driver_path
from utils.log import Log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.pyselenium import logger


class MyTestCase(unittest.TestCase):
    """
    The base class is for all test cases. This is a father .
    """
    success = "SUCCESS   "
    fail = "FAIL   "
    logger = Log()

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options,executable_path=driver_path + "\\" + "chromedriver.exe")
        self.driver = webdriver.Chrome(driver_path + "\\" + "chromedriver.exe")
        self.driver.maximize_window()
        self.driver.set_window_size(1920,1080)
        self.driver.implicitly_wait(30)

    # def spring_festival(self):
    #
    #     try:
    #         self.driver.find_element(By.CSS_SELECTOR,"body > div.festival-modal-bg.new-year-bg > div > a")
    #         a = True
    #     except :
    #         a = False
    #     if a is True:
    #         print("当前无线索,点击申请!")
    #         self.driver.find_element_by_css_selector("body > div.festival-modal-bg.new-year-bg > div > a").click()
    #
    #     elif a is False:
    #         pass

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.logger.info('###############################  END  ###############################')


    @staticmethod
    def my_print(msg):
        logger.info(msg)