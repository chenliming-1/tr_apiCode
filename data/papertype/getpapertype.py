# -*- encoding: utf-8 -*-
# @ModuleName: getpapertype
# @Author：龚远琪
# @Date：2019/11/5 16:14
from common.commonmethod import *

getPaperType = {
    "url": f'{sysURL}tr/api/tr/paper-textbook-types/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}
