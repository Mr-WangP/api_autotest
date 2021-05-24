#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: wp
# @Time: 2021/5/23 22:17
# @File: operation_json.py


import json


class OperationJson:
    """操作json文件"""

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件
        :param file_name:文件路径
        :return:
        """
        with open(self.file_path, 'r') as fp:
            data = json.load(fp)
        return data

    def get_data(self, id):
        """
            根据关键字获取对应数据
        """
        return self.data[id]

    # 写入json
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))


# if __name__ == '__main__':
#     file_path = "../data/token.json"
#     opejson = OperationJson()
#     print(opejson.read_data())
#     print(opejson.get_data('filtrate'))
