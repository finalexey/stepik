import time
import unittest

from loggablelist import LoggableList


class TestLogList(unittest.TestCase):

    def setUp(self):
        self.lst = LoggableList()
        self.msg = 'message'

    def test_log(self):
        result = self.lst.log(self.msg)
        self.assertEqual((time.ctime()) + ": " + str(self.msg), result)

    def test_append(self):
        result = self.lst.append(self.msg)
        self.assertEqual((time.ctime()) + ": " + str(self.msg), result)


if __name__ == '__main__':
    unittest.main()
