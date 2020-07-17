import unittest
from common.commonmethod import cookie, todict
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestMovefile(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_movefile.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data["request"]['json']['sourceIds'] = []
        for i in range(randMethod.getNumByRange(1, 10)):
            new_folders = lecture.add_folders()
            folders_id = new_folders.json()["id"]
            new_lecture = lecture.add_lecture()
            lecture_id = new_lecture.json()["id"]
            cls.data["request"]['json']['sourceIds'].append(folders_id)
            cls.data["request"]['json']['sourceIds'].append(lecture_id)
        target_id = lecture.get_rand_folder()
        while target_id in cls.data["request"]['json']['sourceIds']:
            target_id = lecture.get_rand_folder()
        cls.data["request"]['json']['targetId'] = target_id

    def test_movefile(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_movefile: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code)
            log.info('lecture/test_movefile: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        if len(cls.data["request"]['json']['sourceIds']) != 0:
            lecture.delete_files(cls.data["request"]['json']['sourceIds'])
