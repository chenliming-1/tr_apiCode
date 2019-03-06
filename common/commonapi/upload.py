# -*- coding: utf-8 -*-
# #!Date：2019/2/20 16:30
# # !@Author：龚远琪
from common.commonmethod import *
from module import *
from histudy import *
from data.teacher.item import *
from data.teacher.commonupload import *
from data.teacher.audio import *
from data.teacher.video import *

class Upload():
    def __int__(self):
        pass

    def getToken(self):
        tokenResponse = request.run_main(token["url"],method="GET",headers=token["header"])
        try:
            actsuccess = tokenResponse.json()["success"]
            assert actsuccess == True, " 获取token失败！"
            return tokenResponse
        except AssertionError as error:
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
        except AssertionError as error:
            log.error("上传图片失败，失败原因：" + f'{error}')

    def upload_audio(self):
        """
        上传音频
        """
        uploadaudioResponse = request.run_main(uploadaudio["url"], method='POST', headers=uploadaudio["header"],
                                                    data=uploadaudio[env + "_body_success"])
        try:
            actsuccess = uploadaudioResponse.json()["success"]
            assert actsuccess == True, "上传音频失败！"
            return uploadaudioResponse
        except AssertionError as error:
            log.error("audio/音频：音频上传失败，失败原因："f'{error}')

    def upload_video_resource(self):
        """
        上传视频-有上传到resource并存表接口
        """
        resourceResponse = request.run_main(resource["url"], method='POST', headers=resource["header"],
                                                 data=resource[env + "_body_success"])
        try:
            actsuccess = resourceResponse.json()["success"]
            assert actsuccess == True, "上传音频失败！"
            return resourceResponse
        except AssertionError as error:
            log.error("video/视频：视频上传resource失败，失败原因："f'{error}')

    def upload_video(self):
        """
        上传视频-未上传resource及未存表接口
        """
        uploadfileResponse = request.run_main(uploadfile["url"], method='POST', headers=uploadfile["header"],
                                                   data=uploadfile[env + "_body_success"][0])
        try:
            actsuccess = uploadfileResponse.json()["success"]
            assert actsuccess == True, "上传音频失败！"
            return uploadfileResponse
        except AssertionError as error:
            log.error("video/视频：视频上传接口失败，失败原因："f'{error}')

    def createRelation(self, url="textbook_lessonUrl"):
        """
        创建视频关联记录
        """
        uploadFileResponse = self.upload_video()
        uploadfiledata = uploadFileResponse.json()["data"]
        uploadfiledata[0]["fileLength"] = uploadfile[env + "_body_success"][0][0]["fsize"]
        createRecordResponse = request.run_main(createrelation[url], method='POST', headers=createrelation["header"],
                                               data=uploadfiledata)
        try:
            actsuccess = createRecordResponse.json()["success"]
            actdata = createRecordResponse.json()["data"][0]
            assert actsuccess == True, "上传音频失败！"
            sql = "select id from video_relation where video_id='"f'{actdata["id"]}' "' and ref_id='" + randbusinessId + "' limit 1;"
            recordId = dao(db, sql)[0]["id"]
            return createRecordResponse, recordId
        except AssertionError as error:
            log.error("video/视频：视频上传接口失败，失败原因："f'{error}')

    def delete_video_relation(self, relationId):
        """
        删除视频关联
        """
        deleteResponse = request.run_main(deleterelation["url"]+str(relationId), method='DELETE', headers=deleterelation["header"], data={})
        try:
            actsuccess = deleteResponse.json()["success"]
            assert actsuccess == True, "上传音频失败！"
            return deleteResponse
        except AssertionError as error:
            log.error("video/视频：视频上传接口失败，失败原因："f'{error}')


upload = Upload()

if __name__ == '__main__':
    response, rid = upload.createRelation()
    print(rid)

