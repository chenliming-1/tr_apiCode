# -*- coding: utf-8 -*-
# #!Date：2019/2/22 14:06
# # !@Author：龚远琪
from common.commonapi.upload import *
from module import *


class CreateRelation(unittest.TestCase):
    uploadfiledata = {}
    recordId = ""

    @classmethod
    def setUpClass(self):
        self.createvrecordResponse = {}
        try:
            self.uploadfileResponse = upload.upload_video()
            CreateRelation.uploadfiledata = self.uploadfileResponse.json()["data"]
            CreateRelation.uploadfiledata[0]["fileLength"] = uploadfile[env+"_body_success"][0][0]["fsize"]
        except Exception as error:
            log.error("video/视频：视频上传失败，失败原因："f'{error}')

    def test_TlessonType_success(self):
        """
        video/视频：创建视频记录成功的测试用例-绑定教材章节
        """
        self.tlessonTypeResponse = request.run_main(createrelation["textbook_lessonUrl"], method='POST',
                                                    headers=createrelation["header"], data=CreateRelation.uploadfiledata)
        try:
            actsuccess = self.tlessonTypeResponse.json()["success"]
            actdata = self.tlessonTypeResponse.json()["data"][0]
            sql = "select id from video_relation where video_id='"f'{actdata["id"]}' "' and ref_id='"+randbusinessId+"' limit 1;"
            CreateRelation.recordId = dao(db, sql)[0]["id"]
        except Exception as error:
            log.error("video/视频：创建视频记录接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：创建视频记录success返回false！")
            self.assertEqual(actdata["createTime"], CreateRelation.uploadfiledata[0]["createTime"],
                             "video/视频：创建视频记录创建日期不一致！")
            self.assertEqual(actdata["createUser"], CreateRelation.uploadfiledata[0]["createUser"],
                             "video/视频：创建视频记录创建人不一致！")
            self.assertFalse(actdata["defaultShow"], "video/视频：创建视频记录defaultShow返回True!")
            self.assertEqual(actdata["fileLength"], CreateRelation.uploadfiledata[0]["fileLength"],
                             "video/视频：创建视频记录文件大小不一致！")
            self.assertEqual(actdata["fileName"], CreateRelation.uploadfiledata[0]["fileName"],
                             "video/视频：创建视频记录名称不一致！")
            self.assertIsNotNone(CreateRelation.recordId, "video/视频：创建视频记录ID不存在！")
            self.assertEqual(actdata["sourceType"], "dingdang", "video/视频：创建视频记录类型错误！")
            self.assertEqual(actdata["statusCode"], 1, "video/视频：创建视频记录状态返回错误！")
            self.assertEqual(actdata["videoName"], CreateRelation.uploadfiledata[0]["videoName"],
                             "video/视频：创建视频记录名称不一致！")
            self.assertIsNotNone(actdata["videoNo"], "video/视频：创建视频记录videoNo返回为空！")
            log.info("video/视频：创建视频记录成功用例测试通过！")

    def test_createrecord_businessIdIsNull(self):
        """
        video/视频：创建视频记录失败的测试用例-关联Id为空
        """
        self.businessIdIsNullResponse = request.run_main(createrelation["businessIdIsNull"], method='POST',
                                                    headers=createrelation["header"], data=CreateRelation.uploadfiledata)
        try:
            actsuccess = self.businessIdIsNullResponse.json()["success"]
            actmessage = self.businessIdIsNullResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：创建视频记录接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：创建记录失败用例-关联Id为空success返回true！")
            self.assertEqual(actmessage, "业务ID为空", "video/视频：创建记录失败用例-关联Id为空message返回信息不一致！")
            log.info("video/视频：创建记录失败用例-关联Id为空测试通过！")

    def test_createrecord_businessTypeIsNull(self):
        """
        video/视频：创建视频记录失败的测试用例-关联Type为空
        """
        self.businessTypeIsNullResponse = request.run_main(createrelation["businessTypeIsNull"], method='POST',
                                                           headers=createrelation["header"], data=CreateRelation.uploadfiledata)
        try:
            actsuccess = self.businessTypeIsNullResponse.json()["success"]
            actmessage = self.businessTypeIsNullResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：创建视频记录接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：创建记录失败用例-关联Type为空success返回true！")
            self.assertEqual(actmessage, "视频关联类型为NULL", "video/视频：创建记录失败用例-关联Type为空message返回信息不一致！")
            log.info("video/视频：创建记录失败用例-关联Type为空测试通过！")

    def test_createrecord_businessTypeErr(self):
        """
        video/视频：创建视频记录失败的测试用例-- 关联Type为错误值
        """
        self.businessTypeErrResponse = request.run_main(createrelation["businessTypeErr"], method='POST',
                                                        headers=createrelation["header"], data=CreateRelation.uploadfiledata)
        try:
            actsuccess = self.businessTypeErrResponse.json()["success"]
            actmessage = self.businessTypeErrResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：创建视频记录接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：创建记录失败用例-关联Type为错误值 success返回true！")
            self.assertEqual(actmessage, "参数类型不匹配异常", "video/视频：创建记录失败用例-关联Type为错误值 message返回信息不一致！")
            log.info("video/视频：创建记录失败用例-关联Type为错误值测试通过！")

    def test_createrecord_dataisnull(self):
        """
        video/视频：创建视频记录失败的测试用例-视频列表为空
        """
        self.dataErrResponse = request.run_main(createrelation["textbook_lessonUrl"], method='POST',
                                                headers=createrelation["header"], data=[])
        try:
            actsuccess = self.dataErrResponse.json()["success"]
            actmessage = self.dataErrResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：创建视频记录接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "video/视频：创建视频记录失败用例-视频列表为空success返回true！")
            self.assertEqual(actmessage, "视频列表为空", "video/视频：创建视频记录失败用例-视频列表为空message返回信息不一致！")
            log.info("video/视频：创建视频记录失败用例-视频列表为空测试通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if CreateRelation.recordId != "":
                upload.delete_video_relation(CreateRelation.recordId)
        except Exception as error:
            log.error("video/视频：创建视频记录--删除记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()