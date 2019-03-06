# -*- coding: utf-8 -*-
# #!Date：2019/2/22 14:06
# # !@Author：龚远琪
from histudy import *
from data.teacher.video import *
from common.commonmethod import *
from module import *


class Resource(unittest.TestCase):
    video_id = ""

    @classmethod
    def setUpClass(self):
        self.resourceResponse = {}

    def test_resource_success(self):
        """
        video/视频：视频上传resource成功的测试用例
        """
        self.resourceResponse = request.run_main(resource["url"], method='POST', headers=resource["header"],
                                                 data=resource[env+"_body_success"])
        try:
            actsuccess = self.resourceResponse.json()["success"]
            actdata = self.resourceResponse.json()["data"]
            sql = "select id from tr_video where video_no='"f'{actdata["videoNo"]}' "' limit 1;"
            Resource.video_id = dao(db, sql)[0]["id"]
        except Exception as error:
            log.error("video/视频：视频上传resource接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：视频上传resource success返回false！")
            self.assertFalse(actdata["defaultShow"], "video/视频：视频上传resource defaultShow返回True!")
            self.assertEqual(actdata["fileLength"], resource[env+"_body_success"]["fsize"], "video/视频：视频上传resource文件大小不一致！")
            self.assertEqual(actdata["fileName"], resource[env+"_body_success"]["fileName"], "video/视频：视频上传resource名称不一致！")
            self.assertEqual(Resource.video_id, actdata["id"], "video/视频：视频上传resource ID不存在！")
            self.assertEqual(actdata["sourceType"], "dingdang", "video/视频：视频上传resource类型错误！")
            self.assertEqual(actdata["statusCode"], 1, "video/视频：视频上传resource状态返回错误！")
            self.assertEqual(actdata["videoName"], resource[env+"_body_success"]["aliasName"],
                             "video/视频：视频上传resource名称不一致！")
            self.assertIsNotNone(actdata["videoNo"], "video/视频：视频上传resource video返回为空！")
            log.info("video/视频：视频上传resource成功用例测试通过！")

    def test_resource_typeisnull(self):
        """
        video/视频：视频上传resource失败的测试用例-type为NULL
        """
        self.resourceResponse = request.run_main(resource["url"], method='POST', headers=resource["header"],
                                                    data=resource["body_typeError"])
        try:
            actsuccess = self.resourceResponse.json()["success"]
            actmessage = self.resourceResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：视频上传resource接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：视频上传resource success返回True！")
            self.assertEqual(actmessage, "操作失败:视频上传失败;操作失败,请稍后重试", "video/视频：视频上传resource message返回信息不一致！")
            log.info("video/视频：视频上传resource失败用例-type为NULL测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if Resource.video_id != "":
                dao(db, "delete from tr_video where id='"+Resource.video_id + "';")
        except Exception as error:
            log.error("video/视频：视频上传-删除视频失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()