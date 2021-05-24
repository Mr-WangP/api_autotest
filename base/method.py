#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:13
# @File: method.py


import json
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


class RunMethod:
    def post_method(self, url, data, header=None):
        res = None
        if header is not None:
            urllib3.disable_warnings()
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            urllib3.disable_warnings()
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_method(self, url, data=None, header=None):
        res = None
        if header is not None:
            urllib3.disable_warnings()
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            urllib3.disable_warnings()
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_method(url, data, header)
        elif method == 'get':
            res = self.get_method(url, data, header)
        else:
            print('只支持post/get方法')
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
