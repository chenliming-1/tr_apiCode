import unittest
# from common.commonapi import dataDict
from common.commonapi.item import item
# from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
# import os


class TestAddItemDuoxuan(unittest.TestCase):
    def get_option(self):
        options = item.get_rand_item_option()
        self.data['request']['json']['answer'] = ''
        i = -1
        j = 0
        for option in options:
            i = i + 1
            self.data['request']['json']['options'][i]["content"] = option["content"]
            # 如果最后两项且正确答案小于2个
            if randMethod.getNumByRange(0, 1) or i > 1 and j < 2:
                self.data['request']['json']['options'][i]["answer"] = True
                j = j + 1
                if self.data['request']['json']['answer'] == '':
                    self.data['request']['json']['answer'] = self.data['request']['json']['options'][i]["optionCode"]
                else:
                    self.data['request']['json']['answer'] = self.data['request']['json']['answer'] + "," + \
                                                             self.data['request']['json']['options'][i]["optionCode"]
            else:
                self.data['request']['json']['options'][i]["answer"] = False
        # print(self.data['request']['json']['options'])

    @classmethod
    def setUpClass(self) -> None:
        self.data = item.get_multiple_choice()
        # self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_duoxuan.json'))
        # self.data['request']['headers']['Cookie'] = cookie
        # self.data['request']['json']['pointIds'] = dataDict.get_rand_point(5, 100000282)
        # get_rand_item = item.get_rand_item('MULTIPLE_CHOICE')
        # self.data['request']['json']['content'] = get_rand_item[0]["content"]
        # self.data['request']['json']['detail'] = get_rand_item[0]["detail"]
        # self.get_option(self)
        # self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()

    def test_additem_duoxuan(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_duoxuan: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            self.assertIsNotNone(res.json()["id"])
            log.info('item/test_additem_duoxuan: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
