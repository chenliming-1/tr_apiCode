# -*- coding: utf-8 -*-
# #!Date：2019/7/25 9:43
# # !@Author：龚远琪
from common.commonapi.datadict import *


class GetItemType(unittest.TestCase):
    itemTypeId = ""

    @classmethod
    def setUpClass(self):
        self.getItemTypeResponse = {}
        try:
            self.addItemTypeResponse = dataDict.add_itemType()
            self.addItemTypeData = self.addItemTypeResponse.json()
            self.itemTypeId = self.addItemTypeData["id"]
        except Exception as error:
            log.error("itemType/题型：题型新增失败，失败原因："f'{error}')

    def test_getItemType(self):
        """
        itemType/题型：获取题型成功用例
        """
        self.getItemTypeResponse = request.run_main(getItemType["url"] + str(self.itemTypeId), method='GET',
                                                    headers=getItemType["header"], data={})
        try:
            status_code = self.getItemTypeResponse.status_code
            actdata = self.getItemTypeResponse.json()
        except Exception as error:
            log.error("itemType/题型：获取题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemType/题型：获取题型成功用例-状态码错误！")
            self.assertEqual(actdata["id"], self.itemTypeId, "itemType/题型：获取题型成功用例-返回Id错误！")
            self.assertEqual(actdata["description"], self.addItemTypeData["description"], "itemType/题型：获取题型成功用例-描述不一致！")
            self.assertEqual(actdata["itemMouldType"], self.addItemTypeData["itemMouldType"],
                             "itemType/题型：获取题型成功用例-题型模版不一致！")
            self.assertEqual(actdata["priorityCode"], self.addItemTypeData["priorityCode"],
                             "itemType/题型：获取题型成功用例-排序不一致！")
            self.assertEqual(actdata["typeCode"], self.addItemTypeData["typeCode"], "itemType/题型：获取题型成功用例-题型编码不一致！")
            self.assertEqual(actdata["typeName"], self.addItemTypeData["typeName"], "itemType/题型：获取题型成功用例-题型名称不一致！")
            log.info("itemType/题型：获取题型成功用例测试通过！")

    def test_getItemTypeNoExist(self):
        """
        itemType/题型：获取不存在的题型
        """
        self.getItemTypeResponse = request.run_main(getItemType["url"] + str(99999), method='GET',
                                                    headers=getItemType["header"], data={})
        try:
            status_code = self.getItemTypeResponse.status_code
            actmessage = self.getItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：获取不存在的题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 404, "itemType/题型：获取不存在的题型-状态码错误！")
            self.assertEqual(actmessage, "题型不存在", "itemType/题型：获取不存在的题型 message返回信息不一致！")
            log.info("itemType/题型：获取不存在的题型用例测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.itemTypeId != "":
                dataDict.delete_itemtype(self.itemTypeId)
        except Exception as error:
            log.error("itemType/题型：删除题型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
