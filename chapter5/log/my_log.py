'''
日志级别：
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''

#coding=utf-8
import logging
import os,datetime

class MyLog:
    def __init__(self):
        self.logger = logging.getLogger()
        #将打印出包括这个等级及这个等级之上级别的日志
        self.logger.setLevel(level=logging.DEBUG)

        #####日志文件名称以当前时间命名
        #abspath获取当前文件的绝对路径，dirname获取当前文件所在的目录路径
        basePath = os.path.dirname(os.path.abspath(__file__))
        print("basePath--->",basePath)

        logsPath = os.path.join(basePath,"logs")
        print("logsPath--->",logsPath)

        #我们可以使用strftime()转换成我们想要的格式
        logName = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        print("logName--->",logName)

        logPath = os.path.join(logsPath,logName)
        print("logPath--->",logPath)

        #创建输出到文件的handler
        self.fileHandler = logging.FileHandler(filename=logPath,encoding="utf-8")
        #####日志文件名称以当前时间命名
        #为handler设置info日志级别
        self.fileHandler.setLevel(logging.INFO)
        #设置格式
        formatter = logging.Formatter(fmt = "%(asctime)s %(filename)s ---> %(funcName)s %(lineno)d %(levelname)s ---> %(message)s")
        self.fileHandler.setFormatter(formatter)

        #添加handler
        self.logger.addHandler(self.fileHandler)
        self.logger.debug("this is my debug log")  

        

    def getLogger(self):
        '''供外部调用，获取到getLogger'''
        return self.logger

    def close(self):
        '''供外部调用，关闭日志记录handler'''
        #记得关闭
        self.fileHandler.close()
        self.logger.removeHandler(self.fileHandler)