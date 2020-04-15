import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('测试类之前')

    @classmethod
    def tearDownClass(cls):
        print('测试类之后')

    def setUp(self):
        """
        前置条件:
        测试用例方法执行前自动运行setup里面的程序
        """
        self.data = [
            {'a': 3, 'b': 4, 'expected': 7},
            {'a': 5, 'b': 9, 'expected': 8},
        ]

    def tearDown(self):
        """
        后置条件:
        测试用例方法执行后自动运行setup里面的程序
        """
        print('用例执行后置条件')

    def test_add_success(self):
        self.assertTrue(self.data[0]['expected'] == self.data[0]['a'], self.data[0]['b'])

    def test_add_error(self):
        self.assertTrue(self.data[1]['expected'] == self.data[1]['a'], self.data[1]['b'])


if __name__ == "__main__":
    unittest.main()
