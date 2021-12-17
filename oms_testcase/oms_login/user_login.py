"""
登录接口
"""
import logging
import unittest

import ddt as ddt

from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import json
from log.case_log import log_case_info

result = get_data('../xls/测试用例数据2.xls', 13)


@ddt.ddt
class UserLogin(unittest.TestCase):
    # 封装接口
    def userlogin(self, name, url, methond, Content_Type, x_access_token, datas, message):
        self.req = General_request()
        header = {
            'Content-Type': Content_Type
        }
        data = json.loads(datas)
        if methond == 'POST':
            """
            3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
            """
            res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
            logging.info(res.text)
            re = res.json()  # 转为json格式供assertEqual断言使用
            # 当message等于登录成功时，获取token并将token写入表名称为”登录“且“message”一列等于“登陆成功”token一列列中
            if '登录成功' == message:
                tokens = re['result']['token']
                # 调用写入token的方法
                WrittenToken.written_token(self, tokens)
        else:
            """
             3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
             """
            res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
            if '登录成功' == message:
                tokens = re['result']['token']
                # 调用写入token的方法
                WrittenToken.written_token(self, tokens)

        return re

    @ddt.data(*result)
    @ddt.unpack
    # 进行参数化
    def test_userlogin(self, case_name, url, methond, Content_Type, x_access_token, data, message):
        result = self.userlogin(case_name, url, methond, Content_Type, x_access_token, data, message)
        logging.info(result['message'])
        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, data, message, result)
        self.assertEqual(message, result['message'])
