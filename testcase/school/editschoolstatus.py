# -*- coding: utf-8 -*-
# # !Date：2019/7/25 9:43
# # !@Author：龚远琪
from common.commonmethod import *
from common.commonapi.datadict import *


class EditSchoolStatus(unittest.TestCase):

    def getData(self, flag=1):
        if flag == 1:
            getAreaList = dataDict.getRandArea()
        else:
            getAreaList = dataDict.getRandArea(0)
        schoolBody = addSchool["body_success"].copy()
        schoolBody["provinceId"] = getAreaList[0]["id"]
        schoolBody["cityId"] = getAreaList[1]["id"]
        if len(getAreaList) == 3:
            schoolBody["countyId"] = getAreaList[2]["id"]
            schoolBody["schoolName"] = "AT" + getAreaList[2]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学"
        else:
            schoolBody["countyId"] = None
            schoolBody["schoolName"] = "AT" + getAreaList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学"
        schoolBody["periodIds"] = randdata.getperiod(random.randint(1, 4))
        schoolBody["seq"] = randMethod.getNumByRange(1, 200)
        return schoolBody

    @classmethod
    def setUpClass(self):
        self.editStatusResponse = {}
        try:
            self.addSchoolBody = self.getData(self)
            self.addSchoolResponse = dataDict.addSchool(self.addSchoolBody)
            self.addSchoolData = self.addSchoolResponse.json()
            self.schoolId = self.addSchoolData["id"]
        except Exception as error:
            log.error("school/学校：学校新增失败，失败原因："f'{error}')

    def test_editSchoolENABLE(self):
        """
        school/修改学校状态：SUCCESS-设置学校状态为启用
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + str(self.schoolId) + "/status/ENABLE",
                                                   method='PUT', headers=editSchoolStatus["header"], data=None)
        try:
            status_code = self.editStatusResponse.status_code
        except Exception as error:
            log.error("school/修改状态：SUCCESS-设置学校状态为启用》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(204, status_code, "school/修改状态：SUCCESS-设置学校状态为启用-状态码错误！")
            log.info("school/修改状态：SUCCESS-设置学校状态为启用》测试通过！")

    def test_editSchoolDISABLE(self):
        """
        school/修改学校状态：SUCCESS-设置学校状态为禁用
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + str(self.schoolId) + "/status/DISABLE",
                                                   method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.editStatusResponse.status_code
        except Exception as error:
            log.error("school/修改状态：SUCCESS-设置学校状态为禁用》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(204, status_code, "school/修改状态：SUCCESS-设置学校状态为禁用-状态码错误！")
            log.info("school/修改状态：SUCCESS-设置学校状态为禁用》测试通过！")

    def test_editSchoolNoExist(self):
        """
        school/修改学校状态：FAIL-学校不存在
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + str(999999) + "/status/ENABLE",
                                                   method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.editStatusResponse.status_code
            actmessage = self.editStatusResponse.json()["message"]
        except Exception as error:
            log.error("school/修改状态：FAIL-学校不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "school/修改状态：FAIL-学校不存在-状态码错误！")
            self.assertEqual("学校不存在，id: 999999", actmessage, "school/修改状态：FAIL-学校不存在-message返回信息不一致！")
            log.info("school/修改状态：FAIL-学校不存在》测试通过！")

    def test_editSchoolStatusErr(self):
        """
        school/修改学校状态：FAIL-输入错误状态
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + str(self.schoolId) + "/status/ABLE",
                                                   method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.editStatusResponse.status_code
            actmessage = self.editStatusResponse.json()["message"]
        except Exception as error:
            log.error("school/修改状态：FAIL-输入错误状态》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/修改状态：FAIL-输入错误状态-状态码错误！")
            self.assertEqual("参数类型不匹配异常", actmessage, "school/修改状态：FAIL-输入错误状态-message返回信息不一致！")
            log.info("school/修改状态：FAIL-输入错误状态》测试通过！")

    def test_editSchoolNoStatus(self):
        """
        school/修改学校状态：FAIL-未传入状态
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + str(self.schoolId) + "/status/",
                                                   method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.editStatusResponse.status_code
            # actmessage = self.editStatusResponse.json()["message"]
        except Exception as error:
            log.error("school/修改状态：FAIL-未传入状态》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "school/修改状态：FAIL-未传入状态-状态码错误！")
            # self.assertEqual("参数类型不匹配异常", actmessage, "school/学校：FAIL-未传入状态-message返回信息不一致！")
            log.info("school/修改状态：FAIL-未传入状态》测试通过！")

    def test_editSchoolNoID(self):
        """
        school/修改学校状态：FAIL-未传入学校ID
        """
        self.editStatusResponse = request.run_main(editSchoolStatus["url"] + "/status/ENABLE",
                                                   method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.editStatusResponse.status_code
            # actmessage = self.editStatusResponse.json()["message"]
        except Exception as error:
            log.error("school/修改状态：FAIL-未传入学校ID》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "school/修改状态：FAIL-未传入学校ID-状态码错误！")
            # self.assertEqual("参数类型不匹配异常", actmessage, "school/学校：FAIL-未传入状态-message返回信息不一致！")
            log.info("school/修改状态：FAIL-未传入学校ID》测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.schoolId != None:
                dao(db, "delete from school_period_record where school_id = " + str(self.schoolId) + ";")
                dao(db, "delete from school where id= " + str(self.schoolId) + ";")
                log.info("school/学校：删除学校记录成功！")
        except Exception as error:
            log.error("school/学校：删除学校记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
