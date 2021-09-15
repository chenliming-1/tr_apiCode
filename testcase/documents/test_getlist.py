import os
import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
from data.document import *

from histudy import dao

class TestGetlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'documents_getlist.json'))
        cls.data['request']['headers']['Cookie'] = cookie

    def test_getlist(self):
        """
        documents/我的文档：获取我的文档列表数据成功

        """
        global res
        try:
            res = request.run_main(url=getDocumentList["url"],method=getDocumentList["method"],
                                   params=getDocumentList["params"],headers=getDocumentList["headers"])
            print(res.json())
            #请求数据里面的学段和科目id 例：10002 8
            self.DocPeriodid =getDocumentList['params']['periodId']
            self.DocSubjectid=getDocumentList['params']['subjectId']
            #响应数据
            self.GetlistName=res.json()['list'][0]['name']
            self.GetlistRefType=res.json()['list'][0]['directory']
            print("name",self.GetlistName)
            print("directorytype",self.GetlistRefType)

        except Exception as error:
            log.info(f'documents/test_getlist: FAIL, error is {error}')
        finally:
            # 判断有没有文件夹，
            # 如果有文件夹
            # 搜出第一个文件夹的名字
            # 如果没有文件夹
            # 搜出第一个
            if self.GetlistRefType=="true":
                 sql1 = dao(db="tr_test", sql="""SELECT * FROM tr_document_my where period_id= '{}'
                         and subject_id = '{}'  AND create_user = "gongyq"  and ref_type='{}' ORDER BY update_time DESC """.format(self.DocPeriodid,self.DocSubjectid," "))
                 print("文件夹sql",sql1)
            else: # 肯定执行这个
                sql1 = dao(db="tr_test", sql="""SELECT * FROM tr_document_my where period_id= '{}'
                        and subject_id = '{}'  AND create_user = "gongyq"  ORDER BY update_time DESC """.format(
                    self.DocPeriodid, self.DocSubjectid))
                print("文件sql", sql1)
            self.assertEqual(sql1[0]['name'],self.GetlistName)
            log.info('documents/test_getlist: SUCCESS！')


    @classmethod
    def tearDownClass(cls) -> None:
        pass



if __name__ == '__main__':
    unittest.main()

