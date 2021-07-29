#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter3.business.register_business import RegisterBusiness
from selenium import webdriver
import time
class RegisterCase:

    def __init__(self):
        #1.创建Chrome的driver
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=option)
        driver.get("http://www.5itest.cn/register")
        self.registerBusiness = RegisterBusiness(driver)

    def testRegisterEmailError(self):
        email = "111"
        #调用business层方法
        res = self.registerBusiness.registerWithEmailError(email,"fanyu","1234567","123456")
        if res:
            print("注册成功，testRegisterEmailError case执行失败")
        else:
            print("注册失败，testRegisterEmailError case执行成功")
        #assert断言判断结果
        

    def testRegisterUsernameError(self):
        username = "1,"
        #调用business层方法
        res = self.registerBusiness.registerWithUsernameError("490718876@qq.com",username,"12345678","123456")
        if res:
            print("注册成功，testUsernameError case执行失败")
        else:
            print("注册失败，testUsernameError case执行成功")
        #assert断言判断结果

    def testRegisterPasswordError(self):
        password = "11"
        #调用business层方法
        res = self.registerBusiness.registerWithPasswordError("490718876@qq.com","fanyu",password,"123456")
        if res:
            print("注册成功，testPasswordError case执行失败")
        else:
            print("注册失败，testPasswordError case执行成功")
        #assert断言判断结果

    def testRegisterCodeError(self):
        code = "111111"
        #调用business层方法
        res = self.registerBusiness.registerWithCodeError("490718876@qq.com","fanyu","1234567",code)
        if res:
            print("注册成功，testCodeError case执行失败")
        else:
            print("注册失败，testCodeError case执行成功")

    def testRegisterSuccess(self):
        res = self.registerBusiness.registerSuccess("490718876@qq.com","fanyu","123456","xz47g")
        if res:
            print("注册成功，testRegisterSuccess case执行成功")
        else:
            print("注册失败，testRegisterSuccess case执行失败")

    def main(self):
        self.testRegisterEmailError()
        time.sleep(4)
        self.testRegisterUsernameError()
        time.sleep(4)
        self.testRegisterPasswordError()
        time.sleep(4)
        self.testRegisterCodeError()
        #由于没有接入解析验证码的函数，所以无法验证正向流程
        
if __name__ == "__main__":
    try:
        registerCase = RegisterCase()
        registerCase.main()
    finally:#无论是否发生异常都会执行
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
            print("chrome driver进程不存在")

