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

result = get_data('../xls/测试用例数据2.xls', 9)


@ddt.ddt
class WSearchInbound(unittest.TestCase):
    def search_Inbound(self, case_name, IDX, url, methond, content_type, keyType1, keyWords, statusList1, orderType1,
                       customerCode, boxBarcode, transportType, timeRangeType1, timeRange, timeRangeFrom, timeRangeTo,
                       message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '2'
        }
        keyType = str(int(keyType1))
        statusList = str(statusList1)
        orderType = str(int(orderType1))
        timeRangeType = str(int(timeRangeType1))
        datas = '{' + '"keyType":' + keyType + ',' + '"keyWords":' + '[' + '"' + keyWords + '"' + '],' + '"statusList":' + '[' + statusList + '],' + '"orderType":' + '"' + orderType + '",' + '"customerCode":' + '"' + customerCode + '",' + '"boxBarcode":' + '"' + boxBarcode + '",' + '"transportType":' + '"' + transportType + '",' + '"timeRangeType":' + timeRangeType + ',' + '"timeRange":' + '[' + timeRange + '],' + '"timeRangeFrom":' + '"' + timeRangeFrom + '",' + '"timeRangeTo":' + '"' + timeRangeTo + '"' + '}'
        data = json.loads(datas)
        if methond == 'POST':
            logging.info("res.text")
            """
            3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
            """
            res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
            logging.info(res.text)
            re = res.json()  # 转为json格式供assertEqual断言使用
            # 当message等于登录成功时，获取token并将token写入表名称为”登录“且“message”一列等于“登陆成功”token一列列中
        else:
            """
             3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
             """
            res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
        if 'None' != re['result']:
            logging.info('欢迎')
            WrittenToken.written_taskNo(int(IDX), re['result']['records'][0]['taskNo'], keyWords)
        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_search_Inbound(self, case_name, IDX, url, methond, content_type, keyType1, keyWords, statusList1,
                            orderType1,
                            customerCode, boxBarcode, transportType, timeRangeType1, timeRange, timeRangeFrom,
                            timeRangeTo,
                            message):
        result = self.search_Inbound(case_name, IDX, url, methond, content_type, keyType1, keyWords, statusList1,
                                     orderType1,
                                     customerCode, boxBarcode, transportType, timeRangeType1, timeRange, timeRangeFrom,
                                     timeRangeTo,
                                     message)
        keyType = str(int(keyType1))
        statusList = str(statusList1)
        orderType = str(int(orderType1))
        timeRangeType = str(int(timeRangeType1))
        datas = '{' + '"keyType":' + keyType + ',' + '"keyWords":' + '[' + '"' + keyWords + '"' + '],' + '"statusList":' + '[' + statusList + '],' + '"orderType":' + '"' + orderType + '",' + '"customerCode":' + '"' + customerCode + '",' + '"boxBarcode":' + '"' + boxBarcode + '",' + '"transportType":' + '"' + transportType + '",' + '"timeRangeType":' + timeRangeType + ',' + '"timeRange":' + '[' + timeRange + '],' + '"timeRangeFrom":' + '"' + timeRangeFrom + '",' + '"timeRangeTo":' + '"' + timeRangeTo + '"' + '}'
        """
            4.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "5.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
