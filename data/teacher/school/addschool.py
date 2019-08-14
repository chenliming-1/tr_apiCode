# #!Date：2019/8/14 16:20
# !@Author：龚远琪
#
from common.commonmethod import *
from common.commonapi import *
from histudy import *
from module import *

areaSuccessList = dataDict.getRandArea()
areaNoCountyList = dataDict.getRandArea(0)
addSchool = {
    "url": f'{sysurl}tr/api/tr/dict/schools',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "cityId": areaSuccessList[1]["id"],
        "countyId": areaSuccessList[2]["id"],
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "provinceId": areaSuccessList[0]["id"],
        "schoolName": "AT" + areaSuccessList[2]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyNoCounty": {
        "cityId": areaNoCountyList[1]["id"],
        "countyId": None,
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "provinceId": areaNoCountyList[0]["id"],
        "schoolName": "AT" + areaNoCountyList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyNoCity": {
        "cityId": None,
        "countyId": None,
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "provinceId": areaNoCountyList[0]["id"],
        "schoolName": "AT" + areaNoCountyList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyNoProvince": {
        "cityId": areaNoCountyList[1]["id"],
        "countyId": None,
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "provinceId": None,
        "schoolName": "AT" + areaNoCountyList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyNoSchoolName": {
        "cityId": areaNoCountyList[1]["id"],
        "countyId": None,
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "provinceId": areaNoCountyList[0]["id"],
        "schoolName": None,
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyNoPeriod": {
        "cityId": areaNoCountyList[1]["id"],
        "countyId": None,
        "periodIds": None,
        "provinceId": areaNoCountyList[0]["id"],
        "schoolName": "AT" + areaNoCountyList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    },

    "bodyPeriodErr": {
        "cityId": areaNoCountyList[1]["id"],
        "countyId": None,
        "periodIds": [None, '10001'],
        "provinceId": areaNoCountyList[0]["id"],
        "schoolName": "AT" + areaNoCountyList[1]["name"] + "第" + random.choice("一二三四五六七八九十") + "中学",
        "seq": randMethod.getNumByRange(1, 200)
    }

}