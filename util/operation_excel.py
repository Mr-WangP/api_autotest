#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp 
# @Time: 2021/5/23 22:17
# @File: operation_excel.py


import xlrd
import openpyxl


class OperationExcel:
    """操作excel"""

    def __init__(self, file_name, sheet_id=0):
        self.file_name = file_name
        self.sheet_id = sheet_id

    def get_data(self):
        """
        获取sheets的内容
        :return:
        """
        book = xlrd.open_workbook(self.file_name)
        Sheets = book.sheets()[self.sheet_id]
        return Sheets

    def get_lines(self):
        """
        获取单元格行数
        :return:
        """
        rows = self.get_data().nrows
        return rows

    def get_cell_value(self, row, col):
        """
        获取单元格数据
        :param row: 行
        :param col: 列
        :return:
        """
        cell = self.get_data().cell_value(row, col)
        return cell

    def write_value(self, row, col, text):
        """
        回写数据到excel
        :param row:行
        :param col:列
        :param value:值
        :return:
        """
        book = openpyxl.load_workbook(self.file_name)
        sheet_data = book.worksheets[self.sheet_id]
        sheet_data.cell(row+1, col+1).value = text
        book.save(self.file_name)

    def get_row_data(self, case_id):
        """
        根据对应的case_id获取对应行的内容
        :param case_id: 用例id
        :return:
        """
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data

    def get_row_num(self, case_id):
        """
        根据case_id获取对应行号
        :param case_id:
        :return:
        """
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1
        return num

    def get_row_value(self, row):
        """
        根据行号，找到该行的内容
        :param row:行号
        :return:
        """
        row_data = self.get_data().row_values(row)
        return row_data

    def get_cols_data(self, col_id=None):
        """
        获取某一列的内容
        :param col_id:列号
        :return:
        """
        if col_id is not None:
            col_data = self.get_data().col_values(col_id)
        else:
            col_data = self.get_data().col_values(0)
        return col_data


# if __name__ == '__main__':
#     opera = OperationExcel('../data/case.xlsx')
#
#     opera.get_data()
#     print(opera.get_data())
#     print(opera.get_data().nrows)        # 获取表格总行数
#     print(opera.get_lines())             # 获取表格总行数
#     print(opera.get_cell_value(1, 2))    # 获取第2行、第3列单元格数据
#     print(opera.get_row_data('case2'))   # 获取id为case2的整行数据
#     print(opera.get_row_num('case2'))    # 获取id为case2的行数
#     print(opera.get_row_value(2))        # 获取第3行数据
#     print(opera.get_cols_data(2))        # 获取第3列数据
#     # opera.write_value(3, 2, '模块2')
#     # print(opera.get_cell_value(2, 1))
