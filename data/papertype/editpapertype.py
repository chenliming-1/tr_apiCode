# -*- encoding: utf-8 -*-
# @ModuleName: editpapertype
# @Author：龚远琪
# @Date：2019/11/5 9:57
from common.commonmethod import *
from histudy import *
from module import *

editPaperType = {
    "url": f'{sysURL}tr/api/tr/paper-textbook-types/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "description": randMethod.getMessage(50),
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "requiredBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeNameRepeatBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "单元考"
    },

    "typeCodeRepeatBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "qimokao",
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeNameNoneBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200)
    },

    "typeCodeNoneBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": None,
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "periodIdsNoneBody": {
        "periodIds": None,
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "periodIdsErrBody": {
        "periodIds": [10001, 10004],
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "periodIdsHaveNoneBody": {
        "periodIds": [10001, None],
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "seqIsZeroBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": 0,
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "seqErrBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": 201,
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeNameTooLongBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "typeName": randMethod.getMessage(101)
    },

    "descriptionTooLongBody": {
        "description": randMethod.getMessage(201),
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    }

}

