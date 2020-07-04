# 导包
import logging
import unittest
import api
# 创建测试类
class TestLog(unittest.TestCase):
    # 创建一个打印日志的测试函数
    def test01_log(self):
        logging.info("在script的test_log当中测试打印日志")

