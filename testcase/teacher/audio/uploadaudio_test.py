# -*- coding: utf-8 -*-
# #!Date：2019/2/21 17:00
# # !@Author：龚远琪
from histudy import *
from data.teacher.audio import *
from common.commonmethod import *
from module import *


class UploadAudio(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.uploadaudioResponse = {}

    def test_uploadaudio_success(self):
        """
        audio/音频：音频上传成功的测试用例
        """
        self.uploadaudioResponse = request.run_main(uploadaudio["url"], method='POST', headers=uploadaudio["header"],
                                              data=uploadaudio[env+"_body_success"])
        try:
            actsuccess = self.uploadaudioResponse.json()["success"]
            actdata = self.uploadaudioResponse.json()["data"]
            actaudiourl = actdata["linkUrl"]
            # URL只允许一部分ASCII 字符（数字字母和部分符号），不支持汉字，需编码转换#
            audioresponse = urllib.request.urlopen(quote(actaudiourl, safe=string.printable))
            log.info("audio/音频：音频上传成功用例测试通过！")
        except Exception as error:
            log.error("audio/音频：音频上传接口失败，失败原因："f'{error}')
        finally:
            self.assertTrue(actsuccess, "audio/音频：音频上传success返回false！")
            self.assertEqual(actdata["audioName"], uploadaudio[env+"_body_success"]["fileName"], "audio/音频：音频上传名称不一致！")
            self.assertEqual(actdata["businessType"], "audio", "audio/音频：音频上传类型错误！")
            self.assertEqual(actdata["fileLength"], uploadaudio[env+"_body_success"]["size"], "audio/音频：音频上传文件大小不一致！")
            self.assertIsNotNone(actdata["id"], "audio/音频：音频上传ID返回为空！")
            self.assertIsNotNone(actaudiourl, "audio/音频：音频上传URL返回为空！")
            self.assertEqual(audioresponse.status, 200, "通过URL获取音频失败！")
            self.assertEqual(actdata["originalName"], uploadaudio[env+"_body_success"]["fileName"],
                             "audio/音频：音频上传名称不一致！")
            self.assertEqual(actdata["status"], "AVAILABLE", "audio/音频：音频上传返回状态不一致！")

    def test_uploadaudio_filenameisnull(self):
        """
        audio/音频：音频上传失败的测试用例-filename为NULL
        """
        self.uploadaudioResponse = request.run_main(uploadaudio["url"], method='POST', headers=uploadaudio["header"],
                                                    data=uploadaudio["body_filenameerror"])
        try:
            actsuccess = self.uploadaudioResponse.json()["success"]
            actmessage = self.uploadaudioResponse.json()["message"]
            log.info("audio/音频：音频上传失败用例-filename为NULL测试通过！")
        except Exception as error:
            log.error("audio/音频：音频上传接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "audio/音频：音频上传success返回True！")
            self.assertEqual(actmessage, "文件名称不能为空", "audio/音频：音频上传message返回信息不一致！")

    def test_uploadaudio_keyisnull(self):
        """
        audio/音频：音频上传失败的测试用例-key为NULL
        """
        self.uploadaudioResponse = request.run_main(uploadaudio["url"], method='POST', headers=uploadaudio["header"],
                                                    data=uploadaudio["body_keyerror"])
        try:
            actsuccess = self.uploadaudioResponse.json()["success"]
            actmessage = self.uploadaudioResponse.json()["message"]
            log.info("audio/音频：音频上传失败用例-key为NULL测试通过！")
        except Exception as error:
            log.error("audio/音频：音频上传接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "audio/音频：音频上传success返回false！")
            self.assertEqual(actmessage, "七牛返回key（url相对路径）不能为空", "audio/音频：音频上传message返回信息不一致！")

    def test_uploadaudio_sizeisnull(self):
        """
        audio/音频：音频上传失败的测试用例-size为NULL
        """
        self.uploadaudioResponse = request.run_main(uploadaudio["url"], method='POST', headers=uploadaudio["header"],
                                                    data=uploadaudio["body_sizeerror"])
        try:
            actsuccess = self.uploadaudioResponse.json()["success"]
            actmessage = self.uploadaudioResponse.json()["message"]
            log.info("audio/音频：音频上传失败用例-size为NULL测试通过！")
        except Exception as error:
            log.error("audio/音频：音频上传接口失败，失败原因："f'{error}')
        finally:
            self.assertFalse(actsuccess, "audio/音频：音频上传success返回false！")
            self.assertEqual(actmessage, "文件大小不能为空", "audio/音频：音频上传message返回信息不一致！")

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()