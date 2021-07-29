'''
读取ini配置文件,重构封装
'''
#coding=utf-8
import configparser

class ReadIni:
    def __init__(self,filePath=None):
        '''构造方法'''
        if filePath == None:
            filePath = "D:/D1/code/AutoTest/python_ui_autotest/SeleniumPython/chapter3/config/local_element.ini"
        #cf是全局变量
        self.cf = self.loadIni(filePath)

    def loadIni(self,filePath):
        '''加载读取配置文件'''
        cf = configparser.ConfigParser()
        cf.read(filePath)
        return cf
        

    def getValue(self,node=None,key=None):
        '''获取配置文件指定section，指定key值'''
        if node == None:
            node = "register_element"
        if key == None:
            key = "username"
        var = self.cf.get(node,key)
        return var

readIni = ReadIni()
if(__name__ == "__main__"):
    print(readIni.getValue())