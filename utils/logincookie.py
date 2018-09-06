import time


class DengLuPage:
    # url = "https://pre-www.quandashi.com/"
    url = "https://www.quandashi.com/"


    cookie = ({'name': 'QDS_COOKIE',
             'value': 'a1cc4b9c3531d0a2b6829f82b37a2e818f3ef93b',
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
