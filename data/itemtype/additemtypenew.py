from common.commonmethod import  *
from  histudy import  *
from  module import  *
import  random

addItemTypenew = {
    "headers": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
        },
    "url": f'{sysURL}tr/api/tr/item-types',
    "method": "POST",
    "body_sucess":{
                    "itemMouldType":randdata.getitemmouldtype(),
                    "subjectIds":randdata.getsubject(random.randint(1,10)),
                   "typeCode":randMethod.getStr(3),
                   "typeName": "AT模板"+randMethod.getChinese(3)
                   },
    "body_typeNameIsNull":{
                    "itemMouldType":randdata.getitemmouldtype(),
                    "subjectIds":randdata.getsubject(random.randint(1,10)),
                    "typeCode":randMethod.getStr(3),
                   "typeName":None
    }
}


# print(addItemTypenew["body_sucess"])
#
# print(addItemTypenew["body_typeNameIsNull"])
