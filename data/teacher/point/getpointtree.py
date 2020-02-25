# -*- encoding: utf-8 -*-
# @ModuleName: getpointtree.py
# @Author：龚远琪
# @Date：2020/2/24 17:19
from common.commonmethod import *
from module import *

getPointTree = {
    "url": f'{sysURL}tr/api/point/tree',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "subjectId": random.choice([1, 5, 7, 8, 10, 12]),
        "periodId": randdata.getperiod()[0],
        "regionId": randdata.getregion()
    },

    "listIsNone": {
        "subjectId": random.choice([1522, 2082]),
        "periodId": randdata.getperiod()[0],
        "regionId": randdata.getregion()
    },

    "subjectIsNone": {
        "subjectId": None,
        "periodId": randdata.getperiod()[0],
        "regionId": randdata.getregion()
    },

    "subjectError": {
        "subjectId": 666,
        "periodId": randdata.getperiod()[0],
        "regionId": randdata.getregion()
    },

    "periodIsNone": {
        "subjectId": randdata.getsubject()[0],
        "periodId": None,
        "regionId": randdata.getregion()
    },

    "regionIsNone": {
        "subjectId": randdata.getsubject()[0],
        "periodId": randdata.getperiod()[0],
        "regionId": None
    },
}
