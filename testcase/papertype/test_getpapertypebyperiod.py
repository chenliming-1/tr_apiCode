# -*- encoding: utf-8 -*-
# @ModuleName: getpapertypebyperiod
# @Author：龚远琪
# @Date：2019/11/5 16:57
from common.commonmethod import *
from common.commonapi.datadict import *


class GetPaperTypeByPeriod(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.getPaperTypeByPeriodResponse = {}

    def test_getPaperTypeByPeriod(self):
        """
        paperType/学段获取套卷类型：SUCCESS-获取套卷类型详情
        """
        self.getPaperTypeByPeriodResponse = request.run_main(getPaperTypeByPeriod["url"] + str(randdata.getperiod()[0]),
                                                             method='GET', headers=getPaperTypeByPeriod["header"])
        try:
            status_code = self.getPaperTypeByPeriodResponse.status_code
            actdata = self.getPaperTypeByPeriodResponse.json()
        except Exception as error:
            log.error("paperType/学段获取套卷类型：SUCCESS-获取套卷类型详情》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/学段获取套卷类型：SUCCESS-获取套卷类型详情-状态码错误！")
            self.assertLessEqual(1, len(actdata), "paperType/学段获取套卷类型：SUCCESS-获取套卷类型详情-返回数据大小不一致！")
            log.info("paperType/学段获取套卷类型：SUCCESS-获取套卷类型详情》测试通过！")

    def test_getPaperTypeIdErr(self):
        """
        paperType/学段获取套卷类型：FAIL-输入不存在的学段ID
        """
        self.getPaperTypeByPeriodResponse = request.run_main(getPaperTypeByPeriod["url"] + str(10005), method='GET',
                                                             headers=getPaperTypeByPeriod["header"])
        try:
            status_code = self.getPaperTypeByPeriodResponse.status_code
            actdata = self.getPaperTypeByPeriodResponse.json()
        except Exception as error:
            log.error("paperType/学段获取套卷类型：FAIL-输入不存在的学段ID》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(200, status_code, "paperType/学段获取套卷类型：FAIL-输入不存在的学段ID-状态码错误！")
            self.assertEqual(0, len(actdata), "paperType/学段获取套卷类型：FAIL-输入不存在的学段ID-获取的列表不为空！")
            log.info("paperType/学段获取套卷类型：FAIL-输入不存在的学段ID》测试通过！")

    def test_getPaperTypeIdNone(self):
        """
        paperType/学段获取套卷类型：FAIL-未输入学段ID
        """
        self.getPaperTypeByPeriodResponse = request.run_main(getPaperTypeByPeriod["url"], method='GET',
                                                             headers=getPaperTypeByPeriod["header"])
        try:
            status_code = self.getPaperTypeByPeriodResponse.status_code
            actmessage = self.getPaperTypeByPeriodResponse.json()["message"]
        except Exception as error:
            log.error("paperType/学段获取套卷类型：FAIL-未输入学段ID》接口调用失败，失败原因："f'{error}')
        finally:
            self.assertEqual(400, status_code, "paperType/学段获取套卷类型：FAIL-未输入学段ID-状态码错误！")
            self.assertEqual("参数类型不匹配异常", actmessage, "paperType/学段获取套卷类型：FAIL-未输入学段ID-返回message不一致！")
            log.info("paperType/学段获取套卷类型：FAIL-未输入学段ID》测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
