#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: test_api.py


import pytest
from base.method import RunMethod
from util.get_data import GetData
from util.dependent_data import DependentData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
from config import RunConfig
import json


class Test_Api:

    @pytest.mark.parametrize('args', GetData(RunConfig.file_path, RunConfig.sheet_id).get_datas())
    def test_case(self, args):
        row = int(args[0][-1])
        is_run = args[3]
        if is_run == 'yes':
            url = args[2]
            method = args[4]
            request_data = args[9]
            expect = args[10]
            header = args[5]
            depend_case = args[6]
            request_data = json.loads(request_data)

            if 'case' in depend_case:
                depend_data = DependentData(depend_case, RunConfig.file_path, RunConfig.sheet_id)
                # 获取依赖的响应数据
                depend_response_data = depend_data.get_data_for_key(row)
                # 获取依赖的key
                depend_key = GetData(RunConfig.file_path, RunConfig.sheet_id).get_depend_field(row)
                # 更新请求字段
                request_data[depend_key] = depend_response_data
            # 如果header字段值为write则将该接口的返回的token写入到token.json文件，如果为yes则直接读取token.json文件
            if header == "write":
                res = RunMethod().run_main(method, url, request_data)
                op_header = OperationHeader(res)
                op_header.write_token()
            elif header == 'yes':
                op_json = OperationJson(RunConfig.token_file)
                token = op_json.get_data('data')
                # 把请求数据与登录token合并，并作为请求数据
                request_data = dict(request_data, **token)

                res = RunMethod().run_main(method, url, request_data)
            else:
                res = RunMethod().run_main(method, url, request_data)

            if expect:
                if res in expect:
                    GetData(RunConfig.file_path, RunConfig.sheet_id).write_result(row, res)
                    GetData(RunConfig.file_path, RunConfig.sheet_id).write_test_result(row, "Pass")
                else:
                    GetData(RunConfig.file_path, RunConfig.sheet_id).write_result(row, res)
                    GetData(RunConfig.file_path, RunConfig.sheet_id).write_test_result(row, 'Fail')
            else:
                print(f"用例ID：case-{row}，预期结果不能为空")

            assert res in expect
        else:
            # 跳过测试
            GetData(RunConfig.file_path, RunConfig.sheet_id).write_test_result(row, "Skip")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_api.py"])
