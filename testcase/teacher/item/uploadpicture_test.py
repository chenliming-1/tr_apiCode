# -*- coding: utf-8 -*-
# #!Date：2019/2/14 11:30
# # !@Author：龚远琪

from histudy import *
from data.teacher.item import *
from module import *
from common.commonmethod import *

class UploadPicture(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.uploadpictureResponse = {}

    def test_uploadpicture_png(self):
        """
        item/题库：uploadpicture上传png图片成功的测试用例
        """
        imagepath = os.path.join(projectpath, 'file/image/') + "3-1.png"
        image = open(imagepath, "rb")
        files = [("file", ("4-1.png", image, "image/png"))]
        self.uploadpictureResponse = request.run_main(uploadpicture["url"], method='POST', headers=uploadpicture["header"], files=files)
        image.close()
        try:
            actsuccess = self.uploadpictureResponse.json()["success"]
            actdata = self.uploadpictureResponse.json()["data"]
            actimageurl = actdata["picUrl"]
            imageresponse = urllib.request.urlopen(actimageurl)
            log.info("item/题库：上传png图片成功用例测试通过！")
        except Exception as error:
            log.error("item/题库：上传png图片接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "item/题库-上传png图片success为false！")
            self.assertIsNotNone(actimageurl, "item/题库-上传png图片URL返回为空！")
            self.assertEqual(imageresponse.status, 200, "通过URL获取图片失败！")
            self.assertIsNotNone(actdata["picUuid"], "item/题库-上传png图片ID返回为空！")

    def test_uploadpicture_jpg(self):
        """
        item/题库：uploadpicture上传jpg图片成功的测试用例
        """
        imagepath = os.path.join(projectpath, 'file/image/') + "1-1.jpg"
        image = open(imagepath, "rb")
        files = [("file", ("1-1.jpg", image, "image/jpeg"))]
        self.uploadpictureResponse = request.run_main(uploadpicture["url"], method='POST', headers=uploadpicture["header"], files=files)
        image.close()
        try:
            actsuccess = self.uploadpictureResponse.json()["success"]
            actdata = self.uploadpictureResponse.json()["data"]
            actimageurl = actdata["picUrl"]
            imageresponse = urllib.request.urlopen(actimageurl)
            log.info("item/题库：上传jpg图片成功用例测试通过！")
        except Exception as error:
            log.error("item/题库：上传jpg图片接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "item/题库-上传jpg图片success为false！")
            self.assertIsNotNone(actimageurl, "item/题库-上传jpg图片URL返回为空！")
            self.assertEqual(imageresponse.status, 200, "通过URL获取图片失败！")
            self.assertIsNotNone(actdata["picUuid"], "item/题库-上传jpg图片ID返回为空！")

    def test_uploadpicture_gif(self):
        """
        item/题库：uploadpicture上传gif图片失败的测试用例
        """
        imagepath = os.path.join(projectpath, 'file/image/') + "2-1.gif"
        image = open(imagepath, "rb")
        files = [("file", ("2-1.gif", image, "image/gif"))]
        self.uploadpictureResponse = request.run_main(uploadpicture["url"], method='POST', headers=uploadpicture["header"], files=files)
        image.close()
        try:
            actsuccess = self.uploadpictureResponse.json()["success"]
            log.info("item/题库：上传gif图片失败用例测试通过！")
        except Exception as error:
            log.error("item/题库：上传gif图片测试失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "item/题库-上传gif图片success为false！")

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()
