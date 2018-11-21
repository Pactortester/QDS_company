import time

from config.globalparam import img_path


def get_screenshort(driver, file_name):

    # base_path = "G:\\QDS_company\\image\\"

    time_c = time.strftime("%Y-%m-%d_%H-%M-%S_")
    path = img_path + '\\'+time_c+file_name
    time.sleep(1)
    driver.get_screenshot_as_file(path)


# print(os.path.dirname(__file__))
# print(os.path.abspath(__file__))
# https://www.cnblogs.com/wuxie1989/p/5623435.html
