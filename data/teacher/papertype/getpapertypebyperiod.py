# -*- encoding: utf-8 -*-
# @ModuleName: getpapertypebyperiod
# @Author：龚远琪
# @Date：2019/11/5 17:00
from common.commonmethod import *

getPaperTypeByPeriod = {
    "url": f'{sysURL}tr/api/tr/paper-textbook-types/period/',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}
