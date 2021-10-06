import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os


class TestGetidlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'trolley_getidlist.json'))
        cls.data['request']['headers']['Cookie'] = cookie

    def test_getidlist(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'trolley/test_getidlist: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code, '接口运行失败！接口：{} 入参：{}出参：{}'.format(self.data['request']['url'], self.data['request']['json'], res.text))
            log.info('trolley/test_getidlist: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()