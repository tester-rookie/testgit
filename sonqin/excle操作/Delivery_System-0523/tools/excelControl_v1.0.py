#-*- coding: utf-8 -*-
#@File    : excelControl_v1.0.py
#@Time    : 2021/5/26 20:16
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
"""
需求：实现一个excel用例读取功能
版本:v1.0
具体功能：
    1- 读取指定的数据
    2- 具备过滤一些无效用例
实现方案：
    1- 打开excel文件
    2- 读取对应数据
    3- 过滤数据
    4- 关闭
"""
import xlrd#只能操作  xls，不能操作xlxs
def get_excel_data(excelDir,sheetName,caseName):
    """
    :param excelDir: excel路径
    :param sheetName: 操作的表名
    :param caseName: #获取的用例名
    :return: 返回一个list
    """
    #1- 打开/加载excel文件---
    #formatting_info=True  保持excel样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #2- 查看excel有哪些子表
    #print(workBook.sheet_names())

    #3- 获取需要操作的表
    workSheet = workBook.sheet_by_name(sheetName)

    #4- excel表--代码操作从下标0开始
    # print(workSheet.row_values(0))#0 行
    # print(workSheet.col_values(0))  # 0 列

    #5- 获取某一个单元格数据
    #print(workSheet.cell().value)#cell(行编号，列编号)
    idex = 0#行的初始值
    resList = []#返回的结果！
    for one in workSheet.col_values(0):
        #1- 筛选用例:无效的用例/不相关的接口用例
        if caseName in one:
            #请求参数
            reqData = workSheet.cell(idex,9).value
            #响应预期数据
            expData = workSheet.cell(idex,11).value
            #每一组数据 （请求数据，响应期望数据）
            resList.append((reqData,expData))
        idex += 1#
    return resList



if __name__ == '__main__':
    res = get_excel_data('../data/testCaseFile_V1.5.xls',"我的商铺","listshopping")
    for one in res:
        print(one)
