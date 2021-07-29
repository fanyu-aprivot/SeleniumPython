'''
数据驱动把PO模型精简化，以一条case完成了N条case的结果，这就是数据驱动，以数据为结果导向
'''
#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter5.business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest
import ddt
@ddt.ddt
class RegisterDdtCase(unittest.TestCase):
    def setUp(self):
        #1.创建Chrome的driver
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("http://www.5itest.cn/register")
        self.registerBusiness = RegisterBusiness(self.driver)
        #指定code验证码图片位置,每个case指定不同的
        case_name = self._testMethodName
        self.codeImagePath = os.getcwd() + "/chapter5/image/code_" + case_name + ".png"


    def tearDown(self):
        '''case执行失败自动截图'''
        time.sleep(5)
        # for method_name,error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         base_path = os.getcwd()
        #         file_path = base_path + "/chapter5/report/" + case_name + ".png"
        #         self.driver.save_screenshot(file_path)
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
            print("chrome driver进程不存在")
    '''数据驱动元素：邮箱，用户密码，密码，验证码路径，错误定位元素，错误提示信息'''
    @ddt.data(
        ["12","fanyu116","1234567",os.getcwd() + "/chapter5/image/code_1" + ".png","email_error","请输入正确的邮箱"],
        ["490718800@qq.com",",&","1234567",os.getcwd() + "/chapter5/image/code_2" + ".png","username_error","请输入正确的用户名"],
        ["490718800@qq.com","fanyu117","12",os.getcwd() + "/chapter5/image/code_3" + ".png","password_error","请输入正确的密码"]
    )
    @ddt.unpack
    def testRegisterCase(self,email,username,password,codeImagePath,assertKey,assertValue):
        #调用business层方法
        res = self.registerBusiness.registerBusiness(email,username,password,codeImagePath,assertKey,assertValue)
        #assert断言判断结果
        self.assertFalse(res,"预期注册失败，实际与预期不符")

if(__name__ == "__main__"):
    unittest.main()