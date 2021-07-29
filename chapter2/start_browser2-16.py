#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import random
from ShowapiRequest import ShowapiRequest
from PIL import Image

#1.创建Chrome的driver
option = webdriver.ChromeOptions()
# 防止打印一些无用的日志
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
driver.get("http://www.5itest.cn/register")
#等待页面加载完毕
time.sleep(5)
'''***********************************************************'''

try:
    '''0.输入邮箱，用户名，密码等'''
    resList = random.sample([1,2,3,4,5,'a','b','c','d','e'],5)
    input_email = ''.join([str(x) for x in resList]) + "@163.com"
    driver.find_element_by_id("register_email").send_keys(input_email)
    driver.find_element_by_id("register_nickname").send_keys("fanyu")
    driver.find_element_by_id("register_password").send_keys("123456")

    '''1.保存截图'''
    driver.save_screenshot("D:\D1\TestDevelopment\data\SeleniumData\shot1.png")

    '''2.获取位置'''
    verifyCodeEle = driver.find_element_by_id("getcode_num")
    loc = verifyCodeEle.location     #<class 'dict'> || {'x': 552, 'y': 527}
    # print(type(loc),"||",loc)
    '''坐标轴是向右为正，向下为正'''
    left = loc.get("x")
    top = loc.get("y")
    #注意verifyCodeEle.size是dict，需要通过get方法
    right = verifyCodeEle.size.get("width") + left
    height = verifyCodeEle.size.get("height") + top
    print(left,top,right,height)
    '''3.裁剪保存,使用Pillow对图片进行裁剪'''
    #获取窗口可视范围的width和height
    html = driver.find_element_by_tag_name("html")

    #设置图片重新打开的width和height
    resize_width = html.size['width']
    resize_height = html.size['height']

    #resize图片
    img = Image.open("D:\D1\TestDevelopment\data\SeleniumData\shot1.png")
    resize_img = img.resize((resize_width, resize_height), Image.BILINEAR)
    cropped = resize_img.crop((left, top, right, height))   #左，上，右，下
    cropped.save("D:\D1\TestDevelopment\data\SeleniumData\shot2.png")

    '''4.解析验证二维码并输入'''
    r = ShowapiRequest("http://route.showapi.com/184-4","709433","62fc3f4e824e4213956d971c82126bca" )
    r.addFilePara("image", "D:\D1\TestDevelopment\data\SeleniumData\shot2.png")
    #3表示英文数字混合，5表示总共5位数
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    print("type(res)----->",type(res))
    print("res.text----->",res.text)
    print("type(res.json())----->",type(res.json()))
    input_code = res.json()["showapi_res_body"]["Result"]
    print("二维码验证解析结果res.json()['showapi_res_body']['Result']------------》》",input_code)
    code_element = driver.find_element_by_id("captcha_code")
    code_element.send_keys(input_code)

finally:#无论是否发生异常都会执行
    try:
        os.system('taskkill /im chromedriver.exe /F')
    except:
        print("chrome driver进程不存在")
'''***********************************************************'''
