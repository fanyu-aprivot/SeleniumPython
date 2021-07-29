#coding=utf-8
from PIL import Image
import pytesseract


#非规则性
image = Image.open("D:\D1\TestDevelopment\data\SeleniumData\shot2.png")
text = pytesseract.image_to_string(image)
print("非规则性图片读取----->",text)

#非规则性
image1 = Image.open("D:\D1\TestDevelopment\data\SeleniumData\shot3.webp")
text1 = pytesseract.image_to_string(image1)
print("规则性图片读取----->",text1)