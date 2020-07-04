import unittest
import logging


import requests
from parameterized import parameterized

import app
from utils import assert_common, read_login_data


# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        from api.login_api import TestLoginApi  # 导入封装的API模块
        self.login_api = TestLoginApi()  # 实例化登录API

    def tearDown(self):
        ...


    # 定义数据文件路径
    filename = app.BASE_DIR + '/data/login_data.json'
    # 参数化时，使用定义的数据路径传入读取数据文件的函数，进行参数化
    # 编写第一个案例，测试登录成功
    @parameterized.expand(read_login_data(filename))
    def test01_login(abc, case_name, jsonData, http_code, success, code, message):
        # 发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = jsonData
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登录的结果cvf
        result = response.json()
        logging.info("登录的结果为：{}".format(result))


        # 使用封装的通用断言函数实现优化断言
        assert_common(http_code, success, code, message, response, abc)