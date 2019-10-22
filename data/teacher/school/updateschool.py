# #!Date：2019/8/14 16:20
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *
from module import *

updateSchool = {
    "url": f'{sysURL}tr/api/tr/dict/schools/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body_success": {
        "periodIds": randdata.getperiod(random.randint(1, 4)),
        "seq": randMethod.getNumByRange(1, 200)
    }

}
