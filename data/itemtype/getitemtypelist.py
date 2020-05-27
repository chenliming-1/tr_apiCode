# #!Date：2019/8/13 14:52
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *

getItemTypeList = {
    "url": f'{sysURL}tr/api/tr/item-types',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "currentPage": 1,
        "pageSize": 100
    },

    "body_withTypeName": {
        "currentPage": 1,
        "pageSize": 10,
        "typeName": ""
    },

    "body_randTypeName": {
        "currentPage": 1,
        "pageSize": 10,
        "typeName": randMethod.getChinese(3)
    },

    "body_currentPageIsZero": {
        "currentPage": 0
    },

    "body_currentPageErr": {
        "currentPage": -1
    },

    "body_pageSizeErr": {
        "pageSize": -1
    }

}