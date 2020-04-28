import json
import unittest
import os
from ddt import ddt, data
from common.config_handler import ConfigHandler, config
from common.execl_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from setting.constant import p_path
from common.HTMLTestRunnerNew import OutputRedirector


@ddt
class TestLogin(unittest.TestCase):
    # 读取配置文件
    file_name = 'E:\远信集团\python_22\class_23_api_test_v1\data\cases.xlsx'
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
    def test_login(self, test_info):
        # 调用 requests 模块访问接口
        res = self.req.json(test_info[3],
                            self.url + test_info[4],
                            json=json.loads(test_info[5]),
                            headers=eval(self.headers))
        print(type(res))
        print(type(test_info[7]))
        self.assertEqual(test_info[7], res)


