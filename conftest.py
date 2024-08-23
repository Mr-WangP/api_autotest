#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:13
# @File: conftest.py

import os
import time
import pytest
from config import RunConfig
from pathlib import Path
from utils.LogUtils.log import log


@pytest.fixture(scope="session", autouse=True)
def clear_report():
    try:
        for one in Path(RunConfig.report_path, "temp").iterdir():
            if 'json' or 'txt' in Path(one).suffix:
                Path(one).unlink()
    except Exception as e:
        log().error("allure数据清除失败", e)
    yield


# 获取./data目录下所有excel文件路径
@pytest.fixture(scope="session", autouse=True)
def excel_data():
    cases = []
    # 获取指定路径下所有测试用例excel：在/data/路径下
    for file in Path(RunConfig.data_path).iterdir():
        # 保存获取的所有测试用例文件：就是后缀为xlsx的文件
        # 判断是否为excel
        if file.suffix == '.xlsx':
            # 判断是否需要运行该excel文件用例
            if 'old' not in file.stem:
                cases.append(str(file))
        else:
            log().error('文件类型错误：{}'.format(file))
    RunConfig.files_path = cases


# 参数化获取./data目录下所有excel文件路径
@pytest.fixture(scope="class", autouse=False, params=RunConfig.files_path)
def excel_data_path(request):
    RunConfig.file_path = request.param


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的 item 的 name 和 node_id 的中文显示在控制台上
    :param items:测试用例
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    """
    try:
        _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
        _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
        _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
        _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
        _XFAILED = len([i for i in terminalreporter.stats.get('xfailed', []) if i.when != 'teardown'])
        _XPASSED = len([i for i in terminalreporter.stats.get('xpassed', []) if i.when != 'teardown'])
        _TOTAL = terminalreporter._numcollected
        _TIMES = time.time() - terminalreporter._sessionstarttime

        log().info("————————测试总结————————")
        log().info(f"成功用例数: {_PASSED}")
        log().error(f"异常用例数: {_ERROR}")
        log().error(f"失败用例数: {_FAILED}")
        log().warning(f"跳过用例数: {_SKIPPED}")
        log().warning(f"预期失败用例数: {_XFAILED}")
        log().warning(f"预期成功用例数: {_XPASSED}")
        log().info("用例执行时长: %.2f" % _TIMES + "s")

        _RATE = round((_PASSED + _SKIPPED) / _TOTAL * 100, 2)
        log().info("用例成功率: %.2f" % _RATE + "%")
    except Exception as e:
        log().error("收集测试结果失败", e)