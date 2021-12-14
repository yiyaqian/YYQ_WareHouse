"""
新增入库单接口
"""
import json
import logging
import unittest

import ddt

from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import warnings
from log.case_log import log_case_info

result = get_data('../xls/测试用例数据2.xls', 17)


@ddt.ddt
class WSearchOutbound(unittest.TestCase):
    def wsearch_Outbount(self, case_name, IDX, url, methond, content_type, timeRange, keyType1, keyWords, statusList,
                         businessType, dataSource, timeRangeSelect, transportChannel, pickTypeList, auditTimeFrom,
                         auditTimeTo, skuId1, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '2'
        }
        keyType = str(int(keyType1))
        skuId = str(skuId1)
        datas = '{' + '"timeRange":' + '[' + timeRange + '],' + '"keyType":' + '"' + keyType + '",' + '"keyWords":[' + '"' + keyWords + '"],' + '"statusList":[' + statusList + '],' + '"businessType":' + '"' + businessType + '",' + '"dataSource":' + '"' + dataSource + '",' + '"timeRangeSelect":' + '"' + timeRangeSelect + '",' + '"transportChannel":' + '"' + transportChannel + '",' + '"pickTypeList":[' + pickTypeList + '],' + '"auditTimeFrom":"' + auditTimeFrom + '",' + '"auditTimeTo":"' + auditTimeTo + '",' + '"skuId":' + '"' + skuId + '"' + '}'
        logging.info(datas)
        data = json.loads(datas)

        if methond == 'POST':
            logging.info("res.text")
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

        status = re['result']['records'][0]['status']
        consignmentNo = re['result']['records'][0]['consignmentNo']
        pickType = re['result']['records'][0]['pickType']
        if message in re['message'] and 'O' in status:
            # consignmentNo:出库单号
            WrittenToken.written_OutNoAndPickType(int(IDX), consignmentNo, pickType)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_wsearch_Outbount(self, case_name, IDX, url, methond, content_type, timeRange, keyType1, keyWords,
                              statusList, businessType, dataSource, timeRangeSelect, transportChannel, pickTypeList,
                              auditTimeFrom, auditTimeTo, skuId1, message):

        result = self.wsearch_Outbount(case_name, IDX, url, methond, content_type, timeRange, keyType1, keyWords,
                                       statusList, businessType, dataSource, timeRangeSelect, transportChannel,
                                       pickTypeList,
                                       auditTimeFrom, auditTimeTo, skuId1, message)
        keyType = str(int(keyType1))
        skuId = str(skuId1)

        datas = '{' + '"timeRange":' + '[' + timeRange + '],' + '"keyType":' + '"' + keyType + '",' + '"keyWords":[' + '"' + keyWords + '"],' + '"statusList":[' + statusList + '],' + '"businessType":' + '"' + businessType + '",' + '"dataSource":' + '"' + dataSource + '",' + '"timeRangeSelect":' + '"' + timeRangeSelect + '",' + '"transportChannel":' + '"' + transportChannel + '",' + '"pickTypeList":[' + pickTypeList + '],' + '"auditTimeFrom":"' + auditTimeFrom + '",' + '"auditTimeTo":"' + auditTimeTo + '",' + '"skuId":' + '"' + skuId + '"' + '}'
        """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
