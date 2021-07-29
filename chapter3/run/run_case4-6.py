#coding=utf-8
import unittest
import os

class RunCase(unittest.TestCase):
    def test001(self):
        print("当前工作目录--->",os.getcwd())
        # dir = os.getcwd() + "\chapter3\case"
        dir = os.path.join(os.getcwd(),"chapter3/case")
        # print(os.path.join("111","222","333"))
        print(dir)
        pattern = "unittest_case4*.py"
        suite = unittest.defaultTestLoader.discover(dir,pattern)
        unittest.TextTestRunner().run(suite)


if(__name__ == "__main__"):
    unittest.main()

    
