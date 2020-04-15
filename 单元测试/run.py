import unittest
import os
from HTMLTestRunnerNew import HTMLTestRunner

loader = unittest.TestLoader()

# 自动发现测试用例
start_dir = os.path.dirname(os.path.abspath(__file__))
suite1 = loader.discover(start_dir)

# 运行,测试报告文件
with open('demo.txt', 'wb') as f:
        # 初始化 common
        runner = HTMLTestRunner(f, verbosity=2)

        # 运行
        runner.run(suite1)
