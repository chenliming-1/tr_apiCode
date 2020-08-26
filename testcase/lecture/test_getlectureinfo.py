import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestGetlectureinfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_getlectureinfo.json'))
        cls.data['request']['headers']['Cookie'] = cookie

    def test_getlectureinfo(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'])
        except Exception as error:
            log.info(f'lecture/test_getlectureinfo: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_getlectureinfo: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
