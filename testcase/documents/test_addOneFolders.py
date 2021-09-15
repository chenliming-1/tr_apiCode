import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os
from histudy import dao
from data import  *

class TestAddonefolders(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'documents_addOneFolders.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        cls.DocPeriodid =cls. data['request']['json']['periodId']
        cls.DocSubjectid = cls.data['request']['json']['subjectId']
        cls.DocParentid = cls.data['request']['json']['parentId']


    def test_addOneFolders(self):
        global addOneFolders
        try:
            self.addOneFolders = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data=self.data['request']['json'])
        except Exception as error:
            log.info(f'documents/test_addOneFolders: FAIL, error is {error}')
        finally:
            self.assertEqual(201, self.addOneFolders.status_code, '接口运行失败！,接口：{} ,入参：{} ,出参：{}'
                             .format(self.data['request']['url'], self.data['request']['json'], self.addOneFolders.text))
            log.info('documents/test_addOneFolders: SUCCESS！')


    @classmethod
    def tearDownClass(cls) -> None:
        try:
            sql1 = dao(db="tr_test", sql="""SELECT * FROM tr_document_my where period_id= '{}'
                                                 and subject_id = '{}'  AND create_user = "gongyq"  and ref_type='{}' ORDER BY update_time DESC """
                       .format(cls.DocPeriodid, cls.DocSubjectid, " "))
            if len(sql1) != 0:
                print("执行删除新增的第一条文档")
                sql2 = dao(db="tr_test", sql="""DELETE FROM tr_document_my WHERE period_id= '{}'  
                                and subject_id = '{}' AND create_user = "gongyq" AND ref_type = " " ORDER BY update_time DESC LIMIT 1  """
                           .format(cls.DocPeriodid, cls.DocSubjectid)
                           )
            else:
                print("不删除任何文档")
        except Exception as error:
            log.error("test_addOneDoc/文档类型类型：删除新建的第一条文档数据，失败原因："f'{error}')



if __name__ == '__main__':
    unittest.main()