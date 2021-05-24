#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: get_data.py


from util import data_config
from util.operation_excel import OperationExcel
import json


class GetData:
    """获取excel数据"""

    def __init__(self, file_name, sheet_id=0):
        self.opera_excel = OperationExcel(file_name, sheet_id)

    def get_case_lines(self):
        """获取excel行数，即case的个数"""
        return self.opera_excel.get_lines()

    def get_is_run(self, row):
        """获取是否执行"""
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        """
        是否携带header
        :param row: 行号
        :return:
        """
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    def get_request_method(self, row):
        """
        获取请求方式
        :param row: 行号
        :return:
        """
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    def get_request_url(self, row):
        """
        获取url
        :param row: 行号
        :return:
        """
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    def get_request_data(self, row):
        """
        获取请求数据
        :param row:行号
        :return:
        """
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    def get_data_for_json(self, row):
        """
        通过关键字拿到data数据
        :param row:
        :return:
        """
        data = self.get_request_data(row)
        request_data = json.loads(data)
        return request_data

    def get_expcet_data(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == "":
            return None
        else:
            return expect

    def write_result(self, row, text):
        """
        写入结果数据
        :param row:
        :param col:
        :return:
        """
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, text)

    def write_test_result(self, row, text):
        """
        写入测试结果
        :param row:
        :param col:
        :return:
        """
        col = int(data_config.get_test_result())
        self.opera_excel.write_value(row, col, text)

    def get_depend_key(self, row):
        """
        获取依赖数据的key
        :param row:行号
        :return:
        """
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    def is_depend(self, row):
        """
        判断是否有case依赖
        :param row:行号
        :return:
        """
        col = int(data_config.get_case_depend())  # 获取是否存在数据依赖列
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_depend_field(self, row):
        """
        获取依赖字段
        :param row:
        :return:
        """
        col = int(data_config.get_field_depend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data

    def get_datas(self):
        """
        获取所有用例
        :return:
        """
        datas = []
        rows = self.get_case_lines()
        for r in range(1, rows):
            data = self.opera_excel.get_row_value(r)
            datas.append(data)
        return datas


# if __name__ == '__main__':
#     data = GetData('../data/case.xlsx')
#     print(data.get_datas())
#     data1 = data.get_datas()
#     datas = data.get_datas()
#     datas = tuple(datas)
#     print(datas)
#     print(data1[0])
#     print(data1[0][0])
#     print(GetData('../data/case.xlsx').get_datas()[0])
