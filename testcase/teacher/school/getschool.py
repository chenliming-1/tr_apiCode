# -*- coding: utf-8 -*-
# #!Date：2019/10/18 10:43
# # !@Author：龚远琪
from common.commonmethod import *
from common.commonapi.datadict import *


class GetSchool(unittest.TestCase):

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
        self.getSchoolResponse = {}
        try:
            self.addSchoolBody = self.getData(self)
            self.addSchoolResponse = dataDict.addSchool(self.addSchoolBody)
            self.addSchoolData = self.addSchoolResponse.json()
            self.schoolId = self.addSchoolData["id"]
        except Exception as error:
            log.error("school/学校：学校新增失败，失败原因："f'{error}')

    def test_getSchool(self):
        """
        school/获取学校详情：SUCCESS-获取学校详情
        """
        self.getSchoolResponse = request.run_main(getSchool["url"] + str(self.schoolId), method='GET',
                                                  headers=getSchool["header"])
        try:
            status_code = self.getSchoolResponse.status_code
            actdata = self.getSchoolResponse.json()
        except Exception as error:
            log.error("school/获取学校详情：SUCCESS-获取学校详情》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校详情：SUCCESS-获取学校详情-状态码错误！")
            self.assertEqual(self.addSchoolBody["cityId"], actdata["cityId"],
                             "school/获取学校详情：SUCCESS-获取学校详情-返回市Id不一致！")
            self.assertEqual(self.addSchoolBody["countyId"], actdata["countyId"],
                             "school/获取学校详情：SUCCESS-获取学校详情-返回区Id不一致！")
            self.assertEqual(self.addSchoolBody["provinceId"], actdata["provinceId"],
                             "school/获取学校详情：SUCCESS-获取学校详情-返回省Id不一致！")
            self.assertEqual(self.addSchoolBody["schoolName"], actdata["schoolName"],
                             "school/获取学校详情：SUCCESS-获取学校详情-学校名称不一致！")
            self.assertEqual(self.addSchoolBody["seq"], actdata["seq"], "school/获取学校详情：SUCCESS-获取学校详情-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/获取学校详情：SUCCESS-获取学校详情-学校状态不一致！")
            log.info("school/获取学校详情：SUCCESS-获取学校详情》测试通过！")

    def test_getSchoolNoExist(self):
        """
        school/获取学校详情：FAIL-学校不存在
        """
        self.getSchoolResponse = request.run_main(getSchool["url"] + str(999999), method='GET',
                                                  headers=editSchoolStatus["header"])
        try:
            status_code = self.getSchoolResponse.status_code
            actmessage = self.getSchoolResponse.json()["message"]
        except Exception as error:
            log.error("school/获取学校详情：FAIL-学校不存在》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "school/获取学校详情：FAIL-学校不存在-状态码错误！")
            self.assertEqual("学校不存在，id: 999999", actmessage, "school/获取学校详情：FAIL-学校不存在-message返回信息不一致！")
            log.info("school/获取学校详情：FAIL-学校不存在》测试通过！")

    def test_getSchoolNoID(self):
        """
        school/获取学校详情：FAIL-未传入学校ID
        """
        self.getSchoolResponse = request.run_main(editSchoolStatus["url"] + "/status/ENABLE",
                                                  method='PUT', headers=editSchoolStatus["header"])
        try:
            status_code = self.getSchoolResponse.status_code
        except Exception as error:
            log.error("school/获取学校详情：FAIL-未传入学校ID》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(404, status_code, "school/获取学校详情：FAIL-未传入学校ID-状态码错误！")
            log.info("school/获取学校详情：FAIL-未传入学校ID》测试通过！")

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
