'''
读取ini配置文件
'''
#coding=utf-8
import configparser

cf = configparser.ConfigParser()
cf.read("D:/D1/code/AutoTest/python_ui_autotest/SeleniumPython/chapter2/config/local_element.ini")
var = cf.get("register_element","register_button")
print("var---->",var)
print("type(var)---->",type(var))