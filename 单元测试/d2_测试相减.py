import unittest


def minus(a, b):
    return a - b


x = 3
y = 5
expected = -2


class TestMinus(unittest.TestCase):

    def test_minus_success(self):
        self.assertTrue(expected == minus(x, y))

    def test_minus_error(self):
        self.assertEqual(7, minus(x, y))


if __name__ == "__main__":
    unittest.main()
