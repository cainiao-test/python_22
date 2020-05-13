import json
import unittest
import os
from common.logger_handler import logger
from libs.ddt import ddt, data
from common.config_handler import ConfigHandler, config
from common.execl_handler import ExcelHandler
from common.requests_handler import RequestsHandler
from middler_ware.db_handler import MyDBHandler
from setting.constant import p_path
from common.HTMLTestRunnerNew import OutputRedirector


@ddt
class TestLogin(unittest.TestCase):
    # 读取配置文件
    file_name = 'E:/远信集团/python_22/class_23_api_test_v1/data/cases.xlsx'
    file_path = os.path.join(p_path.DATA_PATH, file_name)

    # Execl表格名称
    sheet_name = config.read('excel', 'login_sheet')
    # 读取url地址
    url = config.read('http', 'host')
    # 读取headers
    headers = config.read('http', 'headers')
    # Excel 操作
    xls = ExcelHandler(file_path, sheet_name)
    test_data = xls.read()
    excel_headers = xls.headers()
    result_index = excel_headers.index('result')

    @classmethod
    def setUpClass(cls):
        cls.req = RequestsHandler()
        cls.logger = logger

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.db = MyDBHandler()

    def tearDown(self):
        self.db.close()

    @data(*test_data)
    def test_login(self, test_info):
        # 调用 requests 模块访问接口
        if "*exist_phone*" in test_info['data']:
            self.db.query('SELECT * FROM member;')

        res = self.req.json(test_info['method'],
                            self.url + test_info['url'],
                            json=eval(test_info['data']),
                            headers=eval(self.headers))
        print(res)
        try:
            self.assertEqual(test_info['expected'], res['message'])
            # 写入Excel 断言成功
            self.xls.write(test_info['case_id'] + 1,
                           self.result_index + 1,
                           'pass')
        except AssertionError as e:
            # 写入Excel 断言失败
            self.xls.write(test_info['case_id'] + 1,
                           self.result_index + 1,
                           'failed')
            raise e
