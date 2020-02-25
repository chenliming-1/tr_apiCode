# -*- encoding: utf-8 -*-
# @ModuleName: getpointtree.py
# @Author：龚远琪
# @Date：2020/2/24 17:17
from common.commonapi.datadict import *
from data.teacher.point import *


class GetPointTree(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.getPointTreeResponse = {}

    def test_getPointTree(self):
        """
        point/知识点：SUCCESS-获取知识树
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["body_success"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actdata = self.getPointTreeResponse.json()["data"]
        except Exception as error:
            log.error("point/知识点：SUCCESS-获取知识树》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "point/知识点：SUCCESS-获取知识树-状态码错误！")
            self.assertNotEqual(0, len(actdata["list"]), "point/知识点：SUCCESS-获取知识树-返回列表为空！")
            log.info("point/知识点：SUCCESS-获取知识树》测试通过！")

    def test_listIsNone(self):
        """
        point/知识点：SUCCESS-输入科目学段查询出空列表
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["listIsNone"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actdata = self.getPointTreeResponse.json()["data"]
        except Exception as error:
            log.error("point/知识点：SUCCESS-输入科目学段查询出空列表》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "point/知识点：SUCCESS-输入科目学段查询出空列表-状态码错误！")
            self.assertEqual(0, len(actdata["list"]), "point/知识点：SUCCESS-输入科目学段查询出空列表-返回列表不为空！")
            log.info("point/知识点：SUCCESS-输入科目学段查询出空列表》测试通过！")

    def test_subjectError(self):
        """
        point/知识点：SUCCESS-科目不存在，列表返回空
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["subjectError"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actdata = self.getPointTreeResponse.json()["data"]
        except Exception as error:
            log.error("point/知识点：SUCCESS-科目不存在，列表返回空》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "point/知识点：SUCCESS-科目不存在，列表返回空-状态码错误！")
            self.assertEqual(0, len(actdata["list"]), "point/知识点：SUCCESS-科目不存在，列表返回空-返回列表不为空！")
            log.info("point/知识点：SUCCESS-科目不存在，列表返回空》测试通过！")
            
    def test_subjectIsNone(self):
        """
        point/知识点：FAIL-未填写科目
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["subjectIsNone"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actmessage = self.getPointTreeResponse.json()["message"]
        except Exception as error:
            log.error("point/知识点：FAIL-未填写科目》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "point/知识点：FAIL-未填写科目-状态码错误！")
            self.assertEqual("科目id为空", actmessage, "point/知识点：FAIL-未填写科目-message返回信息不一致！")
            log.info("point/知识点：FAIL-未填写科目》测试通过！")

    def test_periodIsNone(self):
        """
        point/知识点：FAIL-未填写学段
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["periodIsNone"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actmessage = self.getPointTreeResponse.json()["message"]
        except Exception as error:
            log.error("point/知识点：FAIL-未填写学段》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "point/知识点：FAIL-未填写学段-状态码错误！")
            self.assertEqual("学段id为空", actmessage, "point/知识点：FAIL-未填写学段-message返回信息不一致！")
            log.info("point/知识点：FAIL-未填写学段》测试通过！")

    def test_regionIsNone(self):
        """
        point/知识点：FAIL-未填写地区
        """
        self.getPointTreeResponse = request.run_main(getPointTree["url"], method='POST', headers=getPointTree["header"],
                                                     data=getPointTree["regionIsNone"])
        try:
            status_code = self.getPointTreeResponse.status_code
            actmessage = self.getPointTreeResponse.json()["message"]
        except Exception as error:
            log.error("point/知识点：FAIL-未填写地区》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "point/知识点：FAIL-未填写地区-状态码错误！")
            self.assertEqual("地区id为空", actmessage, "point/知识点：FAIL-未填写地区-message返回信息不一致！")
            log.info("point/知识点：FAIL-未填写地区》测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
