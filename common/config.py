#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: config.py

import os
from utils.FilesUtils.read_conf import ConfigUtil


class RunConfig:
    """
    运行测试配置
    """
    _SLASH = os.sep
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 项目运行url
    conf_path = os.path.join(root_path, "common" + _SLASH + "conf_env.ini")
    url_path = ConfigUtil(conf_path).read_config('DEFAULTS', 'url')

    # 运行测试用例的目录或文件
    cases_path = os.path.join(root_path, "test_cases", "")

    # 选择测试数据文件
    data_path = os.path.join(root_path, "data", "api_case.xlsx")

    # 日志文件目录
    log_path = os.path.join(root_path, 'logs' + _SLASH)

    # 报告文件目录
    report_path = os.path.join(root_path, "report" + _SLASH)

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "3"
