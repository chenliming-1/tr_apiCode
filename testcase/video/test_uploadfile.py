# -*- coding: utf-8 -*-
# #!Date：2019/2/22 14:06
# # !@Author：龚远琪
from histudy import *
from data.video import *
from common.commonmethod import *
from module import *


class UploadFile(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.uploadfileResponse = {}

    def test_uploadfile_success(self):
        """
        video/视频：视频上传成功的测试用例
        """
        self.uploadfileResponse = request.run_main(uploadfile["url"], method='POST', headers=uploadfile["header"],
                                              data=uploadfile[env+"_body_success"][0])
        try:
            actsuccess = self.uploadfileResponse.json()["success"]
            actdata = self.uploadfileResponse.json()["data"][0]
        except Exception as error:
            log.error("video/视频：视频上传接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：视频上传success返回false！")
            self.assertFalse(actdata["defaultShow"], "video/视频：视频上传defaultShow返回True!")
            self.assertEqual(actdata["fileName"], uploadfile[env+"_body_success"][0][0]["fileName"],
                             "video/视频：视频上传名称不一致！")
            self.assertEqual(actdata["sourceType"], "dingdang", "video/视频：视频上传类型错误！")
            self.assertEqual(actdata["statusCode"], 1, "video/视频：视频上传状态返回错误！")
            self.assertEqual(actdata["videoName"], uploadfile[env+"_body_success"][0][0]["aliasName"],
                             "video/视频：视频上传名称不一致！")
            self.assertIsNotNone(actdata["videoNo"], "video/视频：视频上传videoNo返回为空！")
            log.info("video/视频：视频上传成功用例测试通过！")

    def test_uploadfile_typeisnull(self):
        """
        video/视频：视频上传失败的测试用例-type为NULL
        """
        self.uploadfileResponse = request.run_main(uploadfile["url"], method='POST', headers=uploadfile["header"],
                                                    data=uploadfile["body_typeError"][0])
        try:
            status_code = self.uploadfileResponse.status_code
            actmessage = self.uploadfileResponse.json()["message"]
            # print(self.uploadfileResponse.json())
        except Exception as error:
            log.error("video/视频：视频上传失败的测试用例-type为NULL接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 500, "video/视频：视频上传失败的测试用例-type为NULL-状态码错误！")
            self.assertEqual(actmessage, "视频上传失败,操作失败,请稍后重试", "video/视频：视频上传失败的测试用例-type为NULL message返回信息不一致！")
            log.info("video/视频：视频上传失败用例-type为NULL测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()