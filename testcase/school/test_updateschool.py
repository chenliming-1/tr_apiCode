# -*- coding: utf-8 -*-
# #!Date：2019/7/25 9:43
# # !@Author：龚远琪
from common.commonmethod import *
from common.commonapi.datadict import *


class UpdateSchool(unittest.TestCase):
    schoolId = []

    def getData(self, flag=1):
        if flag == 1:
            getAreaList = dataDict.getRandArea()
        else:
            getAreaList = dataDict.getRandArea(0)
        schoolBody = updateSchool["body_success"].copy()
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

    def addSchool(self, schoolBody):
        self.addSchoolResponse = dataDict.addSchool(schoolBody)
        self.addSchoolData = self.addSchoolResponse.json()
        self.schoolId.append(self.addSchoolData["id"])

    @classmethod
    def setUpClass(self):
        self.updateSchoolResponse = {}
        try:
            self.addSchoolBody1 = self.getData(self)
            self.addSchool(self, self.addSchoolBody1)
            addSchoolBody2 = self.getData(self)
            self.addSchool(self, addSchoolBody2)
            self.updateSchoolBody = self.getData(self)
            self.updateBodyNoCounty = self.getData(self, 0)
        except Exception as error:
            log.error("school/学校：学校新增失败，失败原因："f'{error}')

    def test_updateSchool(self):
        """
        school/编辑学校：SUCCESS-编辑学校带区
        """
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=self.updateSchoolBody)
        try:
            status_code = self.updateSchoolResponse.status_code
            actdata = self.updateSchoolResponse.json()
        except Exception as error:
            log.error("school/编辑学校：SUCCESS-编辑学校带区》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code,
                             "school/编辑学校：SUCCESS-编辑学校带区-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                             self.updateSchoolBody))
            self.assertEqual(self.updateSchoolBody["cityId"], actdata["cityId"], "school/编辑学校：SUCCESS-编辑学校带区-返回市Id不一致！")
            self.assertEqual(self.updateSchoolBody["countyId"], actdata["countyId"],
                             "school/编辑学校：SUCCESS-编辑学校带区-返回区Id不一致！")
            self.assertEqual(self.updateSchoolBody["provinceId"], actdata["provinceId"],
                             "school/编辑学校：SUCCESS-编辑学校带区-返回省Id不一致！")
            self.assertEqual(self.updateSchoolBody["schoolName"], actdata["schoolName"],
                             "school/编辑学校：SUCCESS-编辑学校带区-学校名称不一致！")
            self.assertEqual(self.updateSchoolBody["seq"], actdata["seq"], "school/编辑学校：SUCCESS-编辑学校带区-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/编辑学校：SUCCESS-编辑学校带区-学校状态不一致！")
            log.info("school/编辑学校：SUCCESS-编辑学校带区》测试通过！")

    def test_updateSchoolNoCounty(self):
        """
        school/编辑学校：SUCCESS-编辑学校不带区号
        """
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=self.updateBodyNoCounty)
        try:
            status_code = self.updateSchoolResponse.status_code
            actdata = self.updateSchoolResponse.json()
        except Exception as error:
            log.error("school/编辑学校：SUCCESS-编辑学校不带区号》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code,
                             "school/编辑学校：SUCCESS-编辑学校不带区号-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                               self.updateBodyNoCounty))
            self.assertEqual(self.updateBodyNoCounty["cityId"], actdata["cityId"],
                             "school/编辑学校：SUCCESS-编辑学校不带区号-返回市Id不一致！")
            self.assertEqual(self.updateBodyNoCounty["provinceId"], actdata["provinceId"],
                             "school/编辑学校：SUCCESS-编辑学校不带区号-返回省Id不一致！")
            self.assertIsNone(actdata["countyId"], "school/编辑学校：SUCCESS-编辑学校不带区号-返回区Id不为空！")
            self.assertEqual(self.updateBodyNoCounty["schoolName"], actdata["schoolName"],
                             "school/编辑学校：SUCCESS-编辑学校不带区号-学校名称不一致！")
            self.assertEqual(self.updateBodyNoCounty["seq"], actdata["seq"], "school/编辑学校：SUCCESS-编辑学校不带区号-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/编辑学校：SUCCESS-编辑学校不带区号-学校状态不一致！")
            log.info("school/编辑学校：SUCCESS-编辑学校不带区号》测试通过！")

    def test_addSchoolRepeat(self):
        """
        school/编辑学校：FAIL-编辑重复学校
        """
        self.addSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[1]), method='PUT',
                                                  headers=updateSchool["header"], data=self.addSchoolBody1)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-编辑重复学校》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-编辑重复学校-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                          self.addSchoolBody1))
            self.assertEqual("该学校已经存在了噢~", actmessage, "school/编辑学校：FAIL-编辑重复学校-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-编辑重复学校》测试通过！")

    def test_updateSchoolCountyErr(self):
        """
        school/编辑学校：FAIL-区号错误
        """
        bodyCountyErr = self.updateSchoolBody.copy()
        bodyCountyErr["countyId"] = 999999
        self.addSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                  headers=updateSchool["header"], data=bodyCountyErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-区号错误》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-区号错误-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                        bodyCountyErr))
            self.assertEqual("县（区）不存在", actmessage, "school/编辑学校：FAIL-区号错误-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-区号错误》测试通过！")

    def test_updateSchoolNoCity(self):
        """
        school/编辑学校：FAIL-不带市
        """
        bodyNoCity = self.updateBodyNoCounty.copy()
        bodyNoCity["cityId"] = None
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoCity)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-不带市》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-不带市-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"], bodyNoCity))
            self.assertEqual("城市id不能为空", actmessage, "school/编辑学校：FAIL-不带市-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-不带市》测试通过！")

    def test_updateSchoolCityErr(self):
        """
        school/编辑学校：FAIL-市不存在
        """
        bodyCityErr = self.updateBodyNoCounty.copy()
        bodyCityErr["cityId"] = 95
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyCityErr)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-市不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-市不存在-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                        bodyCityErr))
            self.assertEqual("城市不存在", actmessage, "school/编辑学校：FAIL-市不存在-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-市不存在》测试通过！")

    def test_updateSchoolNoProvince(self):
        """
        school/编辑学校：FAIL-不带省
        """
        bodyNoProvince = self.updateBodyNoCounty.copy()
        bodyNoProvince["provinceId"] = None
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoProvince)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-不带省》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-不带省-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                       bodyNoProvince))
            self.assertEqual("省份id不能为空", actmessage, "school/编辑学校：FAIL-不带省-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-不带省》测试通过！")

    def test_updateSchoolProvinceErr(self):
        """
        school/编辑学校：FAIL-省份不存在
        """
        bodyProvinceErr = self.updateBodyNoCounty.copy()
        bodyProvinceErr["provinceId"] = 100
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyProvinceErr)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-省份不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-省份不存在-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                         bodyProvinceErr))
            self.assertEqual("省份不存在", actmessage, "school/编辑学校：FAIL-省份不存在-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-省份不存在》测试通过！")

    def test_updateSchoolNoSchoolName(self):
        """
        school/编辑学校：FAIL-学校名为空
        """
        bodyNoSchoolName = self.updateBodyNoCounty.copy()
        bodyNoSchoolName["schoolName"] = None
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoSchoolName)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-学校名为空》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-学校名为空-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                         bodyNoSchoolName))
            self.assertEqual("学校名称不能为空", actmessage, "school/编辑学校：FAIL-学校名为空-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-学校名为空》测试通过！")

    def test_updateSchoolNoPeriod(self):
        """
        school/编辑学校：FAIL-学段不存在
        """
        bodyNoPeriod = self.updateBodyNoCounty.copy()
        bodyNoPeriod["periodIds"] = None
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoPeriod)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-学段不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-学段不存在-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                         bodyNoPeriod))
            self.assertEqual("学段信息不能为空", actmessage, "school/编辑学校：FAIL-学段不存在-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-学段不存在》测试通过！")

    def test_updateSchoolPeriodErr(self):
        """
        school/编辑学校：FAIL-学段错误
        """
        bodyPeriodErr = self.updateBodyNoCounty.copy()
        bodyPeriodErr["periodIds"] = [None, 10001]
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(self.schoolId[0]), method='PUT',
                                                     headers=updateSchool["header"], data=bodyPeriodErr)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-学段错误》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-学段错误-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                        bodyPeriodErr))
            self.assertEqual("学段id不能为空", actmessage, "school/编辑学校：FAIL-学段错误-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-学段错误》测试通过！")

    def test_updateSchoolNoExist(self):
        """
        school/编辑学校：FAIL-学校不存在
        """
        bodyNoSchoolName = self.updateBodyNoCounty.copy()
        self.updateSchoolResponse = request.run_main(updateSchool["url"] + str(999999), method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoSchoolName)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-学校不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code,
                             "school/编辑学校：FAIL-学校不存在-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                         bodyNoSchoolName))
            self.assertEqual("学校不存在，id: 999999", actmessage, "school/编辑学校：FAIL-学校不存在-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-学校不存在》测试通过！")

    def test_updateSchoolNoID(self):
        """
        school/编辑学校：FAIL-学校ID不存在
        """
        bodyNoSchoolName = self.updateBodyNoCounty.copy()
        self.updateSchoolResponse = request.run_main(updateSchool["url"], method='PUT',
                                                     headers=updateSchool["header"], data=bodyNoSchoolName)
        try:
            status_code = self.updateSchoolResponse.status_code
            actmessage = self.updateSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/编辑学校：FAIL-学校ID不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code,
                             "school/编辑学校：FAIL-学校ID不存在-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(updateSchool["url"],
                                                                                           bodyNoSchoolName))
            self.assertEqual("请求方法不支持", actmessage, "school/编辑学校：FAIL-学校ID不存在-message返回信息不一致！")
            log.info("school/编辑学校：FAIL-学校ID不存在》测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if len(self.schoolId) != 0:
                for i in self.schoolId:
                    dao(db, "delete from school_period_record where school_id = " + str(i) + ";")
                    dao(db, "delete from school where id= " + str(i) + ";")
                    log.info("school/学校：删除学校记录成功！")
        except Exception as error:
            log.error("school/学校：删除学校记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
