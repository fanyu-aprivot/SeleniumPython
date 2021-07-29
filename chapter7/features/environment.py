#coding=utf-8
from selenium import webdriver
import os

def before_all(context):
    option = webdriver.ChromeOptions()
    # 防止打印一些无用的日志
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    context.driver = webdriver.Chrome(chrome_options=option)

def after_all(context):
    try:
        os.system('taskkill /im chromedriver.exe /F')
    except:
        print("chrome driver进程不存在")