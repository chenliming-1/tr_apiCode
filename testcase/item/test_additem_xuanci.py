import unittest
from common.commonapi import dataDict
from common.commonapi.item import item
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from module import random
import os


class TestAddItemXuanci(unittest.TestCase):
    def get_option(self):
        options = item.get_rand_item_option(randMethod.getNumByRange(2, 11))
        i = -1
        answer = []
        self.data['request']['json']['options'] = []
        single_option = {
            "content": None,
            "optionCode": None
        }
        insert_space = ""
        for option in options:
            i = i + 1
            single_option["content"] = option["content"]
            single_option["optionCode"] = chr(65 + i)
            self.data['request']['json']['options'].append(single_option.copy())
            answer.append(chr(65 + i))
            insert_space = insert_space + '(<abbr class=\\"ql-topic-student-answer\\"></abbr>)'
        # 将列表内元素随机打乱
        random.shuffle(answer)
        # 深复制，修改堆中的内容，指针还指向这里
        self.data['request']['json']['answers'][:] = answer
        self.data['request']['json']['content'] = self.data['request']['json'][
                                                      'content'] + "<p>" + insert_space + "</p>"
        # print(self.data['request']['json']['answers'])
        # print(self.data['request']['json']['options'])
        # print(self.data['request']['json']['content'])

    @classmethod
    def setUpClass(self) -> None:
        self.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_xuanci.json'))
        self.data['request']['headers']['Cookie'] = cookie
        self.data['request']['json']['pointIds'] = dataDict.get_rand_point()
        get_rand_item = item.get_rand_item('EXPLANATION')
        self.data['request']['json']['content'] = get_rand_item[0]["content"]
        self.data['request']['json']['detail'] = get_rand_item[0]["detail"]
        self.get_option(self)
        self.data['request']['json']['diffLevelCode'] = randdata.getdifflevel()

    def test_additem_xuanci(self):
        global res
        try:
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'],
                                   method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'item/test_additem_xuanci: FAIL, error is {error}')
        finally:
            self.assertEqual(201, res.status_code)
            log.info('item/test_additem_xuanci: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
