#coding=utf-8
from selenium import webdriver

#3.创建edge的driver
driver = webdriver.Edge(executable_path="msedgedriver.exe")

#2.创建Firefox的driver
# driver = webdriver.Firefox()

#1.创建Chrome的driver
# option = webdriver.ChromeOptions()
# # 防止打印一些无用的日志
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.baidu.com")
