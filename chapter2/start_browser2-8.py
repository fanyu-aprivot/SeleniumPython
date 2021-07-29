#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
#1.创建Chrome的driver
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.5itest.cn/register")
#等待页面加载完毕
time.sleep(5)

# element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")
print(WebDriverWait(driver,10).until(ec.visibility_of_element_located(locator)))
# driver.quit()
try:
    os.system('taskkill /im chromedriver.exe /F')
except:
    print("chrome driver进程不存在")