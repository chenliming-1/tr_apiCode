# -*- coding: utf-8 -*-
# #!Date：2019/7/9 17:35
# # !@Author：龚远琪

from module import *
from common.commonapi.datadict import *


class AddItemType(unittest.TestCase):
    itemTypeId = []

    @classmethod
    def setUpClass(self):
        self.addItemTypeResponse = {}

    def test_additemtype(self):
        """
        itemType/题型：添加题型成功用例
        """
        additemtypebody = additemtype["body_success"]
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtypebody)
        # print("test_additemtype!!!!!!!!!"+additemtypebody["typeName"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actdata = self.addItemTypeResponse.json()
            self.itemTypeId.append(actdata["id"])
        except Exception as error:
            log.error("itemType/题型：添加题型接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 201, "itemType/题型：添加题型成功用例-状态码错误！")
            self.assertIsNotNone(actdata["id"], "itemType/题型：添加题型成功用例-返回Id为空！")
            self.assertEqual(actdata["description"], additemtypebody["description"], "itemType/题型：添加题型成功用例-描述不一致！")
            self.assertEqual(actdata["itemMouldType"], additemtypebody["itemMouldType"], "itemType/题型：添加题型成功用例-题型模版不一致！")
            self.assertEqual(actdata["priorityCode"], additemtypebody["priorityCode"], "itemType/题型：添加题型成功用例-排序不一致！")
            self.assertEqual(actdata["typeCode"], additemtypebody["typeCode"], "itemType/题型：添加题型成功用例-题型编码不一致！")
            self.assertEqual(actdata["typeName"], additemtypebody["typeName"], "itemType/题型：添加题型成功用例-题型名称不一致！")
            log.info("itemType/题型：添加题型成功用例测试通过！")

    def test_additemtype_requried(self):
        """
        itemType/题型：添加题型必填项成功用例
        """
        additemtypebody = additemtype["body_success_requried"]
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtypebody)
        try:
            status_code = self.addItemTypeResponse.status_code
            actdata = self.addItemTypeResponse.json()
            self.itemTypeId.append(actdata["id"])
            # print("id:" + str(self.itemTypeId))
        except Exception as error:
            log.error("itemtype/题型：添加题型必填项接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 201, "itemType/题型：添加题型必填项成功用例-状态码错误！")
            self.assertIsNotNone(actdata["id"], "itemType/题型：添加题型必填项成功用例-返回Id为空！")
            self.assertEqual(actdata["itemMouldType"], additemtypebody["itemMouldType"],
                             "itemType/题型：添加题型必填项成功用例-题型模版不一致！")
            self.assertEqual(actdata["priorityCode"], 99, "itemType/题型：添加题型必填项必填项成功用例-排序不一致！")
            self.assertEqual(actdata["typeCode"], additemtypebody["typeCode"], "itemType/题型：添加题型必填项成功用例-题型编码不一致！")
            self.assertEqual(actdata["typeName"], additemtypebody["typeName"], "itemType/题型：添加题型必填项成功用例-题型名称不一致！")
            log.info("itemType/题型：添加题型必填项成功用例测试通过！")


    def test_additemtype_subjectIdsErr(self):
        """
        itemType/题型：添加题型失败用例-科目Id错误
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_subjectIdsErr"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-科目Id错误，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-科目Id错误-状态码错误！")
            self.assertEqual(actmessage, "字典ID为NULL", "itemType/题型：添加题型失败用例-科目Id错误message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-科目Id错误测试通过！")

    def test_additemtype_retypecode(self):
        """
        itemType/题型：添加题型失败用例-题型编码重复
        """
        additemtypebody = additemtype["body_success"].copy()
        additemtypebody["typeName"] = "AT模版_" + randMethod.getChinese(3)
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtypebody)
        # print("test_additemtype_retypecode!!!!!!!!!" + additemtypebody["typeName"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型编码重复，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型编码重复-状态码错误！")
            self.assertEqual(actmessage, "题型编码已存在", "itemType/题型：添加题型失败用例-题型编码重复message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型编码重复测试通过！")

    def test_additemtype_retypename(self):
        """
        itemType/题型：添加题型失败用例-题型名称重复
        """
        additemtypebody = additemtype["body_success"].copy()
        additemtypebody["typeCode"] = "ATCode_" + randMethod.getStr(4)
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtypebody)
        # print("test_additemtype_retypename!!!!!!!!!" + additemtypebody["typeName"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型名称重复，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型名称重复-状态码错误！")
            self.assertEqual(actmessage, "题型名称已存在", "itemType/题型：添加题型失败用例-题型名称重复message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型名称重复测试通过！")

    def test_additemtype_mouldtypeisnull(self):
        """
        itemType/题型：添加题型失败用例-题型模版为空
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_itemMouldTypeIsNull"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型模版为空，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型模版为空-状态码错误！")
            self.assertEqual(actmessage, "题目模板类型不能为空", "itemType/题型：添加题型失败用例-题型模版为空message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型模版为空测试通过！")

    def test_additemtype_mouldtypeiserr(self):
        """
        itemType/题型：添加题型失败用例-题型模版错误
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_itemMouldTypeIsErr"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型模版错误，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型模版错误-状态码错误！")
            self.assertEqual(actmessage, "参数格式错误", "itemType/题型：添加题型失败用例-题型模版错误message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型模版错误测试通过！")

    def test_additemtype_typecodeisnull(self):
        """
        itemType/题型：添加题型失败用例-题型编码为空
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_typeCodeIsNull"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型编码为空，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型编码为空-状态码错误！")
            self.assertEqual(actmessage, "题型编码不能为空", "itemType/题型：添加题型失败用例-题型编码为空message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型编码为空测试通过！")

    def test_additemtype_typenameisnull(self):
        """
        itemType/题型：添加题型失败用例-题型名称为空
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_typeNameIsNull"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-题型名称为空，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-题型名称为空-状态码错误！")
            self.assertEqual(actmessage, "题型名称不能为空", "itemType/题型：添加题型失败用例-题型名称为空message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-题型名称为空测试通过！")

    def test_priorityCodeError(self):
        """
        itemType/题型：添加题型失败用例-排序超出限制
        """
        self.addItemTypeResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                                    data=additemtype["body_priorityCodeError"])
        try:
            status_code = self.addItemTypeResponse.status_code
            actmessage = self.addItemTypeResponse.json()["message"]
        except Exception as error:
            log.error("itemType/题型：添加题型失败用例-排序超出限制，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemType/题型：添加题型失败用例-排序超出限制-状态码错误！")
            self.assertEqual(actmessage, "参数格式错误", "itemType/题型：添加题型失败用例-排序超出限制message返回信息不一致！")
            log.info("itemType/题型：添加题型失败用例-排序超出限制测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if len(self.itemTypeId) != 0:
                for i in self.itemTypeId:
                    dataDict.delete_itemtype(i)
        except Exception as error:
            log.error("itemType/题型：删除题型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()