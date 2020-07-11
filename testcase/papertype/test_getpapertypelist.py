# -*- encoding: utf-8 -*-
# @ModuleName: getpapertypelist
# @Author：龚远琪
# @Date：2019/11/6 9:47
from common.commonapi.datadict import *


class GetPaperTypeList(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.getPaperTypeListResponse = {}

    def test_getPaperTypeListOne(self):
        """
        paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["searchOneBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actdata = self.getPaperTypeListResponse.json()
        except Exception as error:
            log.error("paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型-状态码错误！")
            self.assertEqual(getPaperTypeList["searchOneBody"]["typeName"], actdata["list"][0]["typeName"],
                             "paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型-套卷类型名称不一致！")
            self.assertEqual(getPaperTypeList["searchOneBody"]["currentPage"], actdata["currentPage"],
                             "paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型-当前页返回错误！")
            self.assertEqual(getPaperTypeList["searchOneBody"]["pageSize"], actdata["pageSize"],
                             "paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型-每页大小不一致！")
            self.assertEqual(1, actdata["total"], "paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型-返回列表数不一致！")
            log.info("paperType/获取套卷类型列表：SUCCESS-获取一条套卷类型》测试通过！")

    def test_getPaperTypeListSome(self):
        """
        paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["searchSomeBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actdata = self.getPaperTypeListResponse.json()
        except Exception as error:
            log.error("paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型-状态码错误！")
            self.assertIn(getPaperTypeList["searchSomeBody"]["typeName"], actdata["list"][0]["typeName"],
                          "paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型-套卷类型名称不一致！")
            self.assertEqual(getPaperTypeList["searchSomeBody"]["currentPage"], actdata["currentPage"],
                             "paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型-当前页返回错误！")
            self.assertEqual(getPaperTypeList["searchSomeBody"]["pageSize"], actdata["pageSize"],
                             "paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型-每页大小不一致！")
            self.assertLess(1, actdata["total"], "paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型-返回列表数不一致！")
            log.info("paperType/获取套卷类型列表：SUCCESS-获取多条套卷类型》测试通过！")

    def test_getPaperTypeListAll(self):
        """
        paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["searchAllBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actdata = self.getPaperTypeListResponse.json()
        except Exception as error:
            log.error("paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型-状态码错误！")
            self.assertEqual(getPaperTypeList["searchAllBody"]["currentPage"], actdata["currentPage"],
                             "paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型-当前页返回错误！")
            self.assertEqual(getPaperTypeList["searchAllBody"]["pageSize"], actdata["pageSize"],
                             "paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型-每页大小不一致！")
            self.assertLess(1, actdata["total"], "paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型-返回列表数不一致！")
            log.info("paperType/获取套卷类型列表：SUCCESS-获取全部套卷类型》测试通过！")
            
    def test_getPaperTypeListNone(self):
        """
        paperType/获取套卷类型列表：SUCCESS-获取空列表
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["searchNoneBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actdata = self.getPaperTypeListResponse.json()
        except Exception as error:
            log.error("paperType/获取套卷类型列表：SUCCESS-获取空列表》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/获取套卷类型列表：SUCCESS-获取空列表-状态码错误！")
            self.assertEqual(getPaperTypeList["searchNoneBody"]["currentPage"], actdata["currentPage"],
                             "paperType/获取套卷类型列表：SUCCESS-获取空列表-当前页返回错误！")
            self.assertEqual(getPaperTypeList["searchNoneBody"]["pageSize"], actdata["pageSize"],
                             "paperType/获取套卷类型列表：SUCCESS-获取空列表-每页大小不一致！")
            self.assertEqual(0, actdata["total"], "paperType/获取套卷类型列表：SUCCESS-获取空列表-返回列表数不一致！")
            log.info("paperType/获取套卷类型列表：SUCCESS-获取空列表》测试通过！")

    def test_getPaperTypeListCurrentPageErr(self):
        """
        paperType/获取套卷类型列表：FAIL-输入错误当前页查询
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["currentPageErrBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actmessage = self.getPaperTypeListResponse.json()["message"]
        except Exception as error:
            log.error("paperType/获取套卷类型列表：FAIL-输入错误当前页查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "paperType/获取套卷类型列表：FAIL-输入错误当前页查询-状态码错误！")
            self.assertEqual("Page index must not be less than zero!", actmessage,
                             "paperType/获取套卷类型列表：FAIL-输入错误当前页查询-message返回信息不一致！")
            log.info("paperType/获取套卷类型列表：FAIL-输入错误当前页查询》测试通过！")
    
    def test_getPaperTypeListPageSizeErr(self):
        """
        paperType/获取套卷类型列表：FAIL-每页大小为负数查询
        """
        self.getPaperTypeListResponse = requests.get(getPaperTypeList["url"], headers=getPaperTypeList["header"],
                                                     params=getPaperTypeList["pageSizeErrBody"])
        try:
            status_code = self.getPaperTypeListResponse.status_code
            actmessage = self.getPaperTypeListResponse.json()["message"]
        except Exception as error:
            log.error("paperType/获取套卷类型列表：FAIL-每页大小为负数查询》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(500, status_code, "paperType/获取套卷类型列表：FAIL-每页大小为负数查询-状态码错误！")
            self.assertEqual("Page size must not be less than one!", actmessage,
                             "paperType/获取套卷类型列表：FAIL-每页大小为负数查询-message返回信息不一致！")
            log.info("paperType/获取套卷类型列表：FAIL-每页大小为负数查询》测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
