#coding=utf-8
import os,sys
sys.path.append(os.getcwd())
from chapter6.util.excel_util import ExcelUtil
from chapter6.keyword.action_method import actionMethod
from chapter6.util.read_ini import ReadIni

class KeywordCase:
    def __init__(self):
        pass

    def runMain(self):
        handleExcel = ExcelUtil(excelPath="chapter6/data/register_keywords.xls")
        handleIni = ReadIni(filePath="chapter6/config/keyword_case.ini")
        caseLines = handleExcel.getRows()
        if caseLines:
            for i in range(1,caseLines):
                isRun = handleExcel.getCellValue(i,handleIni.getValue("register_case","is_run"))
                if isRun == "yes":
                    function = handleExcel.getCellValue(i,handleIni.getValue("register_case","function"))
                    sendValue = handleExcel.getCellValue(i,handleIni.getValue("register_case","send_value"))
                    handleElement = handleExcel.getCellValue(i,handleIni.getValue("register_case","handle_element"))
                    res = self.runMethod(function,sendValue,handleElement)
                    print(res)


    def runMethod(self,methodName,sendValue,handleElement):
        '''利用反射运行methodName对应的函数'''
        #第三个参数表示找不到对应的函数则返回None
        method = getattr(actionMethod, methodName,None)
        if method and sendValue and handleElement:
            method(sendValue,handleElement)
            return True
        if method and sendValue:
            method(sendValue)
            return True  
        if method and handleElement:
            method(handleElement)
            return True

        return False
