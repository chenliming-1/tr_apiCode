#!Date：2019/02/22 11:28
# !@Author：龚远琪
#
from common.commonmethod import *
from module import *

urldata = {
    "test_businessId": ['20180625421dc3ce0dcb4f21bb53f9232b0c9c65', '2018062570234dc2174444d99a769b79c0f84992',
                        '20180625401504396bfb4af99888bc30dd4d9e5c', '201806257c8a3e3196c04f86946bcdf83ec6d9cb'],

    "rls_businessId": ['201807036fa17ff188ca49a5917297d478285fe7', '20180903ea1876e941d949f8b4f47ba087f7014f',
                       '201809034ff385f897a341c0887517642f250e5a'],

    "businessType": ['ITEM', 'POINT', 'TEXTBOOK_CHAPTER_FORMAL', 'TEXTBOOK_CHAPTER_PREPARE_LESSON']
}

randbusinessId = random.choice(urldata[env+"_businessId"])

createrelation = {
    "randomUrl": f'{sysurl}tr/api/video?businessId='+randbusinessId + '&businessType=' + random.choice(urldata["businessType"]),
    "itemUrl": f'{sysurl}tr/api/video?businessId='+randbusinessId + '&businessType=ITEM',
    "pointUrl": f'{sysurl}tr/api/video?businessId='+randbusinessId + '&businessType=POINT',
    "textbook_formalUrl": f'{sysurl}tr/api/video?businessId='+randbusinessId +
                          '&businessType=TEXTBOOK_CHAPTER_FORMAL',   #正课视频#
    "textbook_lessonUrl": f'{sysurl}tr/api/video?businessId='+randbusinessId +
                          '&businessType=TEXTBOOK_CHAPTER_PREPARE_LESSON',  #说课视频#

    "businessIdIsNull": f'{sysurl}tr/api/video?businessId=&businessType=' + random.choice(urldata["businessType"]),
    "businessTypeIsNull": f'{sysurl}tr/api/video?businessId='+randbusinessId + '&businessType=',
    "businessTypeErr": f'{sysurl}tr/api/video?businessId='+randbusinessId + '&businessType=SUIBIAN',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

}


