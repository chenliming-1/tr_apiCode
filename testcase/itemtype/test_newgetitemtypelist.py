import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from data.itemtype import  *
import os
from  histudy import  dao

class TestNewgetitemtypelist(unittest.TestCase):
    @classmethod
    def setUpClass(self) :
        pass

    def test_newgetitemtypelist(self):
        """
        itemType/题型：获取题型列表成功用例
        """
        try:
            self.getItemTypeListResponse= request.run_main(url=getItemTypeListNew["url"],headers=getItemTypeList["header"],method="GET")
            status_code = self.getItemTypeListResponse.status_code
            actdata = self.getItemTypeListResponse.json()
            listlen = len(actdata)  #获取数据数量
            print(listlen)

        except Exception as  error:
            log.error("itemType/题型：获取题型列表接口失败，失败原因："f'{error}')
        finally:
            self.assertEqual(status_code,200,"itemType/题型：获取题型列表成功用例-状态码错误！")
            # sql1 = dao(db="tr_test", sql="""SELECT * FROM item_type   """
            #           )
            sql1 = dao(db="tr_test", sql="""SELECT COUNT(*) as 题型数量 FROM item_type   """
                )
            print(sql1)
            self.assertEqual(sql1[0].get("题型数量"),listlen,"itemType/题型：获取题型列表成功用例-题型数量不一致！")

    @classmethod
    def tearDownClass(self) :
        pass

if __name__ == '__main__':
    unittest.TestCase