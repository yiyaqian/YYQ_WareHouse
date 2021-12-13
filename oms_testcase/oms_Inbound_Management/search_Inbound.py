"""
查询入库单接口
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

result = get_data('../xls/测试用例数据2.xls', 3)


@ddt.ddt
class SearchInbound(unittest.TestCase):
    def search_Inbound(self, case_name, IDX, url, methond, content_type, inboundType, toWarehouseCode,
                       transportType, orderTimeRange, orderNoType, orderNos, dateType, orderTimeStart, orderTimeEnd,
                       orderTime, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        datas = '{' + '"inboundType":' + '"' + inboundType + '",' + '"toWarehouseCode":' + '"' + toWarehouseCode + '",' + '"transportType":' + '"' + transportType + '",' + '"orderTimeRange":' + '[' + orderTimeRange + '],' + '"orderNoType":' + '"' + orderNoType + '",' + '"orderNos":' + '[' + '"' + orderNos + '"' + '],' + '"dateType":' + '"' + dateType + '",' + '"orderTimeStart":' + '"' + orderTimeStart + '",' + '"orderTimeEnd":' + '"' + orderTimeEnd + '",' + '"orderTime":' + '[' + orderTime + ']' + '}'
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

        consignmentNo = re['result']['records'][0]['consignmentNo']

        if message in re['message']:
            # # consignmentNo：入库单号
            WrittenToken.written_consignmentNo(int(IDX), consignmentNo)

        return re

    # 查询申报产品接口
    @ddt.data(*result)
    @ddt.unpack
    def test_search_Inbound(self, case_name, IDX, url, methond, content_type, inboundType, toWarehouseCode,
                            transportType, orderTimeRange, orderNoType, orderNos, dateType, orderTimeStart, orderTimeEnd,
                            orderTime, message):
        result = self.search_Inbound(case_name, IDX, url, methond, content_type, inboundType, toWarehouseCode,
                                     transportType, orderTimeRange, orderNoType, orderNos, dateType, orderTimeStart,
                                     orderTimeEnd,
                                     orderTime, message)
        datas = '{' + '"inboundType":' + '"' + inboundType + '",' + '"toWarehouseCode":' + '"' + toWarehouseCode + '",' + '"transportType":' + '"' + transportType + '",' + '"orderTimeRange":' + '[' + orderTimeRange + '],' + '"orderNoType":' + '"' + orderNoType + '",' + '"orderNos":' + '[' + '"' + orderNos + '"' + '],' + '"dateType":' + '"' + dateType + '",' + '"orderTimeStart":' + '"' + orderTimeStart + '",' + '"orderTimeEnd":' + '"' + orderTimeEnd + '",' + '"orderTime":' + '[' + orderTime + ']' + '}'
        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
