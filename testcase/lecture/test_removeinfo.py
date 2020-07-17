import unittest
from common.commonmethod import cookie, todict
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestRemoveinfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_removeinfo.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data["request"]['json']['ids'] = []
        for i in range(randMethod.getNumByRange(1, 10)):
            new_folders = lecture.add_folders()
            folders_id = new_folders.json()["id"]
            new_lecture = lecture.add_lecture()
            lecture_id = new_lecture.json()["id"]
            cls.data["request"]['json']['ids'].append(folders_id)
            cls.data["request"]['json']['ids'].append(lecture_id)

    def test_removeinfo(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_removeinfo: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_removeinfo: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        if len(cls.data["request"]['json']['ids']) != 0:
            lecture.delete_files(cls.data["request"]['json']['ids'])
