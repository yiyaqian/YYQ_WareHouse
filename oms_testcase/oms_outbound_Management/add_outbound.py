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

result = get_data('../xls/测试用例数据.xls', 5)


@ddt.ddt
class AddOutbound(unittest.TestCase):
    def add_Outbount(self, case_name, IDX, url, methond, content_type, businessType1, logicWarehouseCode, salesNo,
                     refNo_prefix,
                     refNo1, platformCode, shopName, shopId, shippingNo, sellerId, firstName, country, state, city,
                     postCode,
                     houseNumber, company, telephone, street, logisticsProduct, vat, ioss, totalDeclareValue1,
                     declareCurrency,
                     hsCode, exportCompany, exportCompanyAddress, skuId, skuCodeprefix, skuCode1, skuNamePrefix,
                     skuName1, qty1,
                     stockQuality, batchNo, remark, email, audit, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        businessType = str(businessType1)
        refNo = refNo_prefix + str(int(refNo1))
        totalDeclareValue = str(int(totalDeclareValue1))
        skuCode = skuCodeprefix + str(int(skuCode1))
        skuName = skuNamePrefix + str(int(skuName1))
        qty = str(int(qty1))
        datas = '{' + '"businessType":' + '"' + businessType + '",' + '"logicWarehouseCode":' + '"' + logicWarehouseCode + '",' + '"salesNo":' + '"' + salesNo + '",' + '"refNo":''"' + refNo + '",' + '"platformCode":' + '"' + platformCode + '",' + '"shopName":' + '"' + shopName + '",' + '"shopId":' + '"' + shopId + '",' + '"shippingNo":' + '"' + shippingNo + '",' + '"sellerId":' + '"' + sellerId + '",' + '"firstName":' + '"' + firstName + '",' + '"country":' + '"' + country + '",' + '"state":' + '"' + state + '",' + '"city":' + '"' + city + '",' + '"postCode":' + '"' + postCode + '",' + '"houseNumber":' + '"' + houseNumber + '",' + '"company":' + '"' + company + '",' + '"telephone":' + '"' + telephone + '",' + '"street":' + '"' + street + '",' + '"logisticsProduct":' + '"' + logisticsProduct + '",' + '"vat":' + '"' + vat + '",' + '"ioss":' + '"' + ioss + '",' + '"totalDeclareValue":' + totalDeclareValue + ',' + '"declareCurrency":' + '"' + declareCurrency + '",' + '"hsCode":' + '"' + hsCode + '",' + '"exportCompany":' + '"' + exportCompany + '",' + '"exportCompanyAddress":' + '"' + exportCompanyAddress + '",' + '"skus":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"qty":' + qty + ',' + '"stockQuality":' + '"' + stockQuality + '",' + '"batchNo":' + '"' + batchNo + '"' + '}' + '],' + '"remark":' + '"' + remark + '",' + '"skuForm":' + '{' + '"stockQuality":' + '"' + stockQuality + '"' + '},' + '"email":' + '"' + email + '",' + '"audit":' + audit + '}'
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

        if message in re['message']:
            # refNo:参考号
            WrittenToken.written_out_refo(int(IDX), refNo)

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_add_Outbount(self, case_name, IDX, url, methond, content_type, businessType1, logicWarehouseCode, salesNo,
                          refNo_prefix,
                          refNo1, platformCode, shopName, shopId, shippingNo, sellerId, firstName, country, state, city,
                          postCode,
                          houseNumber, company, telephone, street, logisticsProduct, vat, ioss, totalDeclareValue1,
                          declareCurrency,
                          hsCode, exportCompany, exportCompanyAddress, skuId, skuCodeprefix, skuCode1, skuNamePrefix,
                          skuName1, qty1,
                          stockQuality, batchNo, remark, email, audit, message):

        result = self.add_Outbount(case_name, IDX, url, methond, content_type, businessType1, logicWarehouseCode,
                                   salesNo, refNo_prefix,
                                   refNo1, platformCode, shopName, shopId, shippingNo, sellerId, firstName, country,
                                   state, city, postCode,
                                   houseNumber, company, telephone, street, logisticsProduct, vat, ioss,
                                   totalDeclareValue1, declareCurrency,
                                   hsCode, exportCompany, exportCompanyAddress, skuId, skuCodeprefix, skuCode1,
                                   skuNamePrefix, skuName1, qty1,
                                   stockQuality, batchNo, remark, email, audit, message)

        businessType = str(businessType1)
        refNo = refNo_prefix + str(int(refNo1))
        totalDeclareValue = str(int(totalDeclareValue1))
        skuCode = skuCodeprefix + str(int(skuCode1))
        skuName = skuNamePrefix + str(int(skuName1))
        qty = str(int(qty1))
        datas = '{' + '"businessType":' + '"' + businessType + '",' + '"logicWarehouseCode":' + '"' + logicWarehouseCode + '",' + '"salesNo":' + '"' + salesNo + '",' + '"refNo":''"' + refNo + '",' + '"platformCode":' + '"' + platformCode + '",' + '"shopName":' + '"' + shopName + '",' + '"shopId":' + '"' + shopId + '",' + '"shippingNo":' + '"' + shippingNo + '",' + '"sellerId":' + '"' + sellerId + '",' + '"firstName":' + '"' + firstName + '",' + '"country":' + '"' + country + '",' + '"state":' + '"' + state + '",' + '"city":' + '"' + city + '",' + '"postCode":' + '"' + postCode + '",' + '"houseNumber":' + '"' + houseNumber + '",' + '"company":' + '"' + company + '",' + '"telephone":' + '"' + telephone + '",' + '"street":' + '"' + street + '",' + '"logisticsProduct":' + '"' + logisticsProduct + '",' + '"vat":' + '"' + vat + '",' + '"ioss":' + '"' + ioss + '",' + '"totalDeclareValue":' + totalDeclareValue + ',' + '"declareCurrency":' + '"' + declareCurrency + '",' + '"hsCode":' + '"' + hsCode + '",' + '"exportCompany":' + '"' + exportCompany + '",' + '"exportCompanyAddress":' + '"' + exportCompanyAddress + '",' + '"skus":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"qty":' + qty + ',' + '"stockQuality":' + '"' + stockQuality + '",' + '"batchNo":' + '"' + batchNo + '"' + '}' + '],' + '"remark":' + '"' + remark + '",' + '"skuForm":' + '{' + '"stockQuality":' + '"' + stockQuality + '"' + '},' + '"email":' + '"' + email + '",' + '"audit":' + audit + '}'

        """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
        log_case_info(case_name, url, datas, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
