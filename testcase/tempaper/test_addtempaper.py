import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import time
import os


class TestAddTemPaper(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'tempaper_addtempaper.json'))
        self.data['request']['headers']['Cookie'] = cookie
        get_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        paper_name = get_time.replace('/', '') + '临时试卷'
        # print(paper_name)
        self.data['request']['json']['name'] = paper_name
        self.data['request']['json']['periodId'] = randdata.getperiod()[0]
        self.data['request']['json']['subjectId'] = randdata.getsubject()[0]

    def test_addtempaper(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'tempaper/test_addtempaper: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('tempaper/test_addtempaper: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
