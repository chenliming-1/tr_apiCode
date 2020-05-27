import unittest
from common.commonapi.paper import paper
from common.commonmethod import cookie, todict
from histudy import request, randMethod, log
import os


class TestEnable(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_enable.json'))
        self.data['request']['headers']['Cookie'] = cookie
        add_paper = paper.create_paper()
        paper_id = add_paper.text
        self.data['name'] = self.data['name'].replace('201908169fb1aba57e1a407b8c9dea34eb33336b', str(paper_id))
        self.data['request']['url'] = self.data['request']['url'].replace('201908169fb1aba57e1a407b8c9dea34eb33336b',
                                                                          str(paper_id))

    def test_enable(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'paper/test_enable: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code)
            log.info('paper/test_enable: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
