import unittest

from cryptorproj import cryptor


class TestCryptor(unittest.TestCase):

    def setUp(self):
        self.encrypted = open("encrypted.bin", "rb").read()
        self.pwd = open("passwords.txt").readlines()

    def test_encrypt(self):
        result = cryptor.encrypt(self.encrypted, self.pwd)
        self.assertEqual('Alice loves Bob', result)


if __name__ == '__main__':
    unittest.main()
