#coding=utf-8
from ShowapiRequest import ShowapiRequest
from PIL import Image

r = ShowapiRequest("http://route.showapi.com/184-4","709433","62fc3f4e824e4213956d971c82126bca" )
r.addFilePara("image", "D:\D1\TestDevelopment\data\SeleniumData\shot2.png")
#3表示英文数字混合，5表示总共5位数
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
# text = res.json()["showapi_res_body"]["Result"]
print(res.text)

