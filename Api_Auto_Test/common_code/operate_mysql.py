#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/10 0010 9:31


import pymysql
import random
import string

from common_code.operate_config import DoConfig
from common_code.project_path import CONFIG_FILE_PATH

conf = DoConfig(CONFIG_FILE_PATH)


class OperateMysql:

    # 初始化一个数据库连接和游标
    def __init__(self):
        self.connect = pymysql.connect(
            host=conf.read_info('Mysql', 'host'),
            port=conf.read_int('Mysql', 'port'),
            user=conf.read_info('Mysql', 'user'),
            password=conf.read_info('Mysql', 'password'),
            db=conf.read_info('Mysql', 'db'),
            charset=conf.read_info('Mysql', 'charset'),
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.connect.cursor()

    def run_sql(self, sql, args=None, site=2):
        """
        按照sql语句读取数据并返回
        :param sql: 需执行的sql语句
        :param args: 语句中的判读条件
        :param site: 设置返回的是sql的全部数据site=2，还是只返回第一条site=其他
        :return:
        """
        self.cursor.execute(sql, args)
        self.connect.commit()
        if site == 2:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    # 关闭游标以及数据库连接
    def mysql_close(self):
        self.cursor.close()
        self.connect.close()

    @staticmethod
    def create_phone():
        # 按照正确的手机号前三位固定号码段,在配置文件中存储
        top_three = random.choice(eval(conf.read_info('Phone', 'phone_header')))

        # 使用随机函数制造后八位号码，string.digits 0-9的数字，random.sample（序列，数字）在序列中随机数字个元素
        after_eight = ''.join(random.sample(string.digits, 8))

        # 拼接号码
        return str(top_three) + after_eight

    def exists_or_not(self, phone):
        """
        判断传入的号码是否已在数据库中存在
        :param phone: 需要判断的手机号
        :return:
        """
        judge_sql = 'SELECT * FROM `member`WHERE MobilePhone = %s'
        args = (phone,)

        if self.run_sql(judge_sql, args):
            return True
        else:
            return False

    # 创造未注册手机号
    def unreg_phone(self):

        while True:
            unreg_phone = self.create_phone()
            if not self.exists_or_not(unreg_phone):
                break

        return unreg_phone

    # 获取已注册的手机号
    def reg_phone(self):
        reg_sql = 'SELECT MobilePhone FROM member'
        reg_phone = self.run_sql(reg_sql, site=1)
        return reg_phone['MobilePhone']


if __name__ == '__main__':
    sql1 = 'SELECT * FROM `member`WHERE MobilePhone = 13666666666'
    sql2 = 'SELECT * FROM `member`WHERE id BETWEEN %(id1)s and %(id2)s'

    do_mysql = OperateMysql()
    res1 = do_mysql.run_sql(sql1, site=1)
    print(res1, '\n')

    args2 = {'id1': 1220, 'id2': 1355}
    res2 = do_mysql.run_sql(sql2, args2)
    print(res2)
    phone1 = do_mysql.create_phone()
    print(phone1)
    _phone = do_mysql.unreg_phone()
    print(_phone)

    print(do_mysql.exists_or_not(_phone))

    r_phone = do_mysql.reg_phone()
    print(r_phone)
    print(do_mysql.exists_or_not(r_phone))

    do_mysql.mysql_close()
