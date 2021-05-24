#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: dependent_data.py


from util.operation_excel import OperationExcel
from base.method import RunMethod
from util.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json


class DependentData:
    """解决数据依赖问题"""

    def __init__(self, case_id, file_name, sheet_id=0):
        self.case_id = case_id
        self.file_name = file_name
        self.sheet_id = sheet_id

    def get_case_line_data(self):
        """
        通过case_id去获取该case_id的整行数据
        :param case_id: 用例ID
        :return:
        """
        opera_excel = OperationExcel(self.file_name, self.sheet_id)
        rows_data = opera_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependent(self):
        """
        执行依赖测试，获取结果
        :return:
        """
        run_method = RunMethod()
        opera_excel = OperationExcel(self.file_name, self.sheet_id)
        row_num = opera_excel.get_row_num(self.case_id)
        data = GetData(self.file_name, self.sheet_id)
        request_data = data.get_data_for_json(row_num)
        method = data.get_request_method(row_num)
        url = data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data)
        return json.loads(res)

    def get_data_for_key(self, row):
        """
        根据依赖的key去获取执行依赖case的响应然后返回
        :return:
        """
        data = GetData(self.file_name, self.sheet_id)
        depend_data = data.get_depend_key(row)
        response_data = self.run_dependent()
        return [match.value for match in parse(depend_data).find(response_data)][0]
