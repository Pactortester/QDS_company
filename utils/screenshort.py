import  os

import time


def get_screenshort(driver,file_name):
    base_path = "G:\\quandashitest_company\\quandashitest_company\\image\\"
    time_c=time.strftime("%Y-%m-%d_%H-%M-%S_")
    path = base_path + time_c+file_name
    time.sleep(1)
    # 截图
    driver.get_screenshot_as_file(path)


# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))
#https://www.cnblogs.com/wuxie1989/p/5623435.html