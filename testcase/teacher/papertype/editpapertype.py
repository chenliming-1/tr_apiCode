# -*- encoding: utf-8 -*-
# @ModuleName: editpapertype
# @Author：龚远琪
# @Date：2019/11/5 9:51
from common.commonmethod import *
from common.commonapi.datadict import *


class EditPaperType(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.addPaperTypeId = []
        self.editPaperTypeResponse = {}
        try:
            self.addPaperTypeResponse = dataDict.addPaperType()
            self.addPaperTypeData = self.addPaperTypeResponse.json()
            self.addPaperTypeId = self.addPaperTypeData["id"]
        except Exception as error:
            log.error("paperType/套卷类型：套卷类型新增失败，失败原因："f'{error}')

    def test_editPaperType(self):
        """
        paperType/编辑套卷类型：SUCCESS-修改所有参数
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["body_success"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actdata = self.editPaperTypeResponse.json()
        except Exception as error:
            log.error("paperType/编辑套卷类型：SUCCESS-修改所有参数》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/编辑套卷类型：SUCCESS-修改所有参数-状态码错误！")
            self.assertEqual(editPaperType["body_success"]["description"], actdata["description"],
                             "paperType/编辑套卷类型：SUCCESS-修改所有参数-返回描述不一致！")
            self.assertEqual(editPaperType["body_success"]["seq"], actdata["seq"],
                             "paperType/编辑套卷类型：SUCCESS-修改所有参数-返回排名不一致！")
            self.assertEqual(self.addPaperTypeData["typeCode"], actdata["typeCode"],
                             "paperType/编辑套卷类型：SUCCESS-修改所有参数-返回编码一致！")
            self.assertEqual(editPaperType["body_success"]["typeName"], actdata["typeName"],
                             "paperType/编辑套卷类型：SUCCESS-修改所有参数-返回名称不一致！")
            log.info("paperType/编辑套卷类型：SUCCESS-修改所有参数》测试通过！")

    def test_editPaperTypeRequired(self):
        """
        paperType/编辑套卷类型：SUCCESS-非必填项放空
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["requiredBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actdata = self.editPaperTypeResponse.json()
        except Exception as error:
            log.error("paperType/编辑套卷类型：SUCCESS-必填项正常添加》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/编辑套卷类型：SUCCESS-必填项正常添加-状态码错误！")
            self.assertEqual(99, actdata["seq"], "paperType/编辑套卷类型：SUCCESS-必填项正常添加-返回排名不一致！")
            self.assertIsNone(actdata["description"], "paperType/编辑套卷类型：SUCCESS-必填项正常添加-返回编码一致！")
            self.assertEqual(self.addPaperTypeData["typeCode"], actdata["typeCode"],
                             "paperType/编辑套卷类型：SUCCESS-修改所有参数-返回编码一致！")
            self.assertEqual(editPaperType["requiredBody"]["typeName"], actdata["typeName"],
                             "paperType/编辑套卷类型：SUCCESS-必填项正常添加-返回名称不一致！")
            log.info("paperType/编辑套卷类型：SUCCESS-必填项正常添加》测试通过！")

    def test_editPaperTypeNameRepeat(self):
        """
        paperType/编辑套卷类型：FAIL-添加同名称套卷类型
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["typeNameRepeatBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-添加同名称套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-添加同名称套卷类型-状态码错误！")
            self.assertEqual("类型名称已存在,请修改", actmessage, "paperType/编辑套卷类型：FAIL-添加同名称套卷类型-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-添加同名称套卷类型》测试通过！")

    def test_editPaperTypeCodeRepeat(self):
        """
        paperType/编辑套卷类型：FAIL-添加同编码套卷类型
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["typeCodeRepeatBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-添加同编码套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-添加同编码套卷类型-状态码错误！")
            self.assertEqual("类型编码已存在", actmessage, "paperType/编辑套卷类型：FAIL-添加同编码套卷类型-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-添加同编码套卷类型》测试通过！")

    def test_editPaperTypeNameNone(self):
        """
        paperType/编辑套卷类型：FAIL-未填写套卷类型名称
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["typeNameNoneBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-未填写套卷类型名称》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-未填写套卷类型名称-状态码错误！")
            self.assertEqual("类型名称不能为空", actmessage, "paperType/编辑套卷类型：FAIL-未填写套卷类型名称-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-未填写套卷类型名称》测试通过！")

    def test_editPaperTypeCodeNone(self):
        """
        paperType/编辑套卷类型：FAIL-未填写套卷类型编码
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["typeCodeNoneBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-未填写套卷类型编码》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-未填写套卷类型编码-状态码错误！")
            self.assertEqual("类型编码不能为空", actmessage, "paperType/编辑套卷类型：FAIL-未填写套卷类型编码-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-未填写套卷类型编码》测试通过！")

    def test_editPaperTypePeriodIdsNone(self):
        """
        paperType/编辑套卷类型：FAIL-未填写学段
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["periodIdsNoneBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-未填写学段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-未填写学段-状态码错误！")
            self.assertEqual("所属学段不能为空", actmessage, "paperType/编辑套卷类型：FAIL-未填写学段-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-未填写学段》测试通过！")

    def test_editPaperTypePeriodIdsNone(self):
        """
        paperType/编辑套卷类型：FAIL-输入不存在的学段
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["periodIdsErrBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-输入不存在的学段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-输入不存在的学段-状态码错误！")
            self.assertEqual("学段id错误", actmessage, "paperType/编辑套卷类型：FAIL-输入不存在的学段-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-输入不存在的学段》测试通过！")

    def test_editPaperTypePeriodIdsHaveNone(self):
        """
        paperType/编辑套卷类型：FAIL-学段列表存在空字段
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["periodIdsHaveNoneBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-学段列表存在空字段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-学段列表存在空字段-状态码错误！")
            self.assertEqual("学段id为空", actmessage, "paperType/编辑套卷类型：FAIL-学段列表存在空字段-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-学段列表存在空字段》测试通过！")

    def test_editPaperTypeSeqIsZero(self):
        """
        paperType/编辑套卷类型：FAIL-排序不在（1,200）范围内，排序为0
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["seqIsZeroBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-排序为0》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-排序为0-状态码错误！")
            self.assertEqual("排序只允许1-200（包含）之间", actmessage, "paperType/编辑套卷类型：FAIL-排序为0-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-排序为0》测试通过！")

    def test_editPaperTypeSeqErr(self):
        """
        paperType/编辑套卷类型：FAIL-排序不在（1,200）范围内，排序为201
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"], data=editPaperType["seqErrBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-排序为201》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-排序为201-状态码错误！")
            self.assertEqual("排序只允许1-200（包含）之间", actmessage, "paperType/编辑套卷类型：FAIL-排序为201-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-排序为201》测试通过！")

    def test_editPaperTypeNameTooLong(self):
        """
        paperType/编辑套卷类型：FAIL-类型名称超出100字符
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["typeNameTooLongBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-类型名称超出100字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-类型名称超出100字符-状态码错误！")
            self.assertEqual("类型名称不能超过100个字符", actmessage, "paperType/编辑套卷类型：FAIL-类型名称超出100字符-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-类型名称超出100字符》测试通过！")

    def test_editPaperTypeDescriptionTooLong(self):
        """
        paperType/编辑套卷类型：FAIL-描述超出200字符
        """
        self.editPaperTypeResponse = request.run_main(editPaperType["url"] + str(self.addPaperTypeId), method='PUT',
                                                      headers=editPaperType["header"],
                                                      data=editPaperType["descriptionTooLongBody"])
        try:
            status_code = self.editPaperTypeResponse.status_code
            actmessage = self.editPaperTypeResponse.json()["message"]
        except Exception as error:
            log.error("paperType/编辑套卷类型：FAIL-描述超出200字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/编辑套卷类型：FAIL-描述超出200字符-状态码错误！")
            self.assertEqual("描述不能超过200个字符", actmessage, "paperType/编辑套卷类型：FAIL-描述超出200字符-message返回信息不一致！")
            log.info("paperType/编辑套卷类型：FAIL-描述超出200字符》测试通过！")

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
