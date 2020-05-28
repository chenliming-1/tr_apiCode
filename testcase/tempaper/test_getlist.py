import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from module import requests
import os


class TestGetList(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'tempaper_getlist.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['params']['periodId'] = randdata.getperiod()[0]
        self.data['request']['params']['subjectId'] = randdata.getsubject()[0]
        self.data['request']['params']['status'] = randdata.get_paper_status()
        # print(self.data['request']['params']['status'])

    def test_getlist(self):
        global res
        try:
            res = requests.get(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               params=self.data['request']['params'])
        except Exception as error:
            log.info(f'tempaper/test_getlist: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('tempaper/test_getlist: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
