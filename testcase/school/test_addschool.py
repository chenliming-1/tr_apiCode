# -*- coding: utf-8 -*-
# #!Date：2019/7/25 9:43
# # !@Author：龚远琪
from common.commonmethod import *
from common.commonapi.datadict import *


class AddSchool(unittest.TestCase):
    addSchoolId = []

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
        schoolBody["seq"] = randMethod.getNumByRange(1, 2000)
        return schoolBody

    @classmethod
    def setUpClass(self):
        self.addSchoolResponse = {}
        self.addSchoolBody = self.getData(self)
        self.addBodyRepeat = self.getData(self)
        self.addBodyNoCounty = self.getData(self, 0)
        self.addBodyPeriodErr = self.getData(self, 0)

    def test_addSchool(self):
        """
        school/添加学校：SUCCESS-添加学校（带区）
        """
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addSchoolBody)
        try:
            status_code = self.addSchoolResponse.status_code
            actdata = self.addSchoolResponse.json()
            self.addSchoolId.append(actdata["id"])
        except Exception as error:
            log.error("school/添加学校：SUCCESS-添加学校（带区）》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code,
                             r"school/添加学校：SUCCESS-添加学校（带区）-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(addSchool["url"],
                                                                                                self.addSchoolBody))
            self.assertEqual(self.addSchoolBody["cityId"], actdata["cityId"], "school/添加学校：SUCCESS-添加学校（带区）-返回市Id不一致！")
            self.assertEqual(self.addSchoolBody["countyId"], actdata["countyId"],
                             "school/添加学校：SUCCESS-添加学校（带区）-返回区Id不一致！")
            self.assertEqual(self.addSchoolBody["provinceId"], actdata["provinceId"],
                             "school/添加学校：SUCCESS-添加学校（带区）-返回省Id不一致！")
            self.assertEqual(self.addSchoolBody["schoolName"], actdata["schoolName"],
                             "school/添加学校：SUCCESS-添加学校（带区）-学校名称不一致！")
            self.assertEqual(self.addSchoolBody["seq"], actdata["seq"], "school/添加学校：SUCCESS-添加学校（带区）-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/添加学校：SUCCESS-添加学校（带区）-学校状态不一致！")
            log.info("school/添加学校：SUCCESS-添加学校（带区）》测试通过！")

    def test_addSchoolNoCounty(self):
        """
        school/添加学校：SUCCESS-添加学校不带区
        """
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addBodyNoCounty)
        try:
            status_code = self.addSchoolResponse.status_code
            actdata = self.addSchoolResponse.json()
            self.addSchoolId.append(actdata["id"])
        except Exception as error:
            log.error("school/添加学校：SUCCESS-添加学校不带区》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code,
                             "school/添加学校：SUCCESS-添加学校不带区-状态码错误！\n\t 接口：{} \n\t 入参：{}".format(addSchool["url"],
                                                                                              self.addBodyNoCounty))
            self.assertEqual(self.addBodyNoCounty["cityId"], actdata["cityId"], "school/添加学校：SUCCESS-添加学校不带区-返回市Id不一致！")
            self.assertEqual(self.addBodyNoCounty["provinceId"], actdata["provinceId"],
                             "school/添加学校：SUCCESS-添加学校不带区-返回省Id不一致！")
            self.assertIsNone(actdata["countyId"], "school/添加学校：SUCCESS-添加学校不带区-返回区Id不为空！")
            self.assertEqual(self.addBodyNoCounty["schoolName"], actdata["schoolName"],
                             "school/添加学校：SUCCESS-添加学校不带区-学校名称不一致！")
            self.assertEqual(self.addBodyNoCounty["seq"], actdata["seq"], "school/添加学校：SUCCESS-添加学校不带区-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/添加学校：SUCCESS-添加学校不带区-学校状态不一致！")
            log.info("school/添加学校：SUCCESS-添加学校不带区》测试通过！")

    def test_addSchoolRepeat(self):
        """
        school/添加学校：FAIL-添加重复学校
        """

        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addBodyRepeat)
        self.addSchoolId.append(self.addSchoolResponse.json()["id"])
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addBodyRepeat)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-添加重复学校》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-添加重复学校-状态码错误！")
            self.assertEqual("该学校已经存在了噢~", actmessage, "school/添加学校：FAIL-添加重复学校-message返回信息不一致！")
            log.info("school/添加学校：FAIL-添加重复学校》测试通过！")

    def test_addSchoolCountyErr(self):
        """
        school/添加学校：FAIL-区不存在
        """
        bodyCountyErr = self.addBodyNoCounty.copy()
        bodyCountyErr["countyId"] = 999999
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyCountyErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-区不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-区不存在-状态码错误！")
            self.assertEqual("县（区）不存在", actmessage, "school/添加学校：FAIL-区不存在-message返回信息不一致！")
            log.info("school/添加学校：FAIL-区不存在》测试通过！")

    def test_addSchoolNoCity(self):
        """
        school/添加学校：FAIL-添加学校不带市
        """
        bodyNoCity = self.addBodyNoCounty.copy()
        bodyNoCity["cityId"] = None
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyNoCity)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-添加学校不带市》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-添加学校不带市-状态码错误！")
            self.assertEqual("城市id不能为空", actmessage, "school/添加学校：FAIL-添加学校不带市-message返回信息不一致！")
            log.info("school/添加学校：FAIL-添加学校不带市》测试通过！")

    def test_addSchoolCityErr(self):
        """
        school/添加学校：FAIL-添加学校市不存在
        """
        bodyCityErr = self.addBodyNoCounty.copy()
        bodyCityErr["cityId"] = 95
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyCityErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-添加学校市不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-添加学校市不存在-状态码错误！")
            self.assertEqual("城市不存在", actmessage, "school/添加学校：FAIL-添加学校市不存在-message返回信息不一致！")
            log.info("school/添加学校：FAIL-添加学校市不存在》测试通过！")

    def test_addSchoolNoProvince(self):
        """
        school/添加学校：FAIL-添加学校不带省
        """
        bodyNoProvince = self.addBodyNoCounty.copy()
        bodyNoProvince["provinceId"] = None
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyNoProvince)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-添加学校不带省》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-添加学校不带省-状态码错误！")
            self.assertEqual("省份id不能为空", actmessage, "school/添加学校：FAIL-添加学校不带省-message返回信息不一致！")
            log.info("school/添加学校：FAIL-添加学校不带省》测试通过！")

    def test_addSchoolProvinceErr(self):
        """
        school/添加学校：FAIL-添加学校省份不存在
        """
        bodyProvinceErr = self.addBodyNoCounty.copy()
        bodyProvinceErr["provinceId"] = 100
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyProvinceErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-添加学校省份不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-添加学校省份不存在-状态码错误！")
            self.assertEqual("省份不存在", actmessage, "school/添加学校：FAIL-添加学校省份不存在-message返回信息不一致！")
            log.info("school/添加学校：FAIL-添加学校省份不存在》测试通过！")

    def test_addSchoolNoSchoolName(self):
        """
        school/添加学校：FAIL-学校名为空
        """
        bodyNoSchoolName = self.addBodyNoCounty.copy()
        bodyNoSchoolName["schoolName"] = None
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyNoSchoolName)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-学校名为空》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-学校名为空-状态码错误！")
            self.assertEqual("学校名称不能为空", actmessage, "school/添加学校：FAIL-学校名为空-message返回信息不一致！")
            log.info("school/添加学校：FAIL-学校名为空》测试通过！")

    def test_addSchoolNoPeriod(self):
        """
        school/添加学校：FAIL-学段不存在
        """
        bodyNoPeriod = self.addBodyNoCounty.copy()
        bodyNoPeriod["periodIds"] = None
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyNoPeriod)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-学段不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-学段不存在-状态码错误！")
            self.assertEqual("学段信息不能为空", actmessage, "school/添加学校：FAIL-学段不存在-message返回信息不一致！")
            log.info("school/添加学校：FAIL-学段不存在》测试通过！")

    def test_addSchoolPeriodNone(self):
        """
        school/添加学校：FAIL-学段含空
        """
        self.addBodyPeriodErr["periodIds"] = [None, 10001]
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addBodyPeriodErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-学段含空》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-学段含空-状态码错误！")
            self.assertEqual("学段id不能为空", actmessage, "school/添加学校：FAIL-学段含空-message返回信息不一致！")
            log.info("school/添加学校：FAIL-学段含空》测试通过！")

    def test_addSchoolPeriodErr(self):
        """
        school/添加学校：FAIL-学段错误
        """
        self.addBodyPeriodErr["periodIds"] = [10004, 10001]
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=self.addBodyPeriodErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-学段错误》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-学段错误-状态码错误！")
            self.assertEqual("学段id错误", actmessage, "school/添加学校：FAIL-学段错误-message返回信息不一致！")
            log.info("school/添加学校：FAIL-学段错误》测试通过！")

    def test_addSchoolSeqIsZero(self):
        """
        school/添加学校：FAIL-排序不在1-2000范围内
        """
        bodySeqErr = self.addBodyNoCounty.copy()
        bodySeqErr["seq"] = 0
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodySeqErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-排序不在1-2000范围内》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-排序不在1-2000范围内-状态码错误！")
            self.assertEqual("排序只允许1-2000（包含）之间", actmessage, "school/添加学校：FAIL-排序不在1-2000范围内-message返回信息不一致！")
            log.info("school/添加学校：FAIL-排序不在1-2000范围内》测试通过！")

    def test_addSchoolSeqErr(self):
        """
        school/添加学校：FAIL-排序为2001
        """
        bodySeqErr = self.addBodyNoCounty.copy()
        bodySeqErr["seq"] = 2001
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodySeqErr)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-排序为2001》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-排序为2001-状态码错误！")
            self.assertEqual("排序只允许1-2000（包含）之间", actmessage, "school/添加学校：FAIL-排序为2001-message返回信息不一致！")
            log.info("school/添加学校：FAIL-排序为2001》测试通过！")

    def test_addSchoolNameTooLong(self):
        """
        school/添加学校：FAIL-学校名称超出100字符
        """
        bodyNameTooLong = self.addBodyNoCounty.copy()
        bodyNameTooLong["schoolName"] = randMethod.getMessage(101)
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=bodyNameTooLong)
        try:
            status_code = self.addSchoolResponse.status_code
            actmessage = self.addSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/添加学校：FAIL-学校名称超出100字符》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "school/添加学校：FAIL-学校名称超出100字符-状态码错误！")
            self.assertEqual("学校名称过长", actmessage, "school/添加学校：FAIL-学校名称超出100字符-message返回信息不一致！")
            log.info("school/添加学校：FAIL-学校名称超出100字符》测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if len(self.addSchoolId) != 0:
                for i in self.addSchoolId:
                    dao(db, "delete from school_period_record where school_id = " + str(i) + ";")
                    dao(db, "delete from school where id= " + str(i) + ";")
                    log.info("school/学校：删除学校记录成功！")
        except Exception as error:
            log.error("school/学校：删除学校记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()
