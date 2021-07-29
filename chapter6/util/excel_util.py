'''
最终版
'''
#coding=utf-8
import os
import xlrd
import xlutils
from xlutils.copy import copy
class ExcelUtil():
    def __init__(self,excelPath = None,sheetIndex = None):
        if excelPath == None:
            self.excelPath = os.path.join(os.getcwd(),"chapter5/data/register_casedata.xls")
        else:
            self.excelPath = os.path.join(os.getcwd(),excelPath)
        
        if sheetIndex == None:
            sheetIndex = 0
        
        #打开Excel，获取Excel全部数据
        #指定formatting_info，保存之前数据的格式
        self.data = xlrd.open_workbook(self.excelPath,formatting_info=True)
        #获取指定sheet页
        self.table = self.data.sheets()[sheetIndex]
        
    def getRows(self):
        '''获取行数,增加容错处理'''
        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            return None
       

    def getCols(self):
        '''获取列数,增加容错处理'''
        cols = self.table.ncols
        if cols >= 1:
            return cols
        else:
            return None

    def getCellValue(self,row,col):
        '''获取指定单元格内容,增加容错处理'''
        #加入容错处理
        if (self.getRows() != None) and (self.getCols() != None) and (row < self.getRows()) and (col < self.getCols()):
            ctype = self.getCellType(row,col)
            value = self.table.cell(row,col).value
            if ctype == 2:
                #####从Excel里获取到的是浮点型，需转为字符串类型
                value = str(int(value))
        else:
            value = None
        return value

    def getCellType(self,row,col):
        '''获取指定单元格数据类型,增加容错处理'''
        if (self.getRows() != None) and (self.getCols() != None) and (row < self.getRows()) and (col < self.getCols()):
            ctype = self.table.cell(row,col).ctype
        else:
            ctype = None
        return ctype

    def writeCellValue(self,row,col,value):
        '''（6-11更新修复写数据逻辑）向指定单元格写数据,返回为true表示写入成功,增加容错处理'''
        if (self.getRows() != None) and (self.getCols() != None) and (row < self.getRows()) and (col < self.getCols()):
            # print("row || col:",row,"||",col)
            # print("当前写入数据是：--->",value)
            #获取Excel全部数据,每次重新打开获取最新数据
            excelData = xlrd.open_workbook(self.excelPath,formatting_info=True)

            # print(excelData,"||",type(excelData))
            # print("第【",row,"】行写入前 当前actual_value列的列数据是：",excelData.sheets()[0].col_values(8, start_rowx=1, end_rowx=10))

            #获取到Excel的副本
            copyData = copy(excelData)
            #在副本的sheet1上面写
            copyData.get_sheet(0).write(row,col,value)
            #保存
            saveToPath = os.path.join(os.getcwd(),self.excelPath)
            copyData.save(saveToPath)
            # print("第【",row,"】行写入后 当前actual_value列的列数据是：",xlrd.open_workbook(self.excelPath,formatting_info=True).sheets()[0].col_values(8, start_rowx=1, end_rowx=10))
            # print("--------------第【",row,"】行测试结束---------------")
            res = True
        else:
            res = False
        return res

    def getData(self):
        '''以list的形式返回Excel里sheet的数据,增加容错处理'''
        result = []
        curList = []
        rows = self.getRows()
        cols = self.getCols()
        #存在行列数时才执行获取数据操作，组装result并返回
        #否则直接返回None即可
        if rows and cols:
            for i in range(rows):
                #获取指定行的数据
                print("*******************************************")
                for j in range(cols):
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
        else:
            result = None
        return result


excelUtil = ExcelUtil(excelPath = "chapter6/data/register_keywords.xls")
if(__name__ == "__main__"):
    # print("Excel-sheet[0]全部数据list是：",excelUtil.getData())
    # print("行下标为100列下标为2的单元格内容是：",excelUtil.getCellValue(2,6))
    savePath = "chapter6/data/register_keywords_xlsx.xlsx"
    print(excelUtil.writeCellValue(1,6,"test1",savePath))
    
