#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:13
# @File: conftest.py

import json
import jsonpath
import pytest
from config import RunConfig


# 响应结果数据处理
def get_text(res, key):
    try:
        txt = json.loads(res)
        value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
        # jsonpath库默认获取的结果为list类型，如果没有获取到则返回false
        if len(value) == 1:
            return value[0]
        return value
    except:
        return False
