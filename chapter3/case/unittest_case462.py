#coding=utf-8
import unittest
class RegisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("4-6-2所有case执行前执行--------------------")

    @classmethod
    def tearDownClass(cls):
        print("4-6-2所有case执行后执行--------------------")

    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")
    
    def testCase01(self):
        print("4-6-2----------》case01")

    def testCase02(self):
        print("4-6-2----------》case02")


if(__name__ == "__main__"):
    # unittest.main()
    suite = unittest.TestSuite()
    #执行的时候将按照添加case的顺序
    suite.addTest(RegisterCase("testCase01"))
    suite.addTest(RegisterCase("testCase02"))
    unittest.TextTestRunner().run(suite)