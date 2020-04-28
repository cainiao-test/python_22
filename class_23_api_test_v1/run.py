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

# report + 时间戳后缀.html
report_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
report_file = os.path.join(p_path.REPORT_PATH, report_name + '.html')

if __name__ == '__main__':
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(f)
        runner.run(suite)
