# -*- encoding: utf-8 -*-
# @ModuleName: addpapertype
# @Author：龚远琪
# @Date：2019/11/4 11:32
from common.commonmethod import *
from histudy import *
from module import *

addPaperType = {
    "url": f'{sysURL}tr/api/tr/paper-textbook-types',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "description": randMethod.getMessage(50),
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "requiredBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeNameRepeatBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
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
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": None
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
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "periodIdsErrBody": {
        "periodIds": [10001, 10004],
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "periodIdsHaveNoneBody": {
        "periodIds": [10001, None],
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "seqIsZeroBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": 0,
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "seqErrBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": 201,
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeCodeTooLongBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "typeCode": randMethod.getStr(101),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    },

    "typeNameTooLongBody": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": randMethod.getMessage(101)
    },

    "descriptionTooLongBody": {
        "description": randMethod.getMessage(201),
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200),
        "typeCode": "ATCode_" + randMethod.getStr(4),
        "typeName": "AT模版_" + randMethod.getChinese(4)
    }

}
