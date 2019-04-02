import time


class DengLuPage:

    url = "https://www.quandashi.com/"

    cookie = ({'name': 'QDS_COOKIE',
             'value': 'bc165cf81b34afe82f7e8746126a4de232ef3a3d',
            'Domain': '.quandashi.com'})

    url_pre = "https://apre-www.quandashi.com/"

    cookie_pre = ({'name': 'QDS_COOKIE',
               'value': 'aafa7d0f4a13d90dcc200c751f430325d87a0a94',
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
        # self.driver.find_element_by_css_selector("body > div.festival-modal-bg.new-year-bg > div > a").click()

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
