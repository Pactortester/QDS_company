import time


class DengLuPage:
    url = "https://pre-www.quandashi.com/"
    # url = "https://www.quandashi.com/"


    cookie = ({'name': 'QDS_COOKIE',
             'value': 'f728edf7f66014c31b52596c24cd2772a8eaa5c1',
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
