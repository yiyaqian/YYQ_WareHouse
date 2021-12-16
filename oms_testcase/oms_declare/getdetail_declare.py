"""
获取入库单详情内容
"""
import json
import logging
import unittest

import ddt

from excel.read_excel import *
from lib.general_request import General_request
from excel.written_token import WrittenToken
from log.case_log import log_case_info

result = get_data('../xls/测试用例数据2.xls', 4)


@ddt.ddt
class GetDetailDeclare(unittest.TestCase):

    def getdetai_declare(self, case_name, IDX, url, methond, declareGoodsCode, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'x-access-token': session
        }
        datas = '{' + '"declareGoodsCode":' + '"' + declareGoodsCode + '"' + '}'
        data = json.loads(datas)
        if methond == 'POST':
            """
                4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
            res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
        else:
            """
                 4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
            res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用

        return re

    @ddt.data(*result)
    @ddt.unpack
    # 进行参数化
    def test_getdetaideclare(self, case_name, IDX, url, methond, declareGoodsCode, message):
        result = self.getdetai_declare(case_name, IDX, url, methond, declareGoodsCode, message)
        datas = '{' + '"declareGoodsCode":' + '"' + declareGoodsCode + '"' + '}'
        # # "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        self.assertEqual(message, result['message'])
