import unittest
import os
from ddt import ddt, data
from setting.constant import p_path
from 框架设计.common.execl_handler import ExcelHandler
from 框架设计.common.config_handler import ConfigHandler, config
from 框架设计.fun.calc import add
from 框架设计 import logger

# 通过读取配置文件得到cases.xlsx
file_name = config.read('excel', 'file_name')
file_path = os.path.join(p_path.DATA_PATH, file_name)

# 获取 sheetname
sheet_name = config.read('excel', 'add_sheet')

# 读取EXCEL的数据
test_data = ExcelHandler(file_path).read(sheet_name)


@ddt
class TestAdd(unittest.TestCase):
    @data(*test_data)
    def test_add(self, test_info):
        a = test_info[2]
        actual = add(*eval(test_info[1]))
        try:
            self.assertEqual(eval(str(test_info[2])), actual)
            logger.info("测试通过")
        except AssertionError as e:
            logger.error("断言失败")
            raise e
