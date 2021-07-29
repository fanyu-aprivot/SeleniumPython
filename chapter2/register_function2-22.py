#coding=utf-8
import os,sys
print("register_function2-22.py当前工程目录------->",os.getcwd())
sys.path.append(os.getcwd())
from selenium import webdriver
import time
from chapter2.util.find_element import FindElement
import random
from PIL import Image
import base64
import urllib, urllib.request,urllib.parse
import ssl
import json
class RegisterFunction:
    def __init__(self,url):
        '''构造函数'''
        self.driver = self.initDriver(url)

    def initDriver(self,url):
        '''初始化driver'''
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        #最大化窗口
        driver.maximize_window()
        #等待页面加载完毕
        time.sleep(5)
        return driver

    def getElement(self,key):
        '''定位元素'''
        ###driver传进去，初始化FindElement对象
        findElement = FindElement(self.driver)
        element = findElement.findElement(key)
        return element

    def sendInputVal(self,key,val):
        '''(供外部调用）模拟输入'''
        element = self.getElement(key)
        element.send_keys(val)

    def getRandomValue(self):
        '''(供外部调用）获取随机输入值'''
        randomVal = "".join(random.sample("1234567abcdefg",6))
        return randomVal

    # def saveScreenshot(self,shotPath):
    #     '''保存注册页面截图"D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\shot1.png"'''
    #     self.driver.save_screenshot(shotPath)

    def saveCodeImage(self,shotPath,codePath):
        '''(供外部调用）保存验证码图片'''
        '''1.保存注册页面截图'''
        self.driver.save_screenshot(shotPath)
        '''2.定位到矩形区域'''
        verifyCodeEle = self.getElement("code_image")
        loc = verifyCodeEle.location     #<class 'dict'> || {'x': 552, 'y': 527}
        left = loc.get("x")
        top = loc.get("y")
        #注意verifyCodeEle.size是dict，需要通过get方法
        right = verifyCodeEle.size.get("width") + left
        height = verifyCodeEle.size.get("height") + top
        print(left,top,right,height)
        '''3.裁剪保存,使用Pillow对图片进行裁剪'''
        #获取窗口可视范围的width和height
        html = self.getElement("html")

        #设置图片重新打开的width和height
        resize_width = html.size['width']
        resize_height = html.size['height']

        #resize图片,调整分辨率
        img = Image.open(shotPath)
        resize_img = img.resize((resize_width, resize_height), Image.BILINEAR)
        cropped = resize_img.crop((left, top, right, height))   #左，上，右，下
        cropped.save(codePath)

    def getBase64Code(self,codePath):
        '''python生成图片的base64编码'''
        with open (codePath,'rb') as f:
            base64_data=base64.b64encode(f.read())
            s=base64_data.decode()
            data='data:image/jpeg;base64,%s'%s
            return data

    def getTextFromCode(self,codePath):
        '''(供外部调用）阿里云解析验证码图片，返回验证码中文字信息'''
        base64Code = self.getBase64Code(codePath)
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

    def main(self):
        try:
            shotPath = "D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\shot.png"
            codePath = "D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\code.png"
            randomVal = self.getRandomValue()
            self.sendInputVal("email",randomVal + "@qq.com")
            self.sendInputVal("username",randomVal)
            self.sendInputVal("password","123456")

            self.saveCodeImage(shotPath,codePath)
            code = self.getTextFromCode(codePath)
            self.sendInputVal("code",code)
            time.sleep(2)
            self.getElement("register_button").click()
            time.sleep(5)
        finally:#无论是否发生异常都会执行
            try:
                os.system('taskkill /im chromedriver.exe /F')
            except:
                print("chrome driver进程不存在")

if(__name__ == "__main__"):
    url = "http://www.5itest.cn/register"
    registerFunction = RegisterFunction(url)
    registerFunction.main()
