#!/usr/bin/env.python
# -*- coding: utf-8 -*-
# __author__ = yangyd
# Create time: 2019/7/15 23:06

import re

from common_code.operate_mysql import OperateMysql
from common_code.operate_config import DoConfig
from common_code.project_path import USER_FILE_PATH


class Parameter:
    unreg_pattern = r'\$\{no_reg_phone\}'
    reg_pattern = r'\$\{yet_regist_phone\}'
    recharge_pattern = r'\$\{yet_regist_phone\}'
    add_pattern = r'\$\{add_memberid\}'
    loan_pattern = r'\$\{loan_memberid\}'
    loan_id_pattern = r'\$\{loan_Id\}'
    admin_user_pattern = r'\$\{admin_user\}'
    borrow_id_pattern = r'\$\{borrow_memberid\}'

    conf = DoConfig(USER_FILE_PATH)

    @classmethod
    def unreg_phone_replace(cls, reg_data):
        """
        未注册手机号替换
        :param reg_data:
        :return:
        """
        if re.search(cls.unreg_pattern, reg_data):
            do_mysql = OperateMysql()
            unreg_phone = do_mysql.unreg_phone()
            reg_data = re.sub(cls.unreg_pattern, unreg_phone, reg_data)

            do_mysql.mysql_close()
        return reg_data

    @classmethod
    def reg_phone_replace(cls, reg_data):
        """
        已注册手机号替换
        :param reg_data:
        :return:
        """
        if re.search(cls.reg_pattern, reg_data):
            do_mysql = OperateMysql()

            reg_phone = do_mysql.reg_phone()
            reg_data = re.sub(cls.reg_pattern, reg_phone, reg_data)

            do_mysql.mysql_close()

        return reg_data

    @classmethod
    def register_parameter(cls, reg_data):
        """
        注册相关数据正则替换
        :param reg_data:
        :return:
        """
        reg_data = cls.unreg_phone_replace(reg_data)

        reg_data = cls.reg_phone_replace(reg_data)

        return reg_data

    @classmethod
    def login_parameter(cls, login_data):
        """
        登录数据参数化
        :param login_data:
        :return:
        """
        login_data = cls.unreg_phone_replace(login_data)
        login_data = cls.reg_phone_replace(login_data)

        return login_data

    @classmethod
    def recharge_parameter(cls, recharge_data):
        """
        充值数据参数化
        :param recharge_data:
        :return:
        """
        # 读取配置文件中已有投资人号码
        rech_phone = cls.conf.read_info('invest_user', 'mobilephone')

        if re.search(cls.recharge_pattern, recharge_data):
            recharge_data = re.sub(cls.recharge_pattern, rech_phone, recharge_data)

        return recharge_data

    @classmethod
    def add_parameter(cls, add_data):
        add_memberid = cls.conf.read_info('borrow_user', 'memberid')
        add_phone = cls.conf.read_info('invest_user', 'mobilephone')
        if re.search(cls.add_pattern, add_data):
            add_data = re.sub(cls.add_pattern, add_memberid, add_data)
        if re.search(cls.reg_pattern, add_data):
            add_data = re.sub(cls.reg_pattern, add_phone, add_data)

        return add_data

    @classmethod
    def loan_parameter(cls, loan_data):
        admin_phone = cls.conf.read_info('admin_user', 'mobilephone')
        loan_memberid = cls.conf.read_info('invest_user', 'memberid')
        loan_phone = cls.conf.read_info('invest_user', 'mobilephone')
        borrow_id = cls.conf.read_info('borrow_user', 'memberid')

        # 替换投资人ID
        loan_data = re.sub(cls.loan_pattern, loan_memberid, loan_data)
        # 替换投资人帐号
        loan_data = re.sub(cls.recharge_pattern, loan_phone, loan_data)
        # 替换管理员帐号
        loan_data = re.sub(cls.admin_user_pattern, admin_phone, loan_data)
        # 替换借款人ID
        loan_data = re.sub(cls.borrow_id_pattern, borrow_id, loan_data)
        # 获取属性并参数化标ID
        if re.search(cls.loan_id_pattern, loan_data):
            loan_id = str(getattr(cls, "loan_id"))
            loan_data = re.sub(cls.loan_id_pattern, loan_id, loan_data)
        return loan_data


if __name__ == '__main__':
    from common_code.operate_excel import DoExcel
    from common_code.project_path import CASE_FILE_PATH

    data_str = DoExcel(CASE_FILE_PATH, 'register').read_excel(2)
    data_str1 = DoExcel(CASE_FILE_PATH, 'add').read_excel(2)
    data_str2 = DoExcel(CASE_FILE_PATH, 'bidLoan').read_excel(2)
    data_str3 = DoExcel(CASE_FILE_PATH, 'recharge').read_excel(2)
    data_str4 = DoExcel(CASE_FILE_PATH, 'login').read_excel(2)

    print(Parameter.register_parameter(str(data_str[0])))
    print(Parameter.register_parameter(str(data_str[4])))
    print(Parameter.add_parameter(str(data_str1[0])))
    print(Parameter.loan_parameter(str(data_str2)))
    print(Parameter.recharge_parameter(str(data_str3)))
