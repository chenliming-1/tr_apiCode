# -*- encoding: utf-8 -*-
# @ModuleName: addpapertype
# @Author：龚远琪
# @Date：2019/11/4 11:40
from common.commonmethod import *
from common.commonapi.datadict import *


class AddPaperType(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.addPaperTypeId = []
        self.addPaperTypeResponse = {}

    def test_addPaperType(self):
        """
        paperType/添加套卷类型：SUCCESS-所有参数正常添加
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
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

    def test_addPaperTypeRequired(self):
        """
        paperType/添加套卷类型：SUCCESS-必填项正常添加
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["requiredBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actdata = self.addPaperTypeResponse.json()
            self.addPaperTypeId.append(actdata["id"])
        except Exception as error:
            log.error("paperType/添加套卷类型：SUCCESS-必填项正常添加》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code, "paperType/添加套卷类型：SUCCESS-必填项正常添加-状态码错误！")
            self.assertEqual(99, actdata["seq"], "paperType/添加套卷类型：SUCCESS-必填项正常添加-返回排名不一致！")
            self.assertEqual(addPaperType["requiredBody"]["typeCode"], actdata["typeCode"],
                             "paperType/添加套卷类型：SUCCESS-必填项正常添加-返回编码一致！")
            self.assertEqual(addPaperType["requiredBody"]["typeName"], actdata["typeName"],
                             "paperType/添加套卷类型：SUCCESS-必填项正常添加-返回名称不一致！")
            log.info("paperType/添加套卷类型：SUCCESS-必填项正常添加》测试通过！")

    def test_addPaperTypeNameRepeat(self):
        """
        paperType/添加套卷类型：FAIL-添加同名称套卷类型
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeNameRepeatBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-添加同名称套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-添加同名称套卷类型-状态码错误！")
            self.assertEqual("类型名称已存在", actmessage, "paperType/添加套卷类型：FAIL-添加同名称套卷类型-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-添加同名称套卷类型》测试通过！")

    def test_addPaperTypeCodeRepeat(self):
        """
        paperType/添加套卷类型：FAIL-添加同编码套卷类型
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeCodeRepeatBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-添加同编码套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-添加同编码套卷类型-状态码错误！")
            self.assertEqual("类型编码已存在", actmessage, "paperType/添加套卷类型：FAIL-添加同编码套卷类型-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-添加同编码套卷类型》测试通过！")

    def test_addPaperTypeNameNone(self):
        """
        paperType/添加套卷类型：FAIL-未填写套卷类型名称
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeNameNoneBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-未填写套卷类型名称》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-未填写套卷类型名称-状态码错误！")
            self.assertEqual("类型名称不能为空", actmessage, "paperType/添加套卷类型：FAIL-未填写套卷类型名称-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-未填写套卷类型名称》测试通过！")

    def test_addPaperTypeCodeNone(self):
        """
        paperType/添加套卷类型：FAIL-未填写套卷类型编码
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeCodeNoneBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-未填写套卷类型编码》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-未填写套卷类型编码-状态码错误！")
            self.assertEqual("类型编码不能为空", actmessage, "paperType/添加套卷类型：FAIL-未填写套卷类型编码-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-未填写套卷类型编码》测试通过！")

    def test_addPaperTypePeriodIdsNone(self):
        """
        paperType/添加套卷类型：FAIL-未填写学段
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["periodIdsNoneBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-未填写学段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-未填写学段-状态码错误！")
            self.assertEqual("所属学段不能为空", actmessage, "paperType/添加套卷类型：FAIL-未填写学段-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-未填写学段》测试通过！")

    def test_addPaperTypePeriodIdsErr(self):
        """
        paperType/添加套卷类型：FAIL-输入不存在的学段
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["periodIdsErrBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-输入不存在的学段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-输入不存在的学段-状态码错误！")
            self.assertEqual("学段id错误", actmessage, "paperType/添加套卷类型：FAIL-输入不存在的学段-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-输入不存在的学段》测试通过！")

    def test_addPaperTypePeriodIdsHaveNone(self):
        """
        paperType/添加套卷类型：FAIL-学段列表存在空数据
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["periodIdsHaveNoneBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-学段列表存在空数据》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-学段列表存在空数据-状态码错误！")
            self.assertEqual("学段id为空", actmessage, "paperType/添加套卷类型：FAIL-学段列表存在空数据-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-学段列表存在空数据》测试通过！")

    def test_addPaperTypeSeqIsZero(self):
        """
        paperType/添加套卷类型：FAIL-排序不在（1,200）范围内，排序为0
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["seqIsZeroBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-排序为0》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-排序为0-状态码错误！")
            self.assertEqual("排序只允许1-200（包含）之间", actmessage, "paperType/添加套卷类型：FAIL-排序为0-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-排序为0》测试通过！")

    def test_addPaperTypeSeqErr(self):
        """
        paperType/添加套卷类型：FAIL-排序不在（1,200）范围内，排序为201
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["seqErrBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-排序为201》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-排序为201-状态码错误！")
            self.assertEqual("排序只允许1-200（包含）之间", actmessage, "paperType/添加套卷类型：FAIL-排序为201-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-排序为201》测试通过！")

    def test_addPaperTypeCodeTooLong(self):
        """
        paperType/添加套卷类型：FAIL-类型编码超出100字符
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeCodeTooLongBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-类型编码超出100字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-类型编码超出100字符-状态码错误！")
            self.assertEqual("类型编码不能超过100个字符", actmessage, "paperType/添加套卷类型：FAIL-类型编码超出100字符-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-类型编码超出100字符》测试通过！")

    def test_addPaperTypeNameTooLong(self):
        """
        paperType/添加套卷类型：FAIL-类型名称超出100字符
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["typeNameTooLongBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-类型名称超出100字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-类型名称超出100字符-状态码错误！")
            self.assertEqual("类型名称不能超过100个字符", actmessage, "paperType/添加套卷类型：FAIL-类型名称超出100字符-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-类型名称超出100字符》测试通过！")

    def test_addPaperTypeDescriptionTooLong(self):
        """
        paperType/添加套卷类型：FAIL-描述超出200字符
        """
        self.addPaperTypeResponse = request.run_main(addPaperType["url"], method='POST', headers=addPaperType["header"],
                                                     data=addPaperType["descriptionTooLongBody"])
        try:
            status_code = self.addPaperTypeResponse.status_code
            actmessage = self.addPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/添加套卷类型：FAIL-描述超出200字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/添加套卷类型：FAIL-描述超出200字符-状态码错误！")
            self.assertEqual("描述不能超过200个字符", actmessage, "paperType/添加套卷类型：FAIL-描述超出200字符-message返回信息不一致！")
            log.info("paperType/添加套卷类型：FAIL-描述超出200字符》测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if len(self.addPaperTypeId) != 0:
                for i in self.addPaperTypeId:
                    dao(db, "delete from paper_textbook_type_period_record where paper_textbook_type_id = " + str(
                        self.addPaperTypeId) + ";")
                    dao(db, "delete from paper_textbook_type where id = " + str(i) + ";")
                    log.info("paperType/套卷类型：删除套卷类型记录成功！")
        except Exception as error:
            log.error("paperType/套卷类型：删除套卷类型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
