import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from module import requests
import os


class TestGetfolderstree(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_getfolderstree.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data['request']['params']['periodId'] = str(randdata.getperiod()[0])
        cls.data['request']['params']['subjectId'] = str(randdata.getsubject()[0])

    def test_getfolderstree(self):
        global res
        try:
            res = requests.get(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               params=self.data['request']['params'])
        except Exception as error:
            log.info(f'lecture/test_getfolderstree: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_getfolderstree: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
