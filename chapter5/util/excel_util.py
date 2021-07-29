#coding=utf-8
import os
import xlrd
class ExcelUtil():
    def __init__(self,excelPath = None,sheetIndex = None):
        if excelPath == None:
            excelPath = os.path.join(os.getcwd(),"chapter5/data/register_casedata.xlsx")
        if sheetIndex == None:
            sheetIndex = 0
        #打开Excel，获取Excel全部数据
        self.data = xlrd.open_workbook(excelPath)
        #获取指定sheet页
        self.table = self.data.sheets()[sheetIndex]
        #获取行数
        self.rows = self.table.nrows
        self.cols = self.table.ncols

    def getData(self):
        '''以list的形式返回Excel里sheet的数据'''
        result = []
        curList = []
        for i in range(self.rows):
            #获取指定行的数据
            print("*******************************************")
            for j in range(self.cols):
                # print(type(self.table.cell(i, j)),"||",self.table.cell(i, j))
                ctype = self.table.cell(i, j).ctype  #获取表格数据类型
                print(self.table.cell(i, j),",ctype--->",ctype)
                '''ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error'''
                if ctype == 2:  #如果是number类型就转为str类型
                    curList.append(str(int(self.table.cell(i, j).value)))
                else:
                    curList.append(self.table.cell(i, j).value)
            print("*******************************************")
            result.append(curList)
            curList = []
            # rowVal = self.table.row_values(i)
            # result.append(rowVal)
        return result


excelUtil = ExcelUtil()
if(__name__ == "__main__"):
    print(excelUtil.getData())
