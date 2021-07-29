'''
teardown方法里封装失败自动截图---chapter4
4-11 完整得case流程集合破解验证码
'''
#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter3.business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest

import HTMLTestRunner
class RegisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''！！！把driver创建放到这里才会在报告里有错误截图'''
        print("所有case执行前执行--------------------")
        #1.创建Chrome的driver
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        cls.driver = webdriver.Chrome(executable_path="C:/Users/darli/AppData/Local/Google/Chrome/Application/chromedriver.exe",options=option)
        
    @classmethod
    def tearDownClass(cls):
        print("所有case执行后执行--------------------")
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
            print("chrome driver进程不存在")


    def setUp(self):
        
        self.driver.get("http://www.5itest.cn/register")
        self.registerBusiness = RegisterBusiness(self.driver)
        #指定code验证码图片位置,每个case指定不同的
        case_name = self._testMethodName
        self.codeImagePath = os.getcwd() + "/chapter3/image/code_" + case_name + ".png"


    def tearDown(self):
        '''case执行失败自动截图'''
        time.sleep(5)
        '''打印self._outcome.errors信息'''
        print("*************************************************************")
        errors = self._outcome.errors
        print("self._outcome.errors信息如下------>",type(self._outcome.errors),"||",self._outcome.errors)
        for error_info in errors:
            print("self._outcome.errors中的元素error_info信息如下------>",type(error_info),"||",error_info)
            for item in error_info:
                print("self._outcome.errors中的元素error_info的元素item信息如下------>",type(item),"||",item)
                print("&&&&&&&&&&&&&&")
            print("||||||||||||||||||||||||||||||||||||||||||")
        print("*************************************************************")
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                base_path = os.getcwd()
                file_path = base_path + "/chapter3/report/" + case_name + ".png"
                self.driver.save_screenshot(file_path)
        
    # def tearDown(self):
    #     time.sleep(5)
    #     try:
    #         os.system('taskkill /im chromedriver.exe /F')
    #     except:
    #         print("chrome driver进程不存在")

    def testRegisterEmailError(self):
        email = "2"
        #调用business层方法
        res = self.registerBusiness.registerWithEmailError(email,"fanyu124","1234567",self.codeImagePath)
        #assert断言判断结果
        self.assertFalse(res,"实际注册成功，testRegisterEmailError case执行失败")
        

    def testRegisterUsernameError(self):
        username = "1,"
        #调用business层方法
        res = self.registerBusiness.registerWithUsernameError("490718110@qq.com",username,"12345678",self.codeImagePath)
        #assert断言判断结果
        self.assertFalse(res,"实际注册成功，testUsernameError case执行失败")

    def testRegisterPasswordError(self):
        password = "11"
        #调用business层方法
        res = self.registerBusiness.registerWithPasswordError("490718110@qq.com","fanyu111",password,self.codeImagePath)
        #assert断言判断结果
        self.assertFalse(res,"实际注册成功，testPasswordError case执行失败")

    def testRegisterCodeError(self):
        code = "111111"
        #调用business层方法
        res = self.registerBusiness.registerWithCodeError("490718110@qq.com","fanyu111","1234567",code)
        self.assertFalse(res,"实际注册成功，testCodeError case执行失败")


    def testRegisterSuccess(self):
        res = self.registerBusiness.registerSuccess("490710885@qq.com","fanyu123","123456",self.codeImagePath)
        self.assertTrue(res,"注册失败，testRegisterSuccess case执行失败")

        
if __name__ == "__main__":
    basePath = os.getcwd()
    filePath = os.path.join(basePath,"chapter3/report/register_case.html")
    f = open(filePath,"wb")
    suite = unittest.TestSuite()
    suite.addTest(RegisterCase("testRegisterEmailError"))
    # suite.addTest(RegisterCase("testRegisterUsernameError"))
    # suite.addTest(RegisterCase("testRegisterPasswordError"))
    # suite.addTest(RegisterCase("testRegisterCodeError"))
    suite.addTest(RegisterCase("testRegisterSuccess"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="ui autotest report",description="利用HTMLTestRunner来生成测试报告-chapter4")
    runner.run(suite)
    f.close()
