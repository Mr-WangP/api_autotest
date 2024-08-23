#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/26 18:24
# @File: config.py

from pathlib import Path
from utils.FilesUtils.read_conf import ConfigUtil


class RunConfig:
    """
    运行测试配置
    """
    # 项目路径
    root_path = Path(__file__).resolve().parent

    # 项目运行url
    conf_path = Path(root_path, "common", "conf_env.ini")
    url_path = ConfigUtil(conf_path).read_config('DEFAULTS', 'url')

    # 运行测试用例的目录或文件
    cases_path = Path(root_path, "test_cases")

    # 选择测试数据文件
    data_path = Path(root_path, "data")
    files_path = []
    file_path = Path(root_path, "data", "api_case.xlsx")
    # file_path = ''

    # 日志文件目录
    log_path = Path(root_path, "logs")

    # 报告文件目录
    report_path = Path(root_path, "report")

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "3"
