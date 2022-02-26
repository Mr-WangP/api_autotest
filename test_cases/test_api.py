#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2021/6/28 22:12
# @File : test_api.py

import json
import pytest
import allure
from base.method import RunMethod
from data.get_data import GetData
from config import RunConfig
from conftest import get_text
from logs.log import log


@allure.feature('接口请求测试')
class Test_Api:

    @allure.story('api测试')
    @pytest.mark.api
    @pytest.mark.parametrize('args', GetData(RunConfig.data_path).read_excel())
    def test_case(self, args):
        # 获取表格中id列case中的数字
        with allure.step('获取接口请求id'):
            id = args[0]
            row = int(id[4:])
            log().info("✅ 获取接口请求id：'{0}' ".format(id))
        # 获取表格中一行数据的长度
        col = len(args)

        # 判断是否跳过测试，若为yes，则继续进行该测试请求
        if args[3] == 'yes':
            # 获取接口请求url
            with allure.step('获取接口请求url'):
                url = args[2]
                log().info("✅ 获取{0}接口请求url：'{1}' ".format(id, url))
            # 获取接口请求类型
            with allure.step('获取接口请求类型'):
                method = args[4]
                log().info("✅ 获取{0}接口请求类型：'{1}' ".format(id, method))
            # 获取接口请求头参数
            with allure.step('获取接口请求头参数'):
                headers = args[5]
                if headers is not None:
                    headers = json.loads(args[5])
                log().info("✅ 获取{0}接口请求头参数：'{1}' ".format(id, headers))
            # 获取接口请求是否有依赖请求
            with allure.step('获取接口是否有依赖请求'):
                depend_case = args[6]
                log().info("✅ 获取{0}接口是否有依赖请求：'{1}' ".format(id, depend_case))
            # 获取接口请求参数
            with allure.step('获取接口请求参数'):
                request_data = json.loads(args[9])
                log().info("✅ 获取{0}接口请求参数：'{1}' ".format(id, request_data))
            # 获取接口请求预期结果
            with allure.step('获取接口请求预期结果'):
                expect = args[10]
                log().info("✅ 获取{0}接口请求预期结果：'{1}' ".format(id, expect))
            # 获取依赖用例请求的数据
            if depend_case:
                # 依赖用例接口请求
                with allure.step('获取依赖用例请求的数据'):
                    depend_data = GetData(RunConfig.data_path).read_excel()
                    depend_data = depend_data[int(args[6][4:]) - 1]
                    depend_res = RunMethod().run_method(
                        method=depend_data[4], url=depend_data[2], data=json.loads(depend_data[9]), headers=depend_data[5])
                    depend_res = depend_res.text
                    # 获取依赖的key
                    depend_key = args[8]
                    # 获取依赖的响应数据
                    depend_response_data = get_text(depend_res, depend_key)
                    # 更新请求字段
                    if args[7] == 'header':
                        headers[depend_key] = depend_response_data
                        log().info("✅ 获取{0}接口请求的依赖用例{1}的数据：{2}:'{3}',并作为{0}接口的请求头参数 "
                                   .format(id, depend_case, depend_key, depend_response_data))
                    elif args[7] == 'data':
                        request_data[depend_key] = depend_response_data
                        log().info("✅ 获取{0}接口请求的依赖用例{1}的数据：{2}:'{3}',并作为{0}接口的请求参数 "
                                   .format(id, depend_case, depend_key, depend_response_data))

            # 发送接口请求，获取响应数据
            with allure.step('送接口请求，获取响应数据'):
                res = RunMethod().run_method(method=method, url=url, data=request_data, headers=headers)
                res = str(res.json())

            # 向excel中写入响应结果
            with allure.step('向excel中写入响应结果'):
                GetData(RunConfig.data_path).write_excel(row + 1, col - 1, res)
                log().info("✅ {0}接口请求响应结果写入excel：{1} ".format(args[0], res))

            # 进行断言，比较接口请求实际结果和预期结果
            with allure.step('进行断言，比较接口请求实际结果和预期结果'):
                try:
                    assert expect == res
                    GetData(RunConfig.data_path).write_excel(row + 1, col, "Pass")
                    log().info("✅ {0}请求响应断言成功，写入接口测试结果为'Pass' ".format(args[0]))
                    return True
                except:
                    GetData(RunConfig.data_path).write_excel(row + 1, col, 'Fail')
                    log().error("❌ {0}请求响应断言失败，写入接口测试结果为'Fail' ".format(args[0]))
                    return False

        # 判断是否跳过测试，若为no，则跳过该测试请求
        elif args[3] == 'no':
            with allure.step('跳过该接口请求'):
                GetData(RunConfig.data_path).write_excel(row + 1, col, "Skip")
                log().info("✅ 跳过{0}请求，写入接口测试结果为'Skip' ".format(args[0]))
                pytest.skip("跳过{0}请求".format(args[0]))

        # 无法识别是否要运行测试
        else:
            error_msg = "❌ 无法识别是否要运行测试，请选择是否运行'yes/no' "
            log().error(error_msg)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_api.py"])