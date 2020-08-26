import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, log, randMethod
from module import requests
import os


class TestGetFileList(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_getfilelist.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data['request']['json']['subjectId'] = str(randdata.getsubject()[0])
        cls.data['request']['json']['periodId'] = str(randdata.getperiod()[0])
        cls.data['request']['json']['pageSize'] = randMethod.getNumByRange(5, 100)

    def test_getfilelist(self):
        global res
        try:
            # res = requests.get(url=self.data['request']['url'], headers=self.data['request']['headers'],
            #                    params=self.data['request']['params'])
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], params=self.data['request']['params'])
        except Exception as error:
            log.info(f'lecture/test_getfilelist: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_getfilelist: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
