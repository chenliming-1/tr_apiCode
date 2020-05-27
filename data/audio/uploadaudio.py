#!Date：2019/02/20 18:14
# !@Author：龚远琪
#
from common.commonmethod import *
from histudy import *

uploadaudio = {
    "url": f'{sysURL}tr/api/audio/upload/file',

    "header": {
        "Cookie": cookie,
        "Accept": "application/json",
        "Content-Type": "application/json"
    },

    "test_body_success": {
        "fileName": "AT音频_"+randMethod.getMessage(3)+".mp3",
        "key": "resource/tr/courseware/201902211D40ABC526E251C9362531B1276079EE/时间都去哪儿了.mp3",
        "size": 3529132
    },

    "rls_body_success": {
        "fileName": "AT音频_"+randMethod.getMessage(3)+".mp3",
        "key": "resource/tr/courseware/20190221C54021D47C1301CFACAF080AA28C383B/示范音频.mp3",
        "size": 8853850
    },

    "body_filenameerror": {
        "fileName": "",
        "key": "resource/tr/courseware/20190221C54021D47C1301CFACAF080AA28C383B/示范音频.mp3",
        "size": 8853850
    },

    "body_keyerror": {
        "fileName": "AT音频_"+randMethod.getMessage(3)+".mp3",
        "key": "",
        "size": 8853850
    },

    "body_sizeerror": {
        "fileName": "AT音频_"+randMethod.getMessage(3)+".mp3",
        "key": "resource/tr/courseware/20190221C54021D47C1301CFACAF080AA28C383B/示范音频.mp3",
        "size": None
    }
}