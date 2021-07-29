#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter5.page.register_page import RegisterPage
from chapter5.base.get_code import GetCode
class RegisterHandle:

    def __init__(self,driver):
        self.driver = driver
        self.registerPage = RegisterPage(self.driver)
        self.getCode = GetCode(self.driver)
    '''向输入框输入信息'''
    def sendEmail(self,email):
        # self.registerPage.findEmailElement().clear()
        self.registerPage.findEmailElement().send_keys(email)

    def sendUsername(self,username):
        # self.registerPage.findUsernameElement().clear()
        self.registerPage.findUsernameElement().send_keys(username)

    def sendPassword(self,password):
        # self.registerPage.findPasswordElement().clear()
        self.registerPage.findPasswordElement().send_keys(password)

    def sendFalseCode(self,falseCode):
        # self.registerPage.findPasswordElement().clear()
        self.registerPage.findCodeElement().send_keys(falseCode)

    def sendCode(self,codeImagePath):
        self.getCode.saveCodeImage(codeImagePath)
        code = self.getCode.getTextFromCode(codeImagePath)
        self.registerPage.findCodeElement().send_keys(code)

    '''获取错误信息'''
    def getErrorInfo(self,errorType,errorMsg):
        '''添加容错处理'''
        try:
            if errorType == "email_error":
                #element.text获取元素文字信息
                text = self.registerPage.findEmailErrorElement().text
            elif errorType == "username_error":
                text = self.registerPage.findUsernameErrorElement().text
            elif errorType == "password_error":
                text = self.registerPage.findPasswordErrorElement().text
            elif errorType == "code_error":
                text = self.registerPage.findCodeErrorElement().text
        except:
            text = None
        return text
    '''点击注册按钮'''
    def clickRegisterButton(self):
        self.registerPage.findRegisterButtonElement().click()
    '''获取注册按钮文字信息（判断正向case是否注册成功用）'''
    def getRegisterButtonText(self):
        '''添加容错处理'''
        try:
            text = self.registerPage.findRegisterButtonElement().text
        except:
            text = None
        return text