#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import random
#1.创建Chrome的driver
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.5itest.cn/register")
#等待页面加载完毕
time.sleep(5)

for item in range(5):
    # input_email = random.sample([1,2,3,4,5,'a','b','c','d','e'],5)
    
    resList = random.sample([1,2,3,4,5,'a','b','c','d','e'],5)
    '''list转为str类型'''
    input_email = ''.join([str(x) for x in resList]) + "@163.com"
    print(input_email)


try:
    os.system('taskkill /im chromedriver.exe /F')
except:
    print("chrome driver进程不存在")