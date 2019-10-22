# -*- coding: utf-8 -*-
# #!Date：2019/8/14 10:00
# # !@Author：龚远琪
from histudy import *
from module import *
from data.teacher.itemtype import *
from data.teacher.datadict import *
from data.teacher.school import *


class DataDict(object):
    def __int__(self):
        pass

    def add_itemType(self):
        """
        新增题型
        """
        addResponse = request.run_main(additemtype["url"], method='POST', headers=additemtype["header"],
                                       data=additemtype["body_success"])
        try:
            status_code = addResponse.status_code
            assert status_code == 201, "题型新增失败！"
            log.info("itemType/题型：新增题型成功！")
            return addResponse
        except AssertionError as error:
            log.error("itemType/题型：新增题型失败，失败原因："f'{error}')

    def delete_itemtype(self, itemTypeId):
        """
        删除题型
        """
        deleteResponse = request.run_main(deleteitemtype["url"] + str(itemTypeId), method='DELETE',
                                          headers=deleteitemtype["header"], data={})
        try:
            status_code = deleteResponse.status_code
            assert status_code == 204, "题型删除失败！"
            log.info("itemType/题型：删除题型成功！")
            return deleteResponse
        except AssertionError as error:
            log.error("itemType/题型：删除题型失败，失败原因："f'{error}')

    def addSchool(self, addSchoolBody):
        """
        新增学校
        """
        addSchoolResponse = request.run_main(addSchool["url"], method='POST', headers=addSchool["header"],
                                             data=addSchoolBody)
        try:
            status_code = addSchoolResponse.status_code
            assert status_code == 201, "学校新增失败！"
            log.info("school/学校：新增学校成功！")
            return addSchoolResponse
        except AssertionError as error:
            log.error("school/学校：新增学校失败，失败原因："f'{error}')

    def getArea(self):
        """
        获取全国省市区
        """
        getAreaResponse = request.run_main(getArea["url"], method='GET', headers=getArea["header"], data={})
        try:
            status_code = getAreaResponse.status_code
            assert status_code == 200, "获取地区失败！"
            log.info("getArea/地区：获取地区成功！")
            return getAreaResponse
        except AssertionError as error:
            log.error("getArea/地区：获取地区失败，失败原因："f'{error}')

    def getRandArea(self, flag=1):
        getAreaResponse = self.getArea()
        getData = getAreaResponse.json()
        while True:
            getProvince = random.choice(getData)
            areaList = [{"id": getProvince["id"], "name": getProvince["name"]}]
            if len(getProvince["children"]) != 0:
                break
        # print("getProvince:" + str(getProvince))
        getCity = random.choice(getProvince["children"])
        areaList.append({"id": getCity["id"], "name": getCity["name"]})
        if flag == 1 and len(getCity["children"]) != 0:
            getCounty = random.choice(getCity["children"])
            areaList.append({"id": getCounty["id"], "name": getCounty["name"]})
        return areaList


dataDict = DataDict()
# dataDict.add_itemType()