#coding=utf-8
import os,sys
print(os.getcwd())
sys.path.append(os.getcwd())
from features.lib.page.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def __init__(self,context):
        super(RegisterPage,self).__init__(context.driver)

    '''getTitle和getUrl函数可以直接调用BasePage的，无需实现'''

    def sendEmail(self,email):
        element = self.findElement(By.ID,"register_email")
        self.sendValue(element,email)

    def sendUsername(self,username):
        element = self.findElement(By.ID,"register_nickname")
        self.sendValue(element,username)

    def sendPassword(self,password):
        element = self.findElement(By.ID,"register_password")
        self.sendValue(element,password)

    def sendCode(self,code):
        element = self.findElement(By.ID,"captcha_code")
        self.sendValue(element,code)

    def clickRegisterButton(self):
        element = self.findElement(By.ID,"register-btn")
        self.clickElement(element)

    def getCodeErrorInfo(self):
        codeErrorInfo = self.findElement(By.ID,"captcha_code-error").text
        return codeErrorInfo
    