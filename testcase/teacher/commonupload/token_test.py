# -*- coding: utf-8 -*-
# #!Date：2019/2/14 11:30
# # !@Author：龚远琪
from histudy import *
from data.teacher.commonupload import *
from module import *


class Token(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tokenResponse = {}

    def test_token_success(self):
        """
        commonupload/通用上传：获取token接口成功的测试用例
        """
        self.tokenResponse = request.run_main(token["url"], method='GET', headers=token["header"])
        try:
            actsuccess = self.tokenResponse.json()["success"]
            actdata = self.tokenResponse.json()["data"]
            actmessage = self.tokenResponse.json()["message"]
        except Exception as error:
            log.error("commonupload/通用上传：获取token接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "commonupload/通用上传-token:success为false！")
            self.assertIsNotNone(actdata, "commonupload/通用上传-token：返回data为空！")
            self.assertEqual(actmessage, "查询成功", "message对比失败！")
            log.info("commonupload/通用上传：获取token成功用例测试通过！")

    def test_token_fail(self):
        """
        commonupload/通用上传：获取token接口失败的测试用例
        """
        self.tokenResponse = request.run_main(token["url"], method='POST', headers=token["header"])
        try:
            status = self.tokenResponse.json()["status"]
            actsuccess = self.tokenResponse.json()["message"]
        except Exception as error:
            log.error("commonupload/通用上传：获取token接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status, "commonupload/通用上传-token-状态码错误！")
            self.assertEqual("请求方法不支持", actsuccess, "commonupload/通用上传-token:message返回不一致！")
            log.info("commonupload/通用上传：获取token失败用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()