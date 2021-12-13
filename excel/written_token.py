"""
写入xls类
"""
import logging

from xlutils.copy import copy
import os
from excel.read_excel import *  # 导入read_excel中的方法


class WrittenToken:
    # 写入token
    def written_token(self, token):
        # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # 将已存在的excel拷贝进新的excle
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(9)
        new_worksheet.write(6, 4, token)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 读取token
    @staticmethod
    def read_token():
        # 打开xls
        data_values = excel_to_list("../xls/测试用例数据2.xls", "登录")
        case_names = data_values[5].get('场景')
        "通过场景名称:casenames   在data_values[该表中所有用例数据]查找到该用例数据"
        case_data1 = get_test_data(data_values, case_names)
        message1 = case_data1.get('message')  # 期望数据
        if '登录成功' == message1:
            token1 = case_data1.get('x-access-token')
        return token1

    # 读取WMS的token
    @staticmethod
    def read_WMStoken():
        # 打开xls
        data_values = excel_to_list("../xls/测试用例数据.xls", "WMS登录")
        case_names = data_values[5].get('场景')
        "通过场景名称:casenames   在data_values[该表中所有用例数据]查找到该用例数据"
        case_data1 = get_test_data(data_values, case_names)
        message1 = case_data1.get('message')  # 期望数据
        if '登录成功' == message1:
            token1 = case_data1.get('x-access-token')
        return token1

    # 将skucode:sku代码、businessType：业务类型 写入查询SKU的excel【字段：keyWords、businessType】中
    # 供OMS查询SKU接口【search_sku.py】
    @staticmethod
    def written_SKU(length, keyWords, businessType):
        """4.1加载已存在的xls"""
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        "4.2复制一份"
        new_workbook = copy(old_workbook)
        "4.3获取到复制的xls中第一个sheet表"
        new_worksheet = new_workbook.get_sheet(0)
        "4.4往复制的xls第一个表中第i+1行的第5列写入查询条件SKU代码"
        new_worksheet.write(length, 5, keyWords)
        "4.5往复制的xls第一个表中第i+1行的第6列写入查询条件业务类型"
        new_worksheet.write(length, 6, businessType)
        "4.6删除原有的测试用例数据2.xls"
        os.remove('../xls/测试用例数据2.xls')
        "4.7保存复制的测试用例数据2.xls"
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从查询SKU接口【search_sku.py】获取到ids写入审核和作废SKU的sheet表[字段：ids]中
    @staticmethod
    def written_id(length, ids):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(1)
        new_worksheet.write(length, 5, ids)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从新增申报产品接口【add_declarce.py】获取到品牌、skucode，写入获查询申报产品sheet表【表字段brand、skuCode】
    @staticmethod
    def written_brand_and_skuCode(length, brand, skuCode):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(10)
        new_worksheet.write(length, 6, brand)
        new_worksheet.write(length, 7, skuCode)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从新增申报产品接口【add_declarce.py】获取到申报产品代码，写入获取申报产品详情sheet表【表字段declareGoodsCode】
    @staticmethod
    def written_declareGoodsCode(length, declareGoodsCode):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(11)
        new_worksheet.write(length, 4, declareGoodsCode)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从查询申报产品接口【search_declare.py】获取到ids，写入审核和作废申报产品sheet表【表字段ids】
    @staticmethod
    def written_ids(length, ids):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 审核和作废申报产品sheet表
        new_worksheet = new_workbook.get_sheet(12)
        new_worksheet.write(length, 5, ids)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从新增入库单接口【add_Inbound.py】获取到查询入库单接口【getdetail_Inbound_sku.py】时需要的参数写入查询入库单的sheet表【字段：orderNo】中
    @staticmethod
    def written_refNo(length, refNo):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取sheet
        new_worksheet = new_workbook.get_sheet(3)
        new_worksheet.write(length, 10, refNo)
        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从查询入库单接口【search_Inbound.py】获取到审核和取消入库单接口【review_and_void_Inbound.py】
    # 获取入库单详情【getdetail_consignment】时需要的参数写入审核和作废入库单、获取入库单详情sheet表中
    # consignmentNo：入库单号
    @staticmethod
    def written_consignmentNo(length, consignmentNo):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取审核和取消入库单表，并写入consignmentNo【表字段consignmentNos】
        new_worksheet = new_workbook.get_sheet(2)
        new_worksheet.write(length, 5, consignmentNo)

        # 获取入库单详情表，并写入consignmentNo【表字段orderNo】
        new_worksheet1 = new_workbook.get_sheet(4)
        new_worksheet1.write(length, 4, consignmentNo)

        # 获取WSM查询入库单表，并写入consignmentNo【表字段keyWords】
        new_worksheet1 = new_workbook.get_sheet(5)
        new_worksheet1.write(length, 4, consignmentNo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从获取入库单详情接口【getdetail_Inbound.py】获取到skuQty，写入确认收货sheet表【表字段normalQty】
    @staticmethod
    def written_skuQty(length, skuQty):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取到确认收货表，taskNo【表字段：taskNo】
        new_worksheet = new_workbook.get_sheet(8)
        new_worksheet.write(length, 7, skuQty)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从获取入库单详情获取到的入库单箱序号写入wms查询入库单、确认收货sheet表中
    # boxBarcode：箱序号
    @staticmethod
    def written_boxBarcode(length, boxBarcode):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # # 获取到收货-按箱表，写入boxBarcode【表字段：boxBarcode】
        # new_worksheet1 = new_workbook.get_sheet(6)
        # new_worksheet1.write(length, 5, boxBarcode)

        # 获取到确认收货表，写入boxBarcode【表字段：boxBarcode】
        new_worksheet = new_workbook.get_sheet(8)
        new_worksheet.write(length, 5, boxBarcode)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从WMS查询入库单接口【wms_Receiving.search_Inbound.py】获取到taskNo,写入确认收货sheet表【表字段名:taskNo】中
    @staticmethod
    def written_taskNo(length, taskNo, consignmentNo=None):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # # 获取到WMS获取入库单sku信息表，写入【表字段：taskNo、consignmentNo】
        new_worksheet1 = new_workbook.get_sheet(6)
        new_worksheet1.write(length, 5, taskNo)
        new_worksheet1.write(length, 8, consignmentNo)

        # # 获取到上架表，写入【表字段：taskNo】
        new_worksheet2 = new_workbook.get_sheet(13)
        new_worksheet2.write(length, 8, taskNo)

        # 获取到确认收货表，taskNo【表字段：taskNo】
        new_worksheet = new_workbook.get_sheet(8)
        new_worksheet.write(length, 5, taskNo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从WMS获取入库单SKU信息接口【wms_Receiving.getdetail_Inbound_sku.py】获取到skuId,写入确认收货sheet表【表字段：skuBarcode】
    @staticmethod
    def written_skuId(length, skuName, qty, taskNo, consignmentNo, skuId, skuCode, putawayQty):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到确认收货表，skuId【表字段：skuBarcode】
        new_worksheet = new_workbook.get_sheet(8)
        new_worksheet.write(length, 7, skuId)

        # 获取到上架表，skuId【表字段：skuBarcode】
        new_worksheet1 = new_workbook.get_sheet(13)
        new_worksheet1.write(length, 5, skuName)
        new_worksheet1.write(length, 7, qty)
        new_worksheet1.write(length, 8, taskNo)
        new_worksheet1.write(length, 10, consignmentNo)
        new_worksheet1.write(length, 11, skuId)
        new_worksheet1.write(length, 12, skuCode)
        new_worksheet1.write(length, 13, putawayQty)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

   # 从WMS获取入库单SKU信息接口【wms_Receiving.getdetail_Inbound_sku.py】获取到skuId,写入确认收货sheet表【表字段：skuBarcode】
    @staticmethod
    def written_skuIds(length, skuName, qty, taskNo, consignmentNo, skuId, skuCode, putawayQty):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到确认收货表，skuId【表字段：skuBarcode】
        new_worksheet = new_workbook.get_sheet(8)
        new_worksheet.write(length, 7, skuId)

        # 获取到上架表，skuId【表字段：skuBarcode】
        new_worksheet1 = new_workbook.get_sheet(13)
        new_worksheet1.write(length, 5, skuName)
        new_worksheet1.write(length, 7, qty)
        new_worksheet1.write(length, 8, taskNo)
        new_worksheet1.write(length, 10, consignmentNo)
        new_worksheet1.write(length, 11, skuId)
        new_worksheet1.write(length, 12, skuCode)
        new_worksheet1.write(length, 13, putawayQty)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')