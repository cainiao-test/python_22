import unittest

def add(a, b):
    return a + b

# 测试数据 预期结果 caseID
data = [
    {"data": (1, 2), "expected": 4, "case_id": 1},
    {"data": (1, 2, 3), "expected": 6, "case_id": 2},
    {"data": (1, 'a'), "expected": None, "case_id": 3},
    {"data": (1,), "expected": None, "case_id": 4},
]


class TestAdd(unittest.TestCase):

    def test_add(self):
        for d in data:

            self.assertEqual(d['expected'], add(*d['data']))


if __name__ == '__mian__':
    unittest.main()
