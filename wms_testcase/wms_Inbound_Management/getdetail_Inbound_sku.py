"""
收货-查询入库单信息接口
"""
import logging
import unittest
from excel.read_excel import *
import json
from log.case_log import log_case_info
from lib.general_request import General_request
import warnings
from excel.written_token import WrittenToken


class GetDetailInboundSku(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    # WMS获取入库单SKU信息
    def test_getdetail_Inbound_sku_normal(self):
        self.data_list = excel_to_list("../xls/测试用例数据2.xls", "WMS获取入库单sku信息")  # 读取该测试类所有用例数据
        leng = len(self.data_list)
        """
                    1.循环获取场景名称
                    2.通过场景名称获取到该行数据
                    3.
                    """
        for i in range(0, leng):
            logging.info(i)
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
            taskNo = case_data.get('taskNo')
            loading = case_data.get('loading')
            consignmentNo = case_data.get('consignmentNo')
            session = WrittenToken.read_WMStoken()
            datas = '{' + '"taskNo":' + '"' + taskNo + '",' + '"loading":' + loading + '}'
            data = json.loads(datas)
            # 注意字符串格式，需要用json.loads()转化为字典格式
            message = case_data.get('message')  # 期望数据
            content_type = case_data.get('Content-Type')
            header = {
                'Content-Type': content_type,
                'x-access-token': session,
                'tenant_id': '2'
            }  # 注意字符串格式，需要用json.loads()转化为字典格式

            methond = case_data.get('method')

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
            logging.info(re)
            logging.info(re['result']['total'])
            total = re['result']['total']
            for t in (0, total-1):
                logging.info(t)
                # skuId:skuId
                WrittenToken.written_skuId(i + 1, re['result']['records'][t]['skuName'],
                                           re['result']['records'][t]['planBoxQty'], taskNo, consignmentNo,
                                           re['result']['records'][t]['skuId'], re['result']['records'][t]['skuCode'],
                                           re['result']['records'][t]['planBoxQty'])

            """
                5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
                """
            log_case_info(case_name, url, data, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
