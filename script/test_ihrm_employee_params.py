# 创建测试类
import logging
import unittest

import app
from utils import assert_common,read_emp_data
from parameterized import parameterized
# 第三层：在unittest框架中，用5个测试函数，分别实现员工的登录增删改查（理解上，更有难度，大家根据来决定是否花更多时间消化）



class TestIHRMEmployee3(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
        from api.employee_api import TestEmployeeApi
        self.emp_api = TestEmployeeApi()  # 员工实例化
        from api.login_api import TestLoginApi
        self.login_api = TestLoginApi()  # 登录实例化
    # 编写测试函数
    # 登录
    def test01_login(self):
        # 登录
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印登录的数据
        logging.info("登录的结果为：{}".format(response.json()))
        # 提取令牌
        token = response.json().get("data")
        # 保存令牌到请求头当中
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        app.HEADERS = headers  # 将请求头保存到全局变量中
        # 打印令牌
        logging.info("保存到全局变量app中的请求头中令牌为：{}".format(app.HEADERS))


    # 定义员工模块数据文件路径
    filename = app.BASE_DIR + '/data/emp_data.json'
    @parameterized.expand(read_emp_data(filename, 'add_emp'))
    # 添加员工
    def test02_add_emp(self, username, mobile, http_code, success, code, message):
        # 添加员工
        response = self.emp_api.add_emp(app.HEADERS, username, mobile)
        # 打印添加的结果
        logging.info("添加员工的结果为:{}".format(response.json()))
        # 提取添加员工中的id
        emp_id = response.json().get("data").get("id")
        app.EMPID = emp_id  # 将员工id保存到全局变量
        # 断言
        assert_common(http_code, success, code, message, response, self)


    @parameterized.expand(read_emp_data(filename, 'query_emp'))
    # 查询员工
    def test03_query_emp(self, http_code, success, code, message):
        # 查询员工
        # 发送查询员工的请求
        response = self.emp_api.query_emp(app.EMPID, app.HEADERS)
        logging.info("查询员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(http_code, success, code, message, response, self)


    @parameterized.expand(read_emp_data(filename, 'modify_emp'))
    # 修改员工
    def test04_modify_emp(self, username, http_code, success, code, message):
        # 修改员工
        # 发送修改员工的请求
        response = self.emp_api.modify_emp(app.EMPID,
                                           app.HEADERS,
                                           username)
        # 打印修改的结果
        logging.info("修改员工的结果为:{}".format(response.json()))

        # 断言
        assert_common(http_code, success, code, message, response, self)

    # 删除员工
    @parameterized.expand(read_emp_data(filename, 'delete_emp'))
    def test05_delete_emp(self, http_code, success, code, message):
        # 删除员工
        # 发送删除员工的请求
        response = self.emp_api.delete_emp(app.EMPID, app.HEADERS)
        # 打印删除的结果
        logging.info("删除的结果为:{}".format(response.json()))
        # 断言
        assert_common(http_code, success, code, message, response, self)
