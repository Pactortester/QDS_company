import time


class dengLuPage:
    #url = "https://www.quandashi.com/"
    url = "https://www.quandashi.com/"


    cookie=({'name': 'QDS_COOKIE',
             'value': '116b79bb072221f47477b4c5980a685f0b4fa2d1',
              'Domain': '.quandashi.com'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)

    def refresh(self):

        self.driver.add_cookie(self.cookie)
        self.driver.refresh()





