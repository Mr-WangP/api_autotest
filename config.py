#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: config.py

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(BASE_PATH, "test_cases", "")

    # 选择测试数据文件
    data_path = os.path.join(BASE_PATH, "data", "case.xlsx")

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"
