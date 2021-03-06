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
        new_worksheet = new_workbook.get_sheet(13)
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
        data_values = excel_to_list("../xls/测试用例数据.xls", "4-WMS登录")
        case_names = data_values[5].get('场景')
        "通过场景名称:casenames   在data_values[该表中所有用例数据]查找到该用例数据"
        case_data1 = get_test_data(data_values, case_names)
        message1 = case_data1.get('message')  # 期望数据
        if '登录成功' == message1:
            token1 = case_data1.get('x-access-token')
        return token1

    # 从新增sku接口获取到sku编码【keyWords】和业务类型【businessType】
    # 供OMS查询SKU接口【search_sku.py】
    @staticmethod
    def written_SKU(length, keyWords, businessType):
        """4.1加载已存在的xls"""
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        "4.2复制一份"
        new_workbook = copy(old_workbook)
        "4.3获取到复制的xls中0-查询SKU sheet表"
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
        new_worksheet = new_workbook.get_sheet(3)
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
        new_worksheet = new_workbook.get_sheet(4)
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
        new_worksheet = new_workbook.get_sheet(5)
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
        new_worksheet = new_workbook.get_sheet(6)
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

        # 获取7-审核和取消入库单表，并写入consignmentNo【表字段consignmentNos】
        new_worksheet = new_workbook.get_sheet(7)
        new_worksheet.write(length, 5, consignmentNo)

        # 获取8-入库单详情表，并写入consignmentNo【表字段orderNo】
        new_worksheet1 = new_workbook.get_sheet(8)
        new_worksheet1.write(length, 4, consignmentNo)

        # 获取WSM查询入库单表，并写入consignmentNo【表字段keyWords】
        new_worksheet2 = new_workbook.get_sheet(9)
        new_worksheet2.write(length, 6, consignmentNo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从WMS查询入库单接口【wms_Receiving.search_Inbound.py】获取到taskNo,写入确认收货sheet表【表字段名:taskNo】中
    @staticmethod
    def written_taskNo(length, taskNo, consignmentNo):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到10-WMS获取入库单SKU信息表，taskNo【表字段：taskNo】
        new_worksheet = new_workbook.get_sheet(10)
        new_worksheet.write(length, 5, taskNo)
        new_worksheet.write(length, 8, consignmentNo)

        # # # 获取11-确认收货表，写入【表字段：taskNo、consignmentNo】
        # new_worksheet1 = new_workbook.get_sheet(11)
        # new_worksheet1.write(length, 5, taskNo)

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

        # # 获取到确认收货表，写入boxBarcode【表字段：boxBarcode】
        # new_worksheet = new_workbook.get_sheet(11)
        # new_worksheet.write(length, 6, boxBarcode)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从获取入库单详情接口【getdetail_Inbound.py】获取到skuQty，写入确认收货sheet表【表字段normalQty】
    @staticmethod
    def written_skuQty(length, skuQty):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到确认收货表，写入boxBarcode【表字段：normalQty】
        new_worksheet = new_workbook.get_sheet(11)
        new_worksheet.write(length, 8, skuQty)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从WMS获取入库单SKU信息接口【wms_Receiving.getdetail_Inbound_sku.py】获取到skuId,写入确认收货sheet表【表字段：skuBarcode】
    @staticmethod
    def written_skuId(length, skuName, taskNo, consignmentNo, skuId, skuCode, planQty, boxBarcode):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到确认收货表【表字段：skuBarcode】
        new_worksheet = new_workbook.get_sheet(11)
        new_worksheet.write(length, 5, taskNo)
        new_worksheet.write(length, 6, boxBarcode)
        new_worksheet.write(length, 7, skuId)
        new_worksheet.write(length, 8, planQty)

        # 获取到上架表【表字段：skuBarcode】
        new_worksheet1 = new_workbook.get_sheet(12)
        new_worksheet1.write(length, 5, skuName)
        new_worksheet1.write(length, 7, planQty)
        new_worksheet1.write(length, 8, taskNo)
        new_worksheet1.write(length, 10, consignmentNo)
        new_worksheet1.write(length, 11, skuId)
        new_worksheet1.write(length, 12, skuCode)
        new_worksheet1.write(length, 13, planQty)

        # # 获取到新增出库单表【表字段：skuId、skuCode、skuName、batchNo】
        # new_worksheet = new_workbook.get_sheet(8)
        # new_worksheet.write(length, 5, taskNo)
        # new_worksheet.write(length, 6, boxBarcode)
        # new_worksheet.write(length, 7, skuId)
        # new_worksheet.write(length, 8, planQty)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    @staticmethod
    def written_out_refo(length, out_refo):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)
        # 获取到获取出库单详情表【表字段：orderNumber】
        new_worksheet = new_workbook.get_sheet(14)
        new_worksheet.write(length, 12, out_refo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从查询出库单接口【search_outbound.py】获取到出库订单参考号，写入获取出库单详情sheet表和审核和取消出库单、WMS查询出库单【表字段：orderNumber、orderNumber、keyWords】
    @staticmethod
    def written_orderNumber(length, orderNumber):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到获取出库单详情表【表字段：orderNumber】
        new_worksheet = new_workbook.get_sheet(15)
        new_worksheet.write(length, 5, orderNumber)

        # 获取到审核和取消出库单【表字段：orderNumber】
        new_worksheet1 = new_workbook.get_sheet(16)
        new_worksheet1.write(length, 5, orderNumber)

        # 获取到WMS查询出库单【表字段：keyWords】
        new_worksheet2 = new_workbook.get_sheet(17)
        new_worksheet2.write(length, 7, orderNumber)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从WMS查询出库单接口【wsearch_outbound.py】中获取到出库单号【consignmentNo】和订单类型【pickType】，写入18-拣货单生成查询sheet表、20-拣货单管理查询sheet表中【表字段：consignmentNo、pickType】
    @staticmethod
    def written_OutNoAndPickType(length, consignmentNo, pickType):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到18-拣货单生成查询sheet表【表字段：consignmentNo、pickType】
        new_worksheet = new_workbook.get_sheet(18)
        new_worksheet.write(length, 8, pickType)
        new_worksheet.write(length, 11, consignmentNo)

        # 获取到20-拣货单管理查询sheet表【表字段：consignmentNo、pickType】
        new_worksheet1 = new_workbook.get_sheet(20)
        new_worksheet1.write(length, 7, consignmentNo)
        new_worksheet1.write(length, 11, pickType)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从拣货单生成查询接口【search_CreatePick.py】中获取到taskId和订单类型【pickType】，写入taskId sheet表中【表字段：picker、pickType】
    @staticmethod
    def written_TaskIdAndPickType(length, taskId, pickType):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到19-生成拣货单sheet表【表字段：consignmentNo、pickType】
        new_worksheet = new_workbook.get_sheet(19)
        new_worksheet.write(length, 5, taskId)
        new_worksheet.write(length, 7, pickType)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从拣货单管理查询接口【search_Pick.py】获取到拣货单号和id，写入21-打印拣货单 sheet表、22-完成拣货sheet表中【表字段：pickNos、pickIds】
    @staticmethod
    def written_PickAndId(length, pickNo, ids):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到21-打印拣货单sheet表【表字段：pickNos、pickIds】
        new_worksheet = new_workbook.get_sheet(21)
        new_worksheet.write(length, 7, pickNo)
        new_worksheet.write(length, 6, ids)

        # 获取到22-完成拣货sheet表【表字段：pickNo】
        new_worksheet1 = new_workbook.get_sheet(22)
        new_worksheet1.write(length, 5, pickNo)

        # 获取到23-配货页查询拣货单sheet表【表字段：inputNo】
        new_worksheet2 = new_workbook.get_sheet(23)
        new_worksheet2.write(length, 5, pickNo)

        # 获取到26-打包页获取打包单号sheet表【表字段：inputNo】
        new_worksheet3 = new_workbook.get_sheet(26)
        new_worksheet3.write(length, 6, pickNo)

        # 获取到29-拣货单管理页获取订单信息sheet表【表字段：pickNo】
        new_worksheet4 = new_workbook.get_sheet(29)
        new_worksheet4.write(length, 5, pickNo)

        # 获取到29-拣货单管理页获取订单信息sheet表【表字段：pickNo】
        new_worksheet4 = new_workbook.get_sheet(28)
        new_worksheet4.write(length, 6, pickNo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    @staticmethod
    def written_CNo(length, consignmentNo, packNo):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到28-完成打包sheet表【表字段：jobNo、inputNo】
        new_worksheet = new_workbook.get_sheet(28)
        new_worksheet.write(length, 7, consignmentNo)
        new_worksheet.write(length, 5, packNo)

        # 获取到28-完成打包sheet表【表字段：jobNo、inputNo】
        new_worksheet1 = new_workbook.get_sheet(26)
        new_worksheet1.write(length, 6, consignmentNo)
        new_worksheet1.write(length, 5, packNo)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    # 从配货页查询拣货单接口【search_invoicePL.py】获取到jobNo和skuId,写入24-配货sheet表中【表字段、jobNo、inoutNo】
    @staticmethod
    def written_jobNoAndskuId(length, jobNo, skuId):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到24-配货sheet表【表字段：jobNo、inputNo】
        new_worksheet = new_workbook.get_sheet(24)
        new_worksheet.write(length, 8, jobNo)
        new_worksheet.write(length, 5, skuId)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')

    @staticmethod
    def written_packNo(length, packNo, pickType):
        # # 加载已存在的xls
        old_workbook = xlrd.open_workbook('../xls/测试用例数据2.xls')
        # # 将已存在的excel拷贝进新的excl
        new_workbook = copy(old_workbook)

        # 获取到29-拣货单管理页获取订单信息表【表字段：consignmentNo、pickType】
        new_worksheet = new_workbook.get_sheet(27)
        new_worksheet.write(length, 5, packNo)
        new_worksheet.write(length, 6, pickType)

        os.remove('../xls/测试用例数据2.xls')
        new_workbook.save('../xls/测试用例数据2.xls')
