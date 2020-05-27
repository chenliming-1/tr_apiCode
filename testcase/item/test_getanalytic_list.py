import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestGetAnalyticList(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_getanalytic_list.json'))
        self.data['request']['headers']['Cookie'] = cookie

    def test_getanalytic_list(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_getanalytic_list: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('item/test_getanalytic_list: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass