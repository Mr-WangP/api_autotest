#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2021/6/28 22:12
# @File : test_api.py

import pytest
import allure
from base.method import RunMethod
from utils.ExcelUtils.excel_utils import GetExcelData
from config import RunConfig
from utils.LogUtils.log import log


@allure.epic('接口自动化测试')
class Test_Api:

    # 参数化变量存储字典
    global all_val
    all_val = {}

    @pytest.mark.parametrize('args',
                             GetExcelData(RunConfig.file_path).read_excel(),
                             ids=[*[i[10] for i in GetExcelData(RunConfig.file_path).read_excel()]])
    def test_case(self, args):
        log().info("————————运行case{}————————".format(args[0]))
        # allure报告配置
        allure.dynamic.title(f'{args[10]}')
        allure.dynamic.story(f'{args[13]}')
        allure.dynamic.feature(f'{args[14]}')
        allure.dynamic.description(f'{args[15]}')
        allure.dynamic.severity(f'{args[16]}')

        # 获取表格中一行数据的长度
        col = len(args)
        # 获取表格中id列case中的数字
        with allure.step('获取接口请求id'):
            id = args[0]
            row = int(id)
            log().info("✅ 获取接口请求id：case{0} ".format(id))

        # 获取接口请求名称
        with allure.step('获取接口请求名称'):
            titles = args[10]
            log().info("✅ 获取case{0}接口请求名称：{1} ".format(id, titles))

        # 判断是否跳过测试，若为yes，则继续进行该测试请求
        if args[17].lower() == 'yes':
            # 获取接口请求url
            with allure.step('获取接口请求url'):
                if args[1]:
                    url = args[1] + args[2]
                else:
                    url = RunConfig.url_path + args[2]
                log().info("✅ 获取case{0}接口请求url：{1} ".format(id, url))
            # 获取接口请求类型
            with allure.step('获取接口请求类型'):
                method = args[3]
                log().info("✅ 获取case{0}接口请求类型：{1} ".format(id, method))
            # 获取接口请求头参数
            with allure.step('获取接口请求头参数'):
                headers = args[4]
                log().info(
                    "✅ 获取case{0}接口请求头参数headers：{1} ".format(
                        id, headers))
            # 获取接口请求参数
            with allure.step('获取接口请求参数'):
                request_data = args[5]
                log().info("✅ 获取case{0}接口请求参数：{1} ".format(id, request_data))

            # 接口处理
            # 如果存在请求头
            if headers:
                # 存在请求参数
                if request_data:
                    dict_data = {
                        'url': url, 'headers': eval(
                            args[4]), args[6]: eval(request_data)}
                # 不存在请求参数
                else:
                    dict_data = {'url': url, 'headers': eval(args[4])}
            # 如果不存在请求头
            else:
                # 存在请求参数
                if request_data:
                    dict_data = {'url': url, args[6]: eval(request_data)}
                # 不存在请求参数
                else:
                    dict_data = {'url': url}

            # 发送接口请求，获取响应数据
            with allure.step('发送接口请求，获取响应数据'):
                request_method = args[3] + '_method'
                res = getattr(RunMethod(), request_method)(**dict_data)
                log().info(
                    "✅ 获取case{0}接口请求响应结果：{1} ".format(
                        id, str(
                            res.json())))

            # JSON提取接口响应数据
            if args[11]:
                # 多参数
                # 遍历分割JSON提取_引用名称
                var_str = args[11]
                var_list = var_str.split(';')
                # 遍历分割JSON表达式
                json_str = args[12]
                json_list = json_str.split(';')
                for i in range(len(var_list)):
                    key = var_list[i]
                    json_exp = json_list[i]
                    value_json = RunMethod().get_text(res.text, json_exp)
                    all_val[key] = value_json
                log().info(
                    "✅ 获取case{0}接口请求响应JSON提取结果：{1} ".format(
                        id, all_val))

            # 获取接口请求预期结果
            with allure.step('获取接口请求预期结果'):
                verify_exp = args[7]
                expect = args[8]
                log().info(
                    "✅ 获取case{0}接口请求响应字段'{1}'的预期结果：{2} ".format(
                        id, verify_exp, expect))

            # 向excel中写入响应结果
            with allure.step('向excel中写入响应结果'):
                verify_json = RunMethod().get_text(res.text, verify_exp)
                GetExcelData(
                    RunConfig.file_path).write_excel(
                    row + 1, 10, verify_json)
                log().info(
                    "✅ 获取case{0}接口请求响应字段'{1}'的实际结果写入excel：{2} ".format(
                        args[0], verify_exp, verify_json))

            # 进行断言，比较接口请求实际结果和预期结果
            with allure.step('进行断言，比较接口请求实际结果和预期结果'):
                try:
                    assert expect == verify_json
                    GetExcelData(RunConfig.file_path).pass_(row + 1, col)
                    log().info(
                        "✅ 获取case{0}接口请求响应断言成功，写入接口测试结果为'Pass' ".format(
                            args[0]))
                    return True
                except Exception as e:
                    GetExcelData(RunConfig.file_path).failed_(row + 1, col)
                    log().error("❌ 获取case{0}接口请求响应断言失败，写入接口测试结果为'Failed' ".format(args[0]))
                    return e

        # 判断是否跳过测试，若为no，则跳过该测试请求
        elif args[17].lower() == 'no':
            with allure.step('跳过该接口请求'):
                GetExcelData(RunConfig.file_path).skip_(row + 1, col)
                log().info("✅ 跳过case{0}接口请求，写入接口测试结果为'Skip' ".format(args[0]))
                pytest.skip("跳过case{0}接口请求".format(args[0]))

        # 无法识别是否要运行测试
        else:
            error_msg = "❌ 无法识别是否要运行测试，请选择是否运行 'yes/no'"
            log().error(error_msg)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_api.py"])
