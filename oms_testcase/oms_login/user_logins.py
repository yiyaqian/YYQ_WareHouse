"""
登录接口
"""
import logging
import unittest
from excel.read_excel import *
from excel.written_token import WrittenToken
from lib.general_request import General_request
import warnings
import json

from log.case_log import log_case_info


class UserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    # OMS登录接口
    def test_user_login_normal(self):
        # 1.读取该测试类所有用例数据
        self.data_list = excel_to_list("../xls/测试用例数据2.xls", "登录")
        length = len(self.data_list)
        # 2.循环读取每一行数据，拼接请求参数
        for i in range(0, length):
            "2.1获取场景名称 "
            case_name = self.data_list[i - 1].get('场景')

            "2.2通过场景名称:casename   在data_list[该表中所有用例数据]查找到该用例数据"
            case_data = get_test_data(self.data_list, case_name)

            """
            2.3
             3.1 从字典case_data中读取数据url、data、message、headers，
             3.2 并分别保存在变量url、data、message、header中
             3.3 注意字符串格式需用json.loads()转化为字典格式
            """
            url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
            data = json.loads(case_data.get('data'))  # 注意字符串格式，需要用json.loads()转化为字典格式
            message = case_data.get('message')  # 期望数据
            content_type = case_data.get('Content-Type')
            header = {
                    'Content-Type': content_type
                }  # 注意字符串格式，需要用json.loads()转化为字典格式

            methond = case_data.get('method')
            # 3.判断method是否等于"POST" ，是进入if反之则进入else
            if methond == 'POST':
                logging.info("res.text")
                """
                3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
                res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
                logging.info(res.text)
                re = res.json()  # 转为json格式供assertEqual断言使用
                # 当message等于登录成功时，获取token并将token写入表名称为”登录“且“message”一列等于“登陆成功”token一列列中
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    WrittenToken.written_token(self, tokens)
            else:
                """
                 3.1.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
                res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
                re = res.json()  # 转为json格式供assertEqual断言使用
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    WrittenToken.written_token(self, tokens)

            """
            4.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, data, message, res.text)
            "5.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言