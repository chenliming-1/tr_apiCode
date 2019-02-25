#!Date：2019/02/22 11:28
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *

uploadfile = {
    "url": f'{sysurl}tr/api/video/upload/file',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "test_body_success": {
         0: [{
            "aliasName": "AT视频_"+randMethod.getMessage(3),
            "fileId": "5285890786045199844",
            "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
            "fsize": 4892402,
            "label": "",
            "plat": 1,
            "remark": "",
            "seq": 1,
            "type": 2
        }]
    },

    "rls_body_success": {
        0: [{
            "aliasName": "AT视频_"+randMethod.getMessage(3),
            "fileId": "5285890786047206422",
            "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
            "fsize": 8713425,
            "label": "",
            "plat": 1,
            "remark": "",
            "seq": 1,
            "type": 2
        }]
    },

    "body_typeError": {
        0: [{
            "aliasName": "AT视频_"+randMethod.getMessage(3),
            "fileId": "5285890785951238046",
            "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
            "fsize": 3529132,
            "label": "",
            "plat": 1,
            "remark": "",
            "seq": 1,
            "type": None
        }]
    },

    "body_aliasNameError": {
            0: [{
                "aliasName": "",
                "fileId": "5285890786047206422",
                "fileName": "AT视频_"+randMethod.getMessage(3)+".mp4",
                "fsize": 8713425,
                "label": "",
                "plat": 1,
                "remark": "",
                "seq": 1,
                "type": 2
            }]
        }

}


