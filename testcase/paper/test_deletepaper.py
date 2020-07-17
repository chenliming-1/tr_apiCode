import unittest
from common.commonapi.paper import paper
from common.commonmethod import cookie, todict
from histudy import request, log
import os


class TestDelete(unittest.TestCase):
    def getURL(self, delete_url, delete_id):
        url_list = delete_url.split('/')
        url_list.pop()
        url_list.append(delete_id)
        delete_url = "/".join(url_list)
        # print(delete_url)
        return delete_url

    @classmethod
    def setUpClass(self) -> None:
        add_paper = paper.create_paper()
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'paper_deletepaper.json'))
        self.data['request']['headers']['Cookie'] = cookie
        paper_id = add_paper.text
        self.data['name'] = self.getURL(self, self.data['name'], paper_id)
        self.data['request']['url'] = self.getURL(self, self.data['request']['url'], paper_id)

    def test_delete(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'paper/test_delete: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code)
            log.info('paper/test_delete: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()