import os
import unittest

# 初始化 suite
from datetime import datetime

from common.HTMLTestRunnerNew import HTMLTestRunner
from setting.constant import p_path

suite = unittest.TestSuite()

# 初始化 loader加载器
loader = unittest.TestLoader()

# discover 自动发现测试
suite = loader.discover(p_path.CASE_PATH)

# report + 时间戳后缀.html
report_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
print(report_name)
report_file = os.path.join(p_path.REPORT_PATH, report_name + '.html')
print(report_file)

if __name__ == '__main__':
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(f)
        runner.run(suite)
