#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from logger import logger


class BaseRequests:

    def __init__(self, method):
        self.method = method

    def base_request(self, url, params, data, json, **kwargs):
        if self.method.upper() == 'GET':
            res = requests.get(url, params=params, **kwargs)
            return res.text
        elif self.method.upper() == 'POST':
            res = requests.post(url, data=data, json=json, **kwargs)
            return res.text
        elif self.method.upper() == 'PUT':
            res = requests.put(url, data=data, **kwargs)
            return res
        elif self.method.upper() == 'DELETE':
            res = requests.delete(url, **kwargs)
            return res
        else:
            logger.debug("暂不支持{}方法".format(self.method))

    def send_requests(self, **kwargs):
        pass
