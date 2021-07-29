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
                    #执行case
                    res = self.runMethod(function,sendValue,handleElement)
                    print(caseId,"--->执行结束，结果是--->",res)
                    #预期结果判断逻辑
                    expectResult = handleExcel.getCellValue(i,int(handleIni.getValue("register_case","expect_result")))
                    if expectResult:#不为None且不为空
                        expectList = self.getExpectList(expectResult)
                        expectFunction = expectList[0]
                        expectValue = expectList[1]
                        if expectFunction == "getUrlTitle":
                            executeResult = self.runMethod(expectFunction)
                            print("expectValue--->",expectValue)
                            print("executeResult--->",executeResult)
                            if expectValue in executeResult:
                                print("与预期相符，正在写入实际结果---pass")
                                handleExcel.writeCellValue(i,int(handleIni.getValue("register_case","actual_result")),"pass")
                            else:
                                print("与预期不相符，正在写入实际结果---fail")
                                handleExcel.writeCellValue(i,int(handleIni.getValue("register_case","actual_result")),"fail")
                        elif expectFunction == "getElement":
                            executeResult = self.runMethod(expectFunction,handleElement = expectValue)
                            print("executeResult--->",executeResult)
                            if executeResult:
                                print("与预期相符，正在写入实际结果---pass")
                                handleExcel.writeCellValue(i,int(handleIni.getValue("register_case","actual_result")),"pass")
                            else:
                                print("与预期不相符，正在写入实际结果---fail")
                                handleExcel.writeCellValue(i,int(handleIni.getValue("register_case","actual_result")),"fail")
                        else:
                            print("*******暂时未找到该预期函数判断*******")
                    else:
                        print(caseId,"----->expectResult为空")
                    
                    print("----------------------",caseId,"  over--------------------")

    def getExpectList(self,expectResult):
        '''返回分割后的list，如getUrlTitle=注册--->["getUrlTitle","注册"]'''
        expectList = expectResult.split("=")
        return expectList

    def runMethod(self,methodName,sendValue = None,handleElement = None):
        '''利用反射运行methodName对应的函数'''
        #第三个参数表示找不到对应的函数则返回None
        method = getattr(actionMethod, methodName,None)
        if method and sendValue and handleElement:
            print("runMethod---------->进入if 1分支")
            #调用底层传入先定位元素后值
            result = method(handleElement,sendValue)
            return result
        elif method and sendValue:
            print("runMethod---------->进入if 2分支")
            result = method(sendValue)
            return result  
        elif method and handleElement:
            print("runMethod---------->进入if 3分支")
            result = method(handleElement)
            return result
        #增加代码如下，以覆盖无参函数的情形
        elif method:
            print("runMethod---------->进入if 4分支")
            result = method()
            return result
        else:
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
