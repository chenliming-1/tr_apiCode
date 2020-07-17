import unittest
from common.commonmethod import cookie, todict
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestEditFolders(unittest.TestCase):
    folders_id = []

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_editfolders.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        new_folders = lecture.add_folders()
        TestEditFolders.folders_id.append(new_folders.json()["id"])
        cls.data["request"]["url"] = cls.data["request"]["url"].replace('2326', str(TestEditFolders.folders_id[0]))
        cls.data['name'] = cls.data["name"].replace('2326', str(TestEditFolders.folders_id[0]))
        cls.data["request"]["json"]["name"] = 'AT_' + randMethod.getMessage(6)

    def test_editfolders(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'lecture/test_editfolders: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('lecture/test_editfolders: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        if len(TestEditFolders.folders_id) != 0:
            lecture.delete_files(TestEditFolders.folders_id)
