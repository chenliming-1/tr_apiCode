# -*- encoding: utf-8 -*-
# @ModuleName: additem
# @Author：龚远琪
# @Date：2019/11/18 15:26
from common.commonmethod import *
from histudy import *
from module import *

addItem = {
    "url": f'{sysURL}tr/api/tr/v2/item',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "singleChoiceBody": {
        "answer": "<p>2</p>",
        "audios": [],
        "city": "",
        "content": "<p>1</p>",
        "county": "",
        "detail": "",
        "diffLevelCode": 10001,
        "gradeId": "",
        "id": "",
        "itemMouldType": "EXPLANATION",
        "itemTypeId": 1,
        "paperTextbookTypeId": "",
        "periodId": 10001,
        "pointIds": [],
        "province": "",
        "schoolId": "",
        "schoolName": "",
        "schoolYearId": "",
        "semesterId": "",
        "source": "MINI_ITEM",
        "subItems": [],
        "subjectId": 2082,
        "videos": [],
        "yearCode": ""
    }

}
