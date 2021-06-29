#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:13
# @File: method.py


import requests


class RunMethod:
    def post_method(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    def get_method(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def run_method(self, method, url, data=None, **kwargs):
        if method == 'post':
            return self.post_method(url, data, **kwargs)
        elif method == 'get':
            return self.get_method(url, data, **kwargs)
        else:
            print('只支持post/get方法')
