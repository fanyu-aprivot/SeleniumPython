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

logger = logging.getLogger()
#将打印出包括这个等级及这个等级之上级别的日志
logger.setLevel(level=logging.INFO)

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
fileHandler = logging.FileHandler(filename=logPath,encoding="utf-8")
#####日志文件名称以当前时间命名

#设置格式
formatter = logging.Formatter(fmt = "%(asctime)s %(filename)s ---> %(funcName)s %(lineno)d %(levelname)s ---> %(message)s")
fileHandler.setFormatter(formatter)

#添加handler
logger.addHandler(fileHandler)
logger.debug("this is my debug log")  #debug级别的日志信息将不被输出
logger.info("this is my info log")
logger.info("测试中文")
logger.error("this is my error log")
logger.critical("this is my critical log")

#记得关闭
fileHandler.close()
logger.removeHandler(fileHandler)