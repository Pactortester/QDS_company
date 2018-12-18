import time


class DengLuPage:

    url = "https://www.quandashi.com/"

    cookie = ({'name': 'QDS_COOKIE',
             'value': '6b3d6460226e1ba88cfcb7424e082ee0c1b4b9ed',
            'Domain': '.quandashi.com'})

    url_pre = "https://apre-www.quandashi.com/"

    cookie_pre = ({'name': 'QDS_COOKIE',
               'value': 'd7e8a720d5256eb331fa1773f963c1b443e4b70e',
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
        self.open_page_pre()
        self.driver.add_cookie(self.cookie_pre)
        self.driver.refresh()
        time.sleep(1)

    def refresh_pre(self):
        self.driver.add_cookie(self.cookie_pre)
        self.driver.refresh()
        time.sleep(1)
