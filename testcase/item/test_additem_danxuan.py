import unittest
from common.commonapi.item import item
from histudy import request, randMethod, log


class TestAddItemDanxuan(unittest.TestCase):
    # def get_option(self):
    #     options = item.get_rand_item_option()
    #     right_option = randMethod.getNumByRange(0, 3)
    #     i = -1
    #     for option in options:
    #         i = i+1
    #         self.data['request']['json']['options'][i]["content"] = option["content"]
    #         if right_option == i:
    #             self.data['request']['json']['options'][i]["answer"] = True
    #             self.data['request']['json']['answer'] = self.data['request']['json']['options'][i]["optionCode"]
    #         else:
    #             self.data['request']['json']['options'][i]["answer"] = False
    #     print(self.data['request']['json']['options'])


    @classmethod
    def setUpClass(self) -> None:
        self.data = item.get_single_choice()
        # self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_danxuan.json'))
        # self.data['request']['headers']['Cookie'] = cookie
        # self.data['request']['json']['pointIds'] = dataDict.get_rand_point()
        # get_rand_item = item.get_rand_item('SINGLE_CHOICE')
        # self.data['request']['json']['content'] = get_rand_item[0]["content"]
        # self.data['request']['json']['detail'] = get_rand_item[0]["detail"]
        # self.get_option(self)
        # self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()


    def test_additem_danxuan(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_danxuan: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            self.assertIsNotNone(res.json()["id"])
            log.info("item/test_additem_danxuan: SUCCESS！")

    @classmethod
    def tearDownClass(cls) -> None:
        pass