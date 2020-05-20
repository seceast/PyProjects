#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/16 0016 15:58


import os
from common_code.operate_mysql import OperateMysql
from common_code.project_path import CONFIG_PATH
from common_code.operate_http_requests import HttpRequest
from common_code.operate_config import DoConfig


class RegFixeUser:

    def __init__(self):
        self.conf = DoConfig(os.path.join(CONFIG_PATH, 'user.conf'))

    @staticmethod
    def reg_borrow():
        do_mysql = OperateMysql()

        reg_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/register'
        phone = do_mysql.unreg_phone()
        param = {"mobilephone": phone, "pwd": "123456", "regname": "borrow_nesta"}

        reg_request = HttpRequest()

        while True:
            reg_request.http_request(reg_url, 'post', param)

            sql = 'SELECT id FROM member where MobilePhone = %s'
            res = do_mysql.run_sql(sql, (phone,))
            if res:
                borrow_data = {
                    'borrow_user': {'mobilephone': phone,
                                    'memberid': res[0]['id'],
                                    'pwd': 123456
                                    }
                }

                # self.conf.batch_write('borrow_user', data, os.path.join(CONFIG_PATH, 'user.conf'))
                do_mysql.mysql_close()
                break
        return borrow_data

    @staticmethod
    def reg_invest():
        do_mysql = OperateMysql()

        reg_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/register'
        phone = do_mysql.unreg_phone()
        param = {"mobilephone": phone, "pwd": "123456", "regname": "invest_nesta"}
        reg_request = HttpRequest()

        while True:

            reg_request.http_request(reg_url, 'post', param)

            sql = 'SELECT id FROM member where MobilePhone = %s'
            res = do_mysql.run_sql(sql, (phone,))
            if res:
                # invest_data = {'mobilephone': phone,
                #                'memberid': res[0]['id'],
                #                'pwd': 123456
                #                }
                # self.conf.batch_write('invest_user', data, os.path.join(CONFIG_PATH, 'user.conf'))
                do_mysql.mysql_close()
                break

        invest_data = {
            'invest_user': {'mobilephone': phone,
                            'memberid': res[0]['id'],
                            'pwd': 123456
                            }
        }

        return invest_data

    @staticmethod
    def reg_admin():
        do_mysql = OperateMysql()

        reg_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/register'
        phone = do_mysql.unreg_phone()
        param = {"mobilephone": phone, "pwd": "123456", "regname": "admin_nesta"}
        reg_request = HttpRequest()

        while True:
            reg_request.http_request(reg_url, 'post', param)

            sql = 'SELECT id FROM member where MobilePhone = %s'
            res = do_mysql.run_sql(sql, (phone,))
            if res:
                admin_data = {
                    'admin_user': {'mobilephone': phone,
                                   'memberid': res[0]['id'],
                                   'pwd': 123456
                                   }
                }

                # self.conf.write_config(data, os.path.join(CONFIG_PATH, 'user.conf'))
                do_mysql.mysql_close()
                break
        return admin_data

    def crate_config(self):
        data = {}

        data.update(self.reg_borrow())
        data.update(self.reg_invest())
        data.update(self.reg_admin())

        self.conf.write_config(data, os.path.join(CONFIG_PATH, 'user.conf'))


if __name__ == '__main__':
    fix = RegFixeUser()
    fix.crate_config()
