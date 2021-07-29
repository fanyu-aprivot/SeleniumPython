#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
import time

#1.创建Chrome的driver
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.5itest.cn/register")
time.sleep(5)
'''根据id取邮箱对应的元素'''
driver.find_element_by_id("register_email").send_keys("490718870@qq.com")

# driver.find_element_by_class_name("controls").find_element_by_class_name("form-control").send_keys("1111sds")
'''根据父亲class取到的list，取第二个元素就是用户名输入框对应的元素'''
user_father_ele = driver.find_elements_by_class_name("controls")[1]
# print(len(user_father_ele))
user_ele = user_father_ele.find_element_by_class_name("form-control")
# print(len(user_ele))
user_ele.send_keys("fanyu")

'''根据name取密码对应的元素'''
driver.find_element_by_name("password").send_keys("123456")
'''根据xpath取验证码对应的元素'''
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("abcde")
