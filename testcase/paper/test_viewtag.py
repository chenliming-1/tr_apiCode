import unittest
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestViewtag(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_viewtag.json'))
        self.data['request']['headers']['Cookie'] = cookie

    def test_viewtag(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'paper/test_viewtag: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('paper/test_viewtag: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass