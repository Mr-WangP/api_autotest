#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2021/6/28 22:05
# @File : method.py

import json
import jsonpath
import requests
import allure


class RunMethod:

    # post请求封装
    @allure.step("发送post请求")
    def post_method(self, url, **kwargs):
        return requests.post(url=url, **kwargs)

    # get请求封装
    @allure.step("发送get请求")
    def get_method(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # 响应结果数据处理，从响应结果中获取某个字段的值
    def get_text(self, res, key):
        try:
            # 将json格式字符串数据转换为字典
            txt = json.loads(res)
            value = jsonpath.jsonpath(txt, key)
            # jsonpath库默认获取的结果为list类型，如果没有获取到则返回false
            if len(value) == 1:
                return value[0]
            return value
        except:
            return False
