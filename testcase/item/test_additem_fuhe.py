import unittest
# from common.commonmethod import cookie, todict, randdata
from common.commonapi.item import item
from histudy import request, randMethod, log
# import os


class TestAddItemFuhe(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.data = item.get_comprehensive()
        # self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_fuhe.json'))
        # self.data['request']['headers']['Cookie'] = cookie
        # self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        # get_father_item = item.get_rand_item('COMPREHENSIVE')
        # self.data['request']['json']['content'] = get_father_item[0]["content"]
        # self.data['request']['json']['subItems'] = []
        # del_fields = ['province', 'city', 'county', 'schoolId', 'yearCode', 'schoolYearId', 'gradeId', 'semesterId',
        #              'paperTextbookTypeId', 'schoolName', 'subjectId', 'periodId', 'source']
        # randNum = randMethod.getNumByRange(2, 4)
        # print(randNum)
        # for i in range(randNum):
        #     item_type = randMethod.getNumByRange(1, 4)
        #     rand_item = {}
        #     if item_type == 1:
        #         rand_item = item.get_single_choice()
        #     elif item_type == 2:
        #         rand_item = item.get_multiple_choice()
        #     else:
        #         rand_item = item.get_explanation()
        #     # 删除子题中学校信息等
        #     for field in del_fields:
        #         rand_item['request']['json'].pop(field)
        #     self.data['request']['json']['subItems'].append(rand_item['request']['json'])
        # print(self.data['request']['json']['subItems'])

    def test_additem_fuhe(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_fuhe: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('item/test_additem_fuhe: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
