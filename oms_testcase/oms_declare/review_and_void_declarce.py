"""
审核和作废SKU接口
"""
import unittest

import ddt

from excel.read_excel import *
import json
from log.case_log import log_case_info
from lib.general_request import General_request
import warnings
from excel.written_token import WrittenToken

result = get_data("../xls/测试用例数据2.xls", 5)


@ddt.ddt
class ReviewAndVoid_Declarce(unittest.TestCase):

    def ReviewAndVoid_Declarce(self, case_name, IDX, url, methond, content_type, id, status, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'Content-Type': content_type,
            'x-access-token': session
        }
        ids = str(int(id))
        datas = '{' + '"ids":' + '[' + ids + '],' + '"status":' + '"' + status + '"' + '}'
        data = json.loads(datas)
        # 3.判断method是否等于"POST" ，是进入if反之则进入else
        if methond == 'POST':
            """
                3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
            res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用

        else:
            """
                 3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
            res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用

        return re

    @ddt.data(*result)
    @ddt.unpack
    def test_ReviewAndVoid_Declarce(self, case_name, IDX, url, methond, content_type, id, status, message):
        result = self.ReviewAndVoid_Declarce(case_name, IDX, url, methond, content_type, id, status, message)
        ids = str(int(id))
        datas = '{' + '"ids":' + '[' + ids + '],' + '"status":' + '"' + status + '"' + '}'
        "4.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, datas, message, result)
        "5.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
