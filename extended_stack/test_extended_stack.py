import unittest

from extended_stack import ExtendedStack


class TestExStack(unittest.TestCase):

    def setUp(self):
        self.ex_stack = ExtendedStack([5, 10])

    def test_div(self):
        self.ex_stack.div()
        self.assertEqual(2, self.ex_stack.pop())

    def test_sub(self):
        self.ex_stack.sub()
        self.assertEqual(5, self.ex_stack.pop())

    def test_sum(self):
        self.ex_stack.sum()
        self.assertEqual(15, self.ex_stack.pop())

    def test_mul(self):
        self.ex_stack.mul()
        self.assertEqual(50, self.ex_stack.pop())


if __name__ == '__main__':
    unittest.main()
