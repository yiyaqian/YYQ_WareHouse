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

result = get_data('../xls/测试用例数据2.xls', 14)


@ddt.ddt
class SearchOutbound(unittest.TestCase):
    def search_Outbount(self, case_name, IDX, url, methond, content_type, logicWarehouseCode, logisticsProduct, country,
                        skuCode, firstName, orderTimeRange,
                        orderNumberType, orderNumbers, status, businessType, dataSource, platformCode, returnFlag, oda,
                        dateType, orderTimeFrom, orderTimeTo,
                        orderTime, orderTimePeriod, fbaText, fbaShipmentId, fba, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        datas = '{' + '"logicWarehouseCode":' + '"' + logicWarehouseCode + '",' + '"logisticsProduct":' + '"' + logisticsProduct + '",' + '"country":' + '"' + country + '",' + '"skuCode":' + '"' + skuCode + '",' + '"firstName":' + '"' + firstName + '",' + '"orderTimeRange":' + '[' + orderTimeRange + '],' + '"orderNumberType":' + '"' + orderNumberType + '",' + '"orderNumbers":' + '["' + orderNumbers + '"],' + '"status":' + '"' + status + '",' + '"businessType":' + '"' + businessType + '",' + '"dataSource":' + '"' + dataSource + '",' + '"platformCode":' + '"' + platformCode + '",' + '"returnFlag":' + '"' + returnFlag + '",' + '"oda":' + '"' + oda + '",' + '"dateType":' + '"' + dateType + '",' + '"orderTimeFrom":' + '"' + orderTimeFrom + '",' + '"orderTimeTo":' + '"' + orderTimeTo + '",' + '"orderTime":' + '[' + orderTime + '],' + '"orderTimePeriod":' + '"' + orderTimePeriod + '",' + '"fbaText":' + '"' + fbaText + '",' + '"fbaShipmentId":' + '"' + fbaShipmentId + '",' + '"fba":' + fba + '}'
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
        consignmentNo = re['result']['records'][0]['consignmentNo']
        if 'None' != re['result']:
            # consignmentNo:出库单号
            WrittenToken.written_orderNumber(int(IDX), consignmentNo)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_search_Outbount(self, case_name, IDX, url, methond, content_type, logicWarehouseCode,
                             logisticsProduct, country, skuCode, firstName, orderTimeRange, orderNumberType,
                             orderNumbers, status, businessType, dataSource, platformCode, returnFlag, oda, dateType,
                             orderTimeFrom, orderTimeTo, orderTime, orderTimePeriod, fbaText, fbaShipmentId, fba,
                             message):

        result = self.search_Outbount(case_name, IDX, url, methond, content_type, logicWarehouseCode,
                                      logisticsProduct, country, skuCode, firstName, orderTimeRange, orderNumberType,
                                      orderNumbers, status, businessType, dataSource, platformCode, returnFlag, oda,
                                      dateType,
                                      orderTimeFrom, orderTimeTo, orderTime, orderTimePeriod, fbaText, fbaShipmentId,
                                      fba,
                                      message)

        datas = '{' + '"logicWarehouseCode":' + '"' + logicWarehouseCode + '",' + '"logisticsProduct":' + '"' + logisticsProduct + '",' + '"country":' + '"' + country + '",' + '"skuCode":' + '"' + skuCode + '",' + '"firstName":' + '"' + firstName + '",' + '"orderTimeRange":' + '[' + orderTimeRange + '],' + '"orderNumberType":' + '"' + orderNumberType + '",' + '"orderNumbers":' + '["' + orderNumbers + '"],' + '"status":' + '"' + status + '",' + '"businessType":' + '"' + businessType + '",' + '"dataSource":' + '"' + dataSource + '",' + '"platformCode":' + '"' + platformCode + '",' + '"returnFlag":' + '"' + returnFlag + '",' + '"oda":' + '"' + oda + '",' + '"dateType":' + '"' + dateType + '",' + '"orderTimeFrom":' + '"' + orderTimeFrom + '",' + '"orderTimeTo":' + '"' + orderTimeTo + '",' + '"orderTime":' + '[' + orderTime + '],' + '"orderTimePeriod":' + '"' + orderTimePeriod + '",' + '"fbaText":' + '"' + fbaText + '",' + '"fbaShipmentId":' + '"' + fbaShipmentId + '",' + '"fba":' + fba + '}'
        """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
