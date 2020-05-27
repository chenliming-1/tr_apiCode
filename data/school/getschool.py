# #!Date：2019/10/18 11:20
# !@Author：龚远琪
#
from common.commonmethod import *

getSchool = {
    "url": f'{sysURL}tr/api/tr/dict/schools/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
}