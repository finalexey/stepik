import unittest

from classFile import ClassFile


class TestClassFile(unittest.TestCase):

    def setUp(self):
        self.file = ClassFile.File('333.txt')


    def test_write(self, line='sample'):
        self.file.write(line)
        for text in self.file:
            self.assertEqual(line, text)
            
    def tearDown(self):
        f = open('333.txt', 'w')
        f.close()


if __name__ == '__main__':
    unittest.main()
