0  # -*- encoding: utf-8 -*-
# @ModuleName: getpapertype
# @Author：龚远琪
# @Date：2019/11/5 16:08
from common.commonmethod import *
from common.commonapi.datadict import *


class GetPaperType(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.getPaperTypeResponse = {}
        try:
            self.addPaperTypeResponse = dataDict.addPaperType()
            self.addPaperTypeData = self.addPaperTypeResponse.json()
            self.addPaperTypeId = self.addPaperTypeData["id"]
        except Exception as error:
            log.error("paperType/套卷类型：套卷类型新增失败，失败原因："f'{error}')

    def test_getPaperType(self):
        """
        paperType/获取套卷类型：SUCCESS-获取套卷类型详情
        """
        self.getPaperTypeResponse = request.run_main(getPaperType["url"] + str(self.addPaperTypeId), method='GET',
                                                     headers=getPaperType["header"], data={})
        try:
            status_code = self.getPaperTypeResponse.status_code
            actdata = self.getPaperTypeResponse.json()
        except Exception as error:
            log.error("paperType/获取套卷类型：SUCCESS-获取套卷类型详情》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/获取套卷类型：SUCCESS-获取套卷类型详情-状态码错误！")
            self.assertEqual(self.addPaperTypeData["description"], actdata["description"],
                             "paperType/获取套卷类型：SUCCESS-获取套卷类型详情-返回描述不一致！")
            self.assertEqual(self.addPaperTypeData["seq"], actdata["seq"],
                             "paperType/获取套卷类型：SUCCESS-获取套卷类型详情-返回排名不一致！")
            self.assertEqual(self.addPaperTypeData["typeCode"], actdata["typeCode"],
                             "paperType/获取套卷类型：SUCCESS-获取套卷类型详情-返回编码一致！")
            self.assertEqual(self.addPaperTypeData["typeName"], actdata["typeName"],
                             "paperType/获取套卷类型：SUCCESS-获取套卷类型详情-返回名称不一致！")
            log.info("paperType/获取套卷类型：SUCCESS-获取套卷类型详情》测试通过！")

    def test_getPaperTypeIdErr(self):
        """
        paperType/获取套卷类型：FAIL-输入不存在的套卷类型ID
        """
        self.getPaperTypeResponse = request.run_main(getPaperType["url"] + str(999999), method='GET',
                                                     headers=getPaperType["header"], data={})
        try:
            status_code = self.getPaperTypeResponse.status_code
            actmessage = self.getPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/获取套卷类型：FAIL-输入不存在的套卷类型ID》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "paperType/获取套卷类型：FAIL-输入不存在的套卷类型ID-状态码错误！")
            self.assertEqual("套卷类型为空 id :999999", actmessage, "paperType/获取套卷类型：FAIL-输入不存在的套卷类型ID-message返回信息不一致！")
            log.info("paperType/获取套卷类型：FAIL-输入不存在的套卷类型ID》测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.addPaperTypeId != None:
                dao(db, "delete from paper_textbook_type_period_record where paper_textbook_type_id = " + str(
                    self.addPaperTypeId) + ";")
                dao(db, "delete from paper_textbook_type where id = " + str(self.addPaperTypeId) + ";")
                log.info("paperType/套卷类型：删除套卷类型记录成功！")
        except Exception as error:
            log.error("paperType/套卷类型：删除套卷类型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
