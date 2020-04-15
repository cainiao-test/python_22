import unittest

def add(a, b):
    return a + b
x = 3
y = 5
expected = 8

class TestAdd(unittest.TestCase):

    def test_add_success(self):
        # 预期结果
        self.assertTrue(expected == add(x, y))

    def test_add_error(self):
        self.assertEqual(7,add(x,y))
