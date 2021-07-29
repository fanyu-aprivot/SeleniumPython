'''
6-9 对所有函数都返回值,return的可能结果有True,False,value,None
'''
#coding=utf-8
from selenium import webdriver
from chapter6.base.find_element import FindElement
import time
import os
class ActionMethod():
    def __init__(self):
        pass

    def openBrowser(self,browserName=None):
        '''打开浏览器'''
        try:
            if browserName == None or browserName == "chrome":
                option = webdriver.ChromeOptions()
                # 防止打印一些无用的日志
                option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
                self.driver = webdriver.Chrome(chrome_options=option)
            elif browserName == "firefox":
                self.driver = webdriver.Firefox()
            elif browserName == "edge":
                self.driver = webdriver.Edge(executable_path="msedgedriver.exe")
            else:
                self.driver = None
            return True
        except:
            return False
        

    def visitUrl(self,url):
        '''访问url'''
        try:
            self.driver.get(url)
            return True
        except:
            return False

    def getElement(self,key):
        '''获取元素(FindElement已有容错处理，无需容错处理)'''
        find = FindElement(self.driver)
        element = find.findElement(key)
        return element

    def getUrlTitle(self):
        '''6-9 增加获取网页的title值'''
        title = self.driver.title
        return title

    def sendValue(self,key,value):
        '''输入值(需要容错处理）'''
        element = self.getElement(key)
        if element:
            element.send_keys(value)
            return True
        else:
            return False
    
    def clickElement(self,key):
        '''点击元素(需要容错处理)'''
        element = self.getElement(key)
        if element:
            element.click()
            return True
        else:
            return False

    def wait(self,timeLength = None):
        '''等待'''
        try:
            if timeLength == None:
                timeLength = 3
            #从Excel里获取到的数值是str类型
            timeLength = int(timeLength)
            time.sleep(timeLength)
            return True
        except:
            return False

    def closeDriver(self,browser):
        '''关闭浏览器，杀死进程'''
        if browser == "chrome":
            try:
                os.system('taskkill /im chromedriver.exe /F')
            except:
                print("chrome driver进程不存在")
            return True
        elif browser == "firefox":
            try:
                os.system('taskkill /im geckodriver.exe /F')
            except:
                print("gecko driver进程不存在")
            return True
        elif browser == "edge":
            try:
                os.system('taskkill /im msedgedriver.exe /F')
            except:
                print("msedge driver进程不存在")
            return True
        else:
            return False

actionMethod = ActionMethod()
