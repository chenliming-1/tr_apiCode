#!Date：2019/02/20 18:14
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *

resource = {
    "url": f'{sysurl}tr/api/video/upload/file/resource',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "test_body_success": {
        "aliasName": "AT视频_"+randMethod.getMessage(3),
        "fileId": "5285890785951238046",
        "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
        "fsize": 9124352,
        "label": "",
        "plat": 1,
        "remark": "",
        "seq": 1,
        "type": 2
    },

    "rls_body_success": {
        "aliasName": "AT视频_"+randMethod.getMessage(3),
        "fileId": "5285890785939690952",
        "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
        "fsize": 3529132,
        "label": "",
        "plat": 1,
        "remark": "",
        "seq": 1,
        "type": 2
    },

    "body_typeError": {
        "aliasName": "AT视频_"+randMethod.getMessage(3),
        "fileId": "5285890785951238046",
        "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
        "fsize": 3529132,
        "label": "",
        "plat": 1,
        "remark": "",
        "seq": 1,
        "type": None
    }

}