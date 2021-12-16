"""
新增SKU接口
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
from xlutils.copy import copy
import os

# 获取到“新增和编辑SKU”sheet表中的数据
result = get_data('../xls/测试用例数据.xls', 0)


@ddt.ddt
class AddSku(unittest.TestCase):
    def add_sku(self, case_name, IDX, url, methond, Content_Type, skuCodeprefix1, skuCode1, status, skuNamePrefix,
                skuName1, uom, wrapping, packageModel1, packageMaterial1, characteristic, businessType1, firstPassType1,
                salesLink1, remark, specification, weight1, length1, width1, height1, expWeight1, expLength1,
                expWidth1, expHeight1, expiredDate, isBatch, isBattery, batteryConfig, batteryPower,
                batteryNumber1, batteryType, snRuleCode1, logisticsPackage, barcodeList, declareCountryList,
                whetherToDeclare, isSelectDeclare, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': Content_Type,
            'x-access-token': session,
            'tenant_id': '0'
        }
        "SKU代码"
        skuCodeprefix = str(skuCodeprefix1)
        skuCodes = str(int(skuCode1))
        skuCode = skuCodeprefix + skuCodes
        "SKU名称"
        skuNames = str(int(skuName1))
        skuName = skuNamePrefix + skuNames
        packageModel = str(int(packageModel1))
        packageMaterial = str(int(packageMaterial1))
        businessType = str(int(businessType1))
        firstPassType = str(int(firstPassType1))
        salesLink = str(salesLink1)
        weight = str(int(weight1))
        length = str(length1)
        width = str(width1)
        height = str(height1)
        expWeight = str(int(expWeight1))
        expLength = str(expLength1)
        expWidth = str(expWidth1)
        expHeight = str(expHeight1)
        batteryNumber = str(int(batteryNumber1))
        snRuleCode = str(snRuleCode1)
        datas = '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"uom":' + '"' + uom + '",' + '"wrapping":''"' + wrapping + '",' + '"packageModel":' + '"' + packageModel + '",' + '"packageMaterial":' + '"' + packageMaterial + '",' + '"characteristic":' + '"' + characteristic + '",' + '"businessType":' + '"' + businessType + '",' + '"firstPassType":' + '"' + firstPassType + '",' + '"salesLink":' + '"' + salesLink + '",' + '"remark":' + '"' + remark + '",' + '"specification":' + '"' + specification + '",' + '"weight":' + '"' + weight + '",' + '"length":' + '"' + length + '",' + '"width":' + '"' + width + '",' + '"height":' + '"' + height + '",' + '"expWeight":' + '"' + expWeight + '",' + '"expLength":' + '"' + expLength + '",' + '"expWidth":' + '"' + expWidth + '",' + '"expHeight":' + '"' + expHeight + '",' + '"expiredDate":' + '"' + expiredDate + '",' + '"isBatch":' + '"' + isBatch + '",' + '"isBattery":' + '"' + isBattery + '",' + '"batteryConfig":' + '"' + batteryConfig + '",' + '"batteryPower":' + '"' + batteryPower + '",' + '"batteryNumber":' + batteryNumber + ',' + '"batteryType":' + '"' + batteryType + '",' + '"snRuleCode":' + '"' + snRuleCode + '",' + '"logisticsPackage":' + '"' + logisticsPackage + '",' + '"barcodeList":' + barcodeList + ',' + '"declareDTO":' + '{' + '"declareCountryList":' + declareCountryList + '},' + '"whetherToDeclare":' + '"' + whetherToDeclare + '",' + '"isSelectDeclare":' + isSelectDeclare + '}'
        data = json.loads(datas)
        logging.info(int(IDX))
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
            # skucode:sku代码、businessType：业务类型
            WrittenToken.written_SKU(int(IDX), skuCode, businessType)
        return re

    # 新增SKU接口
    @ddt.data(*result)
    @ddt.unpack
    def test_add_sku(self, case_name, IDX, url, methond, Content_Type, skuCodeprefix1, skuCode1, status, skuNamePrefix,
                     skuName1, uom, wrapping, packageModel1, packageMaterial1, characteristic, businessType1,
                     firstPassType1,
                     salesLink1, remark, specification, weight1, length1, width1, height1, expWeight1, expLength1,
                     expWidth1, expHeight1, expiredDate, isBatch, isBattery, batteryConfig, batteryPower,
                     batteryNumber1, batteryType, snRuleCode1, logisticsPackage, barcodeList, declareCountryList,
                     whetherToDeclare, isSelectDeclare, message):
        result = self.add_sku(case_name, IDX, url, methond, Content_Type, skuCodeprefix1, skuCode1, status,
                              skuNamePrefix,
                              skuName1, uom, wrapping, packageModel1, packageMaterial1, characteristic, businessType1,
                              firstPassType1,
                              salesLink1, remark, specification, weight1, length1, width1, height1, expWeight1,
                              expLength1,
                              expWidth1, expHeight1, expiredDate, isBatch, isBattery, batteryConfig, batteryPower,
                              batteryNumber1, batteryType, snRuleCode1, logisticsPackage, barcodeList,
                              declareCountryList,
                              whetherToDeclare, isSelectDeclare, message)
        "SKU代码"
        skuCodeprefix = str(skuCodeprefix1)
        skuCodes = str(int(skuCode1))
        skuCode = skuCodeprefix + skuCodes
        "SKU名称"
        skuNames = str(int(skuName1))
        skuName = skuNamePrefix + skuNames
        packageModel = str(int(packageModel1))
        packageMaterial = str(int(packageMaterial1))
        businessType = str(int(businessType1))
        firstPassType = str(int(firstPassType1))
        salesLink = str(salesLink1)
        weight = str(int(weight1))
        length = str(length1)
        width = str(width1)
        height = str(height1)
        expWeight = str(int(expWeight1))
        expLength = str(expLength1)
        expWidth = str(expWidth1)
        expHeight = str(expHeight1)
        batteryNumber = str(int(batteryNumber1))
        snRuleCode = str(snRuleCode1)
        datas = '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"uom":' + '"' + uom + '",' + '"wrapping":''"' + wrapping + '",' + '"packageModel":' + '"' + packageModel + '",' + '"packageMaterial":' + '"' + packageMaterial + '",' + '"characteristic":' + '"' + characteristic + '",' + '"businessType":' + '"' + businessType + '",' + '"firstPassType":' + '"' + firstPassType + '",' + '"salesLink":' + '"' + salesLink + '",' + '"remark":' + '"' + remark + '",' + '"specification":' + '"' + specification + '",' + '"weight":' + '"' + weight + '",' + '"length":' + '"' + length + '",' + '"width":' + '"' + width + '",' + '"height":' + '"' + height + '",' + '"expWeight":' + '"' + expWeight + '",' + '"expLength":' + '"' + expLength + '",' + '"expWidth":' + '"' + expWidth + '",' + '"expHeight":' + '"' + expHeight + '",' + '"expiredDate":' + '"' + expiredDate + '",' + '"isBatch":' + '"' + isBatch + '",' + '"isBattery":' + '"' + isBattery + '",' + '"batteryConfig":' + '"' + batteryConfig + '",' + '"batteryPower":' + '"' + batteryPower + '",' + '"batteryNumber":' + batteryNumber + ',' + '"batteryType":' + '"' + batteryType + '",' + '"snRuleCode":' + '"' + snRuleCode + '",' + '"logisticsPackage":' + '"' + logisticsPackage + '",' + '"barcodeList":' + barcodeList + ',' + '"declareDTO":' + '{' + '"declareCountryList":' + declareCountryList + '},' + '"whetherToDeclare":' + '"' + whetherToDeclare + '",' + '"isSelectDeclare":' + isSelectDeclare + '}'
        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
