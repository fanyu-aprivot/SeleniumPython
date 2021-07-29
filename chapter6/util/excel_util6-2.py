#coding=utf-8
import os
import xlrd
class ExcelUtil():
    def __init__(self,excelPath = None,sheetIndex = None):
        if excelPath == None:
            excelPath = os.path.join(os.getcwd(),"chapter5/data/register_casedata.xlsx")
        else:
            excelPath = os.path.join(os.getcwd(),excelPath)
        
        if sheetIndex == None:
            sheetIndex = 0
        
        #打开Excel，获取Excel全部数据
        self.data = xlrd.open_workbook(excelPath)
        #获取指定sheet页
        self.table = self.data.sheets()[sheetIndex]
        
    def getRows(self):
        '''获取行数'''
        rows = self.table.nrows
        return rows

    def getCols(self):
        '''获取列数'''
        cols = self.table.ncols
        return cols

    def getCellValue(self,row,col):
        '''获取指定单元格内容'''
        value = self.table.cell(row,col).value
        return value

    def getCellType(self,row,col):
        '''获取指定单元格数据类型'''
        ctype = self.table.cell(row,col).ctype
        return ctype

    def writeCellValue(self,row,col):
        '''向指定单元格写数据'''
        self.


    def getData(self):
        '''以list的形式返回Excel里sheet的数据'''
        result = []
        curList = []
        for i in range(self.getRows()):
            #获取指定行的数据
            print("*******************************************")
            for j in range(self.getCols()):
                # print(type(self.table.cell(i, j)),"||",self.table.cell(i, j))
                ctype = self.getCellType(i,j) #获取表格数据类型
                print(self.table.cell(i, j),",ctype--->",ctype)
                '''ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error'''
                if ctype == 2:  #如果是number类型就转为str类型
                    curList.append(str(int(self.getCellValue(i,j))))
                else:
                    curList.append(self.getCellValue(i,j))
            print("*******************************************")
            result.append(curList)
            curList = []
            # rowVal = self.table.row_values(i)
            # result.append(rowVal)
        return result


excelUtil = ExcelUtil(excelPath = "chapter6/data/register_keywords.xls")
if(__name__ == "__main__"):
    print("Excel-sheet[0]全部数据list是：",excelUtil.getData())
    print("行下标为100列下标为2的单元格内容是：",excelUtil.getCellValue(100,2))
