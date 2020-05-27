# #!Date：2019/7/9 10:21
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *
from module import *

updateItemType = {
    "url": f'{sysURL}tr/api/tr/item-types/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "description": randMethod.getMessage(50),
        "priorityCode": randMethod.getNumByRange(0, 100),
        "subjectIds": randdata.getsubject(random.randint(1, 10)),
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_subjectIdsErr": {
        "subjectIds": [None, 12],
        "typeName": "AT模版_" + randMethod.getChinese(3)
    },

    "body_typeNameIsNull": {
        "priorityCode": randMethod.getNumByRange(0, 100),
        "typeName": None
    },

    "body_priorityCodeError": {
        "priorityCode": 999999999999,
        "typeName": "AT模版_" + randMethod.getChinese(3)
    }

}