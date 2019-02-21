# -*- coding: utf-8 -*-
# #!Date：2019/2/20 16:30
# # !@Author：龚远琪
from common.commonmethod import *
from module import *
from histudy import *
from data.teacher.item import *
from data.teacher.commonupload import *

class Upload():
    def __int__(self):
        pass

    def getToken(self):
        tokenResponse = request.run_main(token["url"],method="GET",headers=token["header"])
        try:
            actsuccess = tokenResponse.json()["success"]
            assert actsuccess == True, " 获取token失败！"
            return tokenResponse
        except Exception as error:
            log.error("获取token失败，失败原因：" + f'{error}')

    def upload_image(self):
        imagepath = os.path.join(projectpath, 'file/image/') + "3-1.png"
        image = open(imagepath, "rb")
        files = [("file", ("4-1.png", image, "image/png"))]
        uploadimageResponse = request.run_main(uploadpicture["url"], method='POST',
                                                      headers=uploadpicture["header"], files=files)
        image.close()
        try:
            actsuccess = uploadimageResponse.json()["success"]
            assert actsuccess == True, "上传图片失败！"
            return uploadimageResponse
        except Exception as error:
            log.error("上传图片失败，失败原因：" + f'{error}')


upload = Upload()

if __name__ == '__main__':
    # print(upload.upload_image())
    print(upload.getToken())

