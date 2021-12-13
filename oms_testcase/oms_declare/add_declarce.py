"""
新增申报产品接口
"""
import ast
import logging
import unittest
from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import warnings
from log.case_log import log_case_info


class AddDeclarce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    # OMS登录接口
    def test_add_declarce_normal(self):
        self.data_list = excel_to_list("../../xls/测试用例数据.xls", "申报产品管理-新增和编辑")  # 读取该测试类所有用例数据
        length = len(self.data_list)
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
            prefix = case_data.get('prefix')
            declareGoodsCodes = str(case_data.get('declareGoodsCode'))
            declareGoodsCode = prefix + declareGoodsCodes
            category = str(case_data.get('category'))
            categoryName = case_data.get('categoryName')
            categoryNameEn = case_data.get('categoryNameEn')
            purpose = case_data.get('purpose')
            model = case_data.get('model')
            originCountry = case_data.get('originCountry')
            material = case_data.get('material')
            brand = case_data.get('brand')
            country = case_data.get('country')
            declareValue = str(case_data.get('declareValue'))
            currency = case_data.get('currency')
            status = case_data.get('status')
            hsCode = str(case_data.get('hsCode'))
            tariffRate = str(case_data.get('tariffRate'))
            skuCodeprefix = case_data.get('skuCodeprefix')
            skuCodes = str(int(case_data.get('skuCode')))
            skuCode = skuCodeprefix + skuCodes
            skuNamePrefix = case_data.get('skuNamePrefix')
            skuNames = str(int(case_data.get('skuName')))
            skuName = skuNamePrefix + skuNames
            declareStatus = case_data.get('declareStatus')
            datas = '{' + '"declareGoodsCode":' + '"' + declareGoodsCode + '",' + '"category":' + '"' + category + '",' + '"categoryName":' + '"' + categoryName + '",' + '"categoryNameEn":' + '"' + categoryNameEn + '",' + '"declareStatus":''"' + declareStatus + '",' + '"purpose":' + '"' + purpose + '",' + '"model":' + '"' + model + '",' + '"originCountry":' + '"' + originCountry + '",' + '"material":' + '"' + material + '",' + '"brand":' + '"' + brand + '",' + '"declareCountryList":' + '[' + '{' + '"country":' + '"' + country + '",' + '"declareValue":' + declareValue + ',' + '"currency":' + '"' + currency + '",' + '"declareValue":' + declareValue + ',' + '"currency":' + '"' + currency + '",' + '"status":' + '"' + status + '",' + '"hsCode":' + '"' + hsCode + '",' + '"tariffRate":' + tariffRate + '}' + '],' + '"declareSkuList":' + '[' + '{' + '"skuCode":' + '"' + skuCode + '",' + '"skuName":' + '"' + skuName + '",' + '"declareStatus":' + '"' + declareStatus + '"' + '}' + ']' + '}'
            data = ast.literal_eval(datas)
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

            # declareGoodsCode:申报产品代码
            WrittenToken.written_declareGoodsCode(i + 1, declareGoodsCode)
            # brand:品牌、skucode：sku代码
            WrittenToken.written_brand_and_skuCode(i + 1, brand, skuCode)
            """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, datas, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
