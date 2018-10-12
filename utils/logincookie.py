import time


class DengLuPage:

    url = "https://www.quandashi.com/"

    cookie = ({'name': 'QDS_COOKIE',
             'value': '1dcb2f2d3a36b86b9c977d966dd9a4eceeb545f7',
            'Domain': '.quandashi.com'})

    url_pre = "https://pre-www.quandashi.com/"

    cookie_pre = ({'name': 'QDS_COOKIE',
               'value': '5ba05f2a218365ebf34451d7e213a0e441684852',
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


    def open_page_pre(self):
        self.driver.get(self.url_pre)

    def login_pre(self):
        self.open_page()
        self.driver.add_cookie(self.cookie_pre)
        self.driver.refresh()
        time.sleep(1)

    def refresh_pre(self):
        self.driver.add_cookie(self.cookie_pre)
        self.driver.refresh()
        time.sleep(1)
