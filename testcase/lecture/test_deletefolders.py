import unittest
from common.commonmethod import cookie, todict
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestDeletefolders(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_deletefiles.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data["request"]['json']['ids'] = []
        for i in range(randMethod.getNumByRange(1, 10)):
            new_folders = lecture.add_folders()
            folders_id = new_folders.json()["id"]
            cls.data["request"]['json']['ids'].append(folders_id)

    def test_deletefolders(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_deletefolders: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code)
            log.info('lecture/test_deletefolders: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
