# -*- coding: utf-8 -*-
# #!Date：2019/2/20 16:30
# # !@Author：龚远琪
from histudy import *
from common.commonmethod import cookie, todict, randdata
from common.commonapi.datadict import dataDict
import os
# from histudy import randMethod
from data.item import *


class Item(object):
    def __int__(self):
        pass

    def delete_item(self, itemId):
        """
        删除题目
        """
        deleteResponse = request.run_main(deleteitem["url"] + str(itemId), method='DELETE',
                                          headers=deleteitem["header"],
                                          data={})
        try:
            actsuccess = deleteResponse.json()["success"]
            assert actsuccess == True, "题目删除失败！"
            log.info("item/题目：删除题目成功！")
            return deleteResponse
        except AssertionError as error:
            log.error("item/题目：删除题目失败，失败原因："f'{error}')

    def get_rand_item(self, item_mould_type="EXPLANATION", subject_id=None):
        """
        数据库随机获取一道题目
        :return:
        """
        try:
            if item_mould_type != None and subject_id == None:
                get_max = "select MAX(id) from at_item where item_mould_type = '" + item_mould_type + "'"
                get_min = "select MIN(id) from at_item where item_mould_type = '" + item_mould_type + "'"
            else:
                get_max = "select MAX(id) from at_item where subject_id = " + str(
                    subject_id) + " and item_type_id in (102,103)"
                get_min = "select MIN(id) from at_item where subject_id = " + str(
                    subject_id) + " and item_type_id in (102,103)"
            get_rand_one = "select * from at_item where id>=((" + get_max + ") - (" + get_min + "))*RAND() + (" + get_min + ") LIMIT 1;"
            rand_item = dao("tr_at", get_rand_one)
            log.info("获取随机题目成功！")
            return rand_item
        except BaseException as error:
            log.error("随机获取题目失败，失败原因："f'{error}')

    def get_rand_item_option(self, limit=4, subject_id=None):
        """
        数据库随机获取选项
        :return:
        """
        try:
            if subject_id == None:
                get_rand_one = "select distinct content from at_item_option LIMIT " + str(
                    randMethod.getNumByRange(2, 1400000)) + "," + str(limit) + ";"
            else:
                get_rand_one = "select distinct content from at_item_option where subject_id = " + str(
                    subject_id) + " LIMIT " + str(randMethod.getNumByRange(2, 101100)) + "," + str(limit) + ";"
            rand_option = dao("tr_at", get_rand_one)
            log.info("获取随机选项成功！")
            return rand_option
        except BaseException as error:
            log.error("随机获取选项失败，失败原因："f'{error}')

    def get_single_choice(self):
        """
        构建一道单选题
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_danxuan.json'))
        data['request']['headers']['Cookie'] = cookie
        data['request']['json']['pointIds'] = dataDict.get_rand_point()
        get_rand_item = self.get_rand_item('SINGLE_CHOICE')
        data['request']['json']['content'] = get_rand_item[0]["content"]
        data['request']['json']['detail'] = get_rand_item[0]["detail"]
        data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        options = self.get_rand_item_option()
        right_option = randMethod.getNumByRange(0, 3)
        i = -1
        for option in options:
            i = i + 1
            data['request']['json']['options'][i]["content"] = option["content"]
            if right_option == i:
                data['request']['json']['options'][i]["answer"] = True
                data['request']['json']['answer'] = data['request']['json']['options'][i]["optionCode"]
            else:
                data['request']['json']['options'][i]["answer"] = False
        return data

    def get_multiple_choice(self):
        """
        构建一道多选题
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_duoxuan.json'))
        data['request']['headers']['Cookie'] = cookie
        data['request']['json']['pointIds'] = dataDict.get_rand_point(5, 100000282)
        data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        get_rand_item = self.get_rand_item('MULTIPLE_CHOICE')
        data['request']['json']['content'] = get_rand_item[0]["content"]
        data['request']['json']['detail'] = get_rand_item[0]["detail"]
        options = self.get_rand_item_option()
        data['request']['json']['answer'] = ''
        i = -1
        j = 0
        for option in options:
            i = i + 1
            data['request']['json']['options'][i]["content"] = option["content"]
            # 如果最后两项且正确答案小于2个
            if randMethod.getNumByRange(0, 1) or i > 1 and j < 2:
                data['request']['json']['options'][i]["answer"] = True
                j = j + 1
                if data['request']['json']['answer'] == '':
                    data['request']['json']['answer'] = data['request']['json']['options'][i]["optionCode"]
                else:
                    data['request']['json']['answer'] = data['request']['json']['answer'] + "," + \
                                                             data['request']['json']['options'][i]["optionCode"]
            else:
                data['request']['json']['options'][i]["answer"] = False
        return data

    def get_explanation(self):
        """
        构建一道解答题
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_jieda.json'))
        data['request']['headers']['Cookie'] = cookie
        data['request']['json']['pointIds'] = dataDict.get_rand_point()
        get_rand_item = self.get_rand_item('EXPLANATION')
        data['request']['json']['content'] = get_rand_item[0]["content"]
        data['request']['json']['detail'] = get_rand_item[0]["detail"]
        data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        return data

    def get_comprehensive(self):
        """
        构建一道复合题
        :return:
        """
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_fuhe.json'))
        data['request']['headers']['Cookie'] = cookie
        data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        get_father_item = self.get_rand_item('COMPREHENSIVE')
        data['request']['json']['content'] = get_father_item[0]["content"]
        data['request']['json']['subItems'] = []
        del_fields = ['province', 'city', 'county', 'schoolId', 'yearCode', 'schoolYearId', 'gradeId', 'semesterId',
                      'paperTextbookTypeId', 'schoolName', 'subjectId', 'periodId', 'source']
        randNum = randMethod.getNumByRange(2, 4)
        for i in range(randNum):
            item_type = randMethod.getNumByRange(1, 4)
            rand_item = {}
            if item_type == 1:
                rand_item = self.get_single_choice()
            elif item_type == 2:
                rand_item = self.get_multiple_choice()
            else:
                rand_item = self.get_explanation()
            # 删除子题中学校信息等
            for field in del_fields:
                rand_item['request']['json'].pop(field)
            data['request']['json']['subItems'].append(rand_item['request']['json'])
        # print(self.data['request']['json']['subItems'])
        return data

    def get_cloze_test(self):
        data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'item_additem_wanxing.json'))
        data['request']['headers']['Cookie'] = cookie
        get_rand_item = item.get_rand_item(None, 6)
        data['request']['json']['content'] = get_rand_item[0]["content"]
        data['request']['json']['diffLevelCode'] = randdata.getdifflevel()
        # 控制子题循环
        for j in range(4):
            data['request']['json']['subItems'][j]['pointIds'] = dataDict.get_rand_point()
            data['request']['json']['subItems'][j]['diffLevelCode'] = randdata.getdifflevel()
            options = []
            options = item.get_rand_item_option(4, 6)
            right_option = randMethod.getNumByRange(0, 3)
            # 控制选项循环
            i = -1
            for option in options:
                i = i + 1
                data['request']['json']['subItems'][j]['options'][i]["content"] = option["content"]
                if right_option == i:
                    data['request']['json']['subItems'][j]['options'][i]["answer"] = True
                    data['request']['json']['subItems'][j]['answer'] = \
                        data['request']['json']['subItems'][j]['options'][i]["optionCode"]
                else:
                    data['request']['json']['subItems'][j]['options'][i]["answer"] = False
        return data


item = Item()
# print(item.get_rand_item(None, 6))
# print(item.get_rand_item_option(3,6))
# print(item.get_single_choice())
# print(item.get_multiple_choice())
# print(item.get_explanation())

