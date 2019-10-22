# #!Date：2019/7/10 11:21
# !@Author：龚远琪
#
from common.commonmethod import *

deleteitemtype = {
    "url": f'{sysURL}tr/api/tr/item-types/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}