import time


class DengLuPage:
    # url = "https://pre-www.quandashi.com/"
    # 7a1bfe107b64262afcec4226789783fa597e0347  5788ec58d3deadd6e9242efb47d456b01ededa3c
    url = "https://www.quandashi.com/"


    cookie = ({'name': 'QDS_COOKIE',
             'value': '5788ec58d3deadd6e9242efb47d456b01ededa3c',
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
        time.sleep(1)
