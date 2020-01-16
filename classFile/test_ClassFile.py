import unittest

from classFile import ClassFile


class TestClassFile(unittest.TestCase):

    def setUp(self):
        self.file = ClassFile.File('333.txt')
        f = open('333.txt', 'w')
        f.close()

    def test_write(self, line='sample'):
        self.file.write(line)
        for text in self.file:
            self.assertEqual(line, text)


if __name__ == '__main__':
    unittest.main()
