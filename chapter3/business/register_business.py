#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter3.handle.register_handle import RegisterHandle
import time
class RegisterBusiness:
    def __init__(self,driver):
        self.registerHandle = RegisterHandle(driver)

    def registerCommon(self,email,username,password,codeImagePath):
        self.registerHandle.sendEmail(email)
        self.registerHandle.sendUsername(username)
        self.registerHandle.sendPassword(password)
        #假传验证码
        self.registerHandle.sendFalseCode("123456")
        # self.registerHandle.sendCode(codeImagePath)
        self.registerHandle.clickRegisterButton()  #点击注册按钮

    def registerWithEmailError(self,email,username,password,codeImagePath):
        '''返回是否注册成功，预期结果是false-注册失败'''
        self.registerCommon(email,username,password,codeImagePath)
        if(self.registerHandle.getErrorInfo("email_error")):
            print("business层 registerWithEmailError-->出现错误提示信息邮箱校验成功")
            return False
        else:
            print("business层 registerWithEmailError-->未出现错误提示信息邮箱校验失败")
            return True

    def registerWithUsernameError(self,email,username,password,codeImagePath):
        '''返回是否注册成功，预期结果是false-注册失败'''
        self.registerCommon(email,username,password,codeImagePath)
        if(self.registerHandle.getErrorInfo("username_error")):
            print("business层 registerWithUsernameError-->出现错误提示信息用户名校验成功")
            return False
        else:
            print("business层 registerWithUsernameError-->未出现错误提示信息用户名校验失败")
            return True

    def registerWithPasswordError(self,email,username,password,codeImagePath):
        '''返回是否注册成功，预期结果是false-注册失败'''
        self.registerCommon(email,username,password,codeImagePath)
        if(self.registerHandle.getErrorInfo("password_error")):
            print("business层 registerWithPasswordError-->出现错误提示信息密码校验成功")
            return False
        else:
            print("business层 registerWithPasswordError-->未出现错误提示信息密码校验失败")
            return True

    def registerWithCodeError(self,email,username,password,codeImagePath):
        '''返回是否注册成功，预期结果是false-注册失败'''
        self.registerCommon(email,username,password,codeImagePath)
        if(self.registerHandle.getErrorInfo("code_error")):
            print("business层 registerWithCodeError-->出现错误提示信息验证码校验成功")
            return False
        else:
            print("business层 registerWithCodeError-->未出现错误提示信息验证码校验失败")
            return True
    '''注册成功'''
    def registerSuccess(self,email,username,password,codeImagePath):
        '''返回是否注册成功，预期结果是true-注册成功'''
        self.registerCommon(email,username,password,codeImagePath)
        if self.registerHandle.getRegisterButtonText() == None:
            print("business层 提示：注册成功-------------------->")
            return True
        else:
            print("business层 提示：注册失败-------------------->")
            return False



        