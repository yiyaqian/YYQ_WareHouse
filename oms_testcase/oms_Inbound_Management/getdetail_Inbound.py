"""
获取入库单详情内容
"""
import logging
import unittest

import ddt

from excel.read_excel import *
from log.case_log import log_case_info
from lib.general_request import General_request
import warnings
from excel.written_token import WrittenToken

result = get_data('../xls/测试用例数据2.xls', 8)


@ddt.ddt
class GetDetailInbound(unittest.TestCase):

    def getdetai_Inbound(self, case_name, IDX, urls, methond, orderNo, message):
        self.req = General_request()
        session = WrittenToken.read_token()  # 调用获取token的方法
        header = {
            'x-access-token': session
        }
        url = urls + orderNo
        logging.info(url)
        if methond == 'POST':
            """
                4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
            res = self.req.post_way(url=url, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
        else:
            """
                 4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
            res = self.req.get_way(url=url, headers=header)  # 请求登录接口
            re = res.json()  # 转为json格式供assertEqual断言使用
        logging.info(re)
        boxBarcode = re['result']['skuList'][0]['boxBarcode']
        skuQty = re['result']['skuList'][0]['planQty']
        # boxBarcode：箱序号
        # 将返回的入库单号传入到方法written_boxBarcode中

        if message in re['message'] or '操作成功！' in re['message']:
            WrittenToken.written_boxBarcode(int(IDX), boxBarcode)
            # # 将返回的skuQty传入到方法written_skuQty中
            WrittenToken.written_skuQty(int(IDX), skuQty)
        return re

    # 查询申报产品接口
    @ddt.data(*result)
    @ddt.unpack
    def test_getdetai_Inbound(self, case_name, IDX, urls, methond, orderNo, message):
        result = self.getdetai_Inbound(case_name, IDX, urls, methond, orderNo, message)
        url = urls + orderNo
        "5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中"
        log_case_info(case_name, url, orderNo, message, result)
        "6.设置断言，判断是否真的登录成功了"
        self.assertEqual(message, result['message'])  # 改为assertEqual断言
