import unittest
from common.commonmethod import cookie, todict, randdata
from common.commonapi.item import item
from histudy import request, randMethod, log
import os


class TestEditItem(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_edititem.json'))
        self.data['request']['headers']['Cookie'] = cookie
        get_rand_item = item.get_rand_item("COMPREHENSIVE")
        self.data['request']['json']['content'] = get_rand_item[0]['content']
        self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()

    def test_edititem(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_edititem: FAIL, error is {error}')
        finally:
            self.assertEqual(200, res.status_code)
            log.info('item/test_edititem: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass