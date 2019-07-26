# -*- coding: utf-8 -*-
# #!Date：2019/2/20 16:30
# # !@Author：龚远琪
from histudy import *
from data.teacher.item import *
from data.teacher.itemtype import *

class Item(object):
    def __int__(self):
        pass

    def add_itemType(self):
        """
        新增题型
        """
        addResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                       data=additemtype["body_success"])
        try:
            status_code = addResponse.status_code
            assert status_code == 201, "题型新增失败！"
            log.info("itemtype/题型：新增题型成功！")
            return addResponse
        except AssertionError as error:
            log.error("itemtype/题型：新增题型失败，失败原因："f'{error}')

    def delete_itemtype(self, itemTypeId):
        """
        删除题型
        """
        deleteResponse = request.run_main(deleteitemtype["url"] + str(itemTypeId), method='DELETE',
                                          headers=deleteitemtype["header"], data={})
        try:
            status_code = deleteResponse.status_code
            assert status_code == 204, "题型删除失败！"
            log.info("itemtype/题型：删除题型成功！")
            return deleteResponse
        except AssertionError as error:
            log.error("itemtype/题型：删除题型失败，失败原因："f'{error}')

    def delete_item(self, itemId):
        """
        删除题目
        """
        deleteResponse = request.run_main(deleteitem["url"]+str(itemId), method='DELETE', headers=deleteitem["header"],
                                          data={})
        try:
            actsuccess = deleteResponse.json()["success"]
            assert actsuccess == True, "题目删除失败！"
            log.info("item/题目：删除题目成功！")
            return deleteResponse
        except AssertionError as error:
            log.error("item/题目：删除题目失败，失败原因："f'{error}')


item = Item()