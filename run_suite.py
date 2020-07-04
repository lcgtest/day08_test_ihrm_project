# 导包
import unittest

import HTMLTestRunner_PY3

import app
from script.test_ihrm_employee_params import TestIHRMEmployee3
from script.test_ihrm_login_params import TestIHRMLogin
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee3))
# 定义测试报告的名称
report_name = app.BASE_DIR + "/report/ihrm.html"
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_name, 'wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="IHRM接口测试报告", description="这是人力资源管理系统的测试报告")
    # 使用runner运行测试套件
    runner.run(suite)