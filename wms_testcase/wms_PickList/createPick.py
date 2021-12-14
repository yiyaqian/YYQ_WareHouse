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

result = get_data('../xls/测试用例数据2.xls', 19)


@ddt.ddt
class CreatePick(unittest.TestCase):

    def createPick(self, case_name, IDX, url, methond, content_type, taskIds1, picker, pickType, priority1, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '2'
        }
        taskIds = str(int(taskIds1))
        priority = str(int(priority1))
        datas = '{' + '"taskIds":[' + taskIds + '],' + '"picker":"' + picker + '",'+'"pickType":'+'"'+pickType+'",'+'"priority":'+priority+'}'
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
        # # # 为收货和上架接口传参数
        # for t in (0, total - 1):
        #     logging.info(int(IDX) + t)
        #     # skuId:skuId
        #     WrittenToken.written_skuId(int(IDX) + t, re['result']['records'][t]['skuName'],
        #                                taskNo, consignmentNo, re['result']['records'][t]['skuId'],
        #                                re['result']['records'][t]['skuCode'],
        #                                re['result']['records'][t]['planQty'],
        #                                re['result']['records'][t]['boxBarcode'])
        #     logging.info(re['result']['records'][t]['skuCode'])
        return re

    # WMS获取入库单SKU信息
    @ddt.data(*result)
    @ddt.unpack
    def test_createPick(self, case_name, IDX, url, methond, content_type, taskIds1, picker, pickType, priority1, message):
        result = self.createPick(case_name, IDX, url, methond, content_type, taskIds1, picker, pickType, priority1, message)
        taskIds = str(int(taskIds1))
        priority = str(int(priority1))
        datas = '{' + '"taskIds":[' + taskIds + '],' + '"picker":"' + picker + '",' + '"pickType":' + '"' + pickType + '",' + '"priority":' + priority + '}'

        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
