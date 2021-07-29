#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
import time
import os

#1.创建Chrome的driver
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.5itest.cn/register")
time.sleep(5)
title = ec.title_contains("注册")
print(title(driver))
title1 = ec.title_contains("哈哈")
print(title1(driver))

try:
    os.system('taskkill /im chromedriver.exe /F')
except:
    print("chrome driver进程不存在")


