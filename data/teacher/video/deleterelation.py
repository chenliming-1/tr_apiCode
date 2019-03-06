#!Date：2019/03/1 15:53
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *
from module import *

deleterelation = {
    "url": f'{sysurl}tr/api/video/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}