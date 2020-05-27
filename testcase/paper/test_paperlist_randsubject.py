import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from module import requests
import os


class TestPaperListRandSubject(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(
            os.path.join(os.path.dirname(__file__), '../../data', 'paper_paperlist_randsubject.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['params']['periodId'] = str(randdata.getperiod()[0])
        self.data['request']['params']['subjectId'] = str(randdata.getsubject()[0])

    def test_paper_list_rand_subject(self):
        global res
        try:
            res = requests.get(url=self.data['request']['url'], headers=self.data['request']['headers'],
                               params=self.data['request']['params'])
        except Exception as error:
            log.info(f'paper/test_paperlist_randsubject: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('paper/test_paperlist_randsubject: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
