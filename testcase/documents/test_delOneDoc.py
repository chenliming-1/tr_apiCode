import unittest
from common.commonmethod import cookie, todict, randdata
from histudy import request, randMethod, log
import os
# from .test_addOneDoc import TestAddonedoc

class TestDelonedoc(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'documents_delOneDoc.json'))
        cls.data['request']['headers']['Cookie'] = cookie
        #新建文档
        cls.data1 = todict.data(os.path.join(os.path.dirname(__file__), '../../data', 'documents_addOneDoc.json'))
        cls.data1['request']['headers']['Cookie'] = cookie
        cls.addOneDocResponse = request.run_main(url=cls.data1['request']['url'],headers=cls.data1['request']['headers'], method=cls.data1['request']['method'],
                                   data=cls.data1['request']['json'])
        print(cls.addOneDocResponse.status_code)
        print(cls.addOneDocResponse.json())
        cls.ResId=cls.addOneDocResponse.json()['id']
        print("新建文档的id是：",cls.ResId)


    def test_delOneDoc(self):
        pass
        global res
        try:
            print(self.ResId)
            res = request.run_main(url=self.data['request']['url'], headers=self.data['request']['headers'], method=self.data['request']['method'], data={'ids':[self.ResId]})
        except Exception as error:
            log.info(f'documents/test_delOneDoc: FAIL, error is {error}')
        finally:
            self.assertEqual(204, res.status_code, '接口运行失败！接口：{} 入参：{} 出参：{}'.format(self.data['request']['url'], self.data['request']['json'], res.text))
            log.info('documents/test_delOneDoc: SUCCESS！')

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()