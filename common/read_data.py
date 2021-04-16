#!/usr/bin/python
# -*- coding: utf-8 -*-
import yaml
from configparser import ConfigParser
from logger import logger


class HandleYAML:

    def read_YAML(self, file_path):
        with open(file_path, encoding='GBK') as fs:
            data = yaml.load(fs, Loader=yaml.FullLoader)
            return data



class MyConfigparser:
    def __init__(self, path):
        self.conf = ConfigParser()
        self.conf.read(path, encoding='utf-8-sig')

    def read_ini(self, section, option):
        try:
            return self.conf.get(section, option)
        except Exception as e:
            logger.log(e, 1)
            return None


if __name__ == '__main__':
    my_yaml = HandleYAML()
    print(my_yaml.read_YAML('../testcase/test_login.yaml'))
    my_configer = MyConfigparser('../config.ini')
    base_url = my_configer.read_ini("test_base_url", "test_base_url")
    print(base_url)
