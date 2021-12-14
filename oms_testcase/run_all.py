"""
运行入口
"""
import unittest
from log.config import *
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

from oms_testcase.oms_login.user_login import UserLogin
from oms_testcase.oms_outbound_Management.getdetail_outbound import GetDetailOutBound
from wms_testcase.wms_outbound_Management.wsearch_outbound import WSearchOutbound
from wms_testcase.wms_PickList.search_CreatePick import SearchCreatePick
from wms_testcase.wms_PickList.createPick import CreatePick
from wms_testcase.wms_PickList.search_Pick import Search_Pick
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
# suite.addTest(unittest.makeSuite(AddOutbound))
# suite.addTest(unittest.makeSuite(SearchOutbound))
# suite.addTest(unittest.makeSuite(GetDetailOutBound))


# suite.addTest(unittest.makeSuite(AddInbound))
# suite.addTest(unittest.makeSuite(SearchInbound))
# suite.addTest(unittest.makeSuite(ReviewAndVoid_Inbound))
# suite.addTest(unittest.makeSuite(GetDetailInbound))
# suite.addTest(unittest.makeSuite(WuserLogin))
# suite.addTest(unittest.makeSuite(WSearchInbound))
# suite.addTest(unittest.makeSuite(GetDetailInboundBox))
# suite.addTest(unittest.makeSuite(ConfirmReceipt))
# suite.addTest(unittest.makeSuite(WSearchOutbound))
# suite.addTest(unittest.makeSuite(SearchCreatePick))
# suite.addTest(unittest.makeSuite(CreatePick))
suite.addTest(unittest.makeSuite(Search_Pick))


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
