# coding=utf-8

import os
from utils.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig', 'project_path')
# 测试用例路径
case_path = os.path.join(prj_path, 'case')
# 日志路径
log_path = os.path.join(prj_path, 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report')
# 默认浏览器
browser = 'Chrome'
# 测试数据路径
data_path = os.path.join(prj_path, 'data')
# 驱动路径
driver_path = os.path.join(prj_path, 'driver')
