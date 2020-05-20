#!/user/bin/env python
# -*- coding: utf-8 -*-
# __author__ = yangyd 
# Create time: 2019/7/8 0008 9:13


import requests
import json
from common_code.operate_log import my_logger


class HttpRequest:

    def __init__(self):
        # 创建一个request的实例实例属性,返回的是一个session对象，自动完成cookie，session的传递
        self.request_session = requests.Session()

    def http_request(self, url, method, datas=None, is_json=False, **kwargs):
        """
        根据传入的参数完成请求
        :param is_json: 传参的类型是否是json
        :param url:请求地址
        :param datas:请求参数
        :param method:请求方法
        :param kwargs:其余参数，headers等
        :return:
        """
        # 将传入的请求方法字符串强制转换为大写，方便方法判断
        method = method.upper()
        result = None

        # 根据不同形式的参数字典进行判断转换，excel中存储的可能是非json形式的字典
        if isinstance(datas, str):
            try:
                datas = json.loads(datas)
            except Exception as e:
                datas = eval(datas)
                # my_logger.error("数据转换异常：", e)

        # 判断请求方法，按照设置的请求方法进行请求
        if method == 'POST':
            # 判断存储参数的形势，是否是json，如果是，则以json的形式进行传参，否则以form表单的形式传参
            if is_json:
                result = self.request_session.request(method=method, url=url, json=datas, **kwargs)
                my_logger.info("post请求成功")
            else:
                result = self.request_session.request(method=method, url=url, data=datas, **kwargs)
                my_logger.info("post请求成功")
        elif method == 'GET':
            result = self.request_session.request(method=method, url=url, params=datas, **kwargs)
            my_logger.info("get请求成功")
        else:
            my_logger.error("【{}】请求方法不允许".format(method))

        return result


if __name__ == '__main__':
    req = HttpRequest()
    # 注册
    reg_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/register'
    reg_param = {'mobilephone': 13888885858, 'pwd': '123456', 'regname': 'nesta'}
    reg_res = req.http_request(reg_url, 'get', reg_param)
    print("注册结果为", reg_res.json())

    # 登录
    login_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/login'
    login_param = {'mobilephone': 13888885858, 'pwd': '123456'}
    header = {"User-Agent": ": Mozilla/5.0 "}

    login_res = req.http_request(login_url, 'post', login_param, headers=header)
    print("登录结果为", login_res.json())

    # 充值
    recharge_url = 'http://tj.lemonban.com/futureloan/mvc/api/member/recharge'
    recharge_param = {'mobilephone': 13888885858, 'amount': 1333}
    req.request_session.request('post', login_url, login_param)
    rec_req = req.request_session.request('post', recharge_url, recharge_param)
    print("充值结果为", rec_req.json())
