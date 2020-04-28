import unittest
import os
from ddt import ddt, data
from common.config_handler import ConfigHandler, config
from common.execl_handler import ExcelHandler
from common.logger_handler import logger
from common.requests_handler import RequestsHandler
from setting.constant import p_path


@ddt
class TestLogin(unittest.TestCase):
    # 读取配置文件
    file_name = config.read('execl', 'file_name')
    print(file_name)
    file_path = os.path.join(p_path.DATA_PATH, file_name)
    print(file_path)
    # Execl表格名称
    sheet_name = config.read('excel', 'login_sheet')
    # 读取url地址
    url = config.read('http', 'host')
    # 读取headers
    headers = config.read('http', 'headers')
    test_data = ExcelHandler(file_path).read(sheet_name)

    @classmethod
    def setUpClass(cls):
        cls.req = RequestsHandler()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_register(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info[3],
                            self.url + test_info[4],
                            json=test_info[5],
                            headers=eval(self.headers))
        print(res)
        self.assertEqual(test_info[7], res)
