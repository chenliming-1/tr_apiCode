import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
from module import requests
import os


class TestStandard_paperlist(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_standard_paperlist.json'))
        self.data['request']['headers']['Cookie'] = cookie

    def test_standard_paperlist(self):
        global res
        try:
            res = requests.get(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               params=self.data['request']['params'])
        except Exception as error:
            log.info(f'paper/test_standard_paperlist: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('paper/test_standard_paperlist: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
