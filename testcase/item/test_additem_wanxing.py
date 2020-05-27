import unittest
from common.commonapi.item import item
from histudy import request, randMethod, log


class TestAddItemWanxing(unittest.TestCase):
    # def get_subItems(self):
    #     # 控制子题循环
    #     for j in range(4):
    #         options = []
    #         options = item.get_rand_item_option(4, 6)
    #         right_option = randMethod.getNumByRange(0, 3)
    #         self.data['request']['json']['subItems'][j]['pointIds'] = dataDict.get_rand_point()
    #         self.data['request']['json']['subItems'][j]['diffLevelCode'] = randdata.getdifflevel()
    #         # 控制选项循环
    #         i = -1
    #         for option in options:
    #             i = i + 1
    #             self.data['request']['json']['subItems'][j]['options'][i]["content"] = option["content"]
    #             if right_option == i:
    #                 self.data['request']['json']['subItems'][j]['options'][i]["answer"] = True
    #                 self.data['request']['json']['subItems'][j]['answer'] = \
    #                 self.data['request']['json']['subItems'][j]['options'][i]["optionCode"]
    #             else:
    #                 self.data['request']['json']['subItems'][j]['options'][i]["answer"] = False
    #     print(self.data['request']['json']['subItems'])

    @classmethod
    def setUpClass(self) -> None:
        self.data = item.get_cloze_test()
        # self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_wanxing.json'))
        # self.data['request']['headers']['Cookie'] = cookie
        # get_rand_item = item.get_rand_item(None, 6)
        # self.data['request']['json']['content'] = get_rand_item[0]["content"]
        # self.get_subItems(self)
        # self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()

    def test_additem_wanxing(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_wanxing: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('item/test_additem_wanxing: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
