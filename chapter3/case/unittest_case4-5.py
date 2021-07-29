#coding=utf-8
import unittest
class RegisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case执行前执行--------------------")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行后执行--------------------")
    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")
    
    def testCase001(self):
        print("case001")

    def testCase002(self):
        print("case002")

    @unittest.skip("不执行case003")
    def testCase003(self):
        print("case003")

if(__name__ == "__main__"):
    # unittest.main()
    suite = unittest.TestSuite()
    #执行的时候将按照添加case的顺序
    suite.addTest(RegisterCase("testCase003"))
    suite.addTest(RegisterCase("testCase002"))
    suite.addTest(RegisterCase("testCase001"))
    unittest.TextTestRunner().run(suite)