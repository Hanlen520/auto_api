#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import time
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:

    def __init__(self):
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)
        self.fomater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s')
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.fomater)
        self.console.setFormatter(self.fomater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

    def log(self, message, level=4):
        if level == 0:
            self.logger.error(message)
        elif level == 1:
            self.logger.exception(message)
        elif level == 2:
            self.logger.warning(message)
        elif level == 3:
            self.logger.info(message)
        else:
            self.logger.debug(message)


logger = Logger()

if __name__ == "__main__":
    logger.log("debug")
