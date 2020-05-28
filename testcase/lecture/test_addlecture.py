import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log, randMethod
import os


class TestAddLecture(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_addlecture.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['subjectId'] = randdata.getsubject()[0]
        self.data['request']['json']['name'] = 'AT_' + randMethod.getChinese(4)
        self.data['request']['json']['courseTypeId'] = randdata.get_course_type()
        self.data['request']['json']['productCode'] = randdata.getproductline()

    def test_addlecture(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_addlecture: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_addlecture: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
