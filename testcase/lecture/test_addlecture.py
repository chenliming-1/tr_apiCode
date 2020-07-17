import unittest
from common.commonmethod import cookie, todict, randdata
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os
import warnings


class TestAddLecture(unittest.TestCase):
    folders_id = []

    @classmethod
    def setUpClass(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_addlecture.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['subjectId'] = str(randdata.getsubject()[0])
        self.data['request']['json']['name'] = 'AT_' + randMethod.getMessage(6)
        self.data['request']['json']['productCode'] = randdata.getproductline()

    def test_addlecture(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
            TestAddLecture.folders_id.append(res.json()["id"])
        except Exception as error:
            log.info(f'lecture/test_addlecture: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('lecture/test_addlecture: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        if len(TestAddLecture.folders_id) != 0:
            lecture.delete_files(TestAddLecture.folders_id)
