# -*- encoding: utf-8 -*-
# @ModuleName: getSchoolList
# @Author：龚远琪
# @Date：2019/10/18 15:17

from common.commonmethod import *
from histudy import *
from module import *

getSchoolList = {
    "url": f'{sysURL}tr/api/tr/dict/schools/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "selectBySchoolNameBody": {
        "currentPage": 1,
        "pageSize": 10,
        "schoolName": '第一中学'
    },

    "selectByStatusBody": {
        "currentPage": 1,
        "pageSize": 10,
        "status": 'DISABLE'
    },

    "statusErrBody": {
        "currentPage": 1,
        "pageSize": 10,
        "status": 'DISAB'
    },

    "selectByAreaBody": {
        "currentPage": 1,
        "pageSize": 100,
        "cityId": 0,
        "countyId": 0,
        "provinceId": 0
    },

    "selectByPeriodBody": {
        "currentPage": 2,
        "pageSize": 5,
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "schoolName": '第一中学'
    },

    "currentPageErrBody": {
        "currentPage": 0
    },

    "pageSizeErrBody": {
        "pageSize": -1
    }
}
