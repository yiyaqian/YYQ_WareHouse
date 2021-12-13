import os
import unittest
from excel.read_excel import *  # 导入read_excel中的方法
import json  # 用来转化excel中的json字符串为字典
from log.case_log import log_case_info  # 导入方法
from lib.general_request import General_request
import warnings
import xlrd
from xlutils.copy import copy


class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', RuntimeWarning)
        # 请求实例化
        cls.req = General_request()

    # 写入token
    def written_token(self, token):
        # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../../xls/测试用例数据.xls')
        # 将已存在的excel拷贝进新的excle
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(0)
        new_worksheet.write(1, 6, token)
        os.remove('../../xls/测试用例数据.xls')
        new_workbook.save('../xls/测试用例数据.xls')

    # OMS登录接口
    def test_user_login_normal(self):
        global url, data, header, message, length, tokens
        self.data_list = excel_to_list("../../xls/测试用例数据.xls", "登录")  # 读取该测试类所有用例数据
        length = len(self.data_list)
        """
        1.循环获取场景名称
        2.通过场景名称获取到该行数据
        3.
        """
        for i in range(0, length):
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
            data = json.loads(case_data.get('data'))  # 注意字符串格式，需要用json.loads()转化为字典格式
            message = case_data.get('message')  # 期望数据
            header = json.loads(case_data.get('headers'))  # 注意字符串格式，需要用json.loads()转化为字典格式
            methond = case_data.get('method')

            if methond == 'POST':
                """
                4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                """
                res = self.req.post_way(url=url, json=data, headers=header)  # 请求登录接口
                re = res.json()  # 转为json格式供assertEqual断言使用
                # 当message等于登录成功时，获取token并将token写入表名称为”登录“且“message”一列等于“登陆成功”token一列列中
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    self.written_token(tokens)
            else:
                """
                 4.请求登录接口，并将请求数据通过json()方法转化为json格式供断言使用
                 """
                res = self.req.get_way(url=url, params=data, headers=header)  # 请求登录接口
                re = res.json()  # 转为json格式供assertEqual断言使用
                if '登录成功' == message:
                    tokens = re['result']['token']
                    # 调用写入token的方法
                    self.written_token(tokens)

            """
            5.将参数case_name、url、data、message、res、text传入封装输出日志的方法中
            """
            log_case_info(case_name, url, data, message, res.text)
            "6.设置断言，判断是否真的登录成功了"
            self.assertEqual(message, re['message'])  # 改为assertEqual断言
            # if self.assertNotEqual(message,re['message']):

        """7.判断length是否等于6，当等于6时说明登录测试场景已全部跑完，可进入查询申报产品方法中"""
        # if length == 6:
        # self.test_declared_search()
