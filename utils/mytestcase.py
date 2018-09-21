import unittest
import time
from utils.log import Log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\Administrator\\AppData\Local\\Google\Chrome\\Application\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')

    @staticmethod
    def my_print(msg):
        logger.info(msg)