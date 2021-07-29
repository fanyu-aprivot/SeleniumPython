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
                isRun = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","is_run")))
                if isRun == "yes":
                    #handleIni.getValue("register_case","case_id")从配置文件读取出来的是str类型还需要转一下
                    caseId = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","case_id")))
                    print(caseId,"--->在执行")
                    function = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","function")))
                    sendValue = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","send_value")))
                    print("sendValue--->",type(sendValue),"||",sendValue)
                    handleElement = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","handle_element")))
                    print("handleElement--->",type(handleElement),"||",handleElement)
                    res = self.runMethod(function,sendValue,handleElement)
                    print(caseId,"--->执行结束，结果是--->",res)
                    print("----------------------",caseId,"  over--------------------")


    def runMethod(self,methodName,sendValue,handleElement):
        '''利用反射运行methodName对应的函数'''
        #第三个参数表示找不到对应的函数则返回None
        method = getattr(actionMethod, methodName,None)
        if method and sendValue and handleElement:
            print("runMethod---------->进入if 1分支")
            #调用底层传入先定位元素后值
            method(handleElement,sendValue)
            return True
        elif method and sendValue:
            print("runMethod---------->进入if 2分支")
            method(sendValue)
            return True  
        elif method and handleElement:
            print("runMethod---------->进入if 3分支")
            method(handleElement)
            return True
        #################增加代码如下，以覆盖无参函数的情形
        elif method:
            print("runMethod---------->进入if 4分支")
            method()
            return True

        return False

if(__name__ == "__main__"):
    try:
        keywordCase = KeywordCase()
        keywordCase.runMain()
    finally:
        try:
            os.system('taskkill /im chromedriver.exe /F')
        except:
                print("chrome driver进程不存在")
