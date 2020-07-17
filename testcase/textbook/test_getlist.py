import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestGetlist(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'textbook_getlist.json'))
        self.data['request']['headers']['Cookie'] = cookie

    def test_getlist(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'textbook/test_getlist: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('textbook/test_getlist: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass