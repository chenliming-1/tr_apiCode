# #!Date：2019/7/9 10:21
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *
from module import *

additemtype = {
    "url": f'{sysurl}tr/api/tr/item-types',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "description": randMethod.getMessage(50),
        "itemMouldType": randdata.getitemmouldtype(),
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": randdata.getsubject(random.randint(1, 10)),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_success_requried": {
        "itemMouldType": randdata.getitemmouldtype(),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_subjectIdsErr": {
        "itemMouldType": randdata.getitemmouldtype(),
        "subjectIds": [None, 12],
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_itemMouldTypeIsNull": {
        "description": "",
        "itemMouldType": None,
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": [],
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_itemMouldTypeIsErr": {
        "description": "",
        "itemMouldType": "suiyi",
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": [],
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_typeCodeIsNull": {
        "description": "",
        "itemMouldType": randdata.getitemmouldtype(),
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": [],
        "typeCode": None,
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_typeNameIsNull": {
        "description": "",
        "itemMouldType": randdata.getitemmouldtype(),
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": [],
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": None
    }
}