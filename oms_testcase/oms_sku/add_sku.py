"""
新增SKU接口
"""

import json
import unittest
from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import warnings
from log.case_log import log_case_info
from xlutils.copy import copy
import os


class AddSku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    # 新增SKU接口
    def test_add_sku_normal(self):
        # 1.读取该测试类所有用例数据
        self.data_list = excel_to_list("../xls/测试用例数据.xls", "新增和编辑SKU")
        length = len(self.data_list)
        # 2.循环读取每一行数据，拼接请求参数
        for i in range(0, length):
            "1.获取场景名称 "
            case_name = self.data_list[i - 1].get('场景')

            "2.通过场景名称:casename   在data_list[该表中所有用例数据]查找到该用例数据"
            case_data = get_test_data(self.data_list, case_name)

            """
            3.
             3.1 从字典case_data中读取数据url、data、message、headers，
             3.2 并分别保存在变量url、data、message、header中
             3.3 注意字符串格式需用json.loads()转化为字典格式
            """
            url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
            message = case_data.get('message')  # 期望数据
            content_type = case_data.get('Content-Type')

            # 获取请求参数
            "SKU代码"
            skuCodeprefix = str(case_data.get('skuCodeprefix'))
            skuCodes = str(int(case_data.get('skuCode')))
            skuCode = skuCodeprefix + skuCodes

            "SKU名称"
            skuNamePrefix = case_data.get('skuNamePrefix')
            skuNames = str(int(case_data.get('skuName')))
            skuName = skuNamePrefix + skuNames

            uom = case_data.get('uom')

            wrapping = case_data.get('wrapping')

            packageModel = str(int(case_data.get('packageModel')))

            packageMaterial = str(int(case_data.get('packageMaterial')))

            characteristic = case_data.get('characteristic')

            businessType = str(int(case_data.get('businessType')))

            firstPassType = str(int(case_data.get('firstPassType')))

            salesLink = str(case_data.get('salesLink'))

            "备注"
            remark = case_data.get('remark')

            specification = case_data.get('specification')

            "实收重量"
            Weight = str(int(case_data.get('weight')))

            "实收长度"
            Length = str(case_data.get('length'))

            "实收宽度"
            Width = str(case_data.get('width'))

            "实收高度"
            Height = str(case_data.get('height'))

            "预报重量"
            expWeight = str(int(case_data.get('expWeight')))

            "预报长度"
            expLength = str(case_data.get('expLength'))

            "预报宽度"
            expWidth = str(case_data.get('expWidth'))

            "预报高度"
            expHeight = str(case_data.get('expHeight'))

            "效期管理"
            expiredDate = case_data.get('expiredDate')

            "批次管理"
            isBatch = case_data.get('isBatch')

            isBattery = case_data.get('isBattery')

            batteryConfig = case_data.get('batteryConfig')

            batteryPower = case_data.get('batteryPower')

            batteryNumber = str(int(case_data.get('batteryNumber')))

            batteryType = case_data.get('batteryType')

            snRuleCode = str(case_data.get('snRuleCode'))

            logisticsPackage = case_data.get('logisticsPackage')

            barcodeList = case_data.get('barcodeList')

            declareCountryList = case_data.get('declareCountryList')

            whetherToDeclare = case_data.get('whetherToDeclare')

            isSelectDeclare = case_data.get('isSelectDeclare')

            # 拼接请求参数
            datas = '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"uom":' + '"' + uom + '",' + '"wrapping":''"' + wrapping + '",' + '"packageModel":' + '"' + packageModel + '",' + '"packageMaterial":' + '"' + packageMaterial + '",' + '"characteristic":' + '"' + characteristic + '",' + '"businessType":' + '"' + businessType + '",' + '"firstPassType":' + '"' + firstPassType + '",' + '"salesLink":' + '"' + salesLink + '",' + '"remark":' + '"' + remark + '",' + '"specification":' + '"' + specification + '",' + '"weight":' + '"' + Weight + '",' + '"length":' + '"' + Length + '",' + '"width":' + '"' + Width + '",' + '"height":' + '"' + Height + '",' + '"expWeight":' + '"' + expWeight + '",' + '"expLength":' + '"' + expLength + '",' + '"expWidth":' + '"' + expWidth + '",' + '"expHeight":' + '"' + expHeight + '",' + '"expiredDate":' + '"' + expiredDate + '",' + '"isBatch":' + '"' + isBatch + '",' + '"isBattery":' + '"' + isBattery + '",' + '"batteryConfig":' + '"' + batteryConfig + '",' + '"batteryPower":' + '"' + batteryPower + '",' + '"batteryNumber":' + batteryNumber + ',' + '"batteryType":' + '"' + batteryType + '",' + '"snRuleCode":' + '"' + snRuleCode + '",' + '"logisticsPackage":' + '"' + logisticsPackage + '",' + '"barcodeList":' + barcodeList + ',' + '"declareDTO":' + '{' + '"declareCountryList":' + declareCountryList + '},' + '"whetherToDeclare":' + '"' + whetherToDeclare + '",' + '"isSelectDeclare":' + isSelectDeclare + '}'

            data = json.loads(datas)
            session = WrittenToken.read_token()  # 调用获取token的方法
            header = {
                'Content-Type': content_type,
                'x-access-token': session
            }  # 注意字符串格式，需要用json.loads()转化为字典格式
            methond = case_data.get('method')

            # 3.判断method是否等于"POST" ，是进入if反之则进入else
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

            # skucode:sku代码、businessType：业务类型
            WrittenToken.written_SKU(i, skuCode, businessType)

            """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, datas, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
