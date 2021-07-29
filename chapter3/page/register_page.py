#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter3.base.find_element import FindElement

class RegisterPage:
    def __init__(self,driver):
        self.findElement = FindElement(driver)

    def findHtmlElement(self):
        return self.findElement.findElement("html")

    '''获取四个输入框元素'''
    def findEmailElement(self):
        return self.findElement.findElement("email")

    def findUsernameElement(self):
        return self.findElement.findElement("username")

    def findPasswordElement(self):
        return self.findElement.findElement("password")

    def findCodeElement(self):
        return self.findElement.findElement("code")
    '''获取验证码图片元素'''
    def findCodeImageElement(self):
        return self.findElement.findElement("code_image")

    '''获取注册按钮元素'''
    def findRegisterButtonElement(self):
        return self.findElement.findElement("register_button")

    '''获取错误信息元素'''
    def findEmailErrorElement(self):
        return self.findElement.findElement("email_error")

    def findUsernameErrorElement(self):
        return self.findElement.findElement("username_error")

    def findPasswordErrorElement(self):
        return self.findElement.findElement("password_error")

    def findCodeErrorElement(self):
        return self.findElement.findElement("code_error")