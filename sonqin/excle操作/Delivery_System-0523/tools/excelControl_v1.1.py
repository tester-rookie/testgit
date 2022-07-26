#-*- coding: utf-8 -*-
#@File    : excelControl_v1.1.py
#@Time    : 2021/5/26 22:48
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/26 
print()
"""
目标：使用excel测试用例实现登录接口的自动化测试！
流程：
    1- 测试接口文档-----ok
    2- 测试用例文件-----ok
    3- 实现登录接口的代码编辑---ok
    4- 读取测试用例-----x
    5- 登录接口结合excel用例实现自动化测试！-----x
"""

#----------------读取excel用例数据-----------------------

#---------------版本迭代-------------------
"""
版本：v1.1
功能描述：
    1- 可以用户选择任何列数据  
        1- 列编号  9,11
        2- 列名--更适合！URL 前置条件
    2- 分类筛选
        1- 全部执行   -all
        2- 分段执行   tc003-tc007
        3- 随机执行   tc001,tc007,tc009
        4- 复合场景   ['tc001','tc004-tc007','tc009']
"""

import xlrd#只能操作  xls，不能操作xlxs
def get_excel_data(excelDir,sheetName,caseName,*colName):
    """
    :param excelDir: excel路径
    :param sheetName: 操作的表名
    :param caseName: #获取的用例名
    :return: 返回一个list
    :*args：不定项列名
    """
    #1- 打开/加载excel文件---
    #formatting_info=True  保持excel样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #3- 获取需要操作的表
    workSheet = workBook.sheet_by_name(sheetName)

    #---------思路的转换------------
    #背景：用户输入的列名，但是python处理获取对应列的数据使用的列编号！
    colIdex = []#列名的下标存放！
    for i in colName:
        #workSheet.row_values(0)--第0行数据 是一个列表，列表通过值取 下标 index
        colIdex.append(workSheet.row_values(0).index(i))
    print("列名下标>>>",colIdex)
    #-----------------------------


    idex = 0#行的初始值
    resList = []#返回的结果！
    for one in workSheet.col_values(0):
        #1- 筛选用例:无效的用例/不相关的接口用例
        if caseName in one:
            getColData = []#列表获取到的数据组合
            for num in colIdex:#遍历列名下标
                res = workSheet.cell(idex,num).value
                getColData.append(res)#这个是列存放列表！
            #每一组数据 （请求数据，响应期望数据）
            resList.append(getColData)#resList  行存放列表
        idex += 1#
    return resList



if __name__ == '__main__':
    res = get_excel_data('../data/testCaseFile_V1.5.xls',"登录模块","Login","用例编号",
                         "请求方式","请求参数")
    for one in res:
        print(one)