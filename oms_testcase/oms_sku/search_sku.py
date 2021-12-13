"""
查询SKU接口
"""
import logging
import unittest

import ddt

from excel.read_excel import *  # 导入read_excel中的方法
import json  # 用来转化excel中的json字符串为字典
from log.case_log import log_case_info  # 导入方法
from lib.general_request import General_request
import warnings
from excel.written_token import WrittenToken

result = get_data('../xls/测试用例数据2.xls', 0)


@ddt.ddt
class SearchSku(unittest.TestCase):

    def search_sku(self, case_name, IDX, url, methond, content_type, keyWords, businessType1, keyType1, originCountry, timeRange, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        businessType = str(businessType1)
        keyType = str(int(keyType1))
        datas = '{' + '"keyWords":' + '[' + '"' + keyWords + '"' + '],' + '"businessType":' + businessType + ',' + '"keyType":' + keyType + ',' + '"originCountry":' + '"' + originCountry + '",' + '"timeRange":' + timeRange + '}'
        data = json.loads(datas)
        if methond == 'POST':

            "3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用"
            res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
        else:
            "3.1请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用"
            res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用

        logging.info(re)
        ids = re['result']['records'][0]['id']

        # # 4.调用写入审核和作废SKU的sheet表中的id方法
        WrittenToken.written_id(int(IDX), ids)
        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_search_sku(self, case_name, IDX, url, methond, content_type, keyWords, businessType1, keyType1, originCountry, timeRange, message):
            result=self.search_sku(case_name, IDX, url, methond, content_type, keyWords, businessType1, keyType1, originCountry, timeRange, message)
            businessType = str(businessType1)
            keyType = str(int(keyType1))
            datas = '{' + '"keyWords":' + '[' + '"' + keyWords + '"' + '],' + '"businessType":' + businessType + ',' + '"keyType":' + keyType + ',' + '"originCountry":' + '"' + originCountry + '",' + '"timeRange":' + timeRange + '}'
            "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
            log_case_info(case_name, url, datas, message, result)
            self.assertEqual(message, result['message'])  # 改为assertEqual断言

