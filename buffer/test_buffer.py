import unittest

from buffer import Buffer


class TestBuffer(unittest.TestCase):

    def setUp(self):
        self.buf = Buffer()

    def test_add(self):
        result = self.buf.add(1, 2, 3, 4, 5)
        self.assertEqual(15, result)


if __name__ == '__main__':
    unittest.main()
