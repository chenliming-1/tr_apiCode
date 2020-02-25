# -*- coding: utf-8 -*-
# #!Date：2019/8/13 14:55
# # !@Author：龚远琪
from common.commonapi.datadict import *


class GetItemTypeList(unittest.TestCase):
    itemTypeId = ""

    @classmethod
    def setUpClass(self):
        self.getItemTypeListResponse = {}
        try:
            self.addItemTypeResponse = dataDict.add_itemType()
            self.addItemTypeData = self.addItemTypeResponse.json()
            self.itemTypeId = self.addItemTypeData["id"]
        except Exception as error:
            log.error("itemType/题型：题型新增失败，失败原因："f'{error}')

    def test_getItemTypeList(self):
        """
        itemType/题型：获取题型列表成功用例
        """
        getItemTypeListBody = getItemTypeList["body_success"]
        self.getItemTypeListResponse = requests.get(getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeListBody)
        try:
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
        except Exception as error:
            log.error("itemType/题型：获取题型列表接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemType/题型：获取题型列表成功用例-状态码错误！")
            self.assertEqual(actdata["currentPage"], getItemTypeListBody["currentPage"],
                             "itemType/题型：获取题型列表成功用例-当前页返回错误！")
            self.assertEqual(actdata["pageSize"], getItemTypeListBody["pageSize"], "itemType/题型：获取题型成功用例-每页大小不一致！")
            self.assertEqual(actdata["total"], len(actdata["list"]), "itemType/题型：获取题型列表成功用例-返回列表数不一致！")
            log.info("itemType/题型：获取题型列表成功用例测试通过！")

    def test_getItemTypeListDefault(self):
        """
        itemType/题型：获取题型列表成功用例
        """
        self.getItemTypeListResponse = requests.get(getItemTypeList["url"], headers=getItemTypeList["header"])
        try:
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
        except Exception as error:
            log.error("itemType/题型：获取题型列表接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "itemType/题型：获取题型列表成功用例-状态码错误！")
            self.assertEqual(1, actdata["currentPage"], "itemType/题型：获取题型列表成功用例-当前页返回错误！")
            self.assertEqual(10, actdata["pageSize"], "itemType/题型：获取题型成功用例-每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "itemType/题型：获取题型列表成功用例-返回列表数不一致！")
            self.assertEqual(10, len(actdata["list"]), "itemType/题型：获取题型列表成功用例-返回列表数不一致！")
            log.info("itemType/题型：获取题型列表成功用例测试通过！")

    def test_getItemTypeListByName(self):
        """
        itemType/题型：通过题型名称获取列表成功用例
        """
        getItemTypeListBody = getItemTypeList["body_withTypeName"].copy()
        getItemTypeListBody["typeName"] = self.addItemTypeData["typeName"]
        self.getItemTypeListResponse = requests.get(getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeListBody)
        try:
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
        except Exception as error:
            log.error("itemType/题型：通过题型名称获取列表接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemType/题型：通过题型名称获取列表成功用例-状态码错误！")
            self.assertEqual(actdata["currentPage"], getItemTypeListBody["currentPage"],
                             "itemType/题型：通过题型名称获取列表成功用例-当前页返回错误！")
            self.assertEqual(actdata["pageSize"], getItemTypeListBody["pageSize"], "itemType/题型：通过题型名称获取列表成功用例-每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "itemType/题型：通过题型名称获取列表成功用例-返回列表数错误！")
            self.assertEqual(actdata["list"][0]["typeName"], self.addItemTypeData["typeName"],
                             "itemType/题型：通过题型名称获取列表成功用例-查询结果与题型名称不一致！")
            log.info("itemType/题型：通过题型名称获取列表成功用例测试通过！")

    def test_getItemTypeListByCode(self):
        """
        itemType/题型：通过题型编码获取列表成功用例
        """
        getItemTypeListBody = getItemTypeList["body_withTypeName"].copy()
        getItemTypeListBody["typeName"] = self.addItemTypeData["typeCode"]
        self.getItemTypeListResponse = requests.get(getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeListBody)
        try:
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
        except Exception as error:
            log.error("itemType/题型：通过题型编码获取列表接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemType/题型：通过题型编码获取列表成功用例-状态码错误！")
            self.assertEqual(actdata["currentPage"], getItemTypeListBody["currentPage"],
                             "itemType/题型：通过题型编码获取列表成功用例-当前页返回错误！")
            self.assertEqual(actdata["pageSize"], getItemTypeListBody["pageSize"], "itemType/题型：通过题型编码获取列表成功用例-每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "itemType/题型：通过题型编码获取列表成功用例-返回列表数错误！")
            self.assertEqual(actdata["list"][0]["typeCode"], self.addItemTypeData["typeCode"],
                             "itemType/题型：通过题型编码获取列表成功用例-查询结果与题型名称不一致！")
            log.info("itemType/题型：通过题型编码获取列表成功用例测试通过！")

    def test_getItemTypeList(self):
        """
        itemType/题型：获取题型列表为空
        """
        self.getItemTypeListResponse = requests.get(url=getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeList["body_randTypeName"])
        try:
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
        except Exception as error:
            log.error("itemType/题型：获取题型列表为空接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "itemType/题型：获取题型列表为空-状态码错误！")
            self.assertEqual(0, actdata["total"], "itemType/题型：获取题型列表为空-列表数不为0！")
            self.assertEqual(0, len(actdata["list"]), "itemType/题型：获取题型列表为空-列表不为空！")
            log.info("itemType/题型：获取题型列表为空用例测试通过！")

    def test_currentPageIsZero(self):
        """
        itemType/题型：获取题型列表当前页为0
        """
        self.getItemTypeListResponse = requests.get(url=getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeList["body_currentPageIsZero"])
        try:
            status_code = self.getItemTypeListResponse.status_code
            actmessage = self.getItemTypeListResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：获取题型列表当前页为0接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "itemType/题型：获取题型列表当前页为0-状态码错误！")
            self.assertEqual(actmessage, "Page index must not be less than zero!",
                             "itemType/题型：获取题型列表当前页为0-message返回信息不一致！")
            log.info("itemType/题型：获取题型列表当前页为0用例测试通过！")

    def test_currentPageErr(self):
        """
        itemType/题型：获取题型列表当前页为负数
        """
        self.getItemTypeListResponse = requests.get(url=getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeList["body_currentPageErr"])
        try:
            status_code = self.getItemTypeListResponse.status_code
            actmessage = self.getItemTypeListResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：获取题型列表当前页为负数接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "itemType/题型：获取题型列表当前页为负数-状态码错误！")
            self.assertEqual(actmessage, "Page index must not be less than zero!",
                             "itemType/题型：获取题型列表当前页为负数-message返回信息不一致！")
            log.info("itemType/题型：获取题型列表当前页为负数用例测试通过！")

    def test_pageSizeErr(self):
        """
        itemType/题型：获取题型列表每页大小为负数
        """
        self.getItemTypeListResponse = requests.get(url=getItemTypeList["url"], headers=getItemTypeList["header"],
                                                    params=getItemTypeList["body_pageSizeErr"])
        try:
            status_code = self.getItemTypeListResponse.status_code
            actmessage = self.getItemTypeListResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：获取题型列表每页大小为负数接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "itemType/题型：获取题型列表每页大小为负数-状态码错误！")
            self.assertEqual(actmessage, "Page size must not be less than one!",
                             "itemType/题型：获取题型列表每页大小为负数-message返回信息不一致！")
            log.info("itemType/题型：获取题型列表每页大小为负数用例测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.itemTypeId != "":
                dataDict.delete_itemtype(self.itemTypeId)
        except Exception as error:
            log.error("itemType/题型：删除题型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()