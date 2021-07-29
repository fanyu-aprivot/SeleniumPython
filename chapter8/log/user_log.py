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

logger = logging.getLogger()
#将打印出包括这个等级及这个等级之上级别的日志
logger.setLevel(level=logging.INFO)

#创建输出到控制台的handler
consoleHandler = logging.StreamHandler()
#添加handler
logger.addHandler(consoleHandler)
logger.debug("this is my debug log")  #debug级别的日志信息将不被输出
logger.info("this is my info log")
logger.error("this is my error log")
logger.critical("this is my critical log")

#记得关闭
consoleHandler.close()
logger.removeHandler(consoleHandler)