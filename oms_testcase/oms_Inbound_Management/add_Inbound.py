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
from log.case_log import log_case_info

result = get_data('../xls/测试用例数据.xls', 3)


@ddt.ddt
class AddInbound(unittest.TestCase):
    def add_Inbound(self, case_name, IDX, url, methond, content_type, refNo_prefix1, refNo1, toWarehouseCode,
                    fromWarehouseCode, inboundType, transportType, shippingNo, planArriveTime1, planTotalWeight1,
                    planTotalVolume1, remark, boxMarkType, boxNo1, batchNo1, skuCodeprefix, skuCode1, skuNamePrefix,
                    skuName1, planWeight1, planLength1, planWidth1, planHeight1, planQty1, logisticsPackage, message
                    ):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        refNo_prefix = str(refNo_prefix1)
        refNos = str(int(refNo1))
        refNo = refNo_prefix + refNos
        planArriveTime = str(int(planArriveTime1))
        planTotalWeight = str(planTotalWeight1)
        planTotalVolume = str(planTotalVolume1)
        boxNo = str(int(boxNo1))
        batchNo = str(int(batchNo1))
        skuCodes = str(int(skuCode1))
        skuCode = skuCodeprefix + skuCodes
        skuNames = str(int(skuName1))
        skuName = skuNamePrefix + skuNames
        planWeight = str(int(planWeight1) * 1000)
        planLength = str(planLength1)
        planWidth = str(planWidth1)
        planHeight = str(planHeight1)
        planQty = str(planQty1)

        datas = '{' + '"refNo":' + '"' + refNo + '",' + '"toWarehouseCode":' + '"' + toWarehouseCode + '",' + '"fromWarehouseCode":' + '"' + fromWarehouseCode + '",' + '"inboundType":''"' + inboundType + '",' + '"transportType":' + '"' + transportType + '",' + '"shippingNo":' + '"' + shippingNo + '",' + '"planArriveTime":' + planArriveTime + ',' + '"planTotalWeight":' + planTotalWeight + ',' + '"planTotalVolume":' + planTotalVolume + ',' + '"remark":' + '"' + remark + '",' + '"boxMarkType":' + '"' + boxMarkType + '",' + '"skus":' + '[' + '{' + '"boxNo":' + '"' + boxNo + '",' + '"batchNo":' + '"' + batchNo + '",' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"planWeight":' + planWeight + ',' + '"planLength":' + planLength + ',' + '"planWidth":' + planWidth + ',' + '"planHeight":' + planHeight + ',' + '"planQty":' + planQty + ',' + '"logisticsPackage":' + '"' + logisticsPackage + '"}' + ']' + '}'
        data = json.loads(datas)
        logging.info(datas)
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

        if message in re['message'] or '操作成功！' in re['message']:
            # refNo：入库单客户参考号
            WrittenToken.written_refNo(int(IDX), refNo)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_add_Inbound(self, case_name, IDX, url, methond, content_type, refNo_prefix1, refNo1, toWarehouseCode,
                         fromWarehouseCode, inboundType, transportType, shippingNo, planArriveTime1, planTotalWeight1,
                         planTotalVolume1, remark, boxMarkType, boxNo1, batchNo1, skuCodeprefix, skuCode1, skuNamePrefix,
                         skuName1, planWeight1, planLength1, planWidth1, planHeight1, planQty1, logisticsPackage, message):

        result = self.add_Inbound(case_name, IDX, url, methond, content_type, refNo_prefix1, refNo1, toWarehouseCode,
                                  fromWarehouseCode, inboundType, transportType, shippingNo, planArriveTime1, planTotalWeight1,
                                  planTotalVolume1, remark, boxMarkType, boxNo1, batchNo1, skuCodeprefix, skuCode1, skuNamePrefix,
                                  skuName1, planWeight1, planLength1, planWidth1, planHeight1, planQty1, logisticsPackage, message)

        refNo_prefix = str(refNo_prefix1)
        refNos = str(int(refNo1))
        refNo = refNo_prefix + refNos
        planArriveTime = str(int(planArriveTime1))
        planTotalWeight = str(planTotalWeight1)
        planTotalVolume = str(planTotalVolume1)
        boxNo = str(int(boxNo1))
        batchNo = str(int(batchNo1))
        skuCodes = str(int(skuCode1))
        skuCode = skuCodeprefix + skuCodes
        skuNames = str(int(skuName1))
        skuName = skuNamePrefix + skuNames
        planWeight = str(int(planWeight1) * 1000)
        planLength = str(planLength1)
        planWidth = str(planWidth1)
        planHeight = str(planHeight1)
        planQty = str(planQty1)

        datas = '{' + '"refNo":' + '"' + refNo + '",' + '"toWarehouseCode":' + '"' + toWarehouseCode + '",' + '"fromWarehouseCode":' + '"' + fromWarehouseCode + '",' + '"inboundType":''"' + inboundType + '",' + '"transportType":' + '"' + transportType + '",' + '"shippingNo":' + '"' + shippingNo + '",' + '"planArriveTime":' + planArriveTime + ',' + '"planTotalWeight":' + planTotalWeight + ',' + '"planTotalVolume":' + planTotalVolume + ',' + '"remark":' + '"' + remark + '",' + '"boxMarkType":' + '"' + boxMarkType + '",' + '"skus":' + '[' + '{' + '"boxNo":' + '"' + boxNo + '",' + '"batchNo":' + '"' + batchNo + '",' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"planWeight":' + planWeight + ',' + '"planLength":' + planLength + ',' + '"planWidth":' + planWidth + ',' + '"planHeight":' + planHeight + ',' + '"planQty":' + planQty + ',' + '"logisticsPackage":' + '"' + logisticsPackage + '"}' + ']' + '}'

        """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
