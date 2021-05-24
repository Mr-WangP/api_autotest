#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: operation_header.py


import json
from util.operation_json import OperationJson


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_token(self):
        """
        获取登录返回的token
        """
        token = {"data": {"token": self.response['data']['token']}}
        return token

    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())
