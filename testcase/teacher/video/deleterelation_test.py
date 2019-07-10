# -*- coding: utf-8 -*-
# #!Date：2019/3/4 15:11
# # !@Author：龚远琪
from common.commonapi.upload import *
from module import *


class DeleteRelation(unittest.TestCase):
    relationId = ""

    @classmethod
    def setUpClass(self):
        self.addrelationResponse = {}
        try:
            self.addrelationResponse, self.relationId = upload.createRelation()
        except Exception as error:
            log.error("video/视频：创建视频关联记录失败，失败原因："f'{error}')

    def test_delete_success(self):
        """
        video/视频：删除视频关联记录成功用例
        """
        self.deleteResponse = request.run_main(deleterelation["url"]+str(self.relationId), method='DELETE',
                                               headers=createrelation["header"], data={})
        try:
            actsuccess = self.deleteResponse.json()["success"]
            actmessage = self.deleteResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：删除视频关联记录接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "video/视频：删除视频关联记录success返回false！")
            self.assertEqual(actmessage, "删除成功", "video/视频：删除视频关联记录message返回信息不一致！")
            log.info("video/视频：删除视频关联记录成功用例测试通过！")

    def test_delete_relationIdIsNull(self):
        """
        video/视频：删除视频关联记录失败用例--Id为空
        """
        self.deleteResponse = request.run_main(deleterelation["url"]+"NULL", method='DELETE',
                                               headers=createrelation["header"], data={})
        try:
            status_code = self.deleteResponse.status_code
            actmessage = self.deleteResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：删除视频关联记录接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "video/视频：删除视频关联记录-状态码错误！")
            self.assertEqual(actmessage, "参数类型不匹配异常", "video/视频：删除视频关联记录message返回信息不一致！")
            log.info("video/视频：删除视频关联记录失败用例测试通过！")

    def test_delete_relationIdErr(self):
        """
        video/视频：删除视频关联记录失败用例--Id不存在
        """
        self.deleteResponse = request.run_main(deleterelation["url"]+"30", method='DELETE',
                                               headers=createrelation["header"], data={})
        try:
            status_code = self.deleteResponse.status_code
            actmessage = self.deleteResponse.json()["message"]
        except Exception as error:
            log.error("video/视频：删除视频关联记录接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code, 400, "video/视频：删除视频关联记录-状态码错误！")
            self.assertEqual(actmessage, "找不到视频关联记录！", "video/视频：删除视频关联记录message返回信息不一致！")
            log.info("video/视频：删除视频关联记录失败用例测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()