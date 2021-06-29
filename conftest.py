#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:13
# @File: conftest.py


import os
import json
import jsonpath
import logging
import time
from config import RunConfig

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "report", "")
LOG_DIR = os.path.join(BASE_DIR, "log", "")


# 响应结果数据处理
def get_text(res, key):
    try:
        txt = json.loads(res)
        value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
        #jsonpath库默认获取的结果为list类型，如果没有获取到则返回false
        if len(value) == 1:
            return value[0]
        return value
    except:
        return False

def log():
    # 创建一个日志器
    logger = logging.getLogger('logger')
    # 设置日志输出最低等级，低于当前等级就会忽略
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        # 创建处理器
        sh = logging.StreamHandler()
        fh = logging.FileHandler(filename='{}\\{}_log'.format(
            LOG_DIR, time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())), encoding='utf-8')
        # 创建一个格式器
        formator = logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(message)s',
                                     datefmt='%Y/%m/%d/%X')
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(sh)
        logger.addHandler(fh)

    return logger
