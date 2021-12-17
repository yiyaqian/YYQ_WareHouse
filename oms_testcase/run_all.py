"""
运行入口
"""
import unittest
from log.config import *
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

from oms_testcase.oms_login.user_login import UserLogin
from oms_testcase.oms_sku.add_sku import AddSku
from oms_testcase.oms_sku.search_sku import SearchSku
from oms_testcase.oms_sku.review_and_void_sku import ReviewAndVoid_sku

from oms_testcase.oms_declare.add_declarce import AddDeclarce
# from oms_testcase.oms_declare.search_declare import SearchDeclare
from oms_testcase.oms_declare.getdetail_declare import GetDetailDeclare
from oms_testcase.oms_declare.review_and_void_declarce import ReviewAndVoid_Declarce

from oms_testcase.oms_Inbound_Management.add_Inbound import AddInbound
from oms_testcase.oms_Inbound_Management.search_Inbound import SearchInbound
from oms_testcase.oms_Inbound_Management.review_and_void_Inbound import ReviewAndVoid_Inbound
from oms_testcase.oms_Inbound_Management.getdetail_Inbound import GetDetailInbound

from wms_testcase.wms_Inbound_Management.search_Inbound import WSearchInbound
from wms_testcase.wms_Inbound_Management.getdetail_Inbound_sku1 import GetDetailInboundSKU
from wms_testcase.wms_Receiving.confirm_receipt import ConfirmReceipt
# from wms_testcase.wms_putaway.putaway import PutAway

from oms_testcase.oms_outbound_Management.add_outbound import AddOutbound
from oms_testcase.oms_outbound_Management.search_outbound import SearchOutbound
from oms_testcase.oms_outbound_Management.getdetail_outbound import GetDetailOutBound
from oms_testcase.oms_outbound_Management.review_and_void_outbound import ReviewAndVoid_OutBound

from wms_testcase.wms_outbound_Management.wsearch_outbound import WSearchOutbound
from wms_testcase.wms_PickList.search_CreatePick import SearchCreatePick
from wms_testcase.wms_PickList.createPick import CreatePick
from wms_testcase.wms_PickList.search_Pick import Search_Pick
from wms_testcase.wms_PickList.getOutBound import GetOutBound
from wms_testcase.wms_PickList.print_Pick import Print_Pick
from wms_testcase.wms_PickList.achieve_Pick import Achieve_Pick
from wms_testcase.wms_invoice.search_invoicePL import Search_InvoicePL
from wms_testcase.wms_invoice.invoice import Invoice
from wms_testcase.wms_pack.getPackNo import GetPackNo
from wms_testcase.wms_pack.search_packPL import Search_PackPL
from wms_testcase.wms_pack.achieve_pack import Achieve_Pack

str.encode("gbk")

logging.info("====================== 测试开始 =======================")
# 实例化测试套件对象
suite = unittest.TestSuite()
# 添加扩展

# suite.addTest(unittest.makeSuite(UserLogin))

# suite.addTest(unittest.makeSuite(AddSku))
# suite.addTest(unittest.makeSuite(SearchSku))
# suite.addTest(unittest.makeSuite(ReviewAndVoid_sku))

# suite.addTest(unittest.makeSuite(AddDeclarce))
# suite.addTest(unittest.makeSuite(SearchDeclare))
# suite.addTest(unittest.makeSuite(GetDetailDeclare))
# suite.addTest(unittest.makeSuite(ReviewAndVoid_Declarce))

# suite.addTest(unittest.makeSuite(AddInbound))
# suite.addTest(unittest.makeSuite(SearchInbound))
# suite.addTest(unittest.makeSuite(ReviewAndVoid_Inbound))
# suite.addTest(unittest.makeSuite(GetDetailInbound))

# suite.addTest(unittest.makeSuite(WuserLogin))
# suite.addTest(unittest.makeSuite(WSearchInbound))
# suite.addTest(unittest.makeSuite(GetDetailInboundSKU))

# suite.addTest(unittest.makeSuite(ConfirmReceipt))
# suite.addTest(unittest.makeSuite(PutAway))


# suite.addTest(unittest.makeSuite(AddOutbound))
# suite.addTest(unittest.makeSuite(SearchOutbound))
# suite.addTest(unittest.makeSuite(GetDetailOutBound))
# suite.addTest(unittest.makeSuite(ReviewAndVoid_OutBound))

# suite.addTest(unittest.makeSuite(WSearchOutbound))
# suite.addTest(unittest.makeSuite(SearchCreatePick))
# suite.addTest(unittest.makeSuite(CreatePick))
# suite.addTest(unittest.makeSuite(Search_Pick))
suite.addTest(unittest.makeSuite(GetOutBound))
# suite.addTest(unittest.makeSuite(Print_Pick))
# suite.addTest(unittest.makeSuite(Achieve_Pick))
# suite.addTest(unittest.makeSuite(Search_InvoicePL))
# suite.addTest(unittest.makeSuite(Invoice))
# suite.addTest(unittest.makeSuite(GetPackNo))
# suite.addTest(unittest.makeSuite(Search_PackPL))

# suite.addTest(unittest.makeSuite(Achieve_Pack))

# 以二进制格式打开../log/report.html文件，如果文件../log/report.html存在则将其覆盖。如果不存在则创建新文件
with open("../report/report.html", 'wb') as f:  # 改为with open 格式
    runner = HTMLTestRunner(stream=f, title='测试报告', description='测试描述')
    runner.run(suite)

logging.info("======================= 测试结束 =======================")

# 以只读方式打开文件../log/report.html。文件指针将会放在文件的开头。默认模式
# with open('../report/report.html', 'r', encoding='utf-8') as wb_data:  # python打开本地网页文件
#     # 解析HTML
#     Soup = BeautifulSoup(wb_data, 'lxml')
#     # 获取id= total_row下所有td元素
#     passrate = str(Soup.select('#total_row td'))
#     # 判断passrate中是否包含“100.00%”
#     # 不包含时，调用发送报警信息到钉钉群提示测试人员的接口
#     if not ("100.00%" in passrate):
#         # emails.send_email()
#         print("你好")
