import unittest
from common.commonapi.item import item
from histudy import request, randMethod, log


class TestAddItemJieda(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = item.get_explanation()
        # self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_jieda.json'))
        # self.data['request']['headers']['Cookie'] = cookie
        # self.data['request']['json']['pointIds'] = dataDict.get_rand_point()
        # get_rand_item = item.get_rand_item('EXPLANATION')
        # self.data['request']['json']['content'] = get_rand_item[0]["content"]
        # self.data['request']['json']['detail'] = get_rand_item[0]["detail"]
        # self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()

    def test_additem_jieda(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_jieda: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('item/test_additem_jieda: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass