import unittest
from common.commonapi.paper import paper
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestOffShelf(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_offshelf.json'))
        self.data['request']['headers']['Cookie'] = cookie
        add_paper = paper.create_paper()
        paper_id = add_paper.text
        paper.enable_paper(paper_id)
        self.data['name'] = self.data['name'].replace('20200408b4bfc01a33a6462ea3b6a250b59e25bc', str(paper_id))
        self.data['request']['url'] = self.data['request']['url'].replace('20200408b4bfc01a33a6462ea3b6a250b59e25bc',
                                                                          str(paper_id))

    def test_offshelf(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'paper/test_offshelf: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code)
            log.info('paper/test_offshelf: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
