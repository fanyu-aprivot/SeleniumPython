#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter6.util.excel_util import ExcelUtil
from chapter6.keyword.action_method import actionMethod

class KeywordCase:
    def __init__(self):
        pass

    def runMain(self):
        handleExcel = ExcelUtil(excelPath="chapter6/data/register_keywords.xls")
        
