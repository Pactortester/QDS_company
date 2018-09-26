import time


class DengLuPage:
    # url = "https://pre-www.quandashi.com/"
    url = "https://www.quandashi.com/"

    cookie = ({'name': 'QDS_COOKIE',
             'value': '1519311da381740acb14415226dc47108b1a2155',
            'Domain': '.quandashi.com'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def login(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)

    def refresh(self):

        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)
