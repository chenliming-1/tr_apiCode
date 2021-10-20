import unittest
from data.itemtype import  *
from common.commonapi.datadict import  *

class TestAdditemtypenew(unittest.TestCase):
    itemTypeId = []
    @classmethod
    def setUpClass(self) :
        pass

    def test_additemtypenew(self):
        """
        additemType/题型：添加题型成功用例
        """
        additemtypebody = addItemTypenew["body_sucess"]
        self.addItemTypeResponse = request.run_main(url=addItemTypenew["url"],method=addItemTypenew["method"],
                                                    data=additemtypebody,headers=addItemTypenew["headers"])

        try:
            status_code = self.addItemTypeResponse.status_code
            actdata = self.addItemTypeResponse.json()
            # print(actdata["id"])
            self.itemTypeId.append(actdata["id"])

        except Exception as error:
            log.info("additemType/题型：获取题型列表接口失败，失败原因："f'{error}')

        finally:
            self.assertEqual(status_code,201,"additemType/题型：添加题型成功用例-接口状态码错误！")
            self.assertIsNotNone(actdata['id'],"additemType/题型：添加题型成功用例-返回id为空！")
            self.assertEqual(actdata['typeName'],additemtypebody['typeName'],"additemType/题型：添加题型成功用例-返回题型模板不一致！")
            self.assertEqual(actdata['typeCode'],additemtypebody['typeCode'],"additemType/题型：添加题型成功用例-返回题型编码不一致！")
            self.assertEqual(actdata['itemMouldType'],additemtypebody['itemMouldType'],"additemType/题型：添加题型成功用例-返回题型名称不一致！")
            log.info("additemType/题型：添加题型成功用例测试通过！")
    def test_additemtypenew_typenameisname(self):
        """
        additemType/题型：添加题型失败用例-题型名称为空
        """
        additemtypebody = addItemTypenew["body_typeNameIsNull"]
        self.addItemTypeResponse = request.run_main(addItemTypenew["url"],method='POST',headers=addItemTypenew["headers"],
                                                    data=additemtypebody)
        try:
            status_code = self.addItemTypeResponse.status_code
        except Exception as  e:
            log.info("additemType/题型：添加题型失败用例-题型名称为空！"f'{e}')
        finally:
            self.assertEqual(status_code,400,"additemType/题型：添加题型失败用例-题型名称不能为空-状态码错误！")
            log.info("itemType/题型：添加题型失败用例-题型名称为空测试通过！")





    @classmethod
    def tearDownClass(self):
        if len(self.itemTypeId)!=0:
            for i in self.itemTypeId:
                # print(i)
                sql1 = dao("tr_test","""DELETE FROM item_type WHERE id={} """.format(i))


if __name__ =='__main__':
    unittest.main()