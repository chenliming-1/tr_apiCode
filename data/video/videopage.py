#!Date：2019/02/22 11:28
# !@Author：龚远琪
#
from common.commonmethod import *
from data.video import *
from module import *

videopage = {
    # "randomUrl": f'{sysURL}tr/api/video?businessId='+randbusinessId + '&businessType=' + random.choice(urldata["businessType"]),
    # "itemUrl": f'{sysURL}tr/api/video?businessId='+randbusinessId + '&businessType=ITEM',
    # "pointUrl": f'{sysURL}tr/api/video?businessId='+randbusinessId + '&businessType=POINT',
    # "textbook_formalUrl": f'{sysURL}tr/api/video/'+randbusinessId + '/TEXTBOOK_CHAPTER_FORMAL/page',   #正课视频#
    "textbook_lessonUrl": f'{sysURL}tr/api/video/'+randbusinessId + '/TEXTBOOK_CHAPTER_PREPARE_LESSON/page',  #说课视频#

    "businessIdNull": f'{sysURL}tr/api/video/NULL/' + random.choice(urldata["businessType"])+'/page',
    "businessTypeNull": f'{sysURL}tr/api/video/'+randbusinessId + '/NULL/page',
    "businessTypeErr": f'{sysURL}tr/api/video/'+randbusinessId + '/SUIBIAN/page',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "body": {
        "currentPage": 1,
        "pageSize": 50
    },

    "searchBody": {
        "currentPage": 1,
        "pageSize": 50,
        "searchVideoName": ""
    },

    "pageSetBody": {
        "currentPage": 2,
        "pageSize": 1,
    }

}
