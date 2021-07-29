#coding=utf-8
from PIL import Image
import base64
import urllib,urllib3,ssl,json
from chapter3.page.register_page import RegisterPage
class GetCode():
    def __init__(self,driver):
        self.driver = driver
        self.registerPage = RegisterPage(driver)

    def saveScreenshot(self,codePath):
        '''保存截图"D:\D1\code\AutoTest\python_ui_autotest\SeleniumPython\chapter2\image\shot1.png"'''
        self.driver.save_screenshot(codePath)

    def saveCodeImage(self,codePath):
        '''(供外部调用）保存验证码图片'''
        '''1.保存注册页面截图'''
        self.saveScreenshot(codePath)
        '''2.定位到矩形区域'''
        verifyCodeEle = self.registerPage.findCodeImageElement()
        loc = verifyCodeEle.location     #<class 'dict'> || {'x': 552, 'y': 527}
        left = loc.get("x")
        top = loc.get("y")
        #注意verifyCodeEle.size是dict，需要通过get方法
        right = verifyCodeEle.size.get("width") + left
        height = verifyCodeEle.size.get("height") + top
        print(left,top,right,height)
        '''3.裁剪保存,使用Pillow对图片进行裁剪'''
        #获取窗口可视范围的width和height
        html = self.registerPage.findHtmlElement()

        #设置图片重新打开的width和height
        resize_width = html.size['width']
        resize_height = html.size['height']

        #resize图片,调整分辨率
        img = Image.open(codePath)
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
        #先调用一下保存生成验证码图片

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

