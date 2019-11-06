# -*- encoding: utf-8 -*-
# @ModuleName: getpapertypelist
# @Author：龚远琪
# @Date：2019/11/6 9:51
from common.commonmethod import *

getPaperTypeList = {
    "url": f'{sysURL}tr/api/tr/paper-textbook-types/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "searchOneBody": {
        "currentPage": 1,
        "pageSize": 10,
        "typeName": '期中考'
    },

    "searchSomeBody": {
        "currentPage": 1,
        "pageSize": 10,
        "typeName": '考'
    },

    "searchNoneBody": {
        "currentPage": 1,
        "pageSize": 10,
        "typeName": 'zhijiankao'
    },

    "searchAllBody": {
        "currentPage": 2,
        "pageSize": 5,
    },

    "currentPageErrBody": {
        "currentPage": 0
    },

    "pageSizeErrBody": {
        "pageSize": -1
    }

}
