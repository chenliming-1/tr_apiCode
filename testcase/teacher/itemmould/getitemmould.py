# -*- coding: utf-8 -*-
# #!Date：2019/7/8 17:35
# # !@Author：龚远琪
from histudy import *
from module import *
from data.teacher.datadict import *


class GetItemMould(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.getmouldResponse = {}

    def test_getitemmould_success(self):
        """
        itemmould/题型模版：获取题型模版成功用例
        """
        self.getmouldResponse = request.run_main(getitemmould["url"], method='GET', headers=getitemmould["header"],
                                                 data={})
        try:
            status_code = self.getmouldResponse.status_code
            actdata = self.getmouldResponse.json()
        except Exception as error:
            log.error("itemmould/题型模版：获取题型模版接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 200, "itemmould/题型模版：获取题型模版成功用例-状态码错误！")
            self.assertIsNotNone(actdata,"itemmould/题型模版：获取题型模版返回列表失败！")
            log.info("itemmould/题型模版：获取题型模版成功用例测试通过！")

    def test_getitemmould_fail(self):
        """
        itemmould/题型模版：获取题型模版失败用例
        """
        self.getmouldResponse = request.run_main(getitemmould["url"], method='POST', headers=getitemmould["header"],
                                                 data={})
        try:
            status_code = self.getmouldResponse.status_code
            actmessage = self.getmouldResponse.json()["message"]
        except Exception as error:
            log.error("itemmould/题型模版：获取题型模版接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "itemmould/题型模版：获取题型模版失败用例-状态码错误！")
            self.assertEqual(actmessage, "请求方法不支持", "itemmould/题型模版：获取题型模版message不一致！")
            log.info("itemmould/题型模版：获取题型模版失败用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()