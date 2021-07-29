'''
不同页面的所共有的公用的方法，在selenium基础上二次封装
'''
#coding=utf-8

from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def getUrl(self,url):
        '''获取url'''
        self.driver.get(url)

    def getTitle(self):
        '''获取标题'''
        return self.driver.title

    def findElement(self,*loc):
        '''定位元素'''
        element = self.driver.find_element(*loc)
        return element

    def sendValue(self,element,value):
        '''向输入框写入值'''
        element.send_keys(value)

    def clickElement(self,element):
        '''元素点击'''
        element.click()

    

    