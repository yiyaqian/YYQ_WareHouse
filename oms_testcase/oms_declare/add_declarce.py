"""
新增申报产品接口
"""
import json
import logging
import unittest
import ddt
from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
from log.case_log import log_case_info

result = get_data('../xls/测试用例数据.xls', 1)


@ddt.ddt
class AddDeclarce(unittest.TestCase):

    def add_declarce(self, case_name, IDX, url, methond, Content_Type, prefix, declareGoodsCodes, categorys,
                     categoryName,
                     categoryNameEn, declareStatus, purpose, model, originCountry, material, brand, country,
                     declareValues,
                     currency, status, hsCodes, tariffRates, skuCodeprefix, skuCodes, skuNamePrefix, skuNames, message):
        self.req = General_request()
        # session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': Content_Type,
            'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzk2MzkxOTQsInVzZXJuYW1lIjoieXVqayJ9.569tSxvYnPbmWVFAW4VO9DMW-nD3YLX-UJn4wCv3Goo'
        }
        declareGoodsCode = prefix + declareGoodsCodes
        skuCode = skuCodeprefix + str(int(skuCodes))
        skuName = skuNamePrefix + str(int(skuNames))
        category = str(int(categorys))
        declareValue = str(int(declareValues))
        hsCode = str(int(hsCodes))
        tariffRate = str(tariffRates)
        datas = '{' + '"declareGoodsCode":' + '"' + declareGoodsCode + '",' + '"category":' + '"' + category + '",' + '"categoryName":' + '"' + categoryName + '",' + \
                '"categoryNameEn":' + '"' + categoryNameEn + '",' + '"declareStatus":''"' + declareStatus + '",' + '"purpose":' + '"' + purpose + '",' + '"model":' + '"' + model + '",' + \
                '"originCountry":' + '"' + originCountry + '",' + '"material":' + '"' + material + '",' + '"brand":' + '"' + brand + '",' + '"declareCountryList":' + '[' + '{' + '"country":' + '"' + country + '",' + '"declareValue":' + \
                declareValue + ',' + '"currency":' + '"' + currency + '",' + '"declareValue":' + declareValue + ',' + '"currency":' + '"' + currency + '",' + '"status":' + '"' + status + '",' + \
                '"hsCode":' + '"' + hsCode + '",' + '"tariffRate":' + tariffRate + '}' + '],' + '"declareSkuList":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' \
                + '"declareStatus":' + '"' + declareStatus + '"' + '}' + ']' + '}'

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

        if message in re['message']:
            # declareGoodsCode:申报产品代码
            WrittenToken.written_declareGoodsCode(int(IDX), declareGoodsCode)
            # brand:品牌、skucode：sku代码
            WrittenToken.written_brand_and_skuCode(int(IDX), brand, skuCode)

        return re

    @ddt.data(*result)
    @ddt.unpack
    # 进行参数化
    def test_add_declarce(self, case_name, IDX, url, methond, Content_Type, prefix, declareGoodsCodes, categorys,
                          categoryName,
                          categoryNameEn, declareStatus, purpose, model, originCountry, material, brand, country,
                          declareValues,
                          currency, status, hsCodes, tariffRates, skuCodeprefix, skuCodes, skuNamePrefix, skuNames,
                          message):

        result = self.add_declarce(case_name, IDX, url, methond, Content_Type, prefix, declareGoodsCodes, categorys,
                                   categoryName,
                                   categoryNameEn, declareStatus, purpose, model, originCountry, material, brand,
                                   country,
                                   declareValues,
                                   currency, status, hsCodes, tariffRates, skuCodeprefix, skuCodes, skuNamePrefix,
                                   skuNames,
                                   message)

        declareGoodsCode = prefix + declareGoodsCodes
        skuCode = skuCodeprefix + str(int(skuCodes))
        skuName = skuNamePrefix + str(int(skuNames))
        category = str(int(categorys))
        declareValue = str(int(declareValues))
        hsCode = str(int(hsCodes))
        tariffRate = str(tariffRates)

        datas = '{' + '"declareGoodsCode":' + '"' + declareGoodsCode + '",' + '"category":' + '"' + category + '",' + '"categoryName":' + '"' + categoryName + '",' + \
                '"categoryNameEn":' + '"' + categoryNameEn + '",' + '"declareStatus":''"' + declareStatus + '",' + '"purpose":' + '"' + purpose + '",' + '"model":' + '"' + model + '",' + \
                '"originCountry":' + '"' + originCountry + '",' + '"material":' + '"' + material + '",' + '"brand":' + '"' + brand + '",' + '"declareCountryList":' + '[' + '{' + '"country":' + '"' + country + '",' + '"declareValue":' + \
                declareValue + ',' + '"currency":' + '"' + currency + '",' + '"declareValue":' + declareValue + ',' + '"currency":' + '"' + currency + '",' + '"status":' + '"' + status + '",' + \
                '"hsCode":' + '"' + hsCode + '",' + '"tariffRate":' + tariffRate + '}' + '],' + '"declareSkuList":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' \
                + '"declareStatus":' + '"' + declareStatus + '"' + '}' + ']' + '}'

        # # "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        self.assertEqual(message, result['message'])
