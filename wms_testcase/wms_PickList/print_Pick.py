"""
收货-查询入库单信息接口
"""
import logging
import unittest

import ddt

from excel.read_excel import *
import json
from log.case_log import log_case_info
from lib.general_request import General_request
import warnings
from excel.written_token import WrittenToken

result = get_data('../xls/测试用例数据2.xls', 21)


@ddt.ddt
class Print_Pick(unittest.TestCase):

    def print_pick(self, case_name, IDX, url, methond, content_type, printType, pickId, pickNos, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '2'
        }
        pickIds = str(int(pickId))
        datas = '{' + '"printType":"' + printType + '",' + '"pickIds":[' + pickIds + '],' + '"pickNos":' + '["' + pickNos + '"]}'
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

    # WMS获取入库单SKU信息
    @ddt.data(*result)
    @ddt.unpack
    def test_print_pick(self, case_name, IDX, url, methond, content_type, printType, pickId, pickNos, message):
        result = self.print_pick(case_name, IDX, url, methond, content_type, printType, pickId, pickNos, message)
        pickIds = str(int(pickId))
        datas = '{' + '"printType":"' + printType + '",' + '"pickIds":[' + pickIds + '],' + '"pickNos":' + '["' + pickNos + '"]}'
        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
