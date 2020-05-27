import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os


class TestAddPaper(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_addpaper.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['paperTextbookTypeId'] = randdata.get_paper_type()
        self.data['request']['json']['subjectId'] = randdata.getsubject()[0]
        self.data['request']['json']['yearId'] = randdata.getyear()
        self.data['request']['json']['schoolYearId'] = randdata.get_school_year()

    def test_addpaper(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'paper/test_addpaper: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('paper/test_addpaper: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
