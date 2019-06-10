# -*- coding: utf-8 -*-
# #!Date：2019/3/05 15:27
# # !@Author：龚远琪
from common.commonapi.upload import *
from module import *


class VideoPage(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.addrelationResponse = {}
        try:
            self.addrelationResponse, self.relationId = upload.createRelation()
            videopage["searchBody"]["searchVideoName"] = self.addrelationResponse.json()["data"][0]["videoName"]
        except Exception as error:
            log.error("video/视频：创建视频关联记录失败，失败原因："f'{error}')

    def test_TlessonPage_success(self):
        """
        video/视频：查询视频列表成功的测试用例-双师教材章节
        """
        self.tlessonPageResponse = request.run_main(videopage["textbook_lessonUrl"], method='POST',
                                                    headers=videopage["header"], data=videopage["body"])
        try:
            actsuccess = self.tlessonPageResponse.json()["success"]
            actmessage = self.tlessonPageResponse.json()["message"]
            actdata = self.tlessonPageResponse.json()["data"]
        except Exception as error:
            log.error("video/视频：查询视频列表接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：查询视频列表success返回false！")
            self.assertEqual(actdata["currentPage"], videopage["body"]["currentPage"],
                             "video/视频：查询视频列表当前页不一致")
            self.assertNotEqual(len(actdata["list"]), 0, "video/视频：查询视频列表为空")
            self.assertEqual(actdata["pageSize"], videopage["body"]["pageSize"],
                             "video/视频：查询视频列表每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "video/视频：查询视频列表总数小于1！")
            self.assertEqual(actmessage, "查询成功", "video/视频：查询视频列表message不一致！")
            log.info("video/视频：查询说课视频列表成功用例测试通过！")

    def test_searchPage_success(self):
        """
        video/视频：查询视频列表成功的测试用例--根据名称查询视频列表
        """
        self.searchPageResponse = request.run_main(videopage["textbook_lessonUrl"], method='POST',
                                                   headers=videopage["header"], data=videopage["searchBody"])
        try:
            actsuccess = self.searchPageResponse.json()["success"]
            actmessage = self.searchPageResponse.json()["message"]
            actdata = self.searchPageResponse.json()["data"]
        except Exception as error:
            log.error("video/视频：根据名称查询视频列表接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：根据名称查询视频列表success返回false！")
            self.assertEqual(actdata["currentPage"], videopage["searchBody"]["currentPage"],
                             "video/视频：根据名称查询视频列表当前页不一致")
            self.assertEqual(actdata["list"][0]["videoName"], videopage["searchBody"]["searchVideoName"],
                             "video/视频：根据名称查询视频列表数据错误！")
            self.assertEqual(actdata["pageSize"], videopage["searchBody"]["pageSize"],
                             "video/视频：根据名称查询视频列表每页大小不一致！")
            self.assertEqual(actdata["total"], 1, "video/视频：根据名称查询视频列表总数不等于1！")
            self.assertEqual(actmessage, "查询成功", "video/视频：根据名称查询视频列表message不一致！")
            log.info("video/视频：根据名称查询视频列表成功用例测试通过！")

    def test_pageSet_success(self):
        """
        video/视频：查询视频列表成功测试用例--设置每页显示大小及当前页
        """
        self.pageSetResponse = request.run_main(videopage["textbook_lessonUrl"], method='POST',
                                                   headers=videopage["header"], data=videopage["pageSetBody"])
        try:
            actsuccess = self.pageSetResponse.json()["success"]
            actmessage = self.pageSetResponse.json()["message"]
            actdata = self.pageSetResponse.json()["data"]
        except Exception as error:
            log.error("video/视频：查询视频列表-列表设置接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：查询视频列表-列表设置success返回false！")
            self.assertEqual(actdata["currentPage"], videopage["pageSetBody"]["currentPage"],
                             "video/视频：查询视频列表-列表设置当前页不一致")
            self.assertEqual(len(actdata["list"]), 1, "video/视频：查询视频列表-列表设置数据错误！")
            self.assertEqual(actdata["pageSize"], videopage["pageSetBody"]["pageSize"],
                             "video/视频：查询视频列表-列表设置每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "video/视频：查询说课视频列表总数小于1！")
            self.assertEqual(actmessage, "查询成功", "video/视频：查询视频列表-列表设置message不一致！")
            log.info("video/视频：查询视频列表-列表设置成功用例测试通过！")

    def test_pageNull_success(self):
        """
        video/视频：查询视频列表成功测试用例--未设置列表（取默认值）
        """
        self.pageSetResponse = request.run_main(videopage["textbook_lessonUrl"], method='POST',
                                                headers=videopage["header"], data={})
        try:
            actsuccess = self.pageSetResponse.json()["success"]
            actmessage = self.pageSetResponse.json()["message"]
            actdata = self.pageSetResponse.json()["data"]
        except Exception as error:
            log.error("video/视频：查询视频列表-未设置列表接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：查询视频列表-未设置列表success返回false！")
            self.assertEqual(actdata["currentPage"], 1, "video/视频：查询视频列表-未设置列表当前页不一致")
            self.assertGreaterEqual(len(actdata["list"]), 1, "video/视频：查询视频列表-未设置列表数据错误！")
            self.assertEqual(actdata["pageSize"], 10, "video/视频：查询视频列表-未设置列表每页大小不一致！")
            self.assertGreaterEqual(actdata["total"], 1, "video/视频：查询视频列表总数小于1！")
            self.assertEqual(actmessage, "查询成功", "video/视频：查询视频列表-未设置列表message不一致！")
            log.info("video/视频：查询视频列表-未设置列表成功用例测试通过！")

    def test_businessTypeNull_fail(self):
        """
        video/视频：查询视频列表失败测试用例--业务类型为空
        """
        self.pageSetResponse = request.run_main(videopage["businessTypeNull"], method='POST',
                                                headers=videopage["header"], data=videopage["body"])
        try:
            actsuccess = self.pageSetResponse.json()["success"]
            actmessage = self.pageSetResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：查询视频列表-业务类型为空接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：查询视频列表-业务类型为空success返回true！")
            self.assertEqual(actmessage, "参数类型不匹配异常", "video/视频：查询视频列表-业务类型为空message不一致！")
            log.info("video/视频：查询视频列表-业务类型为空失败用例测试通过！")

    def test_businessTypeErr_fail(self):
        """
        video/视频：查询视频列表失败测试用例--业务类型错误
        """
        self.pageSetResponse = request.run_main(videopage["businessTypeErr"], method='POST',
                                                headers=videopage["header"], data=videopage["body"])
        try:
            actsuccess = self.pageSetResponse.json()["success"]
            actmessage = self.pageSetResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：查询视频列表-业务类型错误接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：查询视频列表-业务类型错误success返回true！")
            self.assertEqual(actmessage, "参数类型不匹配异常", "video/视频：查询视频列表-业务类型错误message不一致！")
            log.info("video/视频：查询视频列表-业务类型错误 失败用例测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if self.relationId != "":
                upload.delete_video_relation(self.relationId)
        except Exception as error:
            log.error("video/视频：删除关联记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()