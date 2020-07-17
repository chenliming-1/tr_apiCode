import unittest
from common.commonmethod import cookie, todict
from common.commonapi.lecture import lecture
from histudy import request, randMethod, log
import os


class TestAddFolders(unittest.TestCase):
    # folders_id = []

    @classmethod
    def setUpClass(cls):
        cls.folders_id = []
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'lecture_addfolders.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.data['request']['json']['name'] = 'AT_' + randMethod.getMessage(5)

    def test_addfolders(self):
        # global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
            self.folders_id.append(res.json()["id"])
        except Exception as error:
            log.info(f'lecture/test_addfolders: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            self.assertEqual(self.data['request']['json']['name'], res.json()["name"], "文件名称不一致！")
            log.info('lecture/test_addfolders: SUCCESS！')

    @classmethod
    def tearDownClass(cls):
        # pass
        if len(cls.folders_id) != 0:
            lecture.delete_files(TestAddFolders.folders_id)

