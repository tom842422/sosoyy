# -*- coding: utf-8 -*-
# @Time : 2022/8/12 22:52
# @Author : TOM
# @Email : wayne_lau@aliyun.com
# @File : read_ini.py
# @Project : sosoyy_ui_new

import configparser
import os


class ReadIni:
    ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config', 'setting.ini')

    def __init__(self, url):
        # 访问地址
        self.url = url

    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.ini_path, encoding='utf8')
        # 根据接口类型返回对应的url
        return conf['url'][self.url]


if __name__ == '__main__':
    r = ReadIni('测试').read_ini()
    print(r)
