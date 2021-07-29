#coding=utf-8
import unittest
class RegisterCase(unittest.TestCase):
    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")
    
    def testCase001(self):
        print("case001")

    def testCase002(self):
        print("case002")

if(__name__ == "__main__"):
    unittest.main()