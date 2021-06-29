#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: test_api.py


import json
import pytest
from base.method import RunMethod
from data.get_data import GetData
from config import RunConfig
from conftest import get_text, log


class Test_Api:

    @pytest.mark.parametrize('args', GetData(RunConfig.file_path).read_excel())
    def test_case(self, args):
        row = int(args[0][4:])
        col = len(args)

        #判断是否跳过测试
        if args[3] == 'yes':
            url = args[2]
            method = args[4]
            headers = args[5]
            if headers is not None:
                headers = json.loads(args[5])
            depend_case = args[6]
            request_data = json.loads(args[9])
            expect = args[10]

            #获取依赖用例的数据
            if depend_case:
                depend_data = GetData(RunConfig.file_path).read_excel()
                depend_data = depend_data[int(args[6][4:]) - 1]
                depend_res = RunMethod().run_method(method=depend_data[4], url=depend_data[2], data=json.loads(depend_data[9]), headers=depend_data[5])
                depend_res = depend_res.text
                # 获取依赖的key
                depend_key = args[8]
                # 获取依赖的响应数据
                depend_response_data = get_text(depend_res, depend_key)
                # 更新请求字段
                if args[7] == 'header':
                    headers[depend_key] = depend_response_data
                elif args[7] == 'data':
                    request_data[depend_key] = depend_response_data

            #获取响应
            log().info("开始发送{0}请求".format(args[0]))
            res = RunMethod().run_method(method=method, url=url, data=request_data, headers=headers)
            res = str(res.json())

            #写入响应结果
            GetData(RunConfig.file_path).write_excel(row + 1, col - 1, res)

            #断言
            try:
                assert expect == res
                GetData(RunConfig.file_path).write_excel(row + 1, col, "Pass")
                log().info("{0}请求发送成功".format(args[0]))
                return True
            except:
                GetData(RunConfig.file_path).write_excel(row + 1, col, 'Fail')
                log().info('{0}断言失败，{1}不等于{2}'.format(args[0], expect, res))
                return False

        else:
            log().info("跳过{0}请求".format(args[0]))
            GetData(RunConfig.file_path).write_excel(row + 1, col, "Skip")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_api.py"])
