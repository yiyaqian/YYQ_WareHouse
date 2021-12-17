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

result = get_data('../xls/测试用例数据2.xls', 20)


@ddt.ddt
class Search_Pick(unittest.TestCase):

    def search_pick(self, case_name, IDX, url, methond, content_type, status, createTime, consignmentNo, pickNo, picker,
                    createUser1, pickType1, pickModel, skuId, containerNo, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '7'
        }
        createUser = str(createUser1)
        pickType = str(int(pickType1))
        datas = '{' + '"status":"' + status + '",' + '"createTime":[' + createTime + '],' + '"consignmentNo":' + '"' + consignmentNo + '",' + '"pickNo":"' + pickNo + '",' \
                + '"picker":"' + picker + '",' + '"createUser":"' + createUser + '",' + '"pickType":"' + pickType + '",' + '"pickModel":"' + pickModel + '",' + '"skuId":"' + skuId + '",' + '"containerNo":"' + containerNo + '"}'
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

        if re['result']['total'] > 0:
            pickNo = re['result']['records'][0]['pickNo']
            ids = re['result']['records'][0]['id']
            WrittenToken.written_PickAndId(int(IDX), pickNo, ids)
        return re

    # WMS获取入库单SKU信息
    @ddt.data(*result)
    @ddt.unpack
    def test_search_pick(self, case_name, IDX, url, methond, content_type, status, createTime, consignmentNo, pickNo,
                         picker, createUser1, pickType1, pickModel, skuId, containerNo, message):
        result = self.search_pick(case_name, IDX, url, methond, content_type, status, createTime, consignmentNo, pickNo,
                                  picker, createUser1, pickType1, pickModel, skuId, containerNo, message)
        createUser = str(createUser1)
        pickType = str(int(pickType1))
        datas = '{' + '"status":"' + status + '",' + '"createTime":[' + createTime + '],' + '"consignmentNo":' + '"' + consignmentNo + '",' + '"pickNo":"' + pickNo + '",' \
                + '"picker":"' + picker + '",' + '"createUser":"' + createUser + '",' + '"pickType":"' + pickType + '",' + '"pickModel":"' + pickModel + '",' + '"skuId":"' + skuId + '",' + '"containerNo":"' + containerNo + '"}'

        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
