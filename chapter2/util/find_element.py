#coding=utf-8
import os,sys
import time
print("find_element.py当前工程目录------->",os.getcwd())
sys.path.append(os.getcwd())
from chapter2.util.read_ini import readIni
from selenium import webdriver

class FindElement:

    def __init__(self,driver):
        self.driver = driver

    def findElement(self,key):
        ###这里必须要指定参数名，因为两个形参都可为空
        value = readIni.getValue(key=key)
        by = value.split(">")[0]
        eleInfo = value.split(">")[1]
        print("by----->",by)
        print("eleInfo----->",eleInfo)
        try:
            if by == "id":
                element = self.driver.find_element_by_id(eleInfo)
            elif by == "name":
                element = self.driver.find_element_by_name(eleInfo)
            elif by == "className":
                element = self.driver.find_element_by_class_name(eleInfo)
            elif by == "xpath":
                element = self.driver.find_element_by_xpath(eleInfo)
            elif by == "tagName":
                element = self.driver.find_element_by_tag_name(eleInfo)
        except:
            print("findElement函数定位元素失败------------>")
            element = None

        return element

if(__name__ == "__main__"):
    try:
        driver = webdriver.Chrome()
        driver.get("http://www.5itest.cn/register")
        time.sleep(5)
        find = FindElement(driver)
        element = find.findElement("code")
        print("下面开始验证是否获取到了准确的元素-------->")
        element.send_keys("123456")
        print(element)
        print(element.get_attribute("value"))
        print(element.get_attribute("class"))
        print(element.get_attribute("placeholder"))
    finally:#无论是否发生异常都会执行
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
            print("chrome driver进程不存在")
