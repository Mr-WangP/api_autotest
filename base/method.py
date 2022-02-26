#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2021/6/28 22:05
# @File : method.py

import requests
from logs.log import log


class RunMethod:

    def post_method(self, url, data=None, **kwargs):
        try:
            res = requests.post(url=url, data=data, **kwargs)
            log().info("✅ 成功发送post请求：接口请求url'{0}',请求参数'{1}',其它参数'{2}' ".format(url, data, kwargs))
            return res
        except Exception as e:
            error_msg = "❌ 发送post请求失败：接口请求url'{0}',请求参数'{1}',其它参数'{2}' ".format(url, data, kwargs)
            log().error(error_msg)
            return e

    def get_method(self, url, params=None, **kwargs):
        try:
            res = requests.get(url=url, params=params, **kwargs)
            log().info("✅ 成功发送get请求：接口请求url'{0}',请求参数'{1}',其它参数'{2}' ".format(url, params, kwargs))
            return res
        except Exception as e:
            error_msg = "❌ 发送get请求失败：接口请求url'{0}',请求参数'{1}',其它参数'{2}' ".format(url, params, kwargs)
            log().error(error_msg)
            return e

    def run_method(self, method, url, data=None, **kwargs):
        if method == 'post':
            return self.post_method(url, data, **kwargs)
        elif method == 'get':
            return self.get_method(url, data, **kwargs)
        else:
            error_msg = "❌ 只支持post/get请求测试 "
            log().error(error_msg)
