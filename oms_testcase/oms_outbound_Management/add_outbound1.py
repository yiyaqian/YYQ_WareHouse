"""
新增入库单接口
"""
import json
import logging
import unittest
from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import warnings
from log.case_log import log_case_info


class AddOutbound(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    def test_add_Outbount_normal(self):
        self.data_list = excel_to_list("../xls/测试用例数据.xls", "新增出库单")  # 读取该测试类所有用例数据
        length = len(self.data_list)
        logging.info(length)
        for i in range(0, length):
            logging.info("欢迎进入for循环")
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

            # 请求参数
            businessType = str(case_data.get('businessType'))
            logicWarehouseCode = case_data.get('logicWarehouseCode')
            salesNo = case_data.get('salesNo')
            refNo_prefix = case_data.get('refNo-prefix ')
            refNos = str(int(case_data.get('refNo')))
            refNo = refNo_prefix + refNos
            platformCode = case_data.get('platformCode')
            shopName = case_data.get('shopName')
            shopId = case_data.get('shopId')
            shippingNo = case_data.get('shippingNo')
            sellerId = case_data.get('sellerId')
            firstName = case_data.get('firstName')
            country = case_data.get('country')
            state = case_data.get('state')
            city = case_data.get('city')
            postCode = case_data.get('postCode')
            houseNumber = case_data.get('houseNumber')
            company = case_data.get('company')
            telephone = case_data.get('telephone')
            street = case_data.get('street')
            logisticsProduct = case_data.get('logisticsProduct')
            vat = case_data.get('vat')
            ioss = case_data.get('ioss')
            declareCurrency = case_data.get('declareCurrency')
            totalDeclareValue = str(int(case_data.get('totalDeclareValue')))
            hsCode = case_data.get('hsCode')
            exportCompany = case_data.get('exportCompany')
            exportCompanyAddress = case_data.get('exportCompanyAddress')
            skuId = case_data.get('skuId')
            skuCodeprefix = case_data.get('skuCodeprefix')
            skuCodes = str(int(case_data.get('skuCode')))
            skuCode = skuCodeprefix + skuCodes
            skuNamePrefix = case_data.get('skuNamePrefix')
            skuNames = str(int(case_data.get('skuName')))
            skuName = skuNamePrefix + skuNames
            qty = str(int(case_data.get('qty')))
            stockQuality = case_data.get('stockQuality')
            batchNo = case_data.get('batchNo')
            remark = case_data.get('remark')
            email = case_data.get('email')
            audit = case_data.get('audit')

            datas = '{' + '"businessType":' + '"' + businessType + '",' + '"logicWarehouseCode":' + '"' + logicWarehouseCode + '",' + '"salesNo":' + '"' + salesNo + '",' + '"refNo":''"' + refNo + '",' + '"platformCode":' + '"' + platformCode + '",' + '"shopName":' + '"' + shopName + '",' + '"shopId":' + '"' + shopId + '",' + '"shippingNo":' + '"' + shippingNo + '",' + '"sellerId":' + '"' + sellerId + '",' + '"firstName":' + '"' + firstName + '",' + '"country":' + '"' + country + '",' + '"state":' + '"' + state + '",' + '"city":' + '"' + city + '",' + '"postCode":' + '"' + postCode + '",' + '"houseNumber":' + '"' + houseNumber + '",' + '"company":' + '"' + company + '",' + '"telephone":' + '"' + telephone + '",' + '"street":' + '"' + street + '",' + '"logisticsProduct":' + '"' + logisticsProduct + '",' + '"vat":' + '"' + vat + '",' + '"ioss":' + '"' + ioss + '",' + '"totalDeclareValue":' + totalDeclareValue + ',' + '"declareCurrency":' + '"' + declareCurrency + '",' + '"hsCode":' + '"' + hsCode + '",' + '"exportCompany":' + '"' + exportCompany + '",' + '"exportCompanyAddress":' + '"' + exportCompanyAddress + '",' + '"skus":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"qty":' + qty + ',' + '"stockQuality":' + '"' + stockQuality + '",' + '"batchNo":' + '"' + batchNo + '"' + '}' + '],' + '"remark":' + '"' + remark + '",' + '"skuForm":' + '{' + '"stockQuality":' + '"' + stockQuality + '"' + '},' + '"email":' + '"' + email + '",' + '"audit":' + audit + '}'
            logging.info(datas)
            data = json.loads(datas)

            session = WrittenToken.read_token()  # 调用获取token的方法
            header = {
                'Content-Type': content_type,
                'x-access-token': session
            }  # 注意字符串格式，需要用json.loads()转化为字典格式
            methond = case_data.get('method')

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

            # refNo：入库单客户参考号
            # WrittenToken.written_refNo(i + 1, refNo)
            """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, datas, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
