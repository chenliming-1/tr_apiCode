# -*- coding: utf-8 -*-
# #!Date：2019/8/13 9:40
# # !@Author：龚远琪
from module import *
from common.commonapi.datadict import *


class UpdateItemType(unittest.TestCase):
    itemTypeId = ""

    @classmethod
    def setUpClass(self):
        self.updateItemTypeResponse = {}
        try:
            self.addItemTypeResponse = dataDict.add_itemType()
            self.addItemTypeData = self.addItemTypeResponse.json()
            self.itemTypeId = self.addItemTypeData["id"]
        except Exception as error:
            log.error("itemType/题型：题型新增失败，失败原因："f'{error}')

    def test_updateItemType(self):
        """
        itemType/题型：修改题型成功用例
        """
        updateItemTypeBody = updateItemType["body_success"]
        self.updateItemTypeResponse = request.run_main(updateItemType["url"] + str(self.itemTypeId), method='PUT',
                                                       headers=updateItemType["header"], data=updateItemTypeBody)
        try:
            status_code = self.updateItemTypeResponse.status_code
            actdata = self.updateItemTypeResponse.json()
        except Exception as error:
            log.error("itemType/题型：修改题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemType/题型：修改题型成功用例-状态码错误！")
            self.assertEqual(actdata["id"], self.itemTypeId, "itemType/题型：修改题型成功用例-Id不一致！")
            self.assertEqual(actdata["description"], updateItemTypeBody["description"], "itemType/题型：修改题型成功用例-描述不一致！")
            self.assertEqual(actdata["priorityCode"], updateItemTypeBody["priorityCode"], "itemType/题型：修改题型成功用例-排序不一致！")
            self.assertEqual(actdata["typeName"], updateItemTypeBody["typeName"], "itemType/题型：修改题型成功用例-题型名称不一致！")
            log.info("itemType/题型：修改题型成功用例测试通过！")

    def test_subjectIdsErr(self):
        """
        itemType/题型：修改题型失败用例-科目Id错误
        """
        self.updateItemTypeResponse = request.run_main(updateItemType["url"] + str(self.itemTypeId), method='PUT',
                                                       headers=updateItemType["header"],
                                                       data=updateItemType["body_subjectIdsErr"])
        try:
            status_code = self.updateItemTypeResponse.status_code
            actmessage = self.updateItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：修改题型失败用例-科目Id错误，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "itemType/题型：修改题型失败用例-科目Id错误-状态码错误！")
            self.assertEqual("ID不能为NULL", actmessage, "itemType/题型：修改题型失败用例-科目Id错误message返回信息不一致！")
            log.info("itemType/题型：修改题型失败用例-科目Id错误测试通过！")

    def test_reTypeName(self):
        """
        itemType/题型：修改题型失败用例-题型名称重复
        """
        updateItemTypeBody = updateItemType["body_success"].copy()
        updateItemTypeBody["typeName"] = "单选题"
        self.updateItemTypeResponse = request.run_main(updateItemType["url"] + str(self.itemTypeId), method='PUT',
                                                       headers=updateItemType["header"], data=updateItemTypeBody)
        try:
            status_code = self.updateItemTypeResponse.status_code
            actmessage = self.updateItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：修改题型失败用例-题型名称重复，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：修改题型失败用例-题型名称重复-状态码错误！")
            self.assertEqual(actmessage, "题型名称已存在", "itemType/题型：修改题型失败用例-题型名称重复message返回信息不一致！")
            log.info("itemType/题型：修改题型失败用例-题型名称重复测试通过！")

    def test_typeNameIsNull(self):
        """
        itemType/题型：修改题型失败用例-题型名称为空
        """
        self.updateItemTypeResponse = request.run_main(updateItemType["url"] + str(self.itemTypeId), method='PUT',
                                                       headers=updateItemType["header"],
                                                       data=updateItemType["body_typeNameIsNull"])
        try:
            status_code = self.updateItemTypeResponse.status_code
            actmessage = self.updateItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：修改题型失败用例-题型名称为空，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：修改题型失败用例-题型名称为空-状态码错误！")
            self.assertEqual(actmessage, "题型名称不能为空", "itemType/题型：修改题型失败用例-题型名称为空message返回信息不一致！")
            log.info("itemType/题型：修改题型失败用例-题型名称为空测试通过！")

    def test_priorityCodeError(self):
        """
        itemType/题型：修改题型失败用例-排序超出限制
        """
        self.updateItemTypeResponse = request.run_main(updateItemType["url"] + str(self.itemTypeId), method='PUT',
                                                       headers=updateItemType["header"],
                                                       data=additemtype["body_priorityCodeError"])
        try:
            status_code = self.updateItemTypeResponse.status_code
            # actmessage = self.updateItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：修改题型失败用例-排序超出限制，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 500, "itemType/题型：修改题型失败用例-排序超出限制-状态码错误！")
            # self.assertEqual(actmessage, "参数格式错误", "itemType/题型：修改题型失败用例-排序超出限制message返回信息不一致！")
            log.info("itemType/题型：修改题型失败用例-排序超出限制测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.itemTypeId != "":
                dataDict.delete_itemtype(self.itemTypeId)
        except Exception as error:
            log.error("itemType/题型：删除题型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()