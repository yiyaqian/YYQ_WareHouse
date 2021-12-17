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

result = get_data('../xls/测试用例数据2.xls', 18)


@ddt.ddt
class SearchCreatePick(unittest.TestCase):
    def search_CreatePick(self, case_name, IDX, url, methond, content_type, auditTimeRange, pickSortVisible,
                          pickSortActive, pickType1,
                          changeNoStatus1, bizType, consignmentNo, dataSource, orderTimeRange, combinationCodeList,
                          channelList, customerCodeList,
                          roadwayList, layerList, cutOffTime, auditTimeFrom, auditTimeTo, orderTimeFrom, orderTimeTo,
                          fba, fbaShipmentId, refNo, skuId, message):
        self.req = General_request()
        session = WrittenToken.read_WMStoken()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session,
            'tenant_id': '7'
        }
        pickType = str(int(pickType1))
        changeNoStatus = str(int(changeNoStatus1))

        datas = '{' + '"auditTimeRange":' + '[' + auditTimeRange + '],' + '"pickSortVisible":' + pickSortVisible + ',' + '"pickSortActive":' + pickSortActive + ',' + \
                '"pickType":"' + pickType + '",' + '"changeNoStatus":' + '"' + changeNoStatus + '",' + '"bizType":' + '"' + bizType + '",' + '"consignmentNo":' + '"' + \
                consignmentNo + '",' + '"dataSource":' + '"' + dataSource + '",' + '"orderTimeRange":[' + orderTimeRange + '],' + '"combinationCodeList":[' + combinationCodeList + '],' \
                + '"channelList":[' + channelList + '],' + '"customerCodeList":[' + customerCodeList + '],' + '"roadwayList":[' + roadwayList + '],' + '"layerList":[' + layerList + '],' + \
                '"cutOffTime":' + cutOffTime + ',' + '"auditTimeFrom":' + '"' + auditTimeFrom + '",' + '"auditTimeTo":' + '"' + auditTimeTo + '",' + '"orderTimeFrom":' + '"' + orderTimeFrom + '",' + \
                '"orderTimeTo":' + '"' + orderTimeTo + '",' + '"fba":"' + fba + '",' + '"fbaShipmentId":' + '"' + fbaShipmentId + '",' + '"refNo":' + '"' + refNo + '",' + '"skuId":' + '"' + skuId + '"}'
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

        if re['result']['total'] > 0:
            logging.info('info')
            taskId = re['result']['records'][0]['taskId']
            # consignmentNo:出库单号
            WrittenToken.written_TaskIdAndPickType(int(IDX), taskId, pickType)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_search_CreatePick(self, case_name, IDX, url, methond, content_type, auditTimeRange, pickSortVisible,
                               pickSortActive, pickType1,
                               changeNoStatus1, bizType, consignmentNo, dataSource, orderTimeRange, combinationCodeList,
                               channelList, customerCodeList,
                               roadwayList, layerList, cutOffTime, auditTimeFrom, auditTimeTo, orderTimeFrom,
                               orderTimeTo, fba, fbaShipmentId, refNo, skuId, message):

        result = self.search_CreatePick(case_name, IDX, url, methond, content_type, auditTimeRange, pickSortVisible,
                                        pickSortActive, pickType1,
                                        changeNoStatus1, bizType, consignmentNo, dataSource, orderTimeRange,
                                        combinationCodeList, channelList,
                                        customerCodeList, roadwayList, layerList, cutOffTime, auditTimeFrom,
                                        auditTimeTo, orderTimeFrom,
                                        orderTimeTo, fba, fbaShipmentId, refNo, skuId, message)
        pickType = str(int(pickType1))
        changeNoStatus = str(int(changeNoStatus1))

        datas = '{' + '"auditTimeRange":' + '[' + auditTimeRange + '],' + '"pickSortVisible":' + pickSortVisible + ',' + '"pickSortActive":' + pickSortActive + ',' + \
                '"pickType":"' + pickType + '",' + '"changeNoStatus":' + '"' + changeNoStatus + '",' + '"bizType":' + '"' + bizType + '",' + '"consignmentNo":' + '"' + \
                consignmentNo + '",' + '"dataSource":' + '"' + dataSource + '",' + '"orderTimeRange":[' + orderTimeRange + '],' + '"combinationCodeList":[' + combinationCodeList + '],' \
                + '"channelList":[' + channelList + '],' + '"customerCodeList":[' + customerCodeList + '],' + '"roadwayList":[' + roadwayList + '],' + '"layerList":[' + layerList + '],' + \
                '"cutOffTime":' + cutOffTime + ',' + '"auditTimeFrom":' + '"' + auditTimeFrom + '",' + '"auditTimeTo":' + '"' + auditTimeTo + '",' + '"orderTimeFrom":' + '"' + orderTimeFrom + '",' + \
                '"orderTimeTo":' + '"' + orderTimeTo + '",' + '"fba":"' + fba + '",' + '"fbaShipmentId":' + '"' + fbaShipmentId + '",' + '"refNo":' + '"' + refNo + '",' + '"skuId":' + '"' + skuId + '"}'

        """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
