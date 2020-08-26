import unittest
from common.commonmethod import cookie, todict, randdata
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestCopylecture(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lecture_id = []
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_copylecture.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        # cls.data['request']['json']['subjectId'] = str(randdata.getsubject()[0])
        cls.data['request']['json']['name'] = 'AT_copy_' + randMethod.getMessage(4)
        cls.data['request']['json']['productCode'] = randdata.getproductline()
        cls.data['request']['json']['lectureSource'] = randdata.get_lecture_resource()

    def test_copylecture(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
            self.lecture_id.append(res.json()["id"])
        except Exception as error:
            log.info(f'lecture/test_copylecture: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('lecture/test_copylecture: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        if len(cls.lecture_id) != 0:
            lecture.delete_files(cls.lecture_id)
