# -*- coding: utf-8 -*-
# #!Date：2019/2/21 20:31
# # !@Author：龚远琪
from histudy import *
from data.teacher.video import *
from module import *


class Sign(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.signResponse = {}

    def test_sign_success(self):
        """
        video/视频：获取视频上传的签名成功的测试用例
        """
        self.signResponse = request.run_main(sign["url"], method='GET', headers=sign["header"])
        try:
            actsuccess = self.signResponse.json()["success"]
            actdata = self.signResponse.json()["data"]
            actmessage = self.signResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：获取视频上传的签名接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：获取视频上传的签名success返回false！")
            self.assertIsNotNone(actdata, "video/视频：获取视频上传的签名返回data为空！")
            self.assertEqual(actmessage, "操作成功！", "message对比失败！")
            log.info("video/视频：获取视频上传的签名成功用例测试通过！")

    def test_sign_fail(self):
        """
        video/视频：获取视频上传的签名失败的测试用例
        """
        self.signResponse = request.run_main(sign["url"], method='POST', headers=sign["header"])
        try:
            status_code = self.signResponse.status_code
            actmessage = self.signResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：获取视频上传的签名接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "video/视频：获取视频上传的签名失败用例-状态码错误！")
            self.assertEqual(actmessage, "请求方法不支持", "video/视频：获取视频上传的签名失败用例message返回信息不一致！")
            log.info("video/视频：获取视频上传的签名失败用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()