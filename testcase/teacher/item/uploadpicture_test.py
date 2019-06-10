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
        randimage = random.choice(('3-1.png', '3-2.png', '3-3.png', '3-4.png', '3-5.png'))
        imagepath = os.path.join(projectpath, 'file/image/') + randimage
        image = open(imagepath, "rb")
        files = [("file", (randimage, image, "image/png"))]
        self.uploadpictureResponse = request.run_main(uploadpicture["url"], method='POST', headers=uploadpicture["header"], files=files)
        image.close()
        try:
            actsuccess = self.uploadpictureResponse.json()["success"]
            actdata = self.uploadpictureResponse.json()["data"]
            actimageurl = actdata["picUrl"]
            imageresponse = urllib.request.urlopen(actimageurl)
        except Exception as error:
            log.error("item/题库：上传png图片接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "item/题库-上传png图片success为False！")
            self.assertIsNotNone(actimageurl, "item/题库-上传png图片URL返回为空！")
            self.assertEqual(imageresponse.status, 200, "通过URL获取图片失败！")
            self.assertIsNotNone(actdata["picUuid"], "item/题库-上传png图片ID返回为空！")
            log.info("item/题库：上传png图片成功用例测试通过！")

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
        except Exception as error:
            log.error("item/题库：上传jpg图片接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "item/题库-上传jpg图片success为False！")
            self.assertIsNotNone(actimageurl, "item/题库-上传jpg图片URL返回为空！")
            self.assertEqual(imageresponse.status, 200, "通过URL获取图片失败！")
            self.assertIsNotNone(actdata["picUuid"], "item/题库-上传jpg图片ID返回为空！")
            log.info("item/题库：上传jpg图片成功用例测试通过！")

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
        except Exception as error:
            log.error("item/题库：上传gif图片测试失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "item/题库-上传gif图片success为True！")
            log.info("item/题库：上传gif图片失败用例测试通过！")

    def test_uploadpicture_fail(self):
        """
        item/题库：uploadpicture上传图片失败的测试用例-上传列表为空
        """
        self.uploadpictureResponse = request.run_main(uploadpicture["url"], method='POST', headers=uploadpicture["header"], files=[])
        try:
            actsuccess = self.uploadpictureResponse.json()["success"]
        except Exception as error:
            log.error("item/题库：上传图片-上传列表为空测试失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "item/题库-上传图片-上传列表为空success为True！")
            log.info("item/题库：上传图片失败用例-上传列表为空测试通过！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()
