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
from excel.written_token import WrittenToken

result = get_data('../xls/测试用例数据2.xls', 12)


@ddt.ddt
class PutAway(unittest.TestCase):

    def putaway(self, case_name, IDX, url, methond, content_type, skuName, batchNo, qty1,
                taskNo, stockQuality, consignmentNo, skuId1, skuCode, putawayQty1, locationCode, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '2'
        }
        qty = str(int(qty1))
        putawayQty = str(int(putawayQty1))
        skuId = str(int(skuId1))
        logging.info(type(locationCode))
        datas = '{' + '"skuName":' + '"' + skuName + '",' + '"batchNo":"' + batchNo + '",' + '"qty":' + qty + ',' + '"taskNo":"' + taskNo + '",' + '"stockQuality":"' + stockQuality + '",' + \
                '"consignmentNo":"' + consignmentNo + '",' + '"skuId":' + skuId + ',' + '"skuCode":"' + skuCode + '",' + '"putawayQty":"' + putawayQty + '",' + '"locationCode":"' + locationCode + '"}'
        data = json.loads(datas)
        logging.info(datas)
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
    def test_putaway(self, case_name, IDX, url, methond, content_type, skuName, batchNo, qty1,
                     taskNo, stockQuality, consignmentNo, skuId1, skuCode, putawayQty1, locationCode, message):
        result = self.putaway(case_name, IDX, url, methond, content_type, skuName, batchNo, qty1,
                              taskNo, stockQuality, consignmentNo, skuId1, skuCode, putawayQty1, locationCode, message)
        skuId = str(int(skuId1))
        qty = str(int(qty1))
        putawayQty = str(int(putawayQty1))
        datas = '{' + '"skuName":' + '"' + skuName + '",' + '"batchNo":"' + batchNo + '",' + '"qty":' + qty + ',' + '"taskNo":"' + taskNo + '",' + '"stockQuality":"' + stockQuality + '",' + \
                '"consignmentNo":"' + consignmentNo + '",' + '"skuId":' + skuId + ',' + '"skuCode":' + skuCode + '",' + '"putawayQty":"' + putawayQty + '",' + '"locationCode":"' + locationCode + '"}'

        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
