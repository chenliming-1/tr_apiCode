# -*- coding: utf-8 -*-
# #!Date：2019/2/20 16:30
# # !@Author：龚远琪
from histudy import *
from data.teacher.item import *


class Item(object):
    def __int__(self):
        pass

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