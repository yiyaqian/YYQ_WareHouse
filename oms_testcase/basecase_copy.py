import logging
import unittest
import warnings
import json
from excel.read_excel import *
from log.case_log import log_case_info
from lib.general_request import General_request
from excel.written_token import WrittenToken


class BaseCase(unittest.TestCase):  # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    def send_request(self, data_list, len):
        """
                1.循环获取场景名称
                2.通过场景名称获取到该行数据
                3.
                """
        for i in range(0, len):
            logging.info("欢迎进入for循环")
            "1.获取场景名称 "
            case_name = data_list[i - 1].get('场景')

            "2.通过场景名称:casename   在data_list[该表中所有用例数据]查找到该用例数据"
            case_data = get_test_data(data_list, case_name)
            """
            3.
             3.1 从字典case_data中读取数据url、data、message、headers，
             3.2 并分别保存在变量url、data、message、header中
             3.3 注意字符串格式需用json.loads()转化为字典格式
            """
            url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
            data = json.loads(case_data.get('data'))  # 注意字符串格式，需要用json.loads()转化为字典格式
            message = case_data.get('message')  # 期望数据
            content_type = case_data.get('Content-Type')
            x_access_token = case_data.get('x-access-token')
            session = WrittenToken.read_token()  # 调用获取token的方法
            if "无" in x_access_token:
                header = {
                    'Content-Type': content_type,
                    'x-access-token': session
                }  # 注意字符串格式，需要用json.loads()转化为字典格式
            else:
                header = {
                    'Content-Type': content_type,
                    'x-access-token': x_access_token
                }  # 注意字符串格式，需要用json.loads()转化为字典格式

            methond = case_data.get('method')

            if methond == 'POST':
                logging.info("res.text")
                """
                4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
                res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
                re = res.json()  # 转为json格式供assertEqual断言使用
                # 当message等于登录成功时，获取token并将token写入表名称为”登录“且“message”一列等于“登陆成功”token一列列中
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    # WrittenToken.written_token(self, tokens)
            else:
                """
                 4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
                res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
                re = res.json()  # 转为json格式供assertEqual断言使用
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    # WrittenToken.written_token(self, tokens)

            """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, data, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
