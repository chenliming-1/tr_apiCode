import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os


class TestEditlectureinfo_jiaoan(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(
            os.path.join(os.path.dirname(__file__), '../../data', 'lecture_editlectureinfo_jiaoan.json'))
        cls.data['request']['headers']['Cookie'] = cookie

    def test_editlectureinfo_jiaoan(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_editlectureinfo_jiaoan: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_editlectureinfo_jiaoan: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
