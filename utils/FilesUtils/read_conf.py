#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : wp
# @Time : 2022/4/29 17:02
# @File : read_conf.py

import configparser


# 读取配置文件
class ConfigUtil:
    def __init__(self, path):
        """
        传入ini配置文件
        :param path:
        """
        self.path = path

    def read_config(self, selector, option):
        conf = configparser.ConfigParser()
        conf.read(self.path)
        return conf.get(selector, option)


if __name__ == '__main__':
    con = ConfigUtil('../../common/conf_env.ini')
    url = con.read_config('DEFAULTS', 'url')
    print(url)
