import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os


class TestSearchfiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_searchfiles.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data['request']['json']['subjectId'] = str(randdata.getsubject()[0])
        cls.data['request']['json']['pageSize'] = randMethod.getNumByRange(5, 100)
        cls.data['request']['json']['productCode'] = randdata.getproductline()

    def test_searchfiles(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], params=self.data['request']['params'])
        except Exception as error:
            log.info(f'lecture/test_searchfiles: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_searchfiles: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
