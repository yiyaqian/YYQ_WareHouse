"""
查询申报产品接口
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

result = get_data('../xls/测试用例数据2.xls', 10)


@ddt.ddt
class SearchDeclare(unittest.TestCase):

    def search_declared(self, case_name, IDX, url, methond, content_type, category, brand, skuCode, timeRange, timeFrom,
                        timeTo, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        datas = '{' + '"category":' + '"' + category + '",' + '"brand":' + '"' + brand + '",' + '"skuCode":' + '"' + skuCode + '",' + '"timeFange":' + '[' + timeRange + '],' + '"timeFrom":' + '"' + timeFrom + '",' + '"timeTo":' + '"' + timeTo + '"' + '}'
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

        if message in re['message']:
            ids = re['result']['records'][0]['id']
            WrittenToken.written_ids(int(IDX), ids)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_search_declared(self, case_name, IDX, url, methond, content_type, category, brand, skuCode, timeRange,
                             timeFrom, timeTo, message):
        result = self.search_declared(case_name, IDX, url, methond, content_type, category, brand, skuCode, timeRange,
                                      timeFrom, timeTo, message)

        datas = '{' + '"category":' + '"' + category + '",' + '"brand":' + '"' + brand + '",' + '"skuCode":' + '"' + skuCode + '",' + '"timeFange":' + '[' + timeRange + '],' + '"timeFrom":' + '"' + timeFrom + '",' + '"timeTo":' + '"' + timeTo + '"' + '}'
        # # "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        self.assertEqual(message, result['message'])

