# -*- coding: utf-8 -*-
# #!Date：2019/8/12 16:23
# # !@Author：龚远琪
from module import *
from common.commonapi.datadict import *


class DeleteItemType(unittest.TestCase):
    itemTypeId = ""

    @classmethod
    def setUpClass(self):
        self.deleteItemTypeResponse = {}
        try:
            self.addItemTypeResponse = dataDict.add_itemType()
            self.addItemTypeData = self.addItemTypeResponse.json()
            self.itemTypeId = self.addItemTypeData["id"]
        except Exception as error:
            log.error("itemType/题型：题型新增失败，失败原因："f'{error}')

    # def assertResult(self, deleteItemTypeResponse):
    #     self.assertEqual(status_code, 200, "itemtype/题型：获取题型成功用例-状态码错误！")
    #     self.assertEqual(actdata["id"], self.itemTypeId, "itemtype/题型：获取题型成功用例-返回Id错误！")
    #     self.assertEqual(actdata["description"], self.addItemTypeData["description"], "itemtype/题型：获取题型成功用例-描述不一致！")
    #     self.assertEqual(actdata["itemMouldType"], self.addItemTypeData["itemMouldType"],
    #                      "itemtype/题型：获取题型成功用例-题型模版不一致！")
    #     self.assertEqual(actdata["priorityCode"], self.addItemTypeData["priorityCode"], "itemtype/题型：获取题型成功用例-排序不一致！")
    #     self.assertEqual(actdata["typeCode"], self.addItemTypeData["typeCode"], "itemtype/题型：获取题型成功用例-题型编码不一致！")
    #     self.assertEqual(actdata["typeName"], self.addItemTypeData["typeName"], "itemtype/题型：获取题型成功用例-题型名称不一致！")

    def test_deleteItemType(self):
        """
        itemType/题型：删除题型成功用例
        """
        self.deleteItemTypeResponse = request.run_main(deleteitemtype["url"] + str(self.itemTypeId), method='DELETE',
                                                       headers=deleteitemtype["header"], data={})
        try:
            status_code = self.deleteItemTypeResponse.status_code
        except Exception as error:
            log.error("itemType/题型：删除题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 204, "itemType/题型：删除题型成功用例-状态码错误！")
            log.info("itemType/题型：删除题型成功用例测试通过！")

    def test_deleteItemTypeNoExist(self):
        """
        itemType/题型：删除不存在的题型
        """
        self.deleteItemTypeResponse = request.run_main(deleteitemtype["url"] + str(99999), method='DELETE',
                                                       headers=deleteitemtype["header"], data={})
        try:
            status_code = self.deleteItemTypeResponse.status_code
        except Exception as error:
            log.error("itemType/题型：删除不存在的题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 204, "itemType/题型：删除不存在的题型-状态码错误！")
            log.info("itemType/题型：删除不存在的题型用例测试通过！")

    def test_deleteItemTypeHaveItem(self):
        """
        itemType/题型：删除已存在题目的题型
        """
        self.deleteItemTypeResponse = request.run_main(deleteitemtype["url"] + str(2), method='DELETE',
                                                       headers=deleteitemtype["header"], data={})
        try:
            status_code = self.deleteItemTypeResponse.status_code
            actmessage = self.deleteItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：删除已存在题目的题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：删除已存在题目的题型-状态码错误！")
            self.assertEqual(actmessage, "该题型已被题目使用，无法删除", "itemType/题型：删除已存在题目的题型 message返回信息不一致！")
            log.info("itemType/题型：删除已存在题目的题型用例测试通过！")

    def test_deleteItemTypeNoId(self):
        """
        itemType/题型：删除题型未输入ID
        """
        self.deleteItemTypeResponse = request.run_main(deleteitemtype["url"], method='DELETE',
                                                       headers=deleteitemtype["header"], data={})
        try:
            status_code = self.deleteItemTypeResponse.status_code
            actmessage = self.deleteItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：删除题型未输入ID接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "itemType/题型：删除题型未输入ID-状态码错误！")
            self.assertEqual("请求方法不支持", actmessage, "itemType/题型：删除题型未输入ID message返回信息不一致！")
            log.info("itemType/题型：删除题型未输入ID用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()