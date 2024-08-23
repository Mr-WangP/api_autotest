#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/2/25 16:25
# @File : logs.py

import logging
import time
from pathlib import Path
from config import RunConfig


def log():
    # 创建一个日志器
    logger = logging.getLogger('logger')
    # 设置日志输出最低等级，低于当前等级就会忽略
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # 创建处理器
        sh = logging.StreamHandler()
        fh = logging.FileHandler(
            filename='{0}_{1}'.format(
                str(Path(RunConfig.log_path, "log")),
                time.strftime(
                    '%Y_%m_%d_%H_%M_%S',
                    time.localtime())),
            encoding='utf-8')
        # 创建一个格式器
        formator = logging.Formatter(
            fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d-%X')
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        logger.addHandler(sh)
        logger.addHandler(fh)

    return logger
