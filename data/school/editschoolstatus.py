# #!Date：2019/8/14 16:20
# !@Author：龚远琪
#
from common.commonmethod import *

editSchoolStatus = {
    "url": f'{sysURL}tr/api/tr/dict/schools/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
}
