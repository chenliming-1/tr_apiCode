# -*- encoding: utf-8 -*-
# @ModuleName: additem
# @Author：龚远琪
# @Date：2019/11/18 15:25
from common.commonmethod.getjendata_url_cookie import *
# from common.commonmethod import *
from common.commonapi.datadict import *


class AddItem(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.addItemId = []
        self.addItemResponse = {}

    def test_addSingleChoice(self):
        """
        item/添加题目：SUCCESS-添加单选题
        """
        self.addItemResponse = request.run_main(additemtype["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["body_success"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actdata = self.addPaperTypeResponse.json()
            self.addPaperTypeId.append(actdata["id"])
        except Exception as error:
            log.error("paperType/添加套卷类型：SUCCESS-所有参数正常添加》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code, "paperType/添加套卷类型：SUCCESS-所有参数正常添加-状态码错误！")
            self.assertEqual(addPaperType["body_success"]["description"], actdata["description"],
                             "paperType/添加套卷类型：SUCCESS-所有参数正常添加-返回描述不一致！")
            self.assertEqual(addPaperType["body_success"]["seq"], actdata["seq"],
                             "paperType/添加套卷类型：SUCCESS-所有参数正常添加-返回排名不一致！")
            self.assertEqual(addPaperType["body_success"]["typeCode"], actdata["typeCode"],
                             "paperType/添加套卷类型：SUCCESS-所有参数正常添加-返回编码一致！")
            self.assertEqual(addPaperType["body_success"]["typeName"], actdata["typeName"],
                             "paperType/添加套卷类型：SUCCESS-所有参数正常添加-返回名称不一致！")
            log.info("paperType/添加套卷类型：SUCCESS-所有参数正常添加》测试通过！")
