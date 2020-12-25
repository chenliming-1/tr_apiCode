import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
from common.commonapi.tempaper import tempaper
import os


class TestDeleteTemPaper(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'tempaper_deletetempaper.json'))
        self.data['request']['headers']['Cookie'] = cookie
        add_tempaper = tempaper.add_tempaper()
        tempaper_id = add_tempaper.text
        self.data['name'] = self.data['name'].replace("20200528c23e8cbad3e045d698b0b09de03cd869", tempaper_id)
        self.data['request']['url'] = self.data['request']['url'].replace("20200528c23e8cbad3e045d698b0b09de03cd869",
                                                                          tempaper_id)

    def test_deletetempaper(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'tempaper/test_deletetempaper: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code, "删除临时试卷失败！\n 接口：{} \n 入参：{} \n 出参：{}".format(
                                 self.data['request']['url'], self.data['request']['json'], res.text))
            log.info('tempaper/test_deletetempaper: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
