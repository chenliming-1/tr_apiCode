# -*- coding: utf-8 -*-
# #!Date：2019/10/18 15:03
# # !@Author：龚远琪
from common.commonmethod import *
from common.commonapi.datadict import *


class GetSchoolList(unittest.TestCase):

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
        self.getSchoolListResponse = {}
        try:
            self.addSchoolBody = self.getData(self)
            self.addSchoolResponse = dataDict.addSchool(self.addSchoolBody)
            self.addSchoolData = self.addSchoolResponse.json()
            self.schoolId = self.addSchoolData["id"]
        except Exception as error:
            log.error("school/学校：学校新增失败，失败原因："f'{error}')

    def test_getSchoolList(self):
        """
        school/获取学校列表：SUCCESS-根据学校名称模糊查询
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["selectBySchoolNameBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-根据学校名称模糊查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-根据学校名称模糊查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["selectBySchoolNameBody"], self.getSchoolListResponse.text))
            self.assertIn(getSchoolList["selectBySchoolNameBody"]["schoolName"], actdata["list"][0]["schoolName"],
                          "school/获取学校列表：SUCCESS-根据学校名称模糊查询-学校名称不一致！")
            self.assertEqual(getSchoolList["selectBySchoolNameBody"]["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-根据学校名称模糊查询-当前页返回错误！")
            self.assertEqual(getSchoolList["selectBySchoolNameBody"]["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-根据学校名称模糊查询-每页大小不一致！")
            self.assertLessEqual(1, actdata["total"], "school/获取学校列表：SUCCESS-根据学校名称模糊查询-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-根据学校名称模糊查询》测试通过！")

    def test_getListBySchoolName(self):
        """
        school/获取学校列表：SUCCESS-根据学校名称精确查询
        """
        schoolListBody = getSchoolList["selectBySchoolNameBody"].copy()
        schoolListBody["schoolName"] = self.addSchoolBody["schoolName"]
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=schoolListBody)
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-根据学校名称精确查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-根据学校名称精确查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], schoolListBody, self.getSchoolListResponse.text))
            self.assertEqual(schoolListBody["schoolName"], actdata["list"][0]["schoolName"],
                             "school/获取学校列表：SUCCESS-根据学校名称精确查询-学校名称不一致！")
            self.assertEqual(schoolListBody["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-根据学校名称精确查询-当前页返回错误！")
            self.assertEqual(schoolListBody["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-根据学校名称精确查询-每页大小不一致！")
            self.assertEqual(1, actdata["total"], "school/获取学校列表：SUCCESS-根据学校名称精确查询-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-根据学校名称精确查询》测试通过！")

    def test_getListByArea(self):
        """
        school/获取学校列表：SUCCESS-根据地区查询
        """
        schoolListBody = getSchoolList["selectByAreaBody"].copy()
        schoolListBody["provinceId"] = self.addSchoolBody["provinceId"]
        schoolListBody["cityId"] = self.addSchoolBody["cityId"]
        schoolListBody["countyId"] = self.addSchoolBody["countyId"]
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=schoolListBody)
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-根据地区查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-根据地区查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], schoolListBody, self.getSchoolListResponse.text))
            self.assertEqual(schoolListBody["provinceId"], actdata["list"][0]["provinceId"],
                             "school/获取学校列表：SUCCESS-根据地区查询-省份不一致！")
            self.assertEqual(schoolListBody["cityId"], actdata["list"][0]["cityId"],
                             "school/获取学校列表：SUCCESS-根据地区查询-市ID不一致！")
            self.assertEqual(schoolListBody["countyId"], actdata["list"][0]["countyId"],
                             "school/获取学校列表：SUCCESS-根据地区查询-区ID不一致！")
            self.assertEqual(schoolListBody["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-根据地区查询-当前页返回错误！")
            self.assertEqual(schoolListBody["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-根据地区查询-每页大小不一致！")
            self.assertLessEqual(1, actdata["total"], "school/获取学校列表：SUCCESS-根据地区查询-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-根据地区查询》测试通过！")

    def test_getListByAreaErr(self):
        """
        school/获取学校列表：SUCCESS-输入错误市ID查询空列表
        """
        schoolListBody = getSchoolList["selectByAreaBody"].copy()
        schoolListBody["provinceId"] = self.addSchoolBody["provinceId"]
        schoolListBody["cityId"] = 99999
        schoolListBody["countyId"] = self.addSchoolBody["countyId"]
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=schoolListBody)
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-输入错误市ID查询空列表》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-输入错误市ID查询空列表-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], schoolListBody, self.getSchoolListResponse.text))
            self.assertEqual(schoolListBody["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-输入错误市ID查询空列表-当前页返回错误！")
            self.assertEqual(schoolListBody["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-输入错误市ID查询空列表-每页大小不一致！")
            self.assertEqual(0, actdata["total"], "school/获取学校列表：SUCCESS-输入错误市ID查询空列表-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-输入错误市ID查询空列表》测试通过！")

    def test_getListByPeriod(self):
        """
        school/获取学校列表：SUCCESS-根据学校名称和学段查询
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["selectByPeriodBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-根据学校名称和学段查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-根据学校名称和学段查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["selectByPeriodBody"], self.getSchoolListResponse.text))
            self.assertIn(getSchoolList["selectByPeriodBody"]["schoolName"], actdata["list"][0]["schoolName"],
                          "school/获取学校列表：SUCCESS-根据学校名称和学段查询-学校名称不一致！")
            self.assertEqual(getSchoolList["selectByPeriodBody"]["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-根据学校名称和学段查询-当前页返回错误！")
            self.assertEqual(getSchoolList["selectByPeriodBody"]["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-根据学校名称和学段查询-每页大小不一致！")
            self.assertLessEqual(0, actdata["total"], "school/获取学校列表：SUCCESS-根据学校名称和学段查询-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-根据学校名称和学段查询》测试通过！")

    def test_getListByStatus(self):
        """
        school/获取学校列表：SUCCESS-根据学校状态查询
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["selectByStatusBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-根据学校名称模糊查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-根据学校名称模糊查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["selectByStatusBody"], self.getSchoolListResponse.text))
            self.assertIn(getSchoolList["selectByStatusBody"]["status"], actdata["list"][0]["status"],
                          "school/获取学校列表：SUCCESS-根据学校名称模糊查询-查询结果状态不一致！")
            self.assertEqual(getSchoolList["selectByStatusBody"]["currentPage"], actdata["currentPage"],
                             "school/获取学校列表：SUCCESS-根据学校名称模糊查询-当前页返回错误！")
            self.assertEqual(getSchoolList["selectByStatusBody"]["pageSize"], actdata["pageSize"],
                             "school/获取学校列表：SUCCESS-根据学校名称模糊查询-每页大小不一致！")
            self.assertLessEqual(0, actdata["total"], "school/获取学校列表：SUCCESS-根据学校名称模糊查询-返回列表数不一致！")
            log.info("school/获取学校详情：SUCCESS-根据学校名称模糊查询》测试通过！")

    def test_getListStatusErr(self):
        """
        school/获取学校列表：SUCCESS-输入错误状态查询空列表
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["statusErrBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actdata = self.getSchoolListResponse.json()
        except Exception as error:
            log.error("school/获取学校列表：SUCCESS-输入错误状态查询空列表》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "school/获取学校列表：SUCCESS-输入错误状态查询空列表-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["statusErrBody"], self.getSchoolListResponse.text))
            self.assertEqual(0, actdata["total"], "school/获取学校列表：SUCCESS-输入错误状态查询空列表-返回总数不一致！")
            log.info("school/获取学校列表：SUCCESS-输入错误状态查询空列表》测试通过！")

    def test_getListCurrentPageErr(self):
        """
        school/获取学校列表：FAIL-输入错误当前页查询
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["currentPageErrBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actmessage = self.getSchoolListResponse.json()["message"]
        except Exception as error:
            log.error("school/获取学校列表：FAIL-输入错误当前页查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "school/获取学校列表：FAIL-输入错误当前页查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["currentPageErrBody"], self.getSchoolListResponse.text))
            self.assertEqual("Page index must not be less than zero!", actmessage,
                             "school/获取学校列表：FAIL-输入错误当前页查询-message返回信息不一致！")
            log.info("school/获取学校列表：FAIL-输入错误当前页查询》测试通过！")

    def test_getListPageSizeErr(self):
        """
        school/获取学校列表：FAIL-每页大小为负数查询
        """
        self.getSchoolListResponse = requests.get(getSchoolList["url"], headers=getSchoolList["header"],
                                                  params=getSchoolList["pageSizeErrBody"])
        try:
            status_code = self.getSchoolListResponse.status_code
            actmessage = self.getSchoolListResponse.json()["message"]
        except Exception as error:
            log.error("school/获取学校列表：FAIL-每页大小为负数查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "school/获取学校列表：FAIL-每页大小为负数查询-状态码错误！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 getSchoolList["url"], getSchoolList["pageSizeErrBody"], self.getSchoolListResponse.text))
            self.assertEqual("Page size must not be less than one!", actmessage,
                             "school/获取学校列表：FAIL-每页大小为负数查询-message返回信息不一致！")
            log.info("school/获取学校列表：FAIL-每页大小为负数查询》测试通过！")

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
