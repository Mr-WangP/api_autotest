#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: operation_excel.py


import os
from conftest import log
import pytest
from config import RunConfig


def run():

    log().info("测试开始执行！")

    pytest.main(["-vs", RunConfig.cases_path,
                 "--alluredir", './temp/',
                 "--clean-alluredir",
                 "--maxfail", RunConfig.max_fail,
                 "--reruns", RunConfig.rerun,
                 "--reruns-delay", "2"])

    os.system('allure generate ./temp/ -o ./report/ --clean')
    log().info("运行结束，生成测试报告！")


if __name__ == '__main__':
    run()
