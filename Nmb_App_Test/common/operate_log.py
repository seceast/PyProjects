#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/6/27 0027 13:23


import logging
from common import project_path
from common.operate_config import DoConfig

log_path = project_path.LOG_FILE_PATH
conf = DoConfig(project_path.CONFIG_FILE_PATH)


class MyLog:

    def __init__(self):
        # 创建日志收集器，并设置日志等级
        self.logger = logging.getLogger(conf.read_info('log', 'log_name'))
        self.logger.setLevel(conf.read_info('log', 'gather_level'))

        # 创建日志渠道  控制台或者文件
        self.console_log = logging.StreamHandler()
        self.file_log = logging.FileHandler(project_path.LOG_FILE_PATH, encoding='utf-8')

        # 设置日志输出格式
        con_format = logging.Formatter(conf.read_info('log', 'con_format'))
        file_format = logging.Formatter(conf.read_info('log', 'file_format'))

        self.console_log.setFormatter(con_format)
        self.file_log.setFormatter(file_format)

        # 读取配置文件，判断日志输出位置
        site = conf.read_info('log', 'site')

        # 链接收集器和渠道
        if site == '1':
            self.logger.addHandler(self.console_log)
        elif site == '2':
            self.logger.addHandler(self.file_log)
        else:
            self.logger.addHandler(self.console_log)
            self.logger.addHandler(self.file_log)

    def my_log(self):
        return self.logger


my_logger = MyLog().my_log()

if __name__ == "__main__":
    my_logger.warning('www')
    my_logger.debug('ddd')
    my_logger.error('eee')
    my_logger.info('iiii')
    my_logger.critical('cccc')
