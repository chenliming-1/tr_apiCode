# -*- coding: utf-8 -*-
# #!Date：2019/7/25 9:43
# # !@Author：龚远琪
from module import *
from histudy import *
from data.teacher.school import *


class AddSchool(unittest.TestCase):
    addSchoolId = []

    @classmethod
    def setUpClass(self):
        self.addSchoolResponse = {}

    def test_addSchool(self):
        """
        school/学校：添加学校成功用例
        """
        addSuccessBody = addSchool["body_success"]
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=addSuccessBody)
        try:
            status_code = self.addSchoolResponse.status_code
            actdata = self.addSchoolResponse.json()
            self.addSchoolId.append(actdata["id"])
        except Exception as error:
            log.error("school/学校：添加学校接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code, "school/学校：添加学校成功用例-状态码错误！")
            self.assertEqual(addSuccessBody["cityId"], actdata["cityId"], "school/学校：添加学校成功用例-返回市Id不一致！")
            self.assertEqual(addSuccessBody["countyId"], actdata["countyId"], "school/学校：添加学校成功用例-返回区Id不一致！")
            self.assertEqual(addSuccessBody["provinceId"], actdata["provinceId"], "school/学校：添加学校成功用例-返回省Id不一致！")
            self.assertEqual(addSuccessBody["schoolName"], actdata["schoolName"], "school/学校：添加学校成功用例-学校名称不一致！")
            self.assertEqual(addSuccessBody["seq"], actdata["seq"], "school/学校：添加学校成功用例-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/学校：添加学校成功用例-学校状态不一致！")
            log.info("school/学校：添加学校成功用例测试通过！")


    def test_addSchoolNoCounty(self):
        """
        school/学校：添加学校不带区成功用例
        """
        addSchoolBody = addSchool["bodyNoCounty"]
        self.addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                                  data=addSchoolBody)
        try:
            status_code = self.addSchoolResponse.status_code
            actdata = self.addSchoolResponse.json()
            self.addSchoolId.append(actdata["id"])
        except Exception as error:
            log.error("school/学校：添加学校不带区接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(201, status_code, "school/学校：添加学校不带区成功用例-状态码错误！")
            self.assertEqual(addSchoolBody["cityId"], actdata["cityId"], "school/学校：添加学校不带区成功用例-返回市Id不一致！")
            self.assertEqual(addSchoolBody["provinceId"], actdata["provinceId"], "school/学校：添加学校不带区成功用例-返回省Id不一致！")
            self.assertEqual(addSchoolBody["schoolName"], actdata["schoolName"], "school/学校：添加学校不带区成功用例-学校名称不一致！")
            self.assertEqual(addSchoolBody["seq"], actdata["seq"], "school/学校：添加学校不带区成功用例-学校排名不一致！")
            self.assertEqual("ENABLE", actdata["status"], "school/学校：添加学校不带区成功用例-学校状态不一致！")
            log.info("school/学校：添加学校不带区成功用例测试通过！")

    # def test_getItemTypeNoExist(self):
    #     """
    #     itemType/题型：获取不存在的题型
    #     """
    #     self.getItemTypeResponse = request.run_main(getItemType["url"] + str(99999), method='GET',
    #                                                 headers=getItemType["header"], data={})
    #     try:
    #         status_code = self.getItemTypeResponse.status_code
    #         actmessage = self.getItemTypeResponse.json()["message"]
    #     except Exception as error:
    #         log.error("itemType/题型：获取不存在的题型接口失败，失败原因："f'{error}')
    #     finally:
    #         self.assertEqual(status_code, 404, "itemType/题型：获取不存在的题型-状态码错误！")
    #         self.assertEqual(actmessage, "题型不存在", "itemType/题型：获取不存在的题型 message返回信息不一致！")
    #         log.info("itemType/题型：获取不存在的题型用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass
        # try:
        #     if self.itemTypeId != "":
        #         dataDict.delete_itemtype(self.itemTypeId)
        # except Exception as error:
        #     log.error("itemType/题型：删除题型记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()