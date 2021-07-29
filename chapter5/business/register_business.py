#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter5.handle.register_handle import RegisterHandle
import time
class RegisterBusiness:
    def __init__(self,driver):
        self.registerHandle = RegisterHandle(driver)

    def registerCommon(self,email,username,password,codeImagePath):
        self.registerHandle.sendEmail(email)
        self.registerHandle.sendUsername(username)
        self.registerHandle.sendPassword(password)
        #先把code写死
        self.registerHandle.sendFalseCode("123456")
        # self.registerHandle.sendCode(codeImagePath)
        self.registerHandle.clickRegisterButton()  #点击注册按钮

    def registerBusiness(self,email,username,password,codeImagePath,assertKey,assertValue):
        '''返回是否注册成功'''
        self.registerCommon(email,username,password,codeImagePath)
        if self.registerHandle.getErrorInfo(assertKey,assertValue):
            print("--------------->business层 出现错误提示信息注册失败")
            return False
        else:
            print("--------------->business层 未出现错误提示信息注册成功")
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



        