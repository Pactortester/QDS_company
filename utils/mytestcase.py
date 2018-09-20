import unittest
import time

from config.globalparam import driver_path
from utils.log import Log
from selenium import webdriver

from utils.pyselenium import logger


class MyTestCase(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    success = "SUCCESS   "
    fail = "FAIL   "
    logger = Log()

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\Local\\Google\Chrome\\Application\\chromedriver.exe")

        # self.driver = webdriver.Chrome(driver_path+'\\'+'chromedriver.exe')

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')

    def my_print(self,msg):
        logger.info(msg)