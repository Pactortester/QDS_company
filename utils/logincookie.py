import time


class DengLuPage:

    url = "https://www.quandashi.com/"

    cookie = ({'name': 'QDS_COOKIE',
             'value': '8bd5ec460c29a887dd07fb7408836da597d514cc',
            'Domain': '.quandashi.com'})

    url_pre = "https://apre-www.quandashi.com/"

    cookie_pre = ({'name': 'QDS_COOKIE',
               'value': '25d7eb7121863524f1a551598b6d3c0be877f270',
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
