# -*- coding: utf-8 -*-
# #!Date：2019/4/24 16:26
# # !@Author：龚远琪
from common.commonapi.item import *
from common.commonapi.upload import *
from data.explanation import *
from module import *

class InsertExplanation(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        InsertExplanation.insertId = []
        imageresponse1, imageurl1 = upload.upload_image()
        imageresponse2, imageurl2 = upload.upload_image()
        imageresponse3, imageurl3 = upload.upload_image()
        insertexplanation["picturebody"]["itemContent"]["content"] = insertexplanation["picturebody"]["itemContent"]["content"] + imageurl1 + "</p>"
        insertexplanation["picturebody"]["itemAnswer"]["answer"] = insertexplanation["picturebody"]["itemAnswer"]["answer"] + imageurl2 + "</p>"
        insertexplanation["picturebody"]["itemDetail"]["detail"] = insertexplanation["picturebody"]["itemDetail"]["detail"] + imageurl3 + "</p>"
        # audioreponse = upload.upload_audio()
        # insertexplanation["audiobody"]["audios"][0] = audioreponse.json()["data"]

    def test_insertwithword(self):
        """
        explanation/解答题：插入文字的解答题测试用例
        """
        self.insertWordResponse = request.run_main(insertexplanation["url"], method='POST', headers=insertexplanation["header"],
                                                   data=insertexplanation["wordbody"])
        try:
            actsuccess = self.insertWordResponse.json()["success"]
            actdata = self.insertWordResponse.json()["data"]
            if actdata["id"] != "":
                InsertExplanation.insertId.append(actdata["id"])
            actmessage = self.insertWordResponse.json()["message"]
        except Exception as error:
            log.error("explanation/解答题：插入文字的解答题测试用例失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "explanation/解答题：插入文字的解答题success返回false！")
            self.assertEqual(actdata["answer"], insertexplanation["wordbody"]["itemAnswer"]["answer"],
                             "explanation/解答题：插入文字的解答题answer不一致！")
            self.assertEqual(actdata["diffLevelCode"], insertexplanation["wordbody"]["diffLevelCode"],
                             "explanation/解答题：插入文字的解答题diffLevelCode不一致！")
            self.assertEqual(actdata["duration"], insertexplanation["wordbody"]["duration"],
                             "explanation/解答题：插入文字的解答题duration不一致！")
            self.assertIsNotNone(actdata["id"], "explanation/解答题：插入文字的解答题返回ID为空！")
            self.assertEqual(actdata["itemAnswer"]["answer"], insertexplanation["wordbody"]["itemAnswer"]["answer"],
                             "explanation/解答题：插入文字的解答题itemAnswer不一致！")
            self.assertEqual(actdata["itemContent"]["content"], insertexplanation["wordbody"]["itemContent"]["content"],
                             "explanation/解答题：插入文字的解答题itemContent不一致！")
            self.assertEqual(actdata["itemDetail"]["detail"], insertexplanation["wordbody"]["itemDetail"]["detail"],
                             "explanation/解答题：插入文字的解答题itemDetail不一致！")
            self.assertEqual(actdata["periodId"], insertexplanation["wordbody"]["periodId"],
                             "explanation/解答题：插入文字的解答题periodId不一致！")
            self.assertEqual(actdata["productCode"], insertexplanation["wordbody"]["productCode"],
                             "explanation/解答题：插入文字的解答题productCode不一致！")
            self.assertEqual(actdata["regionId"], insertexplanation["wordbody"]["regionId"],
                             "explanation/解答题：插入文字的解答题regionId不一致！")
            self.assertEqual(actdata["sourceDepartmentId"], insertexplanation["wordbody"]["sourceDepartmentId"],
                             "explanation/解答题：插入文字的解答题sourceDepartmentId不一致！")
            self.assertEqual(actdata["subjectId"], insertexplanation["wordbody"]["subjectId"],
                             "explanation/解答题：插入文字的解答题subjectId不一致！")
            self.assertEqual(actdata["yearCode"], insertexplanation["wordbody"]["yearCode"],
                             "explanation/解答题：插入文字的解答题yearCode不一致！")
            self.assertEqual(actmessage, "新增成功", "message对比失败！")
            log.info("explanation/解答题：插入文字的解答题测试用例通过！")

    def test_insertwithlatex(self):
        """
        explanation/解答题：插入latex公式的解答题测试用例
        """
        self.insertLatexResponse = request.run_main(insertexplanation["url"], method='POST', headers=insertexplanation["header"],
                                                   data=insertexplanation["latexbody"])
        try:
            actsuccess = self.insertLatexResponse.json()["success"]
            actdata = self.insertLatexResponse.json()["data"]
            if actdata["id"] != "":
                InsertExplanation.insertId.append(actdata["id"])
            actmessage = self.insertLatexResponse.json()["message"]
        except Exception as error:
            log.error("explanation/解答题：插入latex公式的解答题测试用例失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "explanation/解答题：插入latex公式的解答题success返回false！")
            self.assertEqual(actdata["answer"], insertexplanation["latexbody"]["itemAnswer"]["answer"],
                             "explanation/解答题：插入latex公式的解答题answer不一致！")
            self.assertEqual(actdata["diffLevelCode"], insertexplanation["latexbody"]["diffLevelCode"],
                             "explanation/解答题：插入latex公式的解答题diffLevelCode不一致！")
            self.assertEqual(actdata["duration"], insertexplanation["latexbody"]["duration"],
                             "explanation/解答题：插入latex公式的解答题duration不一致！")
            self.assertIsNotNone(actdata["id"], "explanation/解答题：插入latex公式的解答题返回ID为空！")
            self.assertEqual(actdata["itemAnswer"]["answer"], insertexplanation["latexbody"]["itemAnswer"]["answer"],
                             "explanation/解答题：插入latex公式的解答题itemAnswer不一致！")
            self.assertEqual(actdata["itemContent"]["content"], insertexplanation["latexbody"]["itemContent"]["content"],
                             "explanation/解答题：插入latex公式的解答题itemContent不一致！")
            self.assertEqual(actdata["itemDetail"]["detail"], insertexplanation["latexbody"]["itemDetail"]["detail"],
                             "explanation/解答题：插入latex公式的解答题itemDetail不一致！")
            self.assertEqual(actmessage, "新增成功", "message对比失败！")
            log.info("explanation/解答题：插入latex公式的解答题测试用例通过！")

    def test_insertwithtype(self):
        """
        explanation/解答题：插入带文字格式的解答题测试用例
        """
        typebody = insertexplanation["typebody"]
        self.insertTypeResponse = request.run_main(insertexplanation["url"], method='POST',
                                                    headers=insertexplanation["header"], data=typebody)
        try:
            actsuccess = self.insertTypeResponse.json()["success"]
            actdata = self.insertTypeResponse.json()["data"]
            if actdata["id"] != "":
                InsertExplanation.insertId.append(actdata["id"])
            actmessage = self.insertTypeResponse.json()["message"]
        except Exception as error:
            log.error("explanation/解答题：插入带文字格式的解答题测试用例失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "explanation/解答题：插入带文字格式的解答题success返回false！")
            self.assertEqual(actdata["answer"], typebody["itemAnswer"]["answer"],
                             "explanation/解答题：插入带文字格式的解答题answer不一致！")
            self.assertIsNotNone(actdata["id"], "explanation/解答题：插入带文字格式的解答题返回ID为空！")
            self.assertEqual(actdata["itemAnswer"]["answer"], typebody["itemAnswer"]["answer"],
                             "explanation/解答题：插入带文字格式的解答题itemAnswer不一致！")
            self.assertEqual(actdata["itemContent"]["content"], typebody["itemContent"]["content"],
                             "explanation/解答题：插入带文字格式的解答题itemContent不一致！")
            self.assertEqual(actdata["itemDetail"]["detail"], typebody["itemDetail"]["detail"],
                             "explanation/解答题：插入带文字格式的解答题itemDetail不一致！")
            self.assertEqual(actmessage, "新增成功", "message对比失败！")
            log.info("explanation/解答题：插入带文字格式的解答题测试用例通过！")

    def test_insertwithpicture(self):
        """
        explanation/解答题：插入带图片的解答题测试用例
        """
        picturebody = insertexplanation["picturebody"]
        self.insertTypeResponse = request.run_main(insertexplanation["url"], method='POST',
                                                    headers=insertexplanation["header"], data=picturebody)
        try:
            actsuccess = self.insertTypeResponse.json()["success"]
            actdata = self.insertTypeResponse.json()["data"]
            if actdata["id"] != "":
                InsertExplanation.insertId.append(actdata["id"])
            actmessage = self.insertTypeResponse.json()["message"]
        except Exception as error:
            log.error("explanation/解答题：插入带图片的解答题测试用例失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "explanation/解答题：插入带图片的解答题success返回false！")
            self.assertEqual(actdata["answer"], picturebody["itemAnswer"]["answer"],
                             "explanation/解答题：插入带图片的解答题answer不一致！")
            self.assertIsNotNone(actdata["id"], "explanation/解答题：插入带图片的解答题返回ID为空！")
            self.assertEqual(actdata["itemAnswer"]["answer"], picturebody["itemAnswer"]["answer"],
                             "explanation/解答题：插入带图片的解答题itemAnswer不一致！")
            self.assertEqual(actdata["itemContent"]["content"], picturebody["itemContent"]["content"],
                             "explanation/解答题：插入带图片的解答题itemContent不一致！")
            self.assertEqual(actdata["itemDetail"]["detail"], picturebody["itemDetail"]["detail"],
                             "explanation/解答题：插入带图片的解答题itemDetail不一致！")
            self.assertEqual(actmessage, "新增成功", "message对比失败！")
            log.info("explanation/解答题：插入带图片的解答题测试用例通过！")

    # def test_insertwithaudio(self):
    #     """
    #     explanation/解答题：插入带音频的解答题测试用例
    #     """
    #     audiobody = insertexplanation["audiobody"]
    #     self.insertTypeResponse = request.run_main(insertexplanation["url"], method='POST',
    #                                                 headers=insertexplanation["header"], data=audiobody)
    #     try:
    #         actsuccess = self.insertTypeResponse.json()["success"]
    #         actdata = self.insertTypeResponse.json()["data"]
    #         if actdata["id"] != "":
    #             InsertExplanation.insertId.append(actdata["id"])
    #         actmessage = self.insertTypeResponse.json()["message"]
    #     except Exception as error:
    #         log.error("explanation/解答题：插入带音频的解答题测试用例失败，失败原因："f'{error}')
    #     finally:
    #         self.assertTrue(actsuccess, "explanation/解答题：插入带音频的解答题success返回false！")
    #         self.assertEqual(actmessage, "新增成功", "explanation/解答题：插入带音频的解答题message对比失败！")
    #         log.info("explanation/解答题：插入带音频的解答题测试用例通过！")

    def test_duration_error(self):
        """
        explanation/解答题：讲解时间大于120min的解答题测试用例
        """
        durationerror = insertexplanation["durationerror"]
        self.insertTypeResponse = request.run_main(insertexplanation["url"], method='POST',
                                                    headers=insertexplanation["header"], data=durationerror)
        try:
            actsuccess = self.insertTypeResponse.json()["success"]
            actmessage = self.insertTypeResponse.json()["message"]
        except Exception as error:
            log.error("explanation/解答题：讲解时间大于120min的解答题测试用例失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "explanation/解答题：讲解时间大于120min的解答题success返回false！")
            self.assertEqual(actmessage, "must be less than or equal to 120",
                             "explanation/解答题：讲解时间大于120min的解答题message对比失败！")
            log.info("explanation/解答题：讲解时间大于120min的解答题测试用例通过！")

    @classmethod
    def tearDownClass(self):
        try:
            if len(InsertExplanation.insertId) != 0:
                for i in InsertExplanation.insertId:
                    # print("i："+i)
                    item.delete_item(i)
        except Exception as error:
            log.error("explanation/解答题：创建视频记录--删除记录失败，失败原因："f'{error}')


if __name__ == '__main__':
    unittest.main()