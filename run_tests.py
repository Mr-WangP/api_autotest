#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: operation_excel.py


import os
import pytest
from config import RunConfig
from utils.LogUtils.log import log

'''
说明：
1、用例创建原则，按照data目录下excel表格中格式写入接口请求信息。
2、运行方式：
  > python run_tests.py
'''


def run():

    log().info("测试开始执行！")

    pytest.main(
        [
            "-vs", RunConfig.cases_path,
            "--alluredir", './report/temp/',
            "--clean-alluredir",
            "--maxfail", RunConfig.max_fail,
            "--reruns", RunConfig.rerun,
            "--reruns-delay", "2"
        ]
    )

    os.system('allure generate ./report/temp/ -o ./report/html/ --clean')
    log().info("运行结束，生成测试报告！")


if __name__ == '__main__':
    run()
