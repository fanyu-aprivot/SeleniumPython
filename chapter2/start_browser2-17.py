#coding=utf-8
from selenium import webdriver
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
import os
import random
import base64
import urllib, urllib.request, sys,urllib.parse
import ssl
import json
#urllib2模块直接导入就可以用，在python3中urllib2被改为urllib.request
'''全局变量driver'''
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)
# driver = webdriver.Chrome()
def initDriver():
    '''初始化driver'''
    driver.get("http://www.5itest.cn/register")
    #等待页面加载完毕
    time.sleep(5)

def findElement(key):
    '''根据id定位获取元素'''
    element = driver.find_element_by_id(key)
    return element

def getRandomValue():
    '''获取随机输入值'''
    randomVal = "".join(random.sample("1234567abcdefg",6))
    return randomVal

def saveScreenshot(shotPath):
    '''保存注册页面截图"D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\shot1.png"'''
    driver.save_screenshot(shotPath)

def saveCode(shotPath,codePath):
    '''保存验证码图片'''
    '''2.定位到矩形区域'''
    verifyCodeEle = driver.find_element_by_id("getcode_num")
    loc = verifyCodeEle.location     #<class 'dict'> || {'x': 552, 'y': 527}
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

    #resize图片,调整分辨率
    img = Image.open(shotPath)
    resize_img = img.resize((resize_width, resize_height), Image.BILINEAR)
    cropped = resize_img.crop((left, top, right, height))   #左，上，右，下
    cropped.save(codePath)
'''*****************************************************************************'''
def getBase64Code(codePath):
    '''python生成图片的base64编码'''
    with open (codePath,'rb') as f:
        base64_data=base64.b64encode(f.read())
        s=base64_data.decode()
        data='data:image/jpeg;base64,%s'%s
        return data

def getTextFromCode(codePath):
    '''阿里云解析验证码图片，返回验证码中文字信息'''
    base64Code = getBase64Code(codePath)
    host = 'https://302307.market.alicloudapi.com'
    path = '/ocr/captcha'
    method = 'POST'
    appcode = 'd23f3e0a2af44de7a95503d8355134d0'
    querys = ''
    bodys = {}
    url = host + path

    bodys['image'] = base64Code
    bodys['maxlength'] = "5"
    bodys['minlength'] = "5"
    bodys['type'] = "5002"
    ##将自定义data转换成标准格式，其中，
    #urlencode函数作用是将字符串进行url编码
    #.encode函数：提交类型不能为str，需要为byte类型
    post_data = urllib.parse.urlencode(bodys).encode('utf-8')
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    #根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    #发送请求，返回响应
    response = urllib.request.urlopen(request, context=ctx)
    #read()读取内容，需要decode（）解码，转换成str类型
    content = response.read().decode('utf-8')
    if (content):
        print("content is------>",content)
    #str转成dict
    res = json.loads(content)["data"]["captcha"]
    print("res is------>",res)
    return res
'''*****************************************************************************'''



def main():
    try:
        initDriver()
        shotPath = "D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\shot.png"
        codePath = "D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\code.png"

        randomEmail = getRandomValue() + "@163.com"
        randomUserName = getRandomValue()
        randomPass = getRandomValue()
        findElement("register_email").send_keys(randomEmail)
        findElement("register_nickname").send_keys(randomUserName)
        findElement("register_password").send_keys(randomPass)

        saveScreenshot(shotPath)
        saveCode(shotPath,codePath)
        verifyCode = getTextFromCode(codePath)
        findElement("captcha_code").send_keys(verifyCode)

        time.sleep(5)
        findElement("register-btn").click()  #点击注册按钮
        

    finally:#无论是否发生异常都会执行
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
            print("chrome driver进程不存在")

main()