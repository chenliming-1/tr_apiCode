# #!Date：2019/7/25 9:54
# !@Author：龚远琪
#
from common.commonmethod import *

getArea = {
    "url": f'{sysurl}tr/api/tr/administrative-area/tree',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}